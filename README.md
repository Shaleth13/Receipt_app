Receipt Parser App
This is a Python-based application that allows users to upload receipts in various formats (.txt, .pdf, .jpg, .png), extract key fields from them using OCR and regular expressions, store the extracted data in a SQLite database, and visualize spending insights through an interactive dashboard built with Streamlit.

Features
Upload receipts in .txt, .pdf, .jpg, or .png formats

Automatically extract id, vendor name, date, amount, and category

Store parsed data in a local SQLite database

View all stored receipts in a tabular format

Analyze top vendors by frequency and total spend

Visualize monthly spending trends

Modular code structure split into multiple logical files

Tech Stack
Python

Streamlit

SQLite (via sqlite3)

OCR: Tesseract OCR (pytesseract, pdf2image, Pillow)

Data processing: pandas, re

Visualization: matplotlib, pandas

Project Structure
receipt_app/
├── app.py               # Streamlit application
├── parser.py            # Logic for extracting text and fields from receipts
├── database.py          # SQLite connection, insert, and query functions
├── analytics.py         # Data cleaning and visual analysis functions
├── sample_receipt.txt   # Sample receipt for testing
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Sample Input (Text File Format)
MiniMart Grocery Store
Invoice No: 102938
Date: 15/06/2025

Items Purchased:
Eggs - ₹80
Milk - ₹60
Bread - ₹45
Total: ₹185.00

Author
Shaleth
Email: shalethghosh13@gmail.com
GitHub: https://github.com/Shaleth13
