from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_tweet(db: Session, tweet: schemas.TweetCreate):
    db_tweet = models.Tweet(**tweet.dict())
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet

def get_tweets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tweet).offset(skip).limit(limit).all()