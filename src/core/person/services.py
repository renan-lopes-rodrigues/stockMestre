from sqlalchemy.orm import Session
from src.core.person.schemas import PersonSchemaRequest
from src.core.models import Person
from uuid import uuid4
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

class PersonServices:
    """
    Handles person services
    """
    @staticmethod
    def create_person(db: Session, person: PersonSchemaRequest):

        try:
            db_person = Person(person.name)
            db_person.type = person.type.value
            db_person.address = person.address
            db_person.number = person.number
            db_person.neighborhood = person.neighborhood
            db_person.city = person.city
            db_person.state_id = person.state_id
            db_person.cep = person.cep
            db_person.complement = person.complement
            db_person.document = person.document
            db_person.id = uuid4()
            db.add(db_person)
            db.flush()
            db.refresh(db_person)
            return db_person

        except IntegrityError as ex:
            db.rollback()
            raise HTTPException(status_code=400, detail='Person already exists with this document.')

        except Exception as ex:
            db.rollback()
            raise HTTPException(status_code=500, detail="Internal Error.")