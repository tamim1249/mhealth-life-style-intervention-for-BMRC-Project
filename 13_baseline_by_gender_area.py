from scipy import stats

# --- Numeric: Gender comparison ---
print("=== Baseline Comparison by Gender (Mean ± SD) ===\n")
print(f"{'Variable':<30} {'Female (n=1452)':>18} {'Male (n=1211)':>16} {'p-value':>10} {'Sig.':>5}")
print("-" * 85)

numeric_baseline = [
    ('age_numeric', 'Age (years)'),
    ('before_mean_systolic_bp', 'Systolic BP (mmHg)'),
    ('before_mean_diastolic_bp', 'Diastolic BP (mmHg)'),
    ('before_bmi', 'BMI'),
    ('before_weight_kg', 'Weight (kg)'),
    ('before_fbs', 'Fasting Blood Sugar'),
    ('before_rbs', 'Random Blood Sugar'),
    ('before_hba1c', 'HbA1c'),
]

for col, label in numeric_baseline:
    female = df[df['gender_clean'] == 'Female'][col].dropna()
    male = df[df['gender_clean'] == 'Male'][col].dropna()
    if len(female) < 5 or len(male) < 5:
        continue
    t, p = stats.ttest_ind(female, male)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    f_str = f"{female.mean():.2f} ± {female.std():.2f}"
    m_str = f"{male.mean():.2f} ± {male.std():.2f}"
    print(f"{label:<30} {f_str:>18} {m_str:>16} {p:>10.4f} {sig:>5}")

# --- Categorical: Gender comparison ---
print("\n--- Categorical Variables by Gender ---\n")
cat_baseline = [
    ('before_diabetes_status', 'Diabetes Status'),
    ('before_hypertension_mean_sbp_ge_140', 'Hypertension'),
    ('area', 'Area'),
    ('smoking_status', 'Smoking Status'),
]
for col, label in cat_baseline:
    ct = pd.crosstab(df['gender_clean'], df[col])
    chi2, p, _, _ = stats.chi2_contingency(ct)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    print(f"{label:<30} chi2={chi2:.3f}  p={p:.4f}  {sig}")

# --- Numeric: Area comparison ---
print("\n=== Baseline Comparison by Area (Mean ± SD) ===\n")
print(f"{'Variable':<30} {'Rural':>18} {'Urban':>16} {'p-value':>10} {'Sig.':>5}")
print("-" * 85)

for col, label in numeric_baseline:
    rural = df[df['area'] == 'Rural'][col].dropna()
    urban = df[df['area'] == 'Urban'][col].dropna()
    if len(rural) < 5 or len(urban) < 5:
        continue
    t, p = stats.ttest_ind(rural, urban)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    r_str = f"{rural.mean():.2f} ± {rural.std():.2f}"
    u_str = f"{urban.mean():.2f} ± {urban.std():.2f}"
    print(f"{label:<30} {r_str:>18} {u_str:>16} {p:>10.4f} {sig:>5}")

# --- Categorical: Area comparison ---
print("\n--- Categorical Variables by Area ---\n")
for col, label in cat_baseline:
    area_df = df[df['area'].isin(['Rural', 'Urban'])]
    ct = pd.crosstab(area_df['area'], area_df[col])
    chi2, p, _, _ = stats.chi2_contingency(ct)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    print(f"{label:<30} chi2={chi2:.3f}  p={p:.4f}  {sig}")
