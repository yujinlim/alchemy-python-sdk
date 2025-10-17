import requests
from crypto_alchemy.chain import ChainAPI
from crypto_alchemy.network import Network, get_network_url
from crypto_alchemy.token import TokenAPI
from crypto_alchemy.transfer import TransferAPI


class Client:
  def __init__(self, api_key: str, network: Network = Network.ETH_MAINNET):
    self.api_key = api_key
    self.network = network
    self.base_url = get_network_url(network) + api_key

    self.session = requests.Session()
    self.session.headers.update({
        "Content-Type": "application/json",
    })
    self.token = TokenAPI(self)
    self.transfer = TransferAPI(self)
    self.chain = ChainAPI(self)
