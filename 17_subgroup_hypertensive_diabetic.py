# শুধু Hypertensive রোগী
hyp_only = df[df['before_hypertension_mean_sbp_ge_140'] == 'Yes']

print("=" * 80)
print("SUBGROUP 1: Hypertensive Patients Only (SBP ≥ 140 before intervention)")
print(f"n = {len(hyp_only)}")
print("=" * 80)

tests = [
    ('before_mean_systolic_bp', 'after_mean_systolic_bp', 'Systolic BP (mmHg)', 'reduction'),
    ('before_mean_diastolic_bp', 'after_mean_diastolic_bp', 'Diastolic BP (mmHg)', 'reduction'),
    ('before_bmi', 'after_bmi', 'BMI', 'reduction'),
    ('before_weight_kg', 'after_weight_kg', 'Weight (kg)', 'reduction'),
    ('before_fbs', 'after_fbs', 'Fasting Blood Sugar', 'reduction'),
    ('before_hba1c', 'after_hba1c', 'HbA1c', 'reduction'),
]

for before_col, after_col, label, direction in tests:
    data = hyp_only[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{label} — insufficient data (n={n})")
        continue
    b = data[before_col]
    a = data[after_col]
    change = a.mean() - b.mean()
    change_pct = (change / b.mean()) * 100
    t, p2 = stats.ttest_rel(b, a)
    p1 = p2/2 if (direction=='reduction' and t>0) or (direction=='increase' and t<0) else 1-p2/2
    d = (b-a).mean() / (b-a).std()
    effect = 'Large' if abs(d)>=0.8 else ('Medium' if abs(d)>=0.5 else ('Small' if abs(d)>=0.2 else 'Negligible'))
    sig = '***' if p1<0.001 else ('**' if p1<0.01 else ('*' if p1<0.05 else 'ns'))
    reject = '✅ Reject H0' if p1<0.05 else '❌ Fail to Reject H0'
    print(f"\n{label} (n={n})")
    print(f"  Before: {b.mean():.2f} | After: {a.mean():.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t={t:.3f} | p={p1:.4f} {sig} | Cohen's d={d:.3f} ({effect})")
    print(f"  {reject}")

print("\n\n" + "=" * 80)
print("SUBGROUP 2: Diabetic Patients Only")
dm_only = df[df['before_diabetes_status'] == 'Diabetic']
print(f"n = {len(dm_only)}")
print("=" * 80)

for before_col, after_col, label, direction in tests:
    data = dm_only[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{label} — insufficient data (n={n})")
        continue
    b = data[before_col]
    a = data[after_col]
    change = a.mean() - b.mean()
    change_pct = (change / b.mean()) * 100
    t, p2 = stats.ttest_rel(b, a)
    p1 = p2/2 if (direction=='reduction' and t>0) or (direction=='increase' and t<0) else 1-p2/2
    d = (b-a).mean() / (b-a).std()
    effect = 'Large' if abs(d)>=0.8 else ('Medium' if abs(d)>=0.5 else ('Small' if abs(d)>=0.2 else 'Negligible'))
    sig = '***' if p1<0.001 else ('**' if p1<0.01 else ('*' if p1<0.05 else 'ns'))
    reject = '✅ Reject H0' if p1<0.05 else '❌ Fail to Reject H0'
    print(f"\n{label} (n={n})")
    print(f"  Before: {b.mean():.2f} | After: {a.mean():.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t={t:.3f} | p={p1:.4f} {sig} | Cohen's d={d:.3f} ({effect})")
    print(f"  {reject}")

print("\n\n" + "=" * 80)
print("SUBGROUP 3: Male Patients Only")
male_only = df[df['gender_clean'] == 'Male']
print(f"n = {len(male_only)}")
print("=" * 80)

for before_col, after_col, label, direction in tests:
    data = male_only[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{label} — insufficient data (n={n})")
        continue
    b = data[before_col]
    a = data[after_col]
    change = a.mean() - b.mean()
    change_pct = (change / b.mean()) * 100
    t, p2 = stats.ttest_rel(b, a)
    p1 = p2/2 if (direction=='reduction' and t>0) or (direction=='increase' and t<0) else 1-p2/2
    d = (b-a).mean() / (b-a).std()
    effect = 'Large' if abs(d)>=0.8 else ('Medium' if abs(d)>=0.5 else ('Small' if abs(d)>=0.2 else 'Negligible'))
    sig = '***' if p1<0.001 else ('**' if p1<0.01 else ('*' if p1<0.05 else 'ns'))
    reject = '✅ Reject H0' if p1<0.05 else '❌ Fail to Reject H0'
    print(f"\n{label} (n={n})")
    print(f"  Before: {b.mean():.2f} | After: {a.mean():.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t={t:.3f} | p={p1:.4f} {sig} | Cohen's d={d:.3f} ({effect})")
    print(f"  {reject}")

print("\n\n" + "=" * 80)
print("SUBGROUP 4: Female Patients Only")
female_only = df[df['gender_clean'] == 'Female']
print(f"n = {len(female_only)}")
print("=" * 80)

for before_col, after_col, label, direction in tests:
    data = female_only[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{label} — insufficient data (n={n})")
        continue
    b = data[before_col]
    a = data[after_col]
    change = a.mean() - b.mean()
    change_pct = (change / b.mean()) * 100
    t, p2 = stats.ttest_rel(b, a)
    p1 = p2/2 if (direction=='reduction' and t>0) or (direction=='increase' and t<0) else 1-p2/2
    d = (b-a).mean() / (b-a).std()
    effect = 'Large' if abs(d)>=0.8 else ('Medium' if abs(d)>=0.5 else ('Small' if abs(d)>=0.2 else 'Negligible'))
    sig = '***' if p1<0.001 else ('**' if p1<0.01 else ('*' if p1<0.05 else 'ns'))
    reject = '✅ Reject H0' if p1<0.05 else '❌ Fail to Reject H0'
    print(f"\n{label} (n={n})")
    print(f"  Before: {b.mean():.2f} | After: {a.mean():.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t={t:.3f} | p={p1:.4f} {sig} | Cohen's d={d:.3f} ({effect})")
    print(f"  {reject}")

print("\n\n" + "=" * 80)
print("SUBGROUP 5: Rural Patients Only")
rural_only = df[df['area'] == 'Rural']
print(f"n = {len(rural_only)}")
print("=" * 80)

for before_col, after_col, label, direction in tests:
    data = rural_only[[before_col, after_col]].dropna()
    n = len(data)
    if n < 10:
        print(f"\n{label} — insufficient data (n={n})")
        continue
    b = data[before_col]
    a = data[after_col]
    change = a.mean() - b.mean()
    change_pct = (change / b.mean()) * 100
    t, p2 = stats.ttest_rel(b, a)
    p1 = p2/2 if (direction=='reduction' and t>0) or (direction=='increase' and t<0) else 1-p2/2
    d = (b-a).mean() / (b-a).std()
    effect = 'Large' if abs(d)>=0.8 else ('Medium' if abs(d)>=0.5 else ('Small' if abs(d)>=0.2 else 'Negligible'))
    sig = '***' if p1<0.001 else ('**' if p1<0.01 else ('*' if p1<0.05 else 'ns'))
    reject = '✅ Reject H0' if p1<0.05 else '❌ Fail to Reject H0'
    print(f"\n{label} (n={n})")
    print(f"  Before: {b.mean():.2f} | After: {a.mean():.2f} | Change: {change:+.2f} ({change_pct:+.2f}%)")
    print(f"  t={t:.3f} | p={p1:.4f} {sig} | Cohen's d={d:.3f} ({effect})")
    print(f"  {reject}")
