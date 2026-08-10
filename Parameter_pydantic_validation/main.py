from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Session

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:123456@localhost/ev_charging_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

class Station_types(Base):
    __tablename__ = "station_types"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=True, nullable=False)


class Stations(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    sation_code = Column(String(10), unique=True)
    price_per_kwh = Column(Float, nullable=False)
    station_type_id  = Column(Integer, ForeignKey("station_types.id"))

class StationCreate(BaseModel):
    sation_code: str
    price_per_kwh: float
    station_type_id: int



Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/stations")
def get_students(db: Session = Depends(get_db)):
    return db.query(Stations).all()


@app.get("/stations/{id}")
def get_student(id: int,
                db: Session = Depends(get_db)):
    return db.query(Stations)\
        .filter(Stations.id == id)\
        .first()


@app.post("/stations")
def update_station(
        data: StationCreate,
        db: Session = Depends(get_db)
):


    new_station = new_station (
        station_code = data.station_code,
        price_per_kwh = data.price_per_kwh,
        station_type_id = data.station_type_id
    )

    Stations.append(new_station)

    db.add(new_station)
    db.commit()
    db.refresh(new_station)

    return new_station




@app.delete("/station-types/{id}")
def delete_station(
        id: int,
        db: Session = Depends(get_db)
):
    student = db.query(Stations)\
        .filter(Stations.id == id)\
        .first()

    if not Stations:
        return {"message": "Không tìm thấy"}

    db.delete(Stations)
    db.commit()

    return {"message": "Xóa thành công"}