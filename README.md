# 📊 Automated Reporting and Dashboard Scripts

This repository includes three Python scripts to generate professional reports and interactive dashboards using **Excel**, **Plotly Dash**, and **Streamlit**. These tools support various business intelligence and data reporting use cases.

---

## 📝 Script: `excel_summary_report.py`

**Purpose:**  
Generate a styled Excel summary report with tabular data and bar charts using `pandas` and `openpyxl`.

**Features:**
- Create and format Excel workbooks and sheets
- Write `pandas` DataFrames to Excel
- Apply styling (fonts, alignment, borders)
- Add bar charts with data-driven visuals

**Example Use Case:**
```python
data = pd.DataFrame({
    'Category': ['Electronics', 'Clothing', 'Furniture'],
    'Sales': [10000, 15000, 20000],
    'Profit': [2000, 3000, 4000]
})
generate_summary_report(data, 'summary_report.xlsx')
````

---

## 📈 Script: `plotly_dash_kpi_report.py`

**Purpose:**
Build an interactive KPI dashboard using **Dash** and **Plotly** for quick business insights.

**Features:**

* Load CSV data
* Display KPI cards (e.g., total/average/max/min sales)
* Visualize sales trends using bar, line, and pie charts
* Fully interactive and web-based

**Run the app:**

```bash
python plotly_dash_kpi_report.py
```

**Requirements:**

```bash
pip install dash pandas plotly
```

**Sample Visuals:**

* KPI Cards for summary metrics
* Sales by Category (Bar Chart)
* Sales Trend Over Time (Line Chart)
* Sales Distribution (Pie Chart)

---

## 📊 Script: `streamlit_sales_dashboard.py`

**Purpose:**
Create a modern, interactive sales dashboard using **Streamlit**, with support for charts and user input via sidebar filters.

**Features:**

* Load and explore CSV data
* Sidebar controls for date, sales, category, and product columns
* Visualizations: sales trend, category comparison, sales distribution, top products

**Run the dashboard:**

```bash
streamlit run streamlit_sales_dashboard.py
```

**Requirements:**

```bash
pip install streamlit pandas matplotlib seaborn plotly
```

**Included Charts:**

* 📉 Sales Trend (Matplotlib)
* 📊 Sales by Category (Plotly)
* 📈 Sales Distribution (Seaborn)
* 🏆 Top Products by Sales (Plotly)

---

## 📁 File Structure

```plaintext
.
├── excel_summary_report.py         # Excel report generation using openpyxl
├── plotly_dash_kpi_report.py      # Dash app for KPI visualizations
├── streamlit_sales_dashboard.py   # Streamlit dashboard for interactive sales analysis
└── README.md                      # This documentation
```

---

## 📦 Installation

Install required packages for all scripts:

```bash
pip install pandas openpyxl dash streamlit matplotlib seaborn plotly
```

---
