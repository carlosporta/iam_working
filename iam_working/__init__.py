from fastapi import FastAPI

from iam_working.db import configure_db, insert, select_all


app = FastAPI()


@app.on_event("startup")
def setup_db():
    configure_db()


@app.post("/activity/")
def add_activity(date: str, agent: str, message: str):
    insert(date, agent, message)
    return {"date": date, "agent": agent, "message": message}


@app.get("/activity/")
def list_activity():
    activities = select_all()
    return {'activities': activities}
