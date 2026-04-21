from __future__ import annotations

from typing import Any

from bt_api_coinswitch.feeds.live_coinswitch.request_base import CoinSwitchRequestData


class CoinSwitchRequestDataSpot(CoinSwitchRequestData):
    """CoinSwitch Spot REST Feed."""

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)

    # Market data

    def get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    get_ticker = get_tick
    async_get_ticker = async_get_tick

    def get_all_tickers(self, extra_data=None, **kwargs):
        path, params, extra = self._get_all_tickers(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_all_tickers(self, extra_data=None, **kwargs):
        path, params, extra = self._get_all_tickers(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_trade_history(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_trade_history(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_trade_history(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_trade_history(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    get_trades = get_trade_history
    async_get_trades = async_get_trade_history

    # Trading

    def make_order(self, symbol, side, order_type, amount, price=None, extra_data=None, **kwargs):
        path, body, extra = self._make_order(
            symbol, side, order_type, amount, price, extra_data, **kwargs
        )
        return self.request(path, body=body, extra_data=extra)

    async def async_make_order(
        self, symbol, side, order_type, amount, price=None, extra_data=None, **kwargs
    ):
        path, body, extra = self._make_order(
            symbol, side, order_type, amount, price, extra_data, **kwargs
        )
        return await self.async_request(path, body=body, extra_data=extra)

    def cancel_order(self, order_id, extra_data=None, **kwargs):
        path, params, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_cancel_order(self, order_id, extra_data=None, **kwargs):
        path, params, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_open_orders(self, extra_data=None, **kwargs):
        path, params, extra = self._get_open_orders(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_open_orders(self, extra_data=None, **kwargs):
        path, params, extra = self._get_open_orders(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    # Account

    def get_balance(self, extra_data=None, **kwargs):
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_balance(self, extra_data=None, **kwargs):
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_account(self, extra_data=None, **kwargs):
        path, params, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_account(self, extra_data=None, **kwargs):
        path, params, extra = self._get_account(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)
