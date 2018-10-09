from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, Items, User

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Eslam Adel", email="esadelx@gmail.com",
             picture='')
session.add(User1)
session.commit()


# Menu for restaurant
catalog1 = Catalog(
    user_id=1,
    name="Resaturant",
    picture='https: // encrypted - tbn0.gstatic.com / images'
    '?q=tbn: ANd9GcQ5n1XaVO5MzQfSFjk69zddZ7 - FVG7 - jyb - N0lyBx3TR9Sd4j8m')

session.add(catalog1)
session.commit()

item1 = Items(
    user_id=1,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?'
    'q=tbn:ANd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item1)
session.commit()

item2 = Items(
    user_id=1,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?q'
    '=tbn:ANd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item2)
session.commit()

item3 = Items(
    user_id=1,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?q=tb'
    'n:ANd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item3)
session.commit()
item4 = Items(
    user_id=1,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?q=tbn:AN'
    'd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item4)
session.commit()

item5 = Items(
    user_id=2,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?q=tbn:A'
    'Nd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item5)
session.commit()

item6 = Items(
    user_id=2,
    name="Sobhy",
    description="this is Sobhy restaurant",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/images?q=t'
    'bn:ANd9GcQ5n1XaVO5MzQfSFjk69zddZ7-FVG7-jyb-N0lyBx3TR9Sd4j8m',
    catalog=catalog1)

session.add(item6)
session.commit()


# Menu for Hostels
catalog2 = Catalog(
    user_id=1,
    name="Hostels",
    picture='https://encrypted-tbn0.gstatic.com/images?q=tbn'
    ':ANd9GcTAQCBhCX1KpKYGB7-6osu5xW7M4VeaHVUrPLI9MlgrwzDJtSa68A')


session.add(catalog2)
session.commit()

item1 = Items(
    user_id=1,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://encrypted-tbn0.gstatic.com/image'
    's?q=tbn:ANd9GcRwAfxiD-gs5kV5T6EVuWgN5w5rOMDAlf8WdfmH4t6kEaoGw0iJXg',
    catalog=catalog2)
session.add(item1)
session.commit()

item2 = Items(
    user_id=1,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d'
    '49bb6106edca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item2)
session.commit()


item3 = Items(
    user_id=1,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d49bb'
    '6106edca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item3)
session.commit()


item4 = Items(
    user_id=1,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d49b'
    'b6106edca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item4)
session.commit()

item5 = Items(
    user_id=1,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106ed'
    'ca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item5)
session.commit()

item6 = Items(
    user_id=2,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d49'
    'bb6106edca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item6)
session.commit()

item7 = Items(
    user_id=2,
    name="Hostels",
    description="this is Hostels List",
    price="$7.50",
    picture='https://cdn.mtlblog.com/uploads/262325_6d49bb6106e'
    'dca1ba048c4df3cbda1b6ff2a9e67'
    '.jpg_facebook.jpg',
    catalog=catalog2)
session.add(item7)
session.commit()

print("addd menu items!")
