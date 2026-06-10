from scipy import stats
import numpy as np

print("=" * 90)
print("HYPOTHESIS TESTING: Effect of mHealth Intervention")
print("=" * 90)

tests = [
    ('before_mean_systolic_bp', 'after_mean_systolic_bp', 'Systolic BP (mmHg)', 'reduction'),
    ('before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'Diastolic BP (mmHg)', 'reduction'),
    ('before_bmi', 'after_bmi', 'BMI', 'reduction'),
    ('before_weight_kg', 'after_weight_kg', 'Weight (kg)', 'reduction'),
    ('before_fbs', 'after_fbs', 'Fasting Blood Sugar', 'reduction'),
    ('before_rbs', 'after_rbs', 'Random Blood Sugar', 'reduction'),
    ('before_hba1c', 'after_hba1c', 'HbA1c', 'reduction'),
    ('before_total_cholesterol', 'after_total_cholesterol', 'Total Cholesterol', 'reduction'),
    ('before_ldl', 'after_ldl', 'LDL', 'reduction'),
    ('before_hdl', 'after_hdl', 'HDL', 'increase'),
]

for before_col, after_col, label, direction in tests:
    data = df[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{'─'*90}")
        print(f"Variable : {label}")
        print(f"  ⚠️  Insufficient data (n={n}) — cannot test")
        continue

    b = data[before_col]
    a = data[after_col]
    mean_b = b.mean()
    mean_a = a.mean()
    change = mean_a - mean_b
    change_pct = (change / mean_b) * 100
    t_stat, p_two = stats.ttest_rel(b, a)
    # One-tailed p
    if direction == 'reduction':
        p_one = p_two / 2 if t_stat > 0 else 1 - p_two / 2
    else:
        p_one = p_two / 2 if t_stat < 0 else 1 - p_two / 2

    sig = '***' if p_one < 0.001 else ('**' if p_one < 0.01 else ('*' if p_one < 0.05 else 'ns'))
    reject = p_one < 0.05

    # Cohen's d
    diff = b - a
    d = diff.mean() / diff.std()
    effect = 'Large' if abs(d) >= 0.8 else ('Medium' if abs(d) >= 0.5 else ('Small' if abs(d) >= 0.2 else 'Negligible'))

    print(f"\n{'─'*90}")
    print(f"Variable : {label}  (n={n})")
    print(f"  H0 : No significant change after intervention (mean_before = mean_after)")
    if direction == 'reduction':
        print(f"  H1 : Significant REDUCTION after intervention (mean_before > mean_after)")
    else:
        print(f"  H1 : Significant INCREASE after intervention (mean_before < mean_after)")
    print(f"  Before : {mean_b:.2f} | After : {mean_a:.2f} | Change : {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t = {t_stat:.3f} | p (one-tailed) = {p_one:.4f} | {sig}")
    print(f"  Cohen's d = {d:.3f} ({effect} effect)")
    if reject:
        if direction == 'reduction':
            print(f"  ✅ REJECT H0 → Significant reduction of {abs(change):.2f} units ({abs(change_pct):.2f}%) — p={p_one:.4f} {sig}")
        else:
            print(f"  ✅ REJECT H0 → Significant increase of {abs(change):.2f} units ({abs(change_pct):.2f}%) — p={p_one:.4f} {sig}")
    else:
        print(f"  ❌ FAIL TO REJECT H0 → No significant change observed — p={p_one:.4f} {sig}")

print(f"\n{'='*90}")
print("Significance: *** p<0.001 | ** p<0.01 | * p<0.05 | ns = not significant")
print("Effect size : Large ≥0.8 | Medium ≥0.5 | Small ≥0.2 | Negligible <0.2")
