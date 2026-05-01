# Stock Data Intelligence Dashboard

## Overview

This project is a full-stack Stock Data Intelligence Dashboard built using Python (Flask) and a single-page frontend application using HTML, CSS, and JavaScript. The system is designed to analyze, visualize, and compare stock market data using real-time data fetched from Yahoo Finance.

The project demonstrates backend API development, data processing using Pandas, and frontend visualization using Chart.js.

---

## Key Features

### 1. Stock Market Data Analysis

* Real-time stock data fetched using Yahoo Finance (`yfinance`)
* Historical data processing (default: 6 months)
* Computed metrics:

  * Daily Return
  * 7-day Moving Average
  * Volatility Index
  * Trend Detection (Uptrend / Downtrend)

---

### 2. Interactive Visualization Dashboard

* Dynamic stock price charts using Chart.js
* Click-based stock selection system
* Live update of:

  * High
  * Low
  * Average Close
  * Latest Price
* Graph-based trend analysis with min/max detection

---

### 3. Stock Comparison System

* Compare two stocks dynamically using backend API
* Example:

  * TCS.NS vs INFY.NS
  * INFY.NS vs RELIANCE.NS

Important usage rule:

* Always use full Yahoo Finance symbols
* Correct format: `TCS.NS`
* Incorrect format: `TCS`

---

### 4. Data Export Functionality

* Export stock data in:

  * CSV format
  * Excel (.xlsx format)

Note:

* Exported file corresponds to the currently selected stock only.

---

### 5. Insights Module

* Displays market performance insights:

  * Top Gainers
  * Top Losers
* Computed based on price movement over selected time range

---

## Tech Stack

### Backend

* Python 3.x
* Flask
* Pandas
* NumPy
* yFinance
* openpyxl (Excel export)

### Frontend (Single File Architecture)

* HTML5 (templates/index.html)
* CSS3 (embedded in same file or internal styling)
* JavaScript
* Chart.js

---

## Project Structure

```
stock_dashboard/
│
├── app.py
├── requirements.txt
│
└── templates/
    └── index.html
```

Note:

* Entire frontend UI, logic, and visualization are contained in a single file: `index.html`.

---

## Installation Instructions

### 1. Clone Repository

```
git clone https://github.com/Snigdha977/stock_dashboard
cd stock_dashboard
```

---

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install flask
pip install pandas
pip install numpy
pip install yfinance
pip install openpyxl
```

Or:

```
pip install -r requirements.txt
```

---

## Running the Project

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## API Endpoints

### 1. Get Companies

```
GET /companies
```

---

### 2. Stock Data

```
GET /data/<symbol>?days=30
```

Example:

```
/data/TCS.NS?days=30
```

---

### 3. Stock Summary

```
GET /summary/<symbol>
```

Returns:

* 52-week High
* 52-week Low
* Average Close
* Volatility

---

### 4. Compare Stocks

```
GET /compare?symbol1=TCS.NS&symbol2=INFY.NS
```

---

### 5. Market Insights

```
GET /insights
```

Returns:

* Top Gainer
* Top Loser

---

## Important Notes

* Always use valid Yahoo Finance stock symbols:

  * Correct: `TCS.NS`, `INFY.NS`, `RELIANCE.NS`
  * Incorrect: `TCS`, `INFY`, `RELIANCE`

* The comparison feature requires manual input via the Compare button in the UI.

* No database is used; all data is fetched dynamically using APIs.

---

## Known Limitations

* No persistent database storage
* No cloud deployment included
* Dependency on Yahoo Finance API availability
* No authentication system

---

## Future Improvements

* Database integration (SQLite/PostgreSQL)
* Cloud deployment (Render / AWS / Oracle Cloud)
* WebSocket-based real-time updates
* Machine learning-based stock prediction
* Advanced financial indicators (RSI, MACD)

---

## Author

Snigdha Saha
GitHub: [https://github.com/Snigdha977](https://github.com/Snigdha977)
