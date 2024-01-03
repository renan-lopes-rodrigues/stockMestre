from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.data_base_config import get_db
from src.core.person.schemas import PersonSchemaRequest, PersonSchemaDetail
from src.core.person.services import PersonServices

class PersonResources:
    """
    Responsible to Person Resources
    """
    router = APIRouter()
    tags = ["Core | Persons"]

    @router.post('/core/persons', response_model=PersonSchemaDetail,tags=tags)
    def create_person(person: PersonSchemaRequest, db: Session = Depends(get_db)):
        response = PersonServices.create_person(db=db, person=person)
        db.commit()
        return response