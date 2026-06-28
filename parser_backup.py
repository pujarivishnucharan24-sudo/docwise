"""Receipt text parser for DocWise AI."""

from __future__ import annotations

import re
from datetime import datetime


DATE_PATTERNS = (
    r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b",
    r"\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b",
)

AMOUNT_PATTERN = re.compile(
    r"(?:rs\.?|inr|₹)?\s*([0-9]+(?:,[0-9]{3})*(?:\.\d{1,2})?)",
    re.I,
)
TOTAL_PATTERN = re.compile(r"\b(grand\s+total|net\s+amount|total)\b", re.I)
GST_PATTERN = re.compile(r"\b(gst|cgst|sgst|igst)\b", re.I)


def _parse_amount(line):
    """Return the last currency-like amount from a text line."""
    matches = AMOUNT_PATTERN.findall(line)
    if not matches:
        return None
    return float(matches[-1].replace(",", ""))


def _parse_date(text):
    """Extract a normalized receipt date when one is present."""
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, text)
        if not match:
            continue
        raw_date = match.group(0)
        for date_format in (
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%d-%m-%y",
            "%d/%m/%y",
            "%Y-%m-%d",
            "%Y/%m/%d",
        ):
            try:
                return datetime.strptime(raw_date, date_format).date().isoformat()
            except ValueError:
                pass
        return raw_date
    return None


def parse_receipt_text(text):
    """Parse OCR text into structured receipt fields.

    Args:
        text: Raw OCR output from a receipt, invoice, or bill.

    Returns:
        A dictionary containing merchant, date, total, GST, and item lines.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    merchant = lines[0] if lines else None
    total = None
    gst = 0.0
    items = []

    for line in lines:
        amount = _parse_amount(line)
        if GST_PATTERN.search(line) and amount is not None:
            gst += amount
            continue
        if TOTAL_PATTERN.search(line) and amount is not None:
            total = amount
            continue
        if amount is not None and not re.search(
            r"\b(date|bill|invoice|tax|cash|card)\b",
            line,
            re.I,
        ):
            name = AMOUNT_PATTERN.sub("", line).strip(" -:\t")
            if name:
                items.append({"name": name, "amount": amount})

    return {
        "merchant_name": merchant,
        "date": _parse_date(text),
        "total": total,
        "gst": round(gst, 2),
        "items": items,
        "raw_text": text,
    }
