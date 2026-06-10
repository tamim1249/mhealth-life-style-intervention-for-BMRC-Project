# Fix area typo
df['area'] = df['area'].replace('Suurban', 'Suburban')

# --- Clinical Profile Plots ---
plt.figure(figsize=(16, 14))

# --- Hypertension (Before) ---
plt.subplot(3, 3, 1)
df['before_hypertension_mean_sbp_ge_140'].value_counts().plot(kind='bar', color=['steelblue','tomato'], edgecolor='black')
plt.title('Hypertension Before')
plt.xlabel('Hypertensive (SBP ≥ 140)')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Diabetes Status (Before) ---
plt.subplot(3, 3, 2)
df['before_diabetes_status'].value_counts().plot(kind='bar', color=['mediumseagreen','salmon'], edgecolor='black')
plt.title('Diabetes Status Before')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Smoking Status ---
plt.subplot(3, 3, 3)
df['smoking_status'].value_counts().plot(kind='bar', color='slategray', edgecolor='black')
plt.title('Smoking Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=30, ha='right')

# --- Smokeless Tobacco ---
plt.subplot(3, 3, 4)
df['smokeless_tobacco'].value_counts().plot(kind='bar', color='peru', edgecolor='black')
plt.title('Smokeless Tobacco Use')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=30, ha='right')

# --- Family History Diabetes ---
plt.subplot(3, 3, 5)
df['family_history_diabetes'].value_counts().plot(kind='bar', color='orchid', edgecolor='black')
plt.title('Family History: Diabetes')
plt.xlabel('')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Family History Heart ---
plt.subplot(3, 3, 6)
df['family_history_heart_circulatory'].value_counts().plot(kind='bar', color='crimson', edgecolor='black')
plt.title('Family History: Heart/Circulatory')
plt.xlabel('')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- BMI Before ---
plt.subplot(3, 3, 7)
df['before_bmi'].dropna().hist(bins=25, color='dodgerblue', edgecolor='black')
plt.title('BMI Distribution (Before)')
plt.xlabel('BMI')
plt.ylabel('Count')

# --- Systolic BP Before ---
plt.subplot(3, 3, 8)
df['before_mean_systolic_bp'].dropna().hist(bins=25, color='darkorange', edgecolor='black')
plt.title('Systolic BP Distribution (Before)')
plt.xlabel('SBP (mmHg)')
plt.ylabel('Count')

# --- Diastolic BP Before ---
plt.subplot(3, 3, 9)
df['before_mean_diastolic_bp'].dropna().hist(bins=25, color='mediumvioletred', edgecolor='black')
plt.title('Diastolic BP Distribution (Before)')
plt.xlabel('DBP (mmHg)')
plt.ylabel('Count')

plt.suptitle('Clinical Profile (Before Intervention)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Summary Stats ---
print("BMI (Before) - Summary:")
print(df['before_bmi'].describe().round(2))
print("\nSystolic BP (Before) - Summary:")
print(df['before_mean_systolic_bp'].describe().round(2))
print("\nDiastolic BP (Before) - Summary:")
print(df['before_mean_diastolic_bp'].describe().round(2))
