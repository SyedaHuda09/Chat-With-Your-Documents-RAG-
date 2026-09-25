"""Deterministic tools exposed to the AI agent."""

from decimal import Decimal, InvalidOperation


def calculate_growth(old_value: float, new_value: float) -> dict:
    if old_value == 0:
        raise ValueError("old_value cannot be zero")
    growth = ((new_value - old_value) / old_value) * 100
    return {
        "old_value": old_value,
        "new_value": new_value,
        "growth_percent": round(growth, 2),
    }


def calculate_margin(profit: float, revenue: float) -> dict:
    if revenue == 0:
        raise ValueError("revenue cannot be zero")
    return {"margin_percent": round((profit / revenue) * 100, 2)}


def safe_decimal(value: str) -> float:
    try:
        return float(Decimal(value.replace(",", "").replace("$", "").strip()))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid numeric value: {value}") from exc
