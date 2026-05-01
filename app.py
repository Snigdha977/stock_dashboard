from flask import Flask, jsonify, render_template, request, send_file
import pandas as pd
import yfinance as yf
import os

app = Flask(__name__)

COMPANIES = ["TCS.NS", "INFY.NS", "RELIANCE.NS"]


def fetch(symbol):
    try:
        df = yf.download(symbol, period="6mo", progress=False)

        if df is None or df.empty:
            return None

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()
        df["Date"] = df["Date"].astype(str)

        return df

    except Exception as e:
        print("Error:", e)
        return None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/companies")
def companies():
    return jsonify(COMPANIES)


@app.route("/data/<symbol>")
def data(symbol):
    df = fetch(symbol)
    if df is None:
        return jsonify([])

    return jsonify(df.tail(60)[["Date", "Close"]].to_dict(orient="records"))


@app.route("/summary/<symbol>")
def summary(symbol):
    df = fetch(symbol)
    if df is None:
        return jsonify({})

    return jsonify({
        "high": float(df["High"].max()),
        "low": float(df["Low"].min()),
        "avg": float(df["Close"].mean()),
        "latest": float(df["Close"].iloc[-1])
    })


@app.route("/compare")
def compare():
    s1 = request.args.get("symbol1")
    s2 = request.args.get("symbol2")

    df1 = fetch(s1)
    df2 = fetch(s2)

    if df1 is None or df2 is None:
        return jsonify({})

    return jsonify({
        "labels": df1["Date"].tail(40).tolist(),
        "s1": df1["Close"].tail(40).tolist(),
        "s2": df2["Close"].tail(40).tolist()
    })


@app.route("/insights")
def insights():
    result = []

    for c in COMPANIES:
        df = fetch(c)
        if df is None:
            continue

        change = float(df["Close"].iloc[-1] - df["Close"].iloc[0])

        result.append({
            "symbol": c,
            "change": change
        })

    result.sort(key=lambda x: x["change"], reverse=True)
    return jsonify(result)


@app.route("/download_csv/<symbol>")
def download_csv(symbol):
    df = fetch(symbol)
    if df is None:
        return "No data"

    file = f"{symbol}.csv"
    df.to_csv(file, index=False)
    return send_file(file, as_attachment=True)


@app.route("/download_xlsx/<symbol>")
def download_xlsx(symbol):
    df = fetch(symbol)
    if df is None:
        return "No data"

    file = f"{symbol}.xlsx"
    df.to_excel(file, index=False)
    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)