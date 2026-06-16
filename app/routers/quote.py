from fastapi import APIRouter, Query

from app.schemas.quote import QuoteResponse

router = APIRouter(tags=["Quote"])

@router.get("/quote", response_model=QuoteResponse)
def get_quote(symbol: str = Query(...,
        min_length=1, max_length=10)):
    symbol = symbol.upper()

    return QuoteResponse(
        symbol=symbol,
        high = 196.2,
        low=180.2,
        prev_close=190.1,
        source="local test",
    )
    
    