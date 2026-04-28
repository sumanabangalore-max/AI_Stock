def portfolio_risk(stock_signals):

    risk_score = 0

    for s in stock_signals:

        if s["confidence"] < 30:
            risk_score += 2
        elif s["confidence"] > 70:
            risk_score -= 1

    if risk_score >= 3:
        return "HIGH"
    elif risk_score >= 1:
        return "MEDIUM"
    else:
        return "LOW"