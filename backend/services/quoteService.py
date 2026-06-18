import os
from dotenv import load_dotenv
import httpx

load_dotenv()

async def fetch_quote(symbol: str) -> dict:
    key = os.getenv("FINNHUB_API_KEY")

    if not key:
        raise RuntimeError("FINNHUB_API_KEY is missing")

    async with httpx.AsyncClient(timeout=10) as client:
        response = httpx.get(
        "https://finnhub.io/api/v1/quote",
        params={"symbol": symbol},
        headers={"X-Finnhub-Token":key},
        timeout=10,
    )
    
    response.raise_for_status()
    return response.json()

