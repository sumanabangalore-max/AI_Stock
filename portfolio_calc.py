import yfinance as yf


def calculate_portfolio(portfolio):

    results = []
    total_invested = 0
    total_current = 0

    for ticker, data in portfolio.items():

        qty = data["qty"]
        buy_price = data["avg_price"]

        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d")

        if hist is None or hist.empty:
            continue

        current_price = hist["Close"].iloc[-1]

        invested = qty * buy_price
        current_value = qty * current_price
        pnl = current_value - invested
        return_pct = (pnl / invested) * 100

        results.append({
            "ticker": ticker,
            "qty": qty,
            "buy_price": round(buy_price, 2),
            "current_price": round(current_price, 2),
            "invested": round(invested, 2),
            "current_value": round(current_value, 2),
            "pnl": round(pnl, 2),
            "return_pct": round(return_pct, 2)
        })

        total_invested += invested
        total_current += current_value

    return results, total_invested, total_current, total_current - total_invested