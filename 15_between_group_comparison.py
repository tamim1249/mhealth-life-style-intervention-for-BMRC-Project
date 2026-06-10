# --- Between-group: Improved vs Not Improved ---
print("=== Between-Group Comparison: Improved vs Not Improved ===\n")
print(f"{'Variable':<25} {'Improved (n=1426)':>20} {'Not Improved (n=763)':>22} {'p-value':>10} {'Sig.':>5}")
print("-" * 90)

df_imp = df[df['overall_followup_remark'] == 'Improved after follow-up']
df_not = df[df['overall_followup_remark'] == 'Not improved / worsened after follow-up']

numeric_vars = [
    ('age_numeric', 'Age (years)'),
    ('before_mean_systolic_bp', 'Systolic BP Before'),
    ('before_mean_diastolic_bp', 'Diastolic BP Before'),
    ('before_bmi', 'BMI Before'),
    ('before_weight_kg', 'Weight Before (kg)'),
    ('change_mean_systolic_bp', 'SBP Change'),
    ('change_mean_diastolic_bp', 'DBP Change'),
    ('change_bmi', 'BMI Change'),
    ('number_of_visits_jan_may_2026', 'Number of Visits'),
    ('completeness_score_pct', 'Completeness Score'),
]

for col, label in numeric_vars:
    g1 = df_imp[col].dropna()
    g2 = df_not[col].dropna()
    if len(g1) < 5 or len(g2) < 5:
        continue
    t, p = stats.ttest_ind(g1, g2)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    g1_str = f"{g1.mean():.2f} ± {g1.std():.2f}"
    g2_str = f"{g2.mean():.2f} ± {g2.std():.2f}"
    print(f"{label:<25} {g1_str:>20} {g2_str:>22} {p:>10.4f} {sig:>5}")

# --- Categorical: Improved vs Not Improved ---
print("\n--- Categorical Variables ---\n")
cat_vars = [
    ('gender_clean', 'Gender'),
    ('area', 'Area'),
    ('before_diabetes_status', 'Diabetes Status'),
    ('before_hypertension_mean_sbp_ge_140', 'Hypertension'),
    ('smoking_status', 'Smoking Status'),
    ('life_style', 'Lifestyle'),
    ('age_group', 'Age Group'),
]

for col, label in cat_vars:
    temp = df[df['overall_followup_remark'].isin([
        'Improved after follow-up',
        'Not improved / worsened after follow-up'
    ])]
    ct = pd.crosstab(temp['overall_followup_remark'], temp[col])
    chi2, p, _, _ = stats.chi2_contingency(ct)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    print(f"{label:<30} chi2={chi2:.3f}  p={p:.4f}  {sig}")

# --- Improvement rate table by key groups ---
print("\n=== Improvement Rate by Key Subgroups ===\n")
subgroups = [
    ('gender_clean', 'Gender'),
    ('area', 'Area'),
    ('before_diabetes_status', 'Diabetes Status'),
    ('before_hypertension_mean_sbp_ge_140', 'Hypertension'),
    ('age_group', 'Age Group'),
]

for col, label in subgroups:
    print(f"--- {label} ---")
    grp = df.groupby(col)['improved'].agg(
        N='count',
        Improved='sum'
    )
    grp['Improved %'] = (grp['Improved'] / grp['N'] * 100).round(1)
    print(grp.to_string())
    print()
