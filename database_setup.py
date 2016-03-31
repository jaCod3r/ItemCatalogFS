#Configuration Code Start

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
#Configuration Code End


#Class Representation
class Restaurant(Base):
    #Table
    __tablename__ = 'restaurant'

    #Mapper
    name = Column( String(80), nullable = False)
    id = Column(Integer, primary_key = True)

#Class Representation
class MenuItem(Base):
    #Table
   __tablename__ = 'menu_item'

   #Mapper
   name = Column(String(80), nullable = False)
   id = Column(Integer, primary_key = True)
   course = Column(String(250))
   description = Column(String(250))
   price = Column(String(8))
   restaurant_id = Column (Integer, ForeignKey ('restaurant.id'))
   restaurant = relationship(Restaurant)














#Configuration Code Start

engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)
#Configuration Code End
