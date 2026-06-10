# mHealth-Enabled Lifestyle Intervention to Reduce Hypertension and Diabetes Risk, North-Western Bangladesh

**BMRC mHealth Project** | Rangpur, North-Western Bangladesh | 2026

---

## About This Project

This repository contains the complete data analysis pipeline for the BMRC mHealth study — a community-based intervention trial conducted in Rangpur, North-Western Bangladesh. The study evaluated the effectiveness of mobile health (mHealth) tools in reducing hypertension and diabetes risk through lifestyle modification.

**Study Highlights:**
- Total participants: **N = 2,663** (1,452 female, 1,211 male)
- Study area: Rural, Urban, Suburban — Rangpur division
- Primary outcomes: Blood pressure, BMI, fasting blood sugar, HbA1c
- Follow-up period: January – May 2026
- Dataset: `Before_After_Intervention_Comparison.csv`

---

## Repository Structure

The codebase is organized into **17 sequential Python scripts**. Each script is self-contained and corresponds to a specific analysis step. Run them in order for reproducible results.

| # | File Name | Description | Key Libraries |
|---|-----------|-------------|---------------|
| 01 | `01_setup_imports.py` | Setup & Imports | numpy, pandas, os, kagglehub |
| 02 | `02_load_data.py` | Load Dataset | pandas |
| 03 | `03_basic_overview.py` | Basic Data Overview | pandas, numpy, matplotlib, seaborn |
| 04 | `04_missing_values.py` | Missing Value Analysis | pandas, seaborn, matplotlib |
| 05 | `05_demographic_overview.py` | Demographic Visualizations | matplotlib, pandas |
| 06 | `06_clinical_profile.py` | Clinical Profile (Before Intervention) | matplotlib, pandas |
| 07 | `07_before_vs_after.py` | Before vs After Comparison | scipy, matplotlib, pandas |
| 08 | `08_outcome_analysis.py` | Followup Outcome Analysis | matplotlib, pandas |
| 09 | `09_subgroup_analysis.py` | Subgroup Analysis (Improvement Rate) | scipy, matplotlib, pandas |
| 10 | `10_correlation_heatmap.py` | Correlation Heatmap | numpy, seaborn, matplotlib |
| 11 | `11_statistical_tests.py` | Paired t-test + Cohen's d | scipy, pandas |
| 12 | `12_descriptive_statistics.py` | Descriptive Statistics | pandas |
| 13 | `13_baseline_by_gender_area.py` | Baseline Comparison by Gender & Area | scipy, pandas |
| 14 | `14_prepost_effect_size.py` | Pre-Post + McNemar's + Effect Size | scipy, pandas |
| 15 | `15_between_group_comparison.py` | Improved vs Not Improved | scipy, pandas |
| 16 | `16_hypothesis_testing.py` | Hypothesis Testing (H0/H1) | scipy, numpy |
| 17 | `17_subgroup_hyp_dm_gender_area.py` | Subgroup: Hypertensive, Diabetic, Gender, Area, Rural | scipy, pandas |

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/bmrc-mhealth.git
cd bmrc-mhealth
```

**2. Install dependencies**
```bash
pip install pandas numpy scipy matplotlib seaborn
```

**3. Place the dataset in the correct path**
```
/kaggle/input/datasets/tamimm91437/mhealth/Before_After_Intervention_Comparison.csv
```

**4. Run scripts sequentially**
```bash
python 01_setup_imports.py
python 02_load_data.py
# ... continue through 17_subgroup_hyp_dm_gender_area.py
```

---

## Key Findings

- **Systolic BP:** Significant reduction after mHealth intervention (p < 0.001, ***)
- **Diastolic BP:** Significant reduction after mHealth intervention (p < 0.001, ***)
- **Overall improvement rate:** ~53.6% of participants showed clinical improvement
- **Hypertensive subgroup:** 74.6% improvement rate — highest among all subgroups
- **Diabetic subgroup:** 51.0% improvement; Non-diabetic: 55.8%
- **Rural vs Urban:** No significant difference in improvement rates
- **Gender:** No significant difference between male (55.5%) and female (51.9%)

---

## Statistical Methods

- Paired t-test — pre vs post within intervention group
- Wilcoxon signed-rank test — non-parametric pre-post comparison
- Independent t-test — control vs intervention at baseline & post
- McNemar's test — change in hypertension/diabetes status (binary)
- Chi-square test — categorical variable comparisons across subgroups
- Cohen's d — effect size for continuous outcome variables
- One-tailed hypothesis testing — directional H1 (reduction/increase)

---

## Citation

If you use this code or dataset in your research, please cite:

> BMRC mHealth Study — *mHealth-Enabled Lifestyle Intervention to Reduce Hypertension and Diabetes Risk, North-Western Bangladesh.* Dataset: tamimm91437/mhealth (Kaggle, 2026).

---

*BMRC mHealth Project • North-Western Bangladesh • 2026*
