from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    resume_data = db.Column(db.JSON)
    
    # One-to-many relationship: one student can have multiple interview processes
    interview_processes = db.relationship('InterviewProcess', backref='student', lazy=True)

class InterviewProcess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    stage = db.Column(db.String(50))  # E.g., "Rejected", "Phone Interview", "Technical Interview", "Offer"
    offer_received = db.Column(db.Boolean, default=False)
    
    # Foreign key to associate with a student
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

