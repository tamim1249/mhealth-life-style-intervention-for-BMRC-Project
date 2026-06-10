# --- Overall Followup Remark Distribution ---
plt.figure(figsize=(16, 12))

plt.subplot(2, 2, 1)
remark_counts = df['overall_followup_remark'].value_counts()
colors = ['mediumseagreen', 'tomato', 'steelblue', 'goldenrod']
plt.pie(remark_counts, labels=remark_counts.index, autopct='%1.1f%%',
        colors=colors, startangle=140)
plt.title('Overall Followup Outcome', fontsize=13, fontweight='bold')

# --- Remark by Gender ---
plt.subplot(2, 2, 2)
gender_remark = df.groupby(['gender', 'overall_followup_remark']).size().unstack(fill_value=0)
# Normalize gender
df['gender_clean'] = df['gender'].str.strip().str.capitalize()
gender_remark = df.groupby(['gender_clean', 'overall_followup_remark']).size().unstack(fill_value=0)
gender_remark.plot(kind='bar', ax=plt.gca(), colormap='Set2', edgecolor='black')
plt.title('Outcome by Gender', fontsize=13, fontweight='bold')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(fontsize=8, loc='upper right')

# --- Remark by Area ---
plt.subplot(2, 2, 3)
area_remark = df.groupby(['area', 'overall_followup_remark']).size().unstack(fill_value=0)
area_remark.plot(kind='bar', ax=plt.gca(), colormap='Set3', edgecolor='black')
plt.title('Outcome by Area', fontsize=13, fontweight='bold')
plt.xlabel('Area')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(fontsize=8, loc='upper right')

# --- Completeness Score Distribution ---
plt.subplot(2, 2, 4)
df['completeness_score_pct'].dropna().hist(bins=25, color='cornflowerblue', edgecolor='black')
plt.title('Completeness Score Distribution (%)', fontsize=13, fontweight='bold')
plt.xlabel('Completeness Score (%)')
plt.ylabel('Count')

plt.suptitle('Outcome & Data Quality Analysis', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Summary Prints ---
print("=== Overall Followup Remark ===")
print(df['overall_followup_remark'].value_counts())
print(f"\nTotal patients: {df['overall_followup_remark'].notna().sum()}")

print("\n=== Completeness Score Summary ===")
print(df['completeness_score_pct'].describe().round(2))

print("\n=== Number of Visits Summary ===")
print(df['number_of_visits_jan_may_2026'].describe().round(2))

print("\n=== Remark by Area (%) ===")
area_pct = df.groupby('area')['overall_followup_remark'].value_counts(normalize=True).mul(100).round(1).unstack()
print(area_pct)
