from app.core.db_model import Report
from app.apis.zssn.model import ReportModel

def get_report_by_id(id, db_session):
    session_report = db_session.query(Report).filter(Report.id==id)
    result_report = []
    for i in session_report:
        x = ReportModel(**i.dict)
        result_report.append(x)

    return session_report, result_report

def create_report(payload, db_session):
    item_report = Report(
        percentage_of_infected_survivors = payload.percentage_of_infected_survivors,
        percentage_of_non_infected_survivors = payload.percentage_of_non_infected_survivors,
        average_amount_of_each_kind_of_resource_by_survivor = payload.average_amount_of_each_kind_of_resource_by_survivor,
        points_lost_because_of_infected_survivor = payload.points_lost_because_of_infected_survivor
    )
    db_session.add(item_report)
    db_session.flush()

def update_report(report, payload, db_session):
    report.update({"percentage_of_infected_survivors": payload.percentage_of_infected_survivors})
    report.update({"percentage_of_non_infected_survivors": payload.percentage_of_non_infected_survivors})
    report.update({"average_amount_of_each_kind_of_resource_by_survivor": payload.average_amount_of_each_kind_of_resource_by_survivor})
    report.update({"points_lost_because_of_infected_survivor": payload.points_lost_because_of_infected_survivor})
    db_session.flush()

def delete_report(report, db_session):
    report.delete(synchronize_session="fetch")
    db_session.flush()