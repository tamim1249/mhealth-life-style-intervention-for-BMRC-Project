from scipy import stats

# --- Paired t-test + Wilcoxon + Effect Size (Cohen's d) ---
def cohen_d(before, after):
    diff = before - after
    return diff.mean() / diff.std()

pairs = [
    ('before_mean_systolic_bp', 'after_mean_systolic_bp', 'Systolic BP (mmHg)'),
    ('before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'Diastolic BP (mmHg)'),
    ('before_bmi', 'after_bmi', 'BMI'),
    ('before_weight_kg', 'after_weight_kg', 'Weight (kg)'),
    ('before_fbs', 'after_fbs', 'Fasting Blood Sugar'),
    ('before_rbs', 'after_rbs', 'Random Blood Sugar'),
    ('before_hba1c', 'after_hba1c', 'HbA1c'),
    ('before_total_cholesterol', 'after_total_cholesterol', 'Total Cholesterol'),
    ('before_ldl', 'after_ldl', 'LDL'),
    ('before_hdl', 'after_hdl', 'HDL'),
]

print("=== Pre-Post Analysis ===\n")
print(f"{'Variable':<25} {'N':>5} {'Before':>14} {'After':>14} {'Change':>8} {'t':>7} {'p':>8} {'Sig.':>5} {'Cohen d':>8}")
print("-" * 105)

rows = []
for before_col, after_col, label in pairs:
    data = df[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        continue
    b = data[before_col]
    a = data[after_col]
    mean_b = f"{b.mean():.2f}±{b.std():.2f}"
    mean_a = f"{a.mean():.2f}±{a.std():.2f}"
    change = a.mean() - b.mean()
    t, p_t = stats.ttest_rel(b, a)
    d = cohen_d(b, a)
    sig = '***' if p_t < 0.001 else ('**' if p_t < 0.01 else ('*' if p_t < 0.05 else 'ns'))
    print(f"{label:<25} {n:>5} {mean_b:>14} {mean_a:>14} {change:>8.2f} {t:>7.3f} {p_t:>8.4f} {sig:>5} {d:>8.3f}")
    rows.append([label, n, mean_b, mean_a, f"{change:.2f}", f"{t:.3f}", f"{p_t:.4f}", sig, f"{d:.3f}"])

# --- McNemar's test: Hypertension & Diabetes status change ---
print("\n=== McNemar's Test: Status Change ===\n")

# Hypertension
htn = df[['before_hypertension_mean_sbp_ge_140', 'after_hypertension_mean_sbp_ge_140']].dropna()
htn_ct = pd.crosstab(htn['before_hypertension_mean_sbp_ge_140'],
                     htn['after_hypertension_mean_sbp_ge_140'])
print("Hypertension Transition Table (Before → After):")
print(htn_ct)
b_val = htn_ct.loc['No', 'Yes'] if 'Yes' in htn_ct.columns else 0
c_val = htn_ct.loc['Yes', 'No'] if 'Yes' in htn_ct.index else 0
mcnemar_htn = (abs(b_val - c_val) - 1)**2 / (b_val + c_val)
p_htn = stats.chi2.sf(mcnemar_htn, df=1)
sig = '***' if p_htn < 0.001 else ('**' if p_htn < 0.01 else ('*' if p_htn < 0.05 else 'ns'))
print(f"McNemar chi2 = {mcnemar_htn:.3f}, p = {p_htn:.4f} {sig}")
print(f"Improved (Yes→No): {c_val} | Worsened (No→Yes): {b_val}\n")

# Diabetes
dm = df[['before_diabetes_status', 'after_diabetes_status']].dropna()
dm_ct = pd.crosstab(dm['before_diabetes_status'], dm['after_diabetes_status'])
print("Diabetes Transition Table (Before → After):")
print(dm_ct)
b_val2 = dm_ct.loc['Non-diabetic', 'Diabetic']
c_val2 = dm_ct.loc['Diabetic', 'Non-diabetic']
mcnemar_dm = (abs(b_val2 - c_val2) - 1)**2 / (b_val2 + c_val2)
p_dm = stats.chi2.sf(mcnemar_dm, df=1)
sig2 = '***' if p_dm < 0.001 else ('**' if p_dm < 0.01 else ('*' if p_dm < 0.05 else 'ns'))
print(f"McNemar chi2 = {mcnemar_dm:.3f}, p = {p_dm:.4f} {sig2}")
print(f"Remission (Diabetic→Non-diabetic): {c_val2} | New cases (Non-diabetic→Diabetic): {b_val2}")
