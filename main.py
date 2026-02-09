from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# --- DATA MODEL ---
class Candidate(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    role: str
    resume_text: str
    stage: str = "APPLIED"

# --- FAKE DB ---
db_candidates = []
stages = ["APPLIED", "SCREENING", "INTERVIEW", "HIRED"]

# --- ENDPOINTS ---

@app.post("/candidates/") # Naya candidate add karne ke liye
def add_candidate(c: Candidate):
    c.id = len(db_candidates) + 1
    db_candidates.append(c.dict())
    return c

@app.get("/candidates/") # Sabko dekhne ke liye (Sirf Recruiter)
def list_all(x_role: str = Header(None)):
    if x_role != "Recruiter":
        raise HTTPException(status_code=403, detail="Not authorized")
    return db_candidates

@app.patch("/candidates/{c_id}/move") # Stage badalne ke liye
def move_stage(c_id: int, x_role: str = Header(None)):
    if x_role != "Recruiter":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    for c in db_candidates:
        if c["id"] == c_id:
            curr_idx = stages.index(c["stage"])
            if curr_idx < len(stages) - 1:
                c["stage"] = stages[curr_idx + 1]
                return {"status": "success", "new_stage": c["stage"]}
    return {"error": "Candidate not found or at final stage"}