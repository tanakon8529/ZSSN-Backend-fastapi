from app.core.db_model import Inventory
from app.apis.zssn.model import InventoryModel

def get_inventory_by_id(id, db_session):
    session_inventory = db_session.query(Inventory).filter(Inventory.id==id)
    result_inventory = []
    for i in session_inventory:
        x = InventoryModel(**i.dict)
        result_inventory.append(x)
    return session_inventory, result_inventory

def create_inventory(payload, db_session):
    
    item_inventory = Inventory(
        water = payload.water,
        food = payload.food,
        medication = payload.medication,
        ammunition = payload.ammunition
    )

    db_session.add(item_inventory)
    db_session.flush()

def update_inventory(inventory, payload, db_session):
    inventory.update({"water": payload.water})
    inventory.update({"food": payload.food})
    inventory.update({"medication": payload.medication})
    inventory.update({"ammunition": payload.ammunition})
    db_session.flush()

def delete_inventory(id, db_session):
    session_inventory = db_session.query(Inventory).filter(Inventory.id==id)
    session_inventory.delete(synchronize_session="fetch")
    db_session.flush()

def update_inventory(id, payload, db_session):
    session_inventory = db_session.query(Inventory).filter(Inventory.id==id)
    session_inventory.update({"item": payload.item})
    session_inventory.update({"quantity": payload.quantity})
    db_session.flush()