import sqlalchemy

def clean_sql_every_x_hours(x):
    engine=sqlalchemy.create_engine('mysql://sam_coin:abc123!@mysql.samarghandi.com/samarghandi_bitcoin')
    engine.execute("DELETE FROM Coins WHERE Time <= SYSDATE() - INTERVAL %s HOUR" % x)
