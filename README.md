
# String Calculator

This project is a simple **String Calculator** developed using Python with **FastAPI** as the backend and **React** for the frontend. The application allows users to input a string of numbers separated by different delimiters, and the backend calculates the sum of the valid numbers.

- **Backend (Python + FastAPI)**: [String Calculator API](https://string-calculator.onrender.com/)
- **Frontend (React)**: [TDD Frontend](https://tdd-frontend.onrender.com/)

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Deployment](#deployment)

---

## Features

- Accepts a string of numbers with delimiters (commas, semicolons, or custom).
- Validates the input for valid numbers.
- Handles negative numbers and raises exceptions if they are encountered.
- Frontend allows users to input the string and get results from the backend.
- Demonstrates Test-Driven Development (TDD) principles.

---

## Tech Stack

### Backend:
- **Python**
- **FastAPI**: A modern, fast web framework for building APIs.
- **Uvicorn**: ASGI server for serving FastAPI applications.

### Frontend:
- **React**: JavaScript library for building user interfaces.
- **Material UI**: Styling and design components for a modern and responsive UI.

### Deployment:
- **Render**: For hosting both backend and frontend.


## Getting Started

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/string-calculator.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server**:
   ```bash
   uvicorn api:app --reload
   ```

   The backend will run on `http://127.0.0.1:8000`.

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd string-calculator/frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the React app**:
   ```bash
   npm start
   ```

   The frontend will run on `http://localhost:3000`.

---

## Usage

1. Open the **frontend** URL [https://tdd-frontend.onrender.com](https://tdd-frontend.onrender.com).
2. Enter a string of numbers (e.g., `"1,2,3"` or `"//;
1;2;3"`).
3. Click the "Calculate" button to get the sum.
4. The frontend communicates with the **FastAPI backend** hosted at [https://string-calculator.onrender.com](https://string-calculator.onrender.com) to calculate the result.

---


## Deployment

The backend and frontend are deployed on **Render**:

- Backend: [https://string-calculator.onrender.com](https://string-calculator.onrender.com)
- Frontend: [https://tdd-frontend.onrender.com](https://tdd-frontend.onrender.com)

Both services are continuously deployed from their respective GitHub repositories.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
