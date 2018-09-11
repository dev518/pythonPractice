from sqlalchemy import Column, Integer, String, JSON
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    ukey = Column(String(50), unique=True)
    cid = Column(String(20), unique=False)
    uid = Column(String(50), unique=False)
    abs = Column(String(100000000), unique=False)

    def __init__(self, ukey=None, cid=None, uid=None, abs=None):
        self.ukey = ukey
        self.cid = cid
        self.uid = uid
        self.abs = abs

    def __repr__(self):
        return '<User %r>' % (self.name)

    def jsonForm(self):
        return {'key':self.ukey,'uid':self.uid,'cid':self.cid,'abs':self.abs}
