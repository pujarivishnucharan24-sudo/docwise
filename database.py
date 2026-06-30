"""SQLite persistence helpers for DocWise AI."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

DEFAULT_DB_PATH = "docwise.db"


def get_connection(db_path=DEFAULT_DB_PATH):
    """Create a SQLite connection for the local DocWise database."""
    parent = Path(db_path).parent
    if parent != Path("."):
        parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)


def initialize_database(db_path=DEFAULT_DB_PATH):
    """Create the receipts table if it does not exist."""
    with get_connection(db_path) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS receipts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                merchant_name TEXT,
                receipt_date TEXT,
                total REAL,
                gst REAL,
                items_json TEXT NOT NULL,
                raw_text TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """)


def save_receipt(receipt, db_path=DEFAULT_DB_PATH):
    """Save a parsed receipt and return its database id."""
    initialize_database(db_path)
    with get_connection(db_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO receipts (
                merchant_name, receipt_date, total, gst, items_json, raw_text
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                receipt.get("merchant_name"),
                receipt.get("date"),
                receipt.get("total"),
                receipt.get("gst"),
                json.dumps(receipt.get("items", []), ensure_ascii=False),
                receipt.get("raw_text"),
            ),
        )
        return cursor.lastrowid


def list_receipts(db_path=DEFAULT_DB_PATH):
    """Return all stored receipts as dictionaries."""
    initialize_database(db_path)
    with get_connection(db_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT * FROM receipts ORDER BY created_at DESC"
        ).fetchall()
    receipts = []
    for row in rows:
        receipt = dict(row)
        receipt["items"] = json.loads(receipt.pop("items_json"))
        receipts.append(receipt)
    return receipts
