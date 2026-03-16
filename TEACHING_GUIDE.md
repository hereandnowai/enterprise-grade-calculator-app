# Teaching Guide: Building a Flask Calculator App (Enterprise-Style)

Welcome! This guide will take you through the process of building the iPhone-style Calculator App from scratch. We will use a modular approach, separating the **Backend Logic**, **Frontend UI**, and the **API Layer**.

## Table of Contents
1. [Prerequisites & Environment Setup](#1-prerequisites--environment-setup)
2. [Step 1: Backend Logic (The Brain)](#step-1-backend-logic-the-brain)
3. [Step 2: Frontend Design (The Body - HTML/CSS)](#step-2-frontend-design-the-body---htmlcss)
4. [Step 3: Frontend Interactivity (JS)](#step-3-frontend-interactivity-js)
5. [Step 4: The Web Server (The Skeleton - Flask)](#step-4-the-web-server-the-skeleton---flask)
6. [Step 5: Putting it All Together](#step-5-putting-it-all-together)
7. [How to Run the Project](#how-to-run-the-project)

---

## 1. Prerequisites & Environment Setup

Before we start, ensure you have Python installed on your machine.

### Create a Virtual Environment
It's a best practice to keep your project dependencies isolated.
```bash
# Navigate to your project folder
cd project-1-calculator/calculator_app

# Create a virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Install Dependencies
This project uses **Flask**, a lightweight web framework for Python.
```bash
pip install -r requirements.txt
```

---

## Step 1: Backend Logic (The Brain)

We start by writing the mathematical logic. This is independent of the web interface. In a professional app, we call this the "Business Logic Layer."

**File:** [backend/calculator_logic.py](backend/calculator_logic.py)

- Create a function `calculate(a, op, b)`.
- Use `if/elif` statements to handle `+`, `-`, `*`, and `/`.
- **Edge Case:** Remember to handle division by zero!

**Test your logic early:** 
Run `python backend_test.py` to make sure your math is correct before building the website.

---

## Step 2: Frontend Design (The Body - HTML/CSS)

Next, we build the visual structure. In enterprise apps, the frontend and backend are often built by different teams.

### HTML Structure
**File:** [templates/index.html](templates/index.html)
- Define a `display` input.
- Create buttons for numbers (0-9) and operators (+, -, *, /).

### Styling (CSS)
**File:** [static/css/styles.css](static/css/styles.css)
- Use Flexbox or Grid to align buttons.
- Create the signature rounded buttons and dark theme.

---

## Step 3: Frontend Interactivity (JS)

JavaScript makes our buttons work. It handles the local state (what numbers you've typed) and communicates with the backend.

**File:** [static/js/script.js](static/js/script.js)
- Maintain a local state for the current input.
- When the `=` button is pressed, use `fetch()` to send the data to our `/calculate` endpoint.

---

## Step 4: The Web Server (The Skeleton - Flask)

Now we use Flask to create a bridge between the frontend and our Python logic. This is our "API Layer."

**File:** [app.py](app.py)

1. **Initialize Flask:** `app = Flask(__name__)`
2. **Define Routes:**
   - `/`: Serves the HTML page.
   - `/calculate`: A `POST` route that receives numbers from the frontend, calls `calculate()`, and returns the result as JSON.
3. **Enterprise Pattern:** Notice how `app.py` doesn't do "math"—it just coordinates between the network and the `backend` module.

---

## Step 5: Putting it All Together

1. The user clicks buttons in the browser ([index.html](templates/index.html)).
2. JavaScript ([script.js](static/js/script.js)) collects the numbers and sends them to the server.
3. Flask ([app.py](app.py)) receives the JSON request and calls the Python logic ([calculator_logic.py](backend/calculator_logic.py)).
4. The result (or error) is sent back to the browser as JSON and updated on the display.

---

## How to Run the Project

Once everything is set up:
1. Ensure your virtual environment is active.
2. Run the server:
   ```bash
   python app.py
   ```
3. Open your browser and go to: `http://127.0.0.1:5000`

Happy Coding!
