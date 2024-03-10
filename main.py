from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import session
from database import engine, SessionLocal
import schemas, models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


@app.post("/user_register/", response_model=schemas.UserBase)
def user_register(user:schemas.UserCreate, db :session=Depends(get_db)):
    user_check = db.query(models.User).filter(models.User.email==user.email).first()
    if user_check:
        raise HTTPException(status_code=400, detail= "User Already exists")
    user_registeration = models.User(name = user.name, family = user.family, email = user.email, password = user.password)
    db.add(user_registeration)
    db.commit()
    return user
    