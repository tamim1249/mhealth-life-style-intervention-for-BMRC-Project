
corr_cols = [
    'age_numeric',
    'before_mean_systolic_bp', 'after_mean_systolic_bp', 'change_mean_systolic_bp',
    'before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'change_mean_diastolic_bp',
    'before_bmi', 'after_bmi', 'change_bmi',
    'before_weight_kg', 'after_weight_kg', 'change_weight_kg',
    'number_of_visits_jan_may_2026',
    'completeness_score_pct',
    'improved'
]

corr_df = df[corr_cols].copy()
corr_matrix = corr_df.corr()

# --- Heatmap ---
plt.figure(figsize=(16, 12))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    fmt='.2f',
    cmap='RdYlGn',
    center=0,
    vmin=-1, vmax=1,
    linewidths=0.5,
    annot_kws={'size': 8},
    square=True,
    cbar_kws={'shrink': 0.8}
)
plt.title('Correlation Heatmap: Key Clinical Variables', fontsize=15, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(fontsize=9)
plt.tight_layout()
plt.show()

# --- Improved এর সাথে correlation ---
print("=== Correlation with Improvement Outcome ===\n")
imp_corr = corr_matrix['improved'].drop('improved').sort_values(key=abs, ascending=False)
print(imp_corr.round(3).to_string())

# --- Change variables heatmap ---
change_cols = [c for c in corr_cols if 'change_' in c] + ['improved']
change_corr = df[change_cols].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(
    change_corr,
    annot=True,
    fmt='.2f',
    cmap='RdYlGn',
    center=0,
    vmin=-1, vmax=1,
    linewidths=0.5,
    square=True,
    cbar_kws={'shrink': 0.8}
)
plt.title('Correlation: Change Variables + Improvement', fontsize=13, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(fontsize=9)
plt.tight_layout()
plt.show()
