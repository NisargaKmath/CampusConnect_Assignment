# CampusConnect – Event Management API

## Project Overview
CampusConnect is a simple Campus Event Management Platform that allows:
- College staff (admins) to create and manage events.
- Students to register for events, mark attendance, and give feedback.
- Reports to be generated for popularity, participation, and top students.

This is my prototype implementation as part of the Webknot Technologies Campus Drive Assignment.

---

## Tech Stack
- Python 3.9+
- FastAPI (for APIs)
- SQLite + SQLAlchemy (for database)
- Uvicorn (server)

---

## Features Implemented
- Event Management → Create events.
- Student Registration → Register students for events.
- Attendance → Mark attendance for registered students.
- Feedback → Students can give ratings (1–5).
- Reports:
  - Event Popularity Report
  - Student Participation Report
  - Top 3 Most Active Students

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd CampusConnect_Assignment
```

### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API Server
```bash
uvicorn main:app --reload
```

### 5. Access APIs
- Base URL: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs

---

## Example Reports
- Event Popularity → `/reports/events`
- Student Participation → `/reports/students`
- Top 3 Active Students → `/reports/top-students`

---

## My Understanding
The goal of this project is not just to write code but to design, implement, and explain how a real-world event management system works.  
I have kept the solution:
- Simple and clear (SQLite DB for persistence).
- Practical (API endpoints cover the full flow from registration to reports).
- Extendable (the same structure can later be scaled to PostgreSQL/MySQL).

---

## Deliverables Included
- `main.py` → API code  
- `requirements.txt` → Python dependencies  
- `README.md` → My personal documentation  
- `docs/` → Design document (Word & PDF + ERD diagram)  
- `reports.sql` → Example queries for reports  

---


