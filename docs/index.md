# CoinSwitch Documentation

<!-- English -->
## English

Welcome to the **CoinSwitch** documentation for bt_api.

**CoinSwitch** is a cryptocurrency exchange offering Spot trading with support for multiple legal currencies (INR, USDT, BTC, ETH).

### Overview

`bt_api_coinswitch` provides a unified interface to CoinSwitch exchange through the bt_api plugin architecture. It supports:

- **Spot Trading**: Market data and order placement for spot pairs
- **Market Data**: Ticker, All Tickers, Exchange Info, Trade History
- **Account**: Balance queries, Account information

### Installation

```bash
pip install bt_api_coinswitch
```

### Quick Start

```python
from bt_api_py import BtApi

# Initialize without authentication (public data only)
api = BtApi()

# Spot ticker (public)
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")
print(f"BTC spot: {ticker}")

# With authentication
api_auth = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# Get balance
balance = api_auth.get_balance("COINSWITCH___SPOT")

# Place order
order = api_auth.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
```

### Supported Operations

#### Spot (COINSWITCH___SPOT)

| Operation | Auth Required | Description |
|-----------|---------------|-------------|
| `get_tick` / `get_ticker` | No | Rolling ticker |
| `get_all_tickers` | No | All market tickers |
| `get_exchange_info` | No | Market listings |
| `get_trade_history` / `get_trades` | No | Trade execution records |
| `get_balance` | Yes | Asset balances |
| `get_account` | Yes | Account information |
| `make_order` | Yes | Place order |
| `cancel_order` | Yes | Cancel pending order |
| `get_open_orders` | Yes | Get all open orders |

### Supported Symbols

- **Spot**: `BTC`, `ETH`, `XRP`, `USDT`, and 100+ trading pairs

### Exchange Codes

```
COINSWITCH___SPOT     # Spot trading
```

### Error Handling

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINSWITCH___SPOT")
except Exception as e:
    print(f"Error: {e}")
```

### More Information

- [GitHub Repository](https://github.com/cloudQuant/bt_api_coinswitch)
- [Issue Tracker](https://github.com/cloudQuant/bt_api_coinswitch/issues)
- [bt_api Documentation](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base Documentation](https://bt-api-base.readthedocs.io/)

---

## 中文

欢迎使用 bt_api 的 **CoinSwitch** 文档。

**CoinSwitch** 是一家加密货币交易所，提供现货交易，支持多种法定货币（INR、USDT、BTC、ETH）。

### 概述

`bt_api_coinswitch` 通过 bt_api 插件架构提供连接 CoinSwitch 交易所的统一接口。支持：

- **现货交易**：现货交易对的市场数据和下单
- **行情数据**：行情、全行情、交易所信息、成交历史
- **账户**：余额查询、账户信息

### 安装

```bash
pip install bt_api_coinswitch
```

### 快速开始

```python
from bt_api_py import BtApi

# 初始化（无需认证，仅获取公开数据）
api = BtApi()

# 现货行情（公开接口）
ticker = api.get_tick("COINSWITCH___SPOT", "BTC")
print(f"BTC 现货: {ticker}")

# 需要认证的操作
api_auth = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

# 获取余额
balance = api_auth.get_balance("COINSWITCH___SPOT")

# 下单
order = api_auth.make_order(
    exchange_name="COINSWITCH___SPOT",
    symbol="BTC",
    side="buy",
    order_type="limit",
    amount=0.001,
    price=50000,
)
```

### 支持的操作

#### 现货 (COINSWITCH___SPOT)

| 操作 | 需要认证 | 说明 |
|------|---------|------|
| `get_tick` / `get_ticker` | 否 | 滚动行情 |
| `get_all_tickers` | 否 | 所有市场行情 |
| `get_exchange_info` | 否 | 市场列表 |
| `get_trade_history` / `get_trades` | 否 | 成交记录 |
| `get_balance` | 是 | 资产余额 |
| `get_account` | 是 | 账户信息 |
| `make_order` | 是 | 下单 |
| `cancel_order` | 是 | 取消挂单 |
| `get_open_orders` | 是 | 获取所有挂单 |

### 支持的交易对

- **现货**: `BTC`, `ETH`, `XRP`, `USDT` 等 100+ 交易对

### 交易所代码

```
COINSWITCH___SPOT     # 现货交易
```

### 错误处理

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "COINSWITCH___SPOT": {
        "api_key": "invalid_key",
        "secret": "invalid_secret",
    }
})

try:
    balance = api.get_balance("COINSWITCH___SPOT")
except Exception as e:
    print(f"错误: {e}")
```

### 更多信息

- [GitHub 仓库](https://github.com/cloudQuant/bt_api_coinswitch)
- [问题反馈](https://github.com/cloudQuant/bt_api_coinswitch/issues)
- [bt_api 文档](https://cloudquant.github.io/bt_api_py/)
- [bt_api_base 文档](https://bt-api-base.readthedocs.io/)