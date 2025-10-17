from dataclasses import asdict
import json
from crypto_alchemy.models import AssetTransferParams, TransferResponse


class TransferAPI():
    def __init__(self, client):
        self.client = client

    def get_asset_transfers(self, params: AssetTransferParams) -> TransferResponse:
        url = self.client.base_url
        params = asdict(params)
        
        for key in list(params.keys()):
            if params[key] is None:
                del params[key]

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "alchemy_getAssetTransfers",
            "params": params,
        }
        response = self.client.session.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if "result" in data:
            return TransferResponse(**data["result"])

        raise Exception(f"Error fetching token transfers: {data}")
