hello, world!

This is my slow crawl towards having a working bitcoin trading robot.
The idea sprouted from discovering the API's to use coinbase and eventually moved to bitstamp for various reasons.
Functionality is being added piece by piece but so far this is what we can do with this code.

1. Track the price of bitcoin per ~10 seconds
2. Read and write prices of coins and timestamps to a sql database
3. faux_trader function in order to keep track of balances and test algorithms before real bitstamp trade api's are coded in
4. Calculate simple moving averages which can be used at different intervals to predict crossovers (times to buy and sell)
5. Old code that would removed bitcoin prices every 48 hours that needs to be converted for the sql database


Features to be added:

1. Using matplotlib to create graphs for visual tracking
2. Use the sma function to create basic trade logic
3. Program Bitstamp trade functionality
4. Plan a release and internal build for public and private use (this is the public)
