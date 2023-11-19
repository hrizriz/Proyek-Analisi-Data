# Proyek-Analisis-Data

## This repository provides a step-by-step guide for analyzing datasets to address business questions:

- Identify Business Questions: Clearly define the specific business problems the analysis aims to solve.
- Data Preparation: Assess, clean, and transform data into a usable format, ensuring its accuracy, completeness, and consistency.
- Exploratory Data Analysis: Uncover patterns, trends, and relationships using data visualization techniques and statistical measures.
- Visualization & Explanatory Analysis: Create informative charts and graphs to effectively communicate insights, and perform in-depth analysis to extract deeper understanding from the data.
- Conclusion: Summarize the key findings of the analysis and draw meaningful conclusions that directly address the business questions.
- Creating a Simple Dashboard: Utilize Streamlit to construct a straightforward and user-friendly dashboard.

# Proyek Analisis Data

## SETUP environement

Jalankan perintah dibawah ini
```
conda create --name main-ds python=3.9
conda activate main-ds
```
Install library yang dibutuhkan, seperti:

- `numpy`
- `jupyter`
- `matplotlib`
- `pandas`
- `seaborn`
- `streamlit`

Ketikan perintah pada terminal:
```
pip install numpy jupyter matplotlib pandas seaborn streamlit
```
## Jalankan Streamlit App
Ketikan
```
streamlit run dashboard.py
```

## Tampilan ketika menjalankan Streamlit

**Akan menampilkan:**
- Rata-rata Penyewaan Sepeda per Harinya
  ![Alt Text](assets/avg.png)
- Penyewa Sepeda pada Tiap Jamnya
  ![Alt Text](assets/per_hour.png)
- Total Penyewaan Sepeda per Harinya
  ![Alt Text](assets/per_day.png)
