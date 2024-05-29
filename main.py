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

'''
@app.delete("/guestbook/{entry_id}", status_code=200)
async def delete_entry(entry_id: int):
    global guestbook
    filtered_guestbook = [entry for entry in guestbook if entry['id'] != entry_id]
    if len(filtered_guestbook) == len(guestbook):
        raise HTTPException(status_code=404, detail="Entry not found")
    guestbook = filtered_guestbook
    return {"message": "Entry deleted"}
'''
app.include_router(guestbook_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)