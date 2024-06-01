from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any, List
import json
from model import GuestbookForm, GuestbookEntry

guestbook_router = APIRouter()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o:Any) -> Any:
        if isinstance(o, datetime):
            return o.isoformat() + 'Z'
        return super().default(o)

guestbook : List[Dict[str,Any]] = []
id_counter = 1

@guestbook_router.get("/guestbook", response_model=List[GuestbookEntry])
async def read_guestbook():
    return guestbook

@guestbook_router.post("/guestbook", response_model=GuestbookEntry)
async def add_entry(entry: GuestbookForm):
    global id_counter
    entry_data = entry.dict()
    entry_data["id"] = id_counter
    entry_data["timestamp"] =  datetime.utcnow().isoformat() + 'Z'
    guestbook.append(entry_data)
    id_counter+=1
    return entry_data

@guestbook_router.delete("/guestbook/{entry_id}")
async def delete_entry(entry_id: int):
    global guestbook
    guestbook = [entry for entry in guestbook if entry['id'] != entry_id]
    return {"message": "Entry deleted"}