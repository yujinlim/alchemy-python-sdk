from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class TokenBalance(BaseModel):
    contract_address: str = Field(..., alias="contractAddress")
    token_balance: int = Field(..., alias="tokenBalance")

    @field_validator("token_balance", mode="before")
    def parse_hex(cls, v):
        if isinstance(v, str) and v.startswith("0x"):
            return int(v, 16)
        return v

class TokenBalancesResponse(BaseModel):
    address: str
    token_balances: List[TokenBalance] = Field(..., alias="tokenBalances")

class TokenMetadata(BaseModel):
    decimals: int
    name: str
    symbol: str
    logo: Optional[str] = None
    address: str