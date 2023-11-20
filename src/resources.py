from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=["Olaaa"])
def root():
    return {"message": None}