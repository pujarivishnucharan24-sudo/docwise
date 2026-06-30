# User Manual

DocWise helps process receipt and document images locally. It can extract OCR
text, parse common receipt fields, store parsed receipts, and export results.

## Start the Application

Run the basic command-line entry point:

```bash
python main.py
```

Run the dashboard:

```bash
streamlit run app.py
```

## Process Receipts

1. Open the Streamlit dashboard.
2. Upload a `.png`, `.jpg`, or `.jpeg` receipt.
3. Select the process action.
4. Review extracted OCR text, totals, GST, merchant details, and export options.

## Export Data

The dashboard can export processed receipt records as CSV or JSON. The helper
functions in `export.py` also support programmatic exports to a chosen path.

## Local Data

Uploaded documents, reports, and SQLite databases are local development data.
They are intentionally ignored by Git except for `.gitkeep` placeholders.

## Troubleshooting

- If OCR returns empty text, confirm that Tesseract OCR is installed and the
  receipt image is readable.
- If PDF extraction is empty, ensure the PDF contains embedded text or readable
  page images.
- If tests fail after dependency changes, recreate the virtual environment and
  reinstall `requirements.txt`.
