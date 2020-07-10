from typing import Optional
from ratelimit import limits,RateLimitException,sleep_and_retry
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


userList={}


@app.get("/signup/")
def write_item(user_id:str,pas:str):
    if user_id in userList:
        return {"User Already exist"}
    else:
        userList.update({user_id:pas})
        return{"Signup successful, 5 attempts left !!"} 


ONE_MINUTE = 60
@sleep_and_retry
@limits(calls=5, period=ONE_MINUTE)
def call_api():
    try:
        response = random.randint(0,100000)
        return {"Random number " + str(response)}
    except RateLimitException as e:
        print(e)
        return {"Limit exceed , Wait a minute!"}

@app.get("/login/")
def read_item(user_id:str,pas:str):
    # print(userList.get(user_id))
    if(userList.get(user_id)==pas):
        return call_api()
    else:
        return{"user not found"}    