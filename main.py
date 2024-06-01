from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from guestbook import guestbook_router

#app = FastAPI(json_encoder=DateTimeEncoder)

app = FastAPI()


origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://54.81.196.162"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(guestbook_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)