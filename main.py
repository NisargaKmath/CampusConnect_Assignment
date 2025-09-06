from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./campusconnect.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    type = Column(String)
    date = Column(String)
    college_id = Column(Integer)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    college_id = Column(Integer)

class Registration(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    event_id = Column(Integer, ForeignKey("events.id"))

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    status = Column(Boolean)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    event_id = Column(Integer, ForeignKey("events.id"))
    rating = Column(Float)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusConnect – Event Management API (DB Version)",
    description="SQLite-powered Event Management System",
    version="2.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Welcome to CampusConnect 🚀 – Database Enabled API"}

@app.post("/events")
def create_event(event: dict, db: Session = Depends(get_db)):
    new_event = Event(
        title=event["title"],
        type=event["type"],
        date=event["date"],
        college_id=event["college_id"]
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event created ✅", "event": new_event.__dict__}

@app.post("/register")
def register_student(data: dict, db: Session = Depends(get_db)):
    new_reg = Registration(student_id=data["student_id"], event_id=data["event_id"])
    db.add(new_reg)
    db.commit()
    return {"message": "Student registered 🎓"}

@app.post("/attendance")
def mark_attendance(data: dict, db: Session = Depends(get_db)):
    new_att = Attendance(student_id=data["student_id"], event_id=data["event_id"], status=data["status"])
    db.add(new_att)
    db.commit()
    return {"message": "Attendance marked 📝"}

@app.post("/feedback")
def submit_feedback(data: dict, db: Session = Depends(get_db)):
    new_fb = Feedback(student_id=data["student_id"], event_id=data["event_id"], rating=data["rating"])
    db.add(new_fb)
    db.commit()
    return {"message": "Feedback submitted ⭐"}

@app.get("/reports/events")
def event_popularity(db: Session = Depends(get_db)):
    result = db.query(Registration.event_id).all()
    counts = {}
    for r in result:
        counts[r[0]] = counts.get(r[0], 0) + 1
    sorted_report = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [{"event_id": e, "registrations": c} for e, c in sorted_report]

@app.get("/reports/students")
def student_participation(db: Session = Depends(get_db)):
    result = db.query(Attendance.student_id, Attendance.status).all()
    report = {}
    for s, status in result:
        if status:
            report[s] = report.get(s, 0) + 1
    return [{"student_id": sid, "events_attended": c} for sid, c in report.items()]

@app.get("/reports/top-students")
def top_active_students(db: Session = Depends(get_db)):
    result = db.query(Attendance.student_id, Attendance.status).all()
    report = {}
    for s, status in result:
        if status:
            report[s] = report.get(s, 0) + 1
    sorted_report = sorted(report.items(), key=lambda x: x[1], reverse=True)[:3]
    return [{"student_id": sid, "events_attended": c} for sid, c in sorted_report]
