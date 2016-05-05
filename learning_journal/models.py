from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime,
    desc,
    select,
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
    created = Column(DateTime(timezone=True), default=func.current_timestamp())
    edited = Column(DateTime(timezone=True), default=func.current_timestamp(), onupdate=func.current_timestamp())

    def all(entries):
        # return all entries in database
        # ordered most recent entry first
        ordered_entries = select([entries]).order_by(desc(entries.created)).all()
        return ordered_entries

    def by_id(entries, id):
        # returns a single entry, given an id
        unique_id = int(id)
        find_unique_id = select([entries]).where(id=unique_id)
        return find_unique_id

Index('my_index', Entry.name, unique=True, mysql_length=255)
