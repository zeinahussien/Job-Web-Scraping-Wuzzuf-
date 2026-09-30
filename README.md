# Wuzzuf Job Market Scraper & Data Cleaning Pipeline

An automated web scraping and data preprocessing pipeline built with **Python**, **Selenium**, and **Pandas** to collect, clean, and structure real-time job market intelligence across key technical tracks in Egypt.

---

## 🛠️ Tech Stack
* **Language:** Python (Jupyter Notebooks)
* **Web Automation & Scraping:** Selenium WebDriver, Chrome Options
* **Data Manipulation & Cleaning:** Pandas
* **Version Control:** Git & GitHub

---

## 🎯 Project Overview & Objectives
This project automates the extraction of job listings across four technical tracks, handle dynamic web elements (such as pagination and shadow DOM overlays), removes duplicates by job URL, standardizes column formats, and structures employment and work mode details into clean CSV files.

### Target Job Tracks:
* Data Engineer
* Data Science
* AI Developer
* Machine Learning Engineer

---

## 🔄 Pipeline Architecture

### 1. Automated Web Scraping (`app.ipynb`)
* **Browser Configuration:** Instantiates a headless-ready Google Chrome driver configured with anti-automation detection bypasses (`--disable-blink-features=AutomationControlled`).
* **Multi-Track Iteration:** Dynamically loops through specified tech tracks, handles search queries, and navigates through multi-page pagination with safety caps.
* **Robust Extraction:** Extracts core job attributes using precise relative XPaths and tag-matching:
  * `Track`
  * `Job Title`
  * `Company`
  * `Location`
  * `Job Type`
  * `Job Experience` (with fallback handling)
  * `Job URL` (unique identifier)
* **Output:** Exports raw data to `wuzzuf_jobs.csv`.

### 2. Data Preprocessing & Transformation (`cleaning.ipynb`)
* **Duplicate Deduplication:** Identifies and handles duplicate job URLs across overlapping tracks, merging them into a unified multi-track column.
* **Standardization:** Standardizes column headers to lowercase snake_case and strips extraneous whitespace across all string fields.
* **Feature Engineering:** Parses and splits composite employment types into distinct categorical dimensions (`employment_type` and `work_mode`).
* **Output:** Saves the polished dataset as `wuzzuf_jobs_cleaned.csv`.

### 3. Interactive Intelligence Dashboard (`app_dashboard.py` & `style.css`)
- **Dark Grey & Pastel Aesthetic:** Styled using an external custom CSS sheet (`style.css`) and dark-themed Plotly charts featuring soft pastel palettes.
- **Control Center:** Provides sidebar filters for tech tracks, work modes, and real-time keyword search.
- **Dynamic Metrics & Visuals:** Displays active listings, hiring counts, remote shares, top hiring company bar charts, and work mode distribution pie charts.
- **Live Feed Explorer:** Renders a clean, interactive data table providing direct access to original Wuzzuf job postings.
  
---

## 📊 Dataset Schema (`wuzzuf_jobs_cleaned.csv`)

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `track` | String | Tech domain search category |
| `job_title` | String | Official title of the position |
| `company` | String | Hiring organization name |
| `location` | String | Geographic work location |
| `employment_type` | String | Contract type (e.g., Full Time, Internship) |
| `work_mode` | String | Setup environment (On-site, Remote, Hybrid) |
| `job_experience` | String | Required years of experience |
| `job_url` | String | Direct hyperlink to the Wuzzuf posting |

---

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone [https://github.com/zeinahussien/Wuzzuf-Job-Scraper.git](https://github.com/zeinahussien/Wuzzuf-Job-Scraper.git)
2. Ensure you have the required dependencies installed:
   ```bash
   pip install selenium pandas 
3. Run the scraping notebook to harvest raw data:
   ```bash
   Open and execute app.ipynb
4. Run the cleaning notebook to process the dataset:
   ```bash
   Open and execute cleaning.ipynb
5. Launch the interactive dashboard:
   ```bash
   streamlit run app_dashboard.py
