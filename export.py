"""Export utilities for DocWise AI reports."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def export_receipts_to_csv(receipts, output_path):
    """Export receipt records to a CSV file."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for receipt in receipts:
        rows.append(
            {
                "id": receipt.get("id"),
                "merchant_name": receipt.get("merchant_name"),
                "receipt_date": receipt.get("receipt_date") or receipt.get("date"),
                "total": receipt.get("total"),
                "gst": receipt.get("gst"),
                "items_count": len(receipt.get("items", [])),
            }
        )
    pd.DataFrame(rows).to_csv(output_path, index=False)
    return output_path


def export_receipts_to_json(receipts, output_path):
    """Export receipt records to a JSON file."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(receipts, file, indent=2, ensure_ascii=False)
    return output_path
