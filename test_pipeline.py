"""Smoke tests for the DocWise AI parsing pipeline."""

from parser import parse_receipt_text


def test_parse_receipt_text_extracts_total_and_items():
    """Parser should extract common receipt fields from OCR text."""
    text = """
    DMart
    Date: 28-06-2026
    Milk 60.00
    Rice 240.00
    GST 18.50
    Total 318.50
    """

    result = parse_receipt_text(text)

    assert result["merchant_name"] == "DMart"
    assert result["date"] == "2026-06-28"
    assert result["total"] == 318.50
    assert result["gst"] == 18.50
    assert len(result["items"]) == 2
