from database import engine
from data import fetch_data
from models import Bourse
from database import SessionLocal
from sqlalchemy.dialects.postgresql import insert

def insert_df():
    df = fetch_data()

    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    df = df.drop_duplicates(subset=["id"], keep="first")

    print("Columns DF :", df.columns.tolist())
    print("Shape :", df.shape)
    print(df.dtypes)

    records = df.to_dict(orient="records")

    db = SessionLocal()
    try:
        stmt = insert(Bourse).values(records)
        stmt = stmt.on_conflict_do_update(
            index_elements=["id"],
            set_={
                "current_price": stmt.excluded.current_price,
                "market_cap": stmt.excluded.market_cap,
                "total_volume": stmt.excluded.total_volume,
            }
        )
        db.execute(stmt)
        db.commit()
        print("Upsert réussi")
    except Exception as e:
        db.rollback()
        print("Erreur :", e)
    finally:
        db.close()

if __name__ == "__main__":
    insert_df()

