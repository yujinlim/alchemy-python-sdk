from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator
from enum import Enum

class TransferCategory(str, Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"
    ERC20 = "erc20"
    ERC721 = "erc721"
    ERC1155 = "erc1155"
    SPECIAL_NFT = "specialnft"

@dataclass
class AssetTransferParams:
    fromBlock: str | None = None
    toBlock: str | None = None
    fromAddress: str | None = None
    toAddress: str | None = None
    excludeZeroValue: bool = False
    contractAddress: str | None = None
    category: list[TransferCategory] | None = None
    order: str = "desc"
    withMetadata: bool = False
    maxCount: int | None = None
    pageKey: str | None = None
    
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

class TransferDetail(BaseModel):
    block_num: str = Field(..., alias="blockNum")
    unique_id: str = Field(..., alias="uniqueId")
    hash: str
    from_address: str = Field(..., alias="from")
    to_address: str = Field(..., alias="to")
    value: Optional[Decimal] = None
    erc721_token_id: Optional[str] = Field(None, alias="erc721TokenId")
    erc1155_metadata: Optional[List[Dict[str, Any]]] = Field(None, alias="erc1155Metadata")
    token_id: Optional[str] = Field(None, alias="tokenId")
    asset: Optional[str] = None
    category: str
    raw_contract: Dict[str, Any] = Field(..., alias="rawContract")
    metadata: Optional[Dict[str, Any]] = None

class TransferResponse(BaseModel):
    transfers: List[TransferDetail]
    page_key: Optional[str] = Field(None, alias="pageKey")

class ChainBlockDetails(BaseModel):
    base_fee_per_gas: str = Field(..., alias="baseFeePerGas")
    blob_gas_used: str = Field(..., alias="blobGasUsed")
    excess_blob_gas: str = Field(..., alias="excessBlobGas")
    number: str
    hash: str
    parent_hash: str = Field(..., alias="parentHash")
    nonce: str
    sha3_uncles: str = Field(..., alias="sha3Uncles")
    logs_bloom: str = Field(..., alias="logsBloom")
    transactions_root: str = Field(..., alias="transactionsRoot")
    state_root: str = Field(..., alias="stateRoot")
    receipts_root: str = Field(..., alias="receiptsRoot")
    miner: str
    difficulty: int
    total_difficulty: int = Field(..., alias="totalDifficulty")
    extra_data: str = Field(..., alias="extraData")
    size: int
    gas_limit: int = Field(..., alias="gasLimit")
    gas_used: int = Field(..., alias="gasUsed")
    transactions: List[Any]
    uncles: List[str]
    milli_timestamp: int = Field(..., alias="milliTimestamp")
    timestamp: int = Field(..., alias="timestamp")
    mix_hash: str = Field(..., alias="mixHash")
    partner_beacon_block_root: str = Field(..., alias="parentBeaconBlockRoot")
    requests_hash: str = Field(..., alias="requestsHash")
    uncles: List[str] = Field(..., alias="uncles")
    withdrawals: List[Any]
    withdrawals_root: str = Field(..., alias="withdrawalsRoot")

    @field_validator("timestamp", "milli_timestamp", "gas_limit", "gas_used", "size", "total_difficulty", "difficulty", mode="before")
    def hex_to_int(cls, v):
        if isinstance(v, str) and v.startswith("0x"):
            return int(v, 16)
        if v is None:
            return 0
        return v