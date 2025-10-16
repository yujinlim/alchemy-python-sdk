from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum

class Network(str, Enum):
    ETH_MAINNET = "eth-mainnet"
    ETH_GOERLI = "eth-goerli"
    ETH_SEPOLIA = "eth-sepolia"
    POLYGON_MAINNET = "polygon-mainnet"
    POLYGON_MUMBAI = "polygon-mumbai"
    ARBITRUM_MAINNET = "arb-mainnet"
    ARBITRUM_GOERLI = "arb-goerli"
    OPTIMISM_MAINNET = "optimism-mainnet"
    OPTIMISM_GOERLI = "optimism-goerli"
    BNB_MAINNET = "bnb-mainnet"
    BNB_TESTNET = "bnb-testnet"

def get_network_url(network: Network) -> str:
    base_url = "https://{network}.g.alchemy.com/v2/"
    return base_url.format(network=network.value)
