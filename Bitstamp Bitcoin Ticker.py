###########################
#The first component to a future tradebot #
#Author: Sahm Samarghandi & Others     #
#Date: 5/24/2014                                   #
###########################

#A Redditor liked Py3 so he did this
from __future__ import print_function
#Jason Derulo
import json
#It's a console app and I use os for clear screen
import os
#Time is used for sleep
import time
#Soon to be replaced with requests for authentication when I do any posting
import urllib
#Used for fabs function to find absolute difference between the count up and down
import math
#Bitstamp gives us a Unix timestamp so datetime is used to convert
import datetime
#Simple moving average library
import sma
#My Sql Connection settings
import asql, bsql, csql

#Reads the json file at Bitstamps public api (requests must be <600/10minutes)
def ticker():
    return json.loads(urllib.urlopen('https://www.bitstamp.net/api/ticker/').read())

#My original source was refactored into methods
class Bs_Ticker(object):

    #Sets up all our stuff for use
    def __init__(self):
        self.count_up = 0
        self.count_down = 0
        self.last_direction = '--'
        self.tick = ticker()
        self.last = self.tick['ask']
        os.system("color 5b")
        os.system('cls')
        #for i in range(80):
        #    print(".", end='')
        #    time.sleep(.05)
        print("Downloading Stuff", end='')

    #The update method that calls a bunch of other stuff
    def update(self):
        self.tick = ticker()

                
        #self.alarm()
        self.data_tracker()
        #self.update_time()
        self.faux_trader()
        self.update_ticker()
        self.update_direction()
        self.debug()
        #The line below this should run after processing functions for things to work correctly
        self.last = self.tick['ask']
        self.print_stuff()
        

    #Draws the ticker on the console
    def update_ticker(self):
        self.header = "Hurray Bitcoins!\n"
        self.output = ("High: {high} Low: {low} Bid: {bid} Ask: {ask} ".format(**self.tick))
        os.system('cls')
        print(" " * (len(self.output) /2 - len(self.header)/2) + self.header)
        print(self.output, end='')

    def update_time(self):
        self.file2=open('last updated.wtf', 'a+')
        self.file2.seek(0,2)
        if self.file2.tell()==0:
            self.last_time=420
        else:
            self.file2.seek(0)
            self.last_time=self.file2.readline()
        
       # print("\n\n\n" , self.last_time, (int(self.tick['timestamp'])-172800))
        if int(self.last_time)<(int(self.tick['timestamp'])-172800) or self.last_time is 420:
            self.file2.close()
            open("mah_coins.wtf", 'w').close
            self.file2=open('last updated.wtf', 'w')
            open('last updated.wtf', 'w')
            self.file2.write(unicode(self.tick['timestamp']))
            self.last_time=int(self.tick['timestamp'])
        self.file2.close()

    #Draws the direction of the last move
    def update_direction(self):
        if self.tick['ask'] > self.last:
            self.count_up += 1
            self.last_direction = "^^"
            print(self.last_direction, end='')
        elif self.tick['ask'] < self.last:
            self.count_down += 1
            self.last_direction = "vv"
            print(self.last_direction, end='')
        else:
            print(self.last_direction, end='')

    #Draws a warning on the screen guessing if the prices is going to make a major shift
    #This will be replaced with more robust logic
    def alarm(self):
        if self.count_up==self.count_down+5:
            self.system_warning = "PRICE GOING UP!"
        elif self.count_down == self.count_up+5:
            self.system_warning = "PRICE GOING DOWN!"
        elif math.fabs(self.count_up-self.count_down)<=3:
            self.system_warning = ""
        print("\n" + self.system_warning)

    #Shows the count and timestamp which may or may not be hidden later
    def debug(self):
        print("\n\nup: " + str(self.count_up), "down: " + str(self.count_down))
        print("\n"+datetime.datetime.fromtimestamp(int(self.tick['timestamp'])).strftime("%m-%d-%Y %H:%M:%S"), end='')
  

    def data_tracker(self):
        
        try:
            self.coin_list
        except:            
            self.coin_list=[]

        self.average=sma.SimpleMovingAverage()
        self.average.set(len(self.coin_list), self.coin_list)
                
        try:
            self.coin_list, temp=zip(*csql.get_prices())
        except:
            print ("unable to process prices from SQL Database")
        
        

        if self.tick['ask']!=self.last:
            csql.update_prices(self.tick['ask'], datetime.datetime.fromtimestamp(int(self.tick['timestamp'])).strftime("%Y-%m-%d %H:%M:%S"))
            

        
#Trader function. Contains trading logic as well as balance reading and writing from the bsql source
    def faux_trader(self):

        try:
            self.cash, self.bitcoin
        except:
            self.cash, self.bitcoin=0.0, 0.0
            
        self.cash, self.bitcoin=bsql.get_balance()

        asql.clean_sql_every_x_hours(48)
        

    def print_stuff(self):
        
        try:
            print("\n\nThe average price is:",self.average.calculate()[-1], end='') #"as of", datetime.datetime.fromtimestamp(float(self.last_time)).strftime('%Y-%m-%d %H:%M:%S'),  end='')
        except:
            print("\n\nCalculating Average...", end='')

        print ("\n\nCash:    ", float(self.cash), "\nBitcoin: ", float(self.bitcoin))
            
        

#Main function that calls an instances of the main class (bs_Ticker) 
def main():

    t = Bs_Ticker()

    #Updates the object every 5 seconds (probably)
    while True:
        t.update()
        time.sleep(5)


if __name__ == '__main__':
    main()
