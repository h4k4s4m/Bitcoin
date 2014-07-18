import sqlalchemy


def get_prices():
    engine=sqlalchemy.create_engine('mysql://sam_coin:abc123!@mysql.samarghandi.com/samarghandi_bitcoin')
    result=engine.execute("SELECT Price,Time FROM Coins;")
    price_list=[]
    for n in result:
        price_list.append((n['Price'], n['Time']))
    return price_list

def update_prices(Price, Time):
    engine=sqlalchemy.create_engine('mysql://sam_coin:abc123!@mysql.samarghandi.com/samarghandi_bitcoin')
    engine.execute("INSERT `Coins` SET `Price`='%s', `Time`='%s'"  % (Price, Time))
