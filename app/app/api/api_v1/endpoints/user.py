from ast import parse
from contextlib import nullcontext
from ctypes import Union
from email import message
import os
from traceback import print_tb
from typing import Any, Dict, List
import secrets
from datetime import datetime, time,timedelta,timezone
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import africastalking



# load_dotenv()
router = APIRouter()

# create user
@router.post("/create", response_model=schemas.ResponseBase)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.User,
    # current_user: models.user = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    try:
        user = crud.user.get_by_email(db, email = user_in.email)
        if user:
            
            return schemas.ResponseBase(
                            respodesc = "The user with this email already exists in the system.",
                            error=True,
                            respocode=1,
                            response=[]
                        )
        else:
            user = crud.user.create(db, obj_in=user_in)
            # if settings.EMAILS_ENABLED and user_in.email:
            #     send_new_account_email(
            #         email_to=user_in.email, username=user_in.email, password=user_in.password
            #     )
            return schemas.ResponseBase(
                            respodesc = "User created successfull.Login details will be send to user email specified",
                            error=False,
                            respocode=0,
                            response=[user]
                    )
    except:
                return schemas.ResponseBase(

                respodesc ="Things are getting out of hand",
                error=True,
                respocode=1,
                response=[]
            )
  