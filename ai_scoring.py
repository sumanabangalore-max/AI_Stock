def calculate_confidence(rsi, trend_score):

    score = 50  # base neutral

    # RSI contribution
    if rsi < 30:
        score += 25
    elif rsi > 70:
        score -= 25

    # Trend contribution
    score += trend_score

    # clamp 0–100
    return max(0, min(100, score))