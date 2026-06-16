from pydantic import BaseModel

class QuoteResponse(BaseModel):
    symbol: str
    curr_price: float
    open: float
    high: float
    low: float
    prev_close: float
    source: str
    