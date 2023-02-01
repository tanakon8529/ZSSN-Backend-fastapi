from app.core.db_model import Survivor
from app.apis.zssn.model import SurvivorModel

def get_survivor_by_id(id, db_session):
    session_survivor = db_session.query(Survivor).filter(Survivor.id==id).first()
    result_survivor = []
    for i in session_survivor:
        x = SurvivorModel(**i.dict)
        result_survivor.append(x)

    return session_survivor, result_survivor

def create_survivor(payload, db_session):
    survivor = Survivor(
        name=payload.name,
        age=payload.age,
        gender=payload.gender,
        latitude=payload.latitude,
        longitude=payload.longitude,
        inventory=payload.inventory
    )
    db_session.add(survivor)
    return survivor

def update_survivor(survivor, payload, db_session):
    survivor.name = payload.name
    survivor.age = payload.age
    survivor.gender = payload.gender
    survivor.latitude = payload.latitude
    survivor.longitude = payload.longitude
    db_session.commit()
    return survivor

def delete_survivor(survivor, db_session):
    db_session.delete(survivor)
    db_session.commit()