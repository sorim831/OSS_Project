from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from guestbook import guestbook_router

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
@app.get("/")
async def welcome() -> dict:
    return {
        "msg" : "송승규"
    }

app.include_router(guestbook_router)
app.mount("/",StaticFiles(directory="front-end",html=True),name="front-end")

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="127.0.0.1", port=8080)
    uvicorn.run(app, host="0.0.0.0", port=8080)