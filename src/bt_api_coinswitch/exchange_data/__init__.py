from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    "get_exchange_info": "GET /v2/info",
    "get_tick": "GET /v2/ticker/",
    "get_trade_history": "GET /v2/trades/",
    "make_order": "POST /v2/orders",
    "cancel_order": "DELETE /v2/orders/",
    "get_open_orders": "GET /v2/orders",
    "get_balance": "GET /v2/balance",
    "get_account": "GET /v2/account",
}


class CoinSwitchExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "COINSWITCH___SPOT"
        self.rest_url = "https://api.coinswitch.co"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {}
        self.legal_currency = ["INR", "USDT", "BTC", "ETH"]

    def get_symbol(self, symbol: str) -> str:
        return symbol.upper().replace("/", "").replace("-", "").replace("_", "")

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]


class CoinSwitchExchangeDataSpot(CoinSwitchExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
