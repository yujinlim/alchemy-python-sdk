# Alchemy Python SDK

A Python SDK for the Alchemy API, built with requests and pydantic for type-safe API interactions.

## Installation

```bash
pip install alchemy-python-sdk
```

Or install from source:

```bash
pip install -e .
```

## Quick Start

```python
from alchemy import Client

client = Client(api_key="your_api_key_here", network=Network.ETH)

balances = client.token.get_token_balances("address")
print(balances)
```

## Features

- **Type-safe models**: All request and response models are defined using Pydantic for automatic validation
- **Error handling**: Proper exception handling for common API errors (401, 404, 400, etc.)
- **Bearer token authentication**: Simple API key-based authentication

## Usage Examples
## Development

## TODO
- [ ] Token API
- [ ] NFT API
- [ ] Portfolio API
- [ ] Transfers API
- [ ] Prices API
- [ ] Simulation API
- [ ] Utility API

### Install development dependencies

```bash
pip install -e ".[dev]"
```

### Run tests

```bash
pytest
```

## License

Apache License 2.0

## Support

For API support, contact: cs@1stDigital.com