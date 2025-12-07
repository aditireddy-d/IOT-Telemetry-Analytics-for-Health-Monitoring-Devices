# IOT-Telemetry-Analytics-for-Health-Monitoring-Devices# 🏥 Public Health Analytics for Rochester Regional Health

This project focuses on analyzing public health and nutrition data from the **USDA** to identify key predictors of obesity and physical inactivity across U.S. counties. The analysis was conducted for **Rochester Regional Health** to support data-driven public health planning.

---

## 🎯 Objective
- Identify the most significant predictors of **obesity rates** using multiple linear regression and ANOVA.
- Quantify relationships among **obesity**, **smoking**, **inactivity**, and **food access**.
- Visualize geographic trends and correlations to assist in regional health targeting.

---

## 🧮 Methodology
1. **Data Source:** USDA Food Environment Atlas, CDC Behavior Risk Data  
2. **Tools Used:** Minitab, Excel, Tableau, Python (Pandas, Matplotlib)  
3. **Techniques:**  
   - Multiple Linear Regression  
   - ANOVA and Correlation Analysis  
   - Quartile Mapping and Heatmap Visualization  

---

## 🔍 Key Findings
- **Inactivity** emerged as the **strongest predictor of obesity** (β = 1.0979).  
- Model performance achieved **R² = 57.18 %**.  
- Significant positive correlations:  
  - Smoking and Obesity (r = 0.384)  
  - Inactivity and Obesity (r = 0.710)  
- **Inverse relationship** between fast-food density and obesity prevalence.  

---

## 📊 Visualizations
- Tableau dashboards showing:
  - **Obesity heat maps**
  - **Inactivity quartiles**
  - **Smoking–obesity trends**
- Interactive filters for **state-wise exploration** and **BMI category segmentation**.

---

## 🧠 Insights for Rochester Regional Health
- Target counties with top-quartile inactivity for **intervention campaigns**.  
- Incorporate physical-activity metrics into **community wellness dashboards**.  
- Use dashboard analytics to prioritize **nutrition access and education programs**.

---

## ⚙️ Reproducibility

```bash
git clone https://github.com/<your-username>/public-health-analytics.git
cd public-health-analytics
pip install -r requirements.txt
```

Run the notebooks:
```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

---
