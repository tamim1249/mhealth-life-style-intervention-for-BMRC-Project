# --- Age Distribution ---
plt.figure(figsize=(16, 12))

plt.subplot(2, 3, 1)
df['age_numeric'].dropna().hist(bins=20, color='steelblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

# --- Age Group ---
bins = [0, 30, 45, 60, 75, 120]
labels = ['≤30', '31-45', '46-60', '61-75', '75+']
df['age_group'] = pd.cut(df['age_numeric'], bins=bins, labels=labels)

plt.subplot(2, 3, 2)
df['age_group'].value_counts().sort_index().plot(kind='bar', color='coral', edgecolor='black')
plt.title('Age Group Distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Gender ---
plt.subplot(2, 3, 3)
df['gender'].str.strip().str.capitalize().value_counts().plot(kind='bar', color='mediumpurple', edgecolor='black')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Area ---
plt.subplot(2, 3, 4)
df['area'].value_counts().plot(kind='bar', color='teal', edgecolor='black')
plt.title('Rural vs Urban')
plt.xlabel('Area')
plt.ylabel('Count')
plt.xticks(rotation=0)

# --- Education ---
plt.subplot(2, 3, 5)
df['education'].value_counts().plot(kind='bar', color='goldenrod', edgecolor='black')
plt.title('Education Level')
plt.xlabel('Education')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')

# --- Life Style ---
plt.subplot(2, 3, 6)
df['life_style'].value_counts().plot(kind='bar', color='olivedrab', edgecolor='black')
plt.title('Lifestyle / Activity Level')
plt.xlabel('Lifestyle')
plt.ylabel('Count')
plt.xticks(rotation=0)

plt.suptitle('Demographic Overview', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# --- Print summary ---
print("Gender (normalized):\n", df['gender'].str.strip().str.capitalize().value_counts())
print("\nArea:\n", df['area'].value_counts())
print("\nEducation:\n", df['education'].value_counts())
