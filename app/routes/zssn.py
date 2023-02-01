from __future__ import annotations

from fastapi import APIRouter, Depends
from app.core.auth import verify_token_user_info
from sqlalchemy.orm import Session

from app.apis.zssn.mainmod import create_survivor_mainmod, get_survivor_mainmod, update_survivor_mainmod, \
                                update_survivor_location_mainmod, delete_survivor_mainmod, get_reports_mainmod
from app.apis.zssn.model import SurvivorModel, InventoryModel, ReportModel
from app.utils.database_util import database_controls

db_conn = database_controls()
router = APIRouter()

@router.post("/survivors")
async def create_survivor(
    survivor: SurvivorModel,
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # create a new survivor
    return create_survivor_mainmod(survivor, session)

@router.get("/survivors/{survivor_id}")
async def get_survivor(
    survivor_id: int,
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # get a survivor by id
    return get_survivor_mainmod(survivor_id, session)

@router.put("/survivors/{survivor_id}")
async def update_survivor(
    survivor_id: int, 
    survivor: SurvivorModel,
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # update a survivor
    payload = {
        "survivor_id" : survivor_id,
        "survivor" : survivor
    }
    return update_survivor_mainmod(payload, session)

@router.patch("/survivors/{survivor_id}")
async def update_survivor_location(
    survivor_id: int, 
    latitude: float, 
    longitude: float,
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # update a survivor's location
    payload = {
        "survivor_id" : survivor_id,
        "latitude" : latitude,
        "longitude" : longitude
    }
    return update_survivor_location_mainmod(payload, session)

@router.delete("/survivors/{survivor_id}")
async def delete_survivor(
    survivor_id: int,
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # delete a survivor
    return delete_survivor_mainmod(survivor_id, session)

@router.get("/reports")
async def get_reports(
    session: Session = Depends(db_conn.get_db),
    user_details: Depends = Depends(verify_token_user_info)
):
    # get all reports
    return get_reports_mainmod(session)