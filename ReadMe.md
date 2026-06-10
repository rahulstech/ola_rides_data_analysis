# 🚗 OLA Ride Data Analysis

An interactive data analysis dashboard built with **Streamlit** that explores and visualizes ride-booking data from OLA. The project covers the full analytics pipeline — from raw data cleaning and SQL-based querying to rich, interactive visualizations powered by Plotly and Tableau.

## 🔴 Live Demo

👉 **[Open the Live App](https://ola-ride-da-by-rahulbagchi.streamlit.app/)**

---

## ✨ Features

| Section | Description |
|---|---|
| **Overall** | KPI cards (total rides, completed rides, cancellation rate, total revenue, avg. customer rating), daily ride volume line chart, and booking status donut chart. |
| **Vehicle Type** | Per-vehicle breakdown of total booking value, successful booking value, average distance travelled, and total distance travelled. |
| **Revenue** | Revenue split by payment method, top 5 customers by booking value, and daily ride distance scatter plot. |
| **Cancellation** | Cancellation reason analysis — separate tabs for customer-initiated and driver-initiated cancellations with bar charts. |
| **Ratings** | Average customer and driver ratings displayed per vehicle type with vehicle images. |
| **Embedded Tableau** | Interactive Tableau Public dashboard embedded directly in the app for advanced visual exploration. |

---

## 🛠️ Tech Stack

- **Frontend / Dashboard** — [Streamlit](https://streamlit.io/)
- **Visualizations** — [Plotly Express](https://plotly.com/python/plotly-express/) · [Tableau Public](https://public.tableau.com/)
- **Data Processing** — [Pandas](https://pandas.pydata.org/)
- **Database** — [SQLite3](https://www.sqlite.org/)
- **Language** — Python 3

---

## 📁 Project Structure

```
ola_ride/
├── app/
│   ├── app.py                  # Main Streamlit app entry point & sidebar navigation
│   ├── database.py             # SQLite database connection & query functions
│   ├── overall.py              # Overall KPIs, ride volume & booking status charts
│   ├── vehicle_type.py         # Vehicle-type breakdown table
│   ├── revenue.py              # Revenue analysis charts (payment method, top customers, distance)
│   ├── cancellation.py         # Cancellation reason analysis (customer & driver tabs)
│   ├── ratings.py              # Customer & driver rating cards per vehicle type
│   └── embedded_tableau.py     # Embedded Tableau Public dashboard
│
├── data/
│   ├── OLA_DataSet.xlsx        # Raw dataset
│   └── OLA_Rides_Clean.xlsx    # Cleaned dataset
│
├── notebooks/
│   ├── eda_and_cleaning.ipynb        # Exploratory data analysis & data cleaning
│   └── sqlite_data_export.ipynb      # Script to export cleaned data into SQLite
│
├── sql/
│   ├── ola_rides.sqlite3       # SQLite database file
│   └── sql_queries.sql         # Standalone SQL queries for analysis
│
├── requirements.txt            # Python dependencies
├── ReadMe.md                   # This file
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rahulstech/ola_rides_data_analysis.git
   cd ola_rides_data_analysis
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app/app.py
   ```

   The app will open in your browser at `http://localhost:8501`.

---

## 📊 SQL Queries

The `sql/sql_queries.sql` file contains **10 standalone analytical queries** covering common business questions:

| # | Query |
|---|---|
| 1 | Retrieve all successful bookings |
| 2 | Average ride distance per vehicle type (top 5) |
| 3 | Total rides cancelled by customers |
| 4 | Top 5 customers by number of bookings |
| 5 | Driver cancellations due to personal & car-related issues |
| 6 | Max & min driver ratings for Prime Sedan |
| 7 | All rides paid via UPI |
| 8 | Average customer rating per vehicle type |
| 9 | Total booking value of completed rides |
| 10 | All incomplete rides with reasons |

---

## 📓 Notebooks

| Notebook | Purpose |
|---|---|
| `eda_and_cleaning.ipynb` | Exploratory data analysis, null handling, and data cleaning on the raw OLA dataset. |
| `sqlite_data_export.ipynb` | Exports the cleaned DataFrame into the SQLite database (`ola_rides.sqlite3`). |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📝 License

This project is open source and available for educational and portfolio purposes.

---