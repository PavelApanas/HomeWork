from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from typing import List
import csv
from models import UserCreate, ProductCreate, OrderCreate, OrderItemCreate

def fill_table_from_csv(file_path: str, model: BaseModel, db: Session) -> None:
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)
        items = parse_obj_as(List[model], list(csv_reader))
        for item in items:
            db_item = model(**item)
            db.add(db_item)
        db.commit()


import csv
from sqlalchemy.orm import Session

def export_table_to_csv(session: Session, table: str, file_path: str):
    table_obj = session.get_bind().metadata.tables[table]
    columns = [column.name for column in table_obj.columns]
    data = session.query(table_obj).all()
    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        for row in data:
            writer.writerow([getattr(row, column) for column in columns])
