# The raw-data scenario's known answer: the adjusted odds ratio for treatment, fitted to the fixture.
# Rscript reference.R DIR   (DIR holds data/trial.csv, from make_fixture.py); prints one line of JSON.
args <- commandArgs(trailingOnly = TRUE)
d <- read.csv(file.path(args[1], "data", "trial.csv"))
d$arm <- factor(d$arm, levels = c("control", "treatment"))
fit <- glm(outcome ~ arm + age + sex, family = binomial, data = d)
b <- coef(summary(fit))["armtreatment", ]
wald <- exp(b[["Estimate"]] + c(-1, 1) * qnorm(0.975) * b[["Std. Error"]])
cat(sprintf('{"or": %.4f, "wald_low": %.4f, "wald_high": %.4f, "n": %d}\n', exp(b[["Estimate"]]), wald[1], wald[2], nrow(d)))
