# bt_api_coinswitch

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_coinswitch.svg)](https://pypi.org/project/bt_api_coinswitch/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_coinswitch.svg)](https://pypi.org/project/bt_api_coinswitch/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_coinswitch/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_coinswitch/actions)
[![Docs](https://readthedocs.org/projects/bt-api-coinswitch/badge/?version=latest)](https://bt-api-coinswitch.readthedocs.io/)

---

> **CoinSwitch exchange plugin for bt_api** — Unified REST API for **Spot** trading.

`bt_api_coinswitch` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **CoinSwitch** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-coinswitch.readthedocs.io/ |
| Chinese Docs | https://bt-api-coinswitch.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coinswitch |
| PyPI | https://pypi.org/project/bt_api_coinswitch/ |
| Issues | https://github.com/cloudQuant/bt_api_coinswitch/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | Description |
|---|---|---|---|
| Spot | `COINSWITCH___SPOT` | ✅ | Spot trading |

### Supported Operations

| Category | Operation | Spot |
|---|---|---|
| **Market Data** | `get_tick` / `get_ticker` | ✅ |
| | `get_all_tickers` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_trade_history` / `get_trades` | ✅ |
| **Trading** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `get_open_orders` | ✅ |
| **Account** | `get_balance` | ✅ |
| | `get_account` | ✅ |

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# Spot market data (public - no auth required)
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")

# Account balance (requires auth)
balance = api.get_balance("COINSWITCH___SPOT")

# Place order (requires auth)
order = api.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
```

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_coinswitch
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_coinswitch
cd bt_api_coinswitch
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## Quick Start

### 1. Install

```bash
pip install bt_api_coinswitch
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")
print(f"BTC spot price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
print(f"Order placed: {order}")
```

---

## Architecture

```
bt_api_coinswitch/
├── plugin.py                           # register_plugin() — bt_api plugin entry point
├── registry_registration.py             # register() — plugin registration
├── exchange_data/
│   └── __init__.py                 # CoinSwitchExchangeData, CoinSwitchExchangeDataSpot
├── feeds/
│   ├── request_base.py              # CoinSwitchRequestData — REST base class
│   └── live_coinswitch/
│       ├── spot.py                  # CoinSwitchRequestDataSpot — spot operations
│       └── __init__.py
├── containers/
│   ├── tickers/
│   ├── balances/
│   ├── orders/
│   ├── orderbooks/
│   ├── bars/
│   └── accounts/
└── errors/
    └── coinswitch_translator.py  # CoinSwitchErrorTranslator
```

---

## Supported Symbols

- **Spot**: `BTC`, `ETH`, `XRP`, `USDT`, and 100+ trading pairs

---

## Exchange Code

```
COINSWITCH___SPOT     # Spot trading
```

---

## Error Handling

All CoinSwitch API errors are translated to bt_api_base `ApiError` subclasses.

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-coinswitch.readthedocs.io/ |
| **中文** | https://bt-api-coinswitch.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coinswitch/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 CoinSwitch 交易所插件** — 为**现货**交易提供统一的 REST API。

`bt_api_coinswitch` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **CoinSwitch** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-coinswitch.readthedocs.io/ |
| 中文文档 | https://bt-api-coinswitch.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_coinswitch |
| PyPI | https://pypi.org/project/bt_api_coinswitch/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_coinswitch/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | 说明 |
|---|---|---|---|
| 现货 | `COINSWITCH___SPOT` | ✅ | 现货交易 |

### 支持的操作

| 类别 | 操作 | 现货 |
|---|---|---|
| **行情数据** | `get_tick` / `get_ticker` | ✅ |
| | `get_all_tickers` | ✅ |
| | `get_exchange_info` | ✅ |
| | `get_trade_history` / `get_trades` | ✅ |
| **交易** | `make_order` | ✅ |
| | `cancel_order` | ✅ |
| | `get_open_orders` | ✅ |
| **账户** | `get_balance` | ✅ |
| | `get_account` | ✅ |

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    },
})

# 现货行情（公开接口，无需认证）
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")

# 账户余额（需要认证）
balance = api.get_balance("COINSWITCH___SPOT")

# 下单（需要认证）
order = api.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
```

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_coinswitch
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_coinswitch
cd bt_api_coinswitch
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_coinswitch
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")
print(f"BTC 现货价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
print(f"订单已下单: {order}")
```

---

## 架构

```
bt_api_coinswitch/
├── plugin.py                           # register_plugin() — bt_api 插件入口点
├── registry_registration.py             # register() — 插件注册
├── exchange_data/
│   └── __init__.py                 # CoinSwitchExchangeData, CoinSwitchExchangeDataSpot
├── feeds/
│   ├── request_base.py              # CoinSwitchRequestData — REST 基类
│   └── live_coinswitch/
│       ├── spot.py                  # CoinSwitchRequestDataSpot — 现货操作
│       └── __init__.py
├── containers/
│   ├── tickers/
│   ├── balances/
│   ├── orders/
│   ├── orderbooks/
│   ├── bars/
│   └── accounts/
└── errors/
    └── coinswitch_translator.py  # CoinSwitchErrorTranslator
```

---

## 支持的交易对

- **现货**: `BTC`, `ETH`, `XRP`, `USDT` 等 100+ 交易对

---

## 交易所代码

```
COINSWITCH___SPOT     # 现货交易
```

---

## 错误处理

所有 CoinSwitch API 错误均翻译为 bt_api_base `ApiError` 子类。

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-coinswitch.readthedocs.io/ |
| **中文文档** | https://bt-api-coinswitch.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_coinswitch/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com