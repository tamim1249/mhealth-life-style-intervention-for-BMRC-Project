from scipy import stats

# --- Binary outcome column ---
df['improved'] = (df['overall_followup_remark'] == 'Improved after follow-up').astype(int)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# --- Improvement by Age Group ---
ax = axes[0, 0]
age_imp = df.groupby('age_group')['improved'].mean().mul(100).round(1)
age_imp.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
ax.set_title('Improvement Rate by Age Group', fontweight='bold')
ax.set_xlabel('Age Group')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

# --- Improvement by Gender ---
ax = axes[0, 1]
gender_imp = df.groupby('gender_clean')['improved'].mean().mul(100).round(1)
gender_imp.plot(kind='bar', ax=ax, color='mediumpurple', edgecolor='black')
ax.set_title('Improvement Rate by Gender', fontweight='bold')
ax.set_xlabel('Gender')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

# --- Improvement by Area ---
ax = axes[0, 2]
area_imp = df.groupby('area')['improved'].mean().mul(100).round(1)
area_imp.plot(kind='bar', ax=ax, color='teal', edgecolor='black')
ax.set_title('Improvement Rate by Area', fontweight='bold')
ax.set_xlabel('Area')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

# --- Improvement by Diabetes Status ---
ax = axes[1, 0]
dm_imp = df.groupby('before_diabetes_status')['improved'].mean().mul(100).round(1)
dm_imp.plot(kind='bar', ax=ax, color='mediumseagreen', edgecolor='black')
ax.set_title('Improvement Rate by Diabetes Status', fontweight='bold')
ax.set_xlabel('Diabetes Status (Before)')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

# --- Improvement by Hypertension Status ---
ax = axes[1, 1]
htn_imp = df.groupby('before_hypertension_mean_sbp_ge_140')['improved'].mean().mul(100).round(1)
htn_imp.plot(kind='bar', ax=ax, color='tomato', edgecolor='black')
ax.set_title('Improvement Rate by Hypertension Status', fontweight='bold')
ax.set_xlabel('Hypertensive Before (SBP ≥ 140)')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

# --- Improvement by Number of Visits ---
ax = axes[1, 2]
visit_imp = df.groupby('number_of_visits_jan_may_2026')['improved'].mean().mul(100).round(1)
visit_imp.plot(kind='bar', ax=ax, color='goldenrod', edgecolor='black')
ax.set_title('Improvement Rate by Number of Visits', fontweight='bold')
ax.set_xlabel('Number of Visits')
ax.set_ylabel('Improved (%)')
ax.set_ylim(0, 100)
ax.axhline(53.6, color='red', linestyle='--', label='Overall avg')
ax.legend()
ax.tick_params(axis='x', rotation=0)

plt.suptitle('Subgroup Analysis: Who Improved?', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Statistical Tests ---
print("=== Chi-Square Tests: Improvement vs Subgroups ===\n")

subgroups = [
    ('gender_clean', 'Gender'),
    ('area', 'Area'),
    ('before_diabetes_status', 'Diabetes Status'),
    ('before_hypertension_mean_sbp_ge_140', 'Hypertension Status'),
    ('age_group', 'Age Group'),
]

for col, label in subgroups:
    ct = pd.crosstab(df[col], df['improved'])
    chi2, p, dof, _ = stats.chi2_contingency(ct)
    sig = '***' if p < 0.001 else ('**' if p < 0.01 else ('*' if p < 0.05 else 'ns'))
    print(f"{label:<30} chi2={chi2:.2f}  p={p:.4f}  {sig}")

print("\n*** p<0.001  ** p<0.01  * p<0.05  ns = not significant")

# --- Improvement rate by visits detail ---
print("\n=== Improvement Rate by Number of Visits ===")
print(df.groupby('number_of_visits_jan_may_2026')['improved'].agg(['mean', 'count'])
      .rename(columns={'mean': 'Improvement Rate', 'count': 'N'})
      .assign(**{'Improvement Rate': lambda x: (x['Improvement Rate'] * 100).round(1)}))
