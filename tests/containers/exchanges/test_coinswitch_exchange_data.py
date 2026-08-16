"""Tests for CoinSwitchExchangeData container."""

from __future__ import annotations

import pytest

from bt_api_coinswitch.exchange_data import (
    CoinSwitchExchangeData,
    CoinSwitchExchangeDataSpot,
)


class TestCoinSwitchExchangeData:
    """Tests for CoinSwitchExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = CoinSwitchExchangeData()

        assert exchange.exchange_name == "COINSWITCH___SPOT"

    def test_symbol_period_and_rest_path_helpers(self):
        """test_symbol_period_and_rest_path_helpers method"""
        exchange = CoinSwitchExchangeData()

        assert exchange.get_symbol("BTCINR") == "BTCINR"
        assert exchange.get_period("1m") == "1m"
        assert exchange.get_rest_path("get_tick") == "GET /v2/ticker/"

    def test_get_rest_path_raises_when_missing(self):
        """test_get_rest_path_raises_when_missing method"""
        exchange = CoinSwitchExchangeData()
        with pytest.raises(ValueError):
            exchange.get_rest_path("missing")


class TestCoinSwitchExchangeDataSpot:
    """Class TestCoinSwitchExchangeDataSpot"""
    def test_spot_subclass_sets_asset_type(self):
        """test_spot_subclass_sets_asset_type method"""
        exchange = CoinSwitchExchangeDataSpot()
        assert exchange.asset_type == "SPOT"
