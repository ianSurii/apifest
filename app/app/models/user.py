# Every model represents a table in our database
from enum import unique
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from typing import Any
from pydantic import BaseModel, computed_field

from sqlalchemy.ext.declarative import as_declarative, declared_attr
# from .database import Base #import Base from db file
from typing import TYPE_CHECKING
# from app.db.base_class import Base

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()



class User(Base):
    __tablename__ = 'user'
   
    userid = Column(Integer,primary_key=True,nullable=False ,autoincrement=True)
    name = Column(String,nullable=False ,autoincrement=True)
    email = Column(String,nullable=False,  default=datetime.now(),)
    periodend = Column(TIMESTAMP,nullable=False,  default=datetime.now(),)
    value=Column(String,nullable=False)#allowance,bonusmortage//so on so on
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))