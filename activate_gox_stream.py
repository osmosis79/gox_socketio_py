#!/usr/bin/python

from socketio import SocketIO
from pprint import pprint
import time, sys, decimal
from datetime import datetime
import json


def main_callback(msg):
    #m = json.loads(msg, use_decimal=True)
    m = json.loads(msg, parse_float=decimal.Decimal)

    trade =  "dbf1dee9-4f2e-4a08-8cb7-748919a71b21" #Trades
    ticker = "d5f06780-30a8-4a48-a2f8-7ed181b4a13f" #Ticker USD
    depth =  "24e67e0d-1cad-4cc0-9e7a-f8523ef460fe" #Depth  USD

    channel = m['channel']
    if channel==trade:    channel_name = 'trade'
    elif channel==ticker: channel_name = 'ticker'
    elif channel==depth:  channel_name = 'depth'
    else:                 channel_name = 'unknown'

    op = m['op'] #'private'
    if op == 'subscribe':
        print "subscribed to channel",channel_name
        #pprint(m)
    elif op == 'unsubscribe':
        pprint(m)
    elif op == 'remark':
        pprint(m)
    elif op == 'private':
        origin = m['origin'] #'broadcast'
        private = m['private'] #ticker, trade, depth

        if   private=='trade'  and channel==trade:      
            sys.stdout.write("T") ; sys.stdout.flush()
            #save_trade(m['trade'])
        elif private=='ticker' and channel==ticker: 
            sys.stdout.write(".") ; sys.stdout.flush()
            #save_ticker(m['ticker'])
        elif private=='depth'  and channel==depth:   
            sys.stdout.write("d") ; sys.stdout.flush()
            #save_depth(m['depth'])

sio = SocketIO('socketio.mtgox.com/socket.io', main_callback)
sio.connect()
#sio.thread.join()
while True:
    time.sleep(30)

