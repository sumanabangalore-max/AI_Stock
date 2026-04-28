from portfolio import portfolio
from portfolio_calc import calculate_portfolio
from strategy import analyze_stock
from telegram_sender import send_telegram_message


results, invested, current, pnl = calculate_portfolio(portfolio)

# HEADER
message = "<b>📊 PORTFOLIO DASHBOARD</b>\n\n"

message += "<pre>"
message += (
"Ticker  Buy   Curr   Invested   Value     Ret%   Sig   Conf\n"
"------------------------------------------------------------\n"
)

for r in results:

    signal = analyze_stock(r["ticker"])

    message += (
        f"{r['ticker']:<7} "
        f"{r['buy_price']:<5} "
        f"{r['current_price']:<6} "
        f"{r['invested']:<10} "
        f"{r['current_value']:<8} "
        f"{r['return_pct']:<6}% "
        f"{signal['signal']:<5} "
        f"{signal['confidence']}\n"
    )

message += "</pre>"

# SUMMARY
message += (
    "\n\n📈 <b>SUMMARY</b>\n"
    f"Invested: {invested:.2f}\n"
    f"Current: {current:.2f}\n"
    f"P&L: {pnl:.2f}\n"
    f"Return: {(pnl/invested)*100:.2f}%\n"
)

send_telegram_message(message)