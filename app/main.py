from fastapi import FastAPI

app = FastAPI()

# Initialize your database here
# from database import init_db
# init_db()

# Import routes
# from routes import router
# app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
