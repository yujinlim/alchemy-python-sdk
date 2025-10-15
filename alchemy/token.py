from alchemy.models import TokenBalancesResponse, TokenMetadata


class TokenAPI():
    metadata_cache: dict[str, TokenMetadata] = {}

    def __init__(self, client):
        self.client = client

    def get_balances(self, address: str, token_specs: list[str] | None = None) -> TokenBalancesResponse:
        url = self.client.base_url
        params = [
            address
        ]
        if token_specs and len(token_specs):
            params.append(token_specs)

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "alchemy_getTokenBalances",
            "params": params,
        }
        response = self.client.session.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            return TokenBalancesResponse(**data["result"])
        
        raise Exception(f"Error fetching token balances: {data}")

    def get_token_metadata(self, contract_address: str) -> TokenMetadata:
        if self.metadata_cache.get(contract_address):
            return self.metadata_cache[contract_address]
        
        url = self.client.base_url
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "alchemy_getTokenMetadata",
            "params": [
                contract_address,
            ],
        }
        response = self.client.session.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            metadata = TokenMetadata(**data["result"], address=contract_address)
            self.metadata_cache[contract_address] = metadata
            return metadata

        raise Exception(f"Error fetching token metadata: {data}")