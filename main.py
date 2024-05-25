from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime
from typing import Optional
from typing import Dict
from typing import Any
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o:Any) -> Any:
        if isinstance(o, datetime):
            return o.isoformat() + 'Z'
        return super().default(o)

#app = FastAPI(json_encoder=DateTimeEncoder)

app = FastAPI()


origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuestbookForm(BaseModel):
    name : str
    message : str

class GuestbookEntry(GuestbookForm):
    id : int
    timestamp: str


#guestbook =[]
guestbook : List[Dict[str,Any]] = []
id_counter = 1

@app.get("/guestbook", response_model=List[GuestbookEntry])
async def read_guestbook():
    #print("Guestbook data:", guestbook)  # 로그 추가
    return guestbook

@app.post("/guestbook", response_model=GuestbookEntry)
async def add_entry(entry: GuestbookForm):
    global id_counter
    entry_data = entry.dict()
    entry_data["id"] = id_counter
    entry_data["timestamp"] =  datetime.utcnow().isoformat() + 'Z'
    guestbook.append(entry_data)
    id_counter+=1
    return entry_data

@app.delete("/guestbook/{entry_id}")
async def delete_entry(entry_id: int):
    global guestbook
    guestbook = [entry for entry in guestbook if entry['id'] != entry_id]
    return {"message": "Entry deleted"}
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)