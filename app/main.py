from fastapi import FastAPI
from .routes import contacts, phones, tags
from .database import get_db_connection

app = FastAPI()

app.include_router(contacts.router)
app.include_router(phones.router)
app.include_router(tags.router)

@app.on_event("startup")
async def startup():
    # Test database connection
    try:
        conn = get_db_connection()
        conn.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

@app.get("/")
async def root():
    return {"message": "Contact Book API"}
