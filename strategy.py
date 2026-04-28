import yfinance as yf
from ta.momentum import RSIIndicator


def analyze_stock(ticker):

    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo")

    close = hist["Close"]

    rsi = RSIIndicator(close).rsi().iloc[-1]
    price = close.iloc[-1]

    # SIMPLE LOGIC
    if rsi < 30:
        signal = "BUY"
        confidence = 80
    elif rsi > 70:
        signal = "SELL"
        confidence = 75
    else:
        signal = "HOLD"
        confidence = 50

    return {
        "ticker": ticker,
        "signal": signal,
        "confidence": confidence
    }