# Numeric variables
numeric_cols = [
    'age_numeric', 'before_mean_systolic_bp', 'before_mean_diastolic_bp',
    'before_bmi', 'before_weight_kg', 'before_height_cm',
    'before_fbs', 'before_rbs', 'before_hba1c',
    'before_total_cholesterol', 'before_ldl', 'before_hdl',
    'number_of_visits_jan_may_2026', 'completeness_score_pct'
]

desc = df[numeric_cols].describe().T
desc['median'] = df[numeric_cols].median()
desc['skewness'] = df[numeric_cols].skew().round(3)
desc = desc[['count', 'mean', 'std', '50%', 'min', 'max', 'skewness']]
desc.columns = ['N', 'Mean', 'SD', 'Median', 'Min', 'Max', 'Skewness']
desc = desc.round(2)
print("=== Descriptive Statistics (Numeric Variables) ===\n")
print(desc.to_string())

# Categorical variables
cat_cols = [
    'gender_clean', 'area', 'education', 'life_style',
    'smoking_status', 'before_diabetes_status',
    'before_hypertension_mean_sbp_ge_140', 'overall_followup_remark'
]

print("\n=== Descriptive Statistics (Categorical Variables) ===\n")
for col in cat_cols:
    counts = df[col].value_counts()
    pct = df[col].value_counts(normalize=True).mul(100).round(1)
    table = pd.DataFrame({'N': counts, '%': pct})
    print(f"--- {col} ---")
    print(table.to_string())
    print()
