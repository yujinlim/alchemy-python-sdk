import requests
from alchemy.network import Network, get_network_url
from alchemy.token import TokenAPI


class Client:
  def __init__(self, api_key: str, network: Network = Network.ETH_MAINNET):
    self.api_key = api_key
    self.network = network
    self.base_url = get_network_url(network) + api_key

    self.session = requests.Session()
    self.token = TokenAPI(self)
