"""
Processor module for stock-backtest-factor signal generation.

Validates incoming messages and computes a factor-based signal using
placeholder scoring logic. Replace with actual factor models as needed.
"""

from typing import Any

from app.utils.setup_logger import setup_logger
from app.utils.types import ValidatedMessage
from app.utils.validate_data import validate_message_schema

logger = setup_logger(__name__)


def validate_input_message(message: dict[str, Any]) -> ValidatedMessage:
    """
    Validate the incoming raw message against the expected schema.

    Args:
        message (dict[str, Any]): The raw message payload.

    Returns:
        ValidatedMessage: A validated message object.

    Raises:
        ValueError: If the message format is invalid.
    """
    logger.debug("🔍 Validating message schema...")
    if not validate_message_schema(message):
        logger.error("❌ Invalid message schema: %s", message)
        raise ValueError("Invalid message format")
    return message  # type: ignore[return-value]


def compute_factor_signal(message: ValidatedMessage) -> dict[str, Any]:
    """
    Compute a factor-based signal using placeholder rules.

    In real-world use, this would use multiple financial ratios or
    factor weights to compute a ranking or signal.

    Args:
        message (ValidatedMessage): The validated input data.

    Returns:
        dict[str, Any]: The enriched message with factor score and signal.
    """
    symbol = message.get("symbol", "UNKNOWN")
    pe_ratio = float(message.get("pe_ratio", 15))
    roe = float(message.get("roe", 0.12))

    logger.info("📊 Computing factor score for %s", symbol)

    # Placeholder scoring logic: lower PE and higher ROE = better score
    score = (1 / pe_ratio) + roe
    signal = "BUY" if score > 0.2 else "HOLD"

    result = {
        "factor_score": round(score, 4),
        "factor_signal": signal,
    }

    logger.debug("✅ Factor result for %s: %s", symbol, result)
    return {**message, **result}
