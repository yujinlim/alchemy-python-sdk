from crypto_alchemy.models import ChainBlockDetails, TransferResponse


class ChainAPI():
    def __init__(self, client):
        self.client = client

    def get_block_by_number(self, block_number: str, hydrated_transactions: bool = False) -> TransferResponse:
        url = self.client.base_url
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_getBlockByNumber",
            "params": [block_number, hydrated_transactions],
        }
        response = self.client.session.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            return ChainBlockDetails(**data["result"])

        raise Exception(f"Error fetching token transfers: {data}")
