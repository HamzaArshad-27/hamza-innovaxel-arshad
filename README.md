# 🔗 URL Shortening Service - Innovaxel Take-Home Assignment

This project is a RESTful API for a URL Shortening Service built with **Python Flask** and **SQLite** using SQLAlchemy ORM.

---

## 🚀 Features

- 🔗 Create short URLs
- 🔍 Retrieve original URLs by shortCode
- ✏️ Update existing short URLs
- ❌ Delete short URLs
- 📊 Track and return access statistics
- 🆔 Short codes are randomly and uniquely generated
- ⚙️ Simple local SQLite database setup
- 🧪 Fully testable via Postman, curl, or CLI

---

## 🛠️ Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Language     | Python         |
| Framework    | Flask          |
| ORM          | SQLAlchemy     |
| Database     | SQLite         |
| Tooling      | curl / Postman |

---

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/hamza/hamza-innovaxel-arshad.git
cd hamza-innovaxel-arshad

# Create and activate virtual environment
python -m venv url_shortner
source url_shortner/bin/activate        # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
