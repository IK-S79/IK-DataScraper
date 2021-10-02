import os
import random


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = \
        "mongodb+srv://dbUser:fallenover@serverlessinstance0.5d4xq.mongodb.net/data?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['data']

def dump_data():
    import datetime

    players = []

    time = datetime.datetime.today()

    for i in range(0, 5000):
        players.append({
            "name": "DummyPlayer" + str(i),
            "server": 78,
            "alliance": "DummyAlliance",
            "rank": random.choice(['Leader', 'Officer', 'Backbones', 'Elites', 'Members', 'Newbies']),
            "troop_power": random.randrange(10000, 125000),
            "lord_power": random.randrange(85000, 800000),
            "tech_contributions": random.randrange(0, 10000),
            "defeat": random.randrange(0, 1000000),
            "dismantle": random.randrange(0, 1000000),
            "time": time
        })

    # Get the database
    print(0)
    dbname = get_database()
    print(1)
    print(dbname['players'].insert_many(players))
    print(2)

