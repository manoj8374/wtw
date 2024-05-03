from sqlalchemy import INTEGER, Integer, create_engine, Column, String, VARCHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Base2 = declarative_base()

engine = create_engine("mysql://ucqojmslvkutogcc:woxPxWyuaVzbVYjwMv0r@bfr7xlwn6iqg6qgeievt-mysql.services.clever-cloud.com:3306/bfr7xlwn6iqg6qgeievt")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

class wardrobe(Base):
    __tablename__ = 'wardrobe'

    name = Column(String, primary_key=True)
    occupation = Column(String)
    gender = Column(String)
    top = Column(VARCHAR)
    bottom = Column(VARCHAR)
    others = Column(VARCHAR)

def readdata():
    try:
        user = session.query(wardrobe).filter_by(name="Pavan").first()
        if user:
            return user
        else:
            session.rollback()
            return "Some Error occourred"
    except:
        session.rollback()

def updatewardrobe(top, bottom, others):
    user = session.query(wardrobe).filter_by(name="Pavan").first()
    if user:
        user.top = top
        user.bottom = bottom
        user.others = others
        session.commit()
        return "True"
    else:
        session.rollback()
