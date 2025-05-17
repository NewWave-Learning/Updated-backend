# [TAG: DiagnosticAPI v1.0]
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class DiagnosticQuestion(BaseModel):
    question: str
    options: List[str]

class DiagnosticSubmission(BaseModel):
    subject: str
    answers: Dict[int, str]

@app.get("/diagnostics/start/{student_id}/{subject}")
def start_diagnostic(student_id: str, subject: str):
    return {
        "student_id": student_id,
        "subject": subject,
        "questions": [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"]},
            {"question": "Which word rhymes with 'cat'?", "options": ["dog", "bat", "sun"]}
        ]
    }

@app.post("/diagnostics/submit/{student_id}")
def submit_diagnostic(student_id: str, submission: DiagnosticSubmission):
    return {
        "message": f"Diagnostic for {submission.subject} submitted by {student_id}",
        "results": {
            "strengths": ["Comprehension"],
            "gaps": ["Phonics"]
        }
    }
