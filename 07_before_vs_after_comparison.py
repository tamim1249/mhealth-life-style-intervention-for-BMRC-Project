from scipy import stats

# --- Box Plots: Before vs After ---
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

comparisons = [
    ('before_mean_systolic_bp', 'after_mean_systolic_bp', 'Systolic BP (mmHg)', 'darkorange'),
    ('before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'Diastolic BP (mmHg)', 'mediumvioletred'),
    ('before_bmi', 'after_bmi', 'BMI', 'dodgerblue'),
    ('before_fbs', 'after_fbs', 'Fasting Blood Sugar', 'mediumseagreen'),
    ('before_rbs', 'after_rbs', 'Random Blood Sugar', 'tomato'),
    ('before_weight_kg', 'after_weight_kg', 'Weight (kg)', 'slateblue'),
]

for ax, (before_col, after_col, title, color) in zip(axes.flatten(), comparisons):
    data = df[[before_col, after_col]].dropna()
    ax.boxplot(
        [data[before_col], data[after_col]],
        labels=['Before', 'After'],
        patch_artist=True,
        boxprops=dict(facecolor=color, alpha=0.6),
        medianprops=dict(color='black', linewidth=2)
    )
    ax.set_title(title)
    ax.set_ylabel(title)

plt.suptitle('Before vs After Intervention: Key Clinical Measures', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Paired t-test & Wilcoxon ---
print("=" * 65)
print(f"{'Variable':<30} {'Mean Before':>11} {'Mean After':>10} {'Change':>8} {'p-value':>10}")
print("=" * 65)

test_pairs = [
    ('before_mean_systolic_bp', 'after_mean_systolic_bp', 'Systolic BP'),
    ('before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'Diastolic BP'),
    ('before_bmi', 'after_bmi', 'BMI'),
    ('before_weight_kg', 'after_weight_kg', 'Weight (kg)'),
    ('before_fbs', 'after_fbs', 'Fasting Blood Sugar'),
    ('before_rbs', 'after_rbs', 'Random Blood Sugar'),
    ('before_hba1c', 'after_hba1c', 'HbA1c'),
    ('before_total_cholesterol', 'after_total_cholesterol', 'Total Cholesterol'),
    ('before_ldl', 'after_ldl', 'LDL'),
    ('before_hdl', 'after_hdl', 'HDL'),
]

for before_col, after_col, label in test_pairs:
    data = df[[before_col, after_col]].dropna()
    if len(data) < 10:
        print(f"{label:<30} {'Insufficient data':>30}")
        continue
    t_stat, p_val = stats.wilcoxon(data[before_col], data[after_col])
    mean_before = data[before_col].mean()
    mean_after = data[after_col].mean()
    change = mean_after - mean_before
    sig = '***' if p_val < 0.001 else ('**' if p_val < 0.01 else ('*' if p_val < 0.05 else 'ns'))
    print(f"{label:<30} {mean_before:>11.2f} {mean_after:>10.2f} {change:>8.2f} {p_val:>8.4f} {sig}")

print("=" * 65)
print("*** p<0.001  ** p<0.01  * p<0.05  ns = not significant")

# --- Hypertension & Diabetes Status Change ---
print("\n--- Hypertension Status Change ---")
htn = df[['before_hypertension_mean_sbp_ge_140', 'after_hypertension_mean_sbp_ge_140']].dropna()
print(pd.crosstab(htn['before_hypertension_mean_sbp_ge_140'],
                  htn['after_hypertension_mean_sbp_ge_140'],
                  rownames=['Before'], colnames=['After']))

print("\n--- Diabetes Status Change ---")
dm = df[['before_diabetes_status', 'after_diabetes_status']].dropna()
print(pd.crosstab(dm['before_diabetes_status'],
                  dm['after_diabetes_status'],
                  rownames=['Before'], colnames=['After']))
