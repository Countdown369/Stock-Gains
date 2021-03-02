#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:04:04 2021

@author: cabrown802
"""

import yfinance as yf
import threading

# Average cost PER STOCK that you have bought.
PRICE_AT_BUY = 128.078516

# TOTAL money spent on the stock.
COST = 159.00

# The stock itself.
STOCK = "GME"

# How often you want the script to print the stock price and gains.
# Set to 5 seconds by default, just don't do too many calls too fast.
UPDATE = 5.0

# Gets the current price of a stock using Yahoo Finance
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

# Prints most recent value of stock and unrealized gains.
def printit():
    threading.Timer(UPDATE, printit).start()
    price = get_current_price(STOCK)
    print(str(round(price, 3)) + "    " + "(Gain: " + str(round(((price * COST / PRICE_AT_BUY) - COST), 2)) + ")")

printit()


        

        

