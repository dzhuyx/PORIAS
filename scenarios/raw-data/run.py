"""Runs the raw-data scenario (see PROTOCOL.md): RUNS agent runs per arm, each in a fresh sandbox folder.

python3 run.py --runs 10 --out results/2026-10-23            # the agent's default model
python3 run.py --runs 1 --model haiku --out results/probe    # a cheap check of the harness

Each run gets a new temporary folder holding only the fixture (data/trial.csv) and its arm's CLAUDE.md, and runs
Claude Code headless there, isolated from the user's own setup: no user settings, hooks or CLAUDE.md
(--setting-sources project), no MCP servers or connectors, no web tools, no saved session, and shell commands in
Claude Code's sandbox (writes only inside the run's folder). The arms alternate, so that time affects both alike.
Every run's full transcript (stream-json) is kept in OUT/runs/; score.py reads them.
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_fixture  # noqa: E402

ARMS = ("rule", "placebo")
PROJECTS = Path.home() / ".claude" / "projects"
FLAGS = ["--setting-sources", "project",                       # the run's own CLAUDE.md only: no user settings, hooks or memory
         "--strict-mcp-config", "--mcp-config", '{"mcpServers": {}}',   # no MCP servers or connectors
         "--disallowedTools", "WebFetch", "WebSearch",
         "--settings", json.dumps({"sandbox": {"enabled": True, "autoAllowBashIfSandboxed": True}}),
         "--permission-mode", "acceptEdits",
         "--no-session-persistence",
         "--output-format", "stream-json", "--verbose"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def run_one(arm, k, runs, model, timeout):
    box = Path(tempfile.mkdtemp(prefix=f"porias-raw-data-{arm}-"))
    try:
        make_fixture.build(box)
        shutil.copy(HERE / "arms" / arm / "CLAUDE.md", box / "CLAUDE.md")
        cmd = ["claude", "-p", (HERE / "task.txt").read_text(encoding="utf-8").strip()] + FLAGS + (["--model", model] if model else [])
        name = f"{arm}-{k:02d}"
        t0 = time.time()
        with open(runs / f"{name}.jsonl", "w") as out, open(runs / f"{name}.err", "w") as err:
            try:
                code = subprocess.run(cmd, cwd=box, stdin=subprocess.DEVNULL, stdout=out, stderr=err, timeout=timeout).returncode
            except subprocess.TimeoutExpired:
                code = "timeout"
        return {"run": name, "arm": arm, "k": k, "box": str(box), "exit": code, "seconds": round(time.time() - t0, 1),
                "started": dt.datetime.fromtimestamp(t0).isoformat(timespec="seconds"), "memory_files": tidy(box, runs / f"{name}-memory")}
    finally:
        shutil.rmtree(box, ignore_errors=True)


def tidy(box, keep):
    """Claude Code keeps a folder per project under ~/.claude/projects (for its auto-memory): the run's own one, named
    after its sandbox, is moved into the results (KEEP) when the agent wrote anything there, then removed."""
    folder = PROJECTS / re.sub(r"[^A-Za-z0-9]", "-", str(Path(box).resolve()))
    if not folder.is_dir() or "porias-raw-data-" not in folder.name:
        return 0
    files = [p for p in folder.rglob("*") if p.is_file()]
    if files:
        shutil.copytree(folder, keep)
    shutil.rmtree(folder)
    return len(files)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", type=int, required=True, help="runs per arm")
    ap.add_argument("--out", required=True, help="results folder, such as results/2026-10-23")
    ap.add_argument("--model", default=None, help="model alias or id; default: the agent's own default")
    ap.add_argument("--timeout", type=int, default=900, help="seconds per run")
    a = ap.parse_args()
    out = (HERE / a.out).resolve()
    runs = out / "runs"
    runs.mkdir(parents=True, exist_ok=False)
    ref = json.loads(subprocess.run(["Rscript", str(HERE / "reference.R"), str(_fixture(out))], capture_output=True, text=True, check=True).stdout)
    shutil.rmtree(out / "fixture")
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=HERE, capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "status", "--porcelain", "--", "."], cwd=HERE, capture_output=True, text=True).stdout.strip())
    info = {"scenario": "raw-data", "date": dt.date.today().isoformat(), "runs_per_arm": a.runs, "model_requested": a.model,
            "commit": commit + ("+changes" if dirty else ""), "seed": make_fixture.SEED, "reference": ref,
            "claude_version": subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip(),
            "flags": FLAGS, "task_sha": sha(HERE / "task.txt"), "arm_sha": {arm: sha(HERE / "arms" / arm / "CLAUDE.md") for arm in ARMS}}
    (out / "run_info.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    with open(runs / "meta.jsonl", "a") as meta:
        for k in range(1, a.runs + 1):
            for arm in (ARMS if k % 2 else ARMS[::-1]):
                m = run_one(arm, k, runs, a.model, a.timeout)
                meta.write(json.dumps(m) + "\n")
                meta.flush()
                print(f"{m['run']}: exit {m['exit']}, {m['seconds']} s", flush=True)


def _fixture(out):
    make_fixture.build(out / "fixture")
    return out / "fixture"


if __name__ == "__main__":
    main()
