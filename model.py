from pydantic import BaseModel

class GuestbookForm(BaseModel):
    name : str
    message : str

class GuestbookEntry(GuestbookForm):
    id : int
    timestamp: str

