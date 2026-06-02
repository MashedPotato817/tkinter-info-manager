# tkinter-info-manager

A simple information management system built with Python tkinter. Supports CRUD operations (Create, Read, Update, Delete) with a clean graphical interface.

## Features

- **Login** — Simple password-protected access
- **Add Records** — Add person info (name, gender, height, weight, age, hobbies) with input validation
- **Delete Records** — Remove records by name with confirmation dialog
- **Update Records** — Auto-fill existing info when searching by name, then modify
- **Query Records** — Search for individual records by name
- **View All** — Display all records in a table format
- **Data Persistence** — All data saved to JSON file automatically

## Requirements

- Python 3.8+
- tkinter (built-in)
- Pillow (`pip install Pillow`) — for background image

## Quick Start

```bash
# Install dependency
pip install Pillow

# Run the application
python information_management.py
```

Default password: `123456`

## Project Structure

```
├── information_management.py   # Main application
├── background.png              # Login background image
├── data.txt                    # Data storage (JSON format)
└── README.md
```

## License

MIT
