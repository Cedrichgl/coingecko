from fastapi import FastAPI, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Bourse

app = FastAPI()

#get tous les cryptos
@app.get("/data/")
async def all_data(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    cryptos = db.query(Bourse).offset(skip).limit(limit).all()
    return cryptos

#get crypto by id
@app.get("/data/{data_id}")
async def get_data_by_id(data_id:str, db: Session = Depends(get_db)):
    crypto = db.query(Bourse).filter(Bourse.id == data_id).first()
    if not crypto:
        raise HTTPException(status_code=404, detail="Crypto introuvable")
    return crypto

#filter par prix : max ou min
@app.get("/data/filter/price")
async def get_filter_price(min_price=0,max_price=100,db: Session = Depends(get_db)):
    query = db.query(Bourse).filter(Bourse.current_price >= min_price)
    if max_price:
        query = query.filter(Bourse.current_price <= max_price)

    results = query.all()

    if not results:
        raise HTTPException(status_code=404, detail="Crypto introuvable")
    return results













