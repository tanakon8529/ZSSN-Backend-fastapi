from __future__ import annotations

from app.utils.databases.inventory import get_inventory_by_id, create_inventory, update_inventory, delete_inventory, update_inventory
from app.utils.databases.reports import get_report_by_id, create_report, update_report, delete_report
from app.utils.databases.survivors import get_survivor_by_id, create_survivor, update_survivor, delete_survivor

from loguru import logger

def create_survivor_submod(survivor, session):
    try:
        result = "create_survivor_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error create_survivor_submod"}
    return result

        
def get_survivor_submod(survivor_id, session):
    try:
        result = "create_survivor_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error create_survivor_submod"}
    return result

        
def update_survivor_submod(payload, session):
    try:
        result = "update_survivor_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error update_survivor_submod"}
    return result

        
def update_survivor_location_submod(payload, session):
    try:
        result = "update_survivor_location_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error update_survivor_location_submod"}
    return result

        
def delete_survivor_submod(survivor_id, session):
    try:
        result = "delete_survivor_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error delete_survivor_submod"}
    return result

        
def get_reports_submod(session):
    try:
        result = "get_reports_submod"
    except Exception as e:
        result = {"error_code" : "01", "msg" : "error get_reports_submod"}
    return result

