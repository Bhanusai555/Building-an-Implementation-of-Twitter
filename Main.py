from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Initialize database
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/tweets/", response_model=schemas.Tweet)
def create_tweet(tweet: schemas.TweetCreate, db: Session = Depends(get_db)):
    return crud.create_tweet(db=db, tweet=tweet)

@app.get("/tweets/", response_model=list[schemas.Tweet])
def read_tweets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tweets = crud.get_tweets(db, skip=skip, limit=limit)
    return tweets
