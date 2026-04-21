from __future__ import annotations

from bt_api_base.error import ErrorTranslator, UnifiedErrorCode


class CoinSwitchErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, error_data: dict) -> UnifiedErrorCode:
        code = error_data.get("code", error_data.get("errorCode"))
        msg = error_data.get("message", error_data.get("error"))
        if code == 401 or "auth" in str(msg).lower() or "api key" in str(msg).lower():
            return UnifiedErrorCode.AUTHENTICATION_ERROR
        if code == 429:
            return UnifiedErrorCode.RATE_LIMIT
        if "balance" in str(msg).lower() or "insufficient" in str(msg).lower():
            return UnifiedErrorCode.INSUFFICIENT_BALANCE
        if "not found" in str(msg).lower() or code == 404:
            return UnifiedErrorCode.NOT_FOUND
        if "invalid" in str(msg).lower() or code == 400:
            return UnifiedErrorCode.INVALID_PARAMETER
        return UnifiedErrorCode.UNKNOWN
