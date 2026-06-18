from fastapi import APIRouter, Query

from app.schemas.quote import QuoteResponse

from app.services import quoteService

router = APIRouter(tags=["Quote"])

@router.get("/quote", response_model=QuoteResponse)
async def get_quote(symbol: str = Query(..., min_length=1, max_length=10)):
    symbol = symbol.upper()
    data = await quoteService.fetch_quote(symbol)
    return {
        "symbol": symbol,
        "curr_price": data["c"],
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "prev_close": data["pc"],
        "source": "finnhub",
    }
    
    