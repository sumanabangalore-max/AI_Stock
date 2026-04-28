import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def generate_summary(stock_data, pnl_summary):

    # SAFETY CHECK (VERY IMPORTANT)
    if not os.getenv("OPENROUTER_API_KEY"):
        return "❌ Missing OpenRouter API Key in .env"

    prompt = f"""
You are a stock analyst.

Keep response STRICTLY under 8-10 lines.

Stock Data:
{stock_data}

Portfolio:
{pnl_summary}

Give:
- Buy/Hold/Sell
- Risk level
- 1-line explanation per stock
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content