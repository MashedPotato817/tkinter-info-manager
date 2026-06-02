# tkinter-info-manager

> English | [中文](./README.md)

A simple information management system built with Python tkinter, ideal as a **Python course project reference**. Features full CRUD operations with a clean GUI and JSON data persistence.

## Features

- 🔐 **Login** — Password-protected access
- ➕ **Add Records** — Name, gender, height, weight, age, hobbies with input validation
- ❌ **Delete Records** — Remove by name with confirmation dialog
- ✏️ **Update Records** — Auto-fill existing info when searching by name
- 🔍 **Query Records** — Search individual records by name
- 📋 **View All** — Display all records in table format
- 💾 **Data Persistence** — Auto-save to JSON file

## Requirements

- Python 3.8+
- tkinter (built-in)
- Pillow: `pip install Pillow`

## Quick Start

```bash
pip install Pillow
python information_management.py
```

Default password: `123456`

## Project Structure

```
├── information_management.py   # Main application
├── background.png              # Login background image
├── data.txt                    # Data storage (JSON format)
├── README.md                   # Chinese documentation
├── README.en.md                # English documentation
└── .gitignore
```

## License

MIT
