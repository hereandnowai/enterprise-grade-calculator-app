# Enterprise Grade Calculator App

A production-ready Flask application for performing calculations with a separate business logic layer and a modern web frontend.

## 🚀 Features
- **Flask Backend:** RESTful API to handle calculations.
- **Separated Logic:** Calculation engine isolated in the `logic/` module.
- **Modern Frontend:** Vanilla JavaScript, CSS3, and HTML5.
- **Production Ready:** Configured for WSGI using Gunicorn.

## 🛠️ Tech Stack
- **Languages:** Python 3.x, JavaScript, HTML, CSS.
- **Frameworks/Libraries:** Flask, Gunicorn.

## 📁 Project Structure
- `backend/`: Flask application and business logic.
- `frontend/`: HTML, CSS, and JS files.
- `FLOWCHART.html`: System architecture and logic flow.
- `TEACHING_GUIDE.md`: Educational material for understanding the codebase.

## 🏁 Getting Started

### Prerequisites
- Python 3.8+
- [Optional] Virtual environment (venv)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

### Running the Application

#### Development Mode
To run with the built-in Flask development server:
```bash
python backend/app.py
```

#### Production Mode (WSGI)
To run with Gunicorn:
```bash
cd backend
gunicorn app:app
```

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
