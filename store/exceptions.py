# store/exceptions.py
from fastapi import HTTPException

class DataInsertionError(HTTPException):
    def __init__(self, detail: str = "Failed to insert data"):
        super().__init__(status_code=400, detail=detail)
