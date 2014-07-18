import sqlalchemy


def get_balance():
    engine=sqlalchemy.create_engine('mysql://sam_coin:abc123!@mysql.samarghandi.com/samarghandi_bitcoin')
    result=engine.execute("SELECT Cash,Bitcoin FROM Balance;")
    for n in result:
        return n['Cash'], n['Bitcoin']

def update_balance(Cash, Bitcoin):
    engine=sqlalchemy.create_engine('mysql://sam_coin:abc123!@mysql.samarghandi.com/samarghandi_bitcoin')
    engine.execute("UPDATE `Balance` SET `Cash`='%s', `Bitcoin`='%s'"  % (Cash, Bitcoin))
