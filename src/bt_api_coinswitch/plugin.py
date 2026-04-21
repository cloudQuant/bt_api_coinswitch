from __future__ import annotations

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_coinswitch.exchange_data import CoinSwitchExchangeDataSpot
from bt_api_coinswitch.feeds.live_coinswitch.spot import CoinSwitchRequestDataSpot


def get_plugin_info() -> PluginInfo:
    return PluginInfo(
        name="coinswitch",
        display_name="CoinSwitch",
        version="0.1.0",
        supported_asset_types=["SPOT"],
        feed_classes=[CoinSwitchRequestDataSpot],
        exchange_data_classes=[CoinSwitchExchangeDataSpot],
    )
