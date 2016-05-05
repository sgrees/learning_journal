from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
    )

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False, unique=True)
    body = Column(UnicodeText())
    created = Column(DateTime(timezone=True), default=func.now())
    edited = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

# classmethod all that returns all the entries in the database, ordered so that the most recent entry is first.
# classmethod by_id that returns a single entry, given an id.

Index('my_index', Entry.name, unique=True, mysql_length=255)
