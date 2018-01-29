# coding=utf-8
import os
import sys
import re
import json
import getopt
import requests
from amazonBeautifulParser import *

# https://www.amazon.com/dp/B0716SVLXH
commodityPrefix = "https://www.amazon.com/dp/"


def systemExit(message):
    os.system('echo ' + message)
    sys.exit(0)


def getCurrentGoodsWebContent(commodityID):
    response = requests.get(commodityPrefix + commodityID)
    if (response.status_code == 404):
        print('No found the commodity')
    return response.text


if __name__ == '__main__':
    try:
        opts, argvs = getopt.getopt(sys.argv[1:], 'l:', '')
    except getopt.GetoptError as err:
        print (str(err))
        systemExit('Please write commodity ID')

    if (len(opts) == 0):
        systemExit('Please write commodity ID')

    commodityID = ""
    for option, value in opts:
        if option == '-l':
            if value == "":
                print('CommodityID is empty')
                systemExit('Please write commodity ID')
            commodityID = value
    response = getCurrentGoodsWebContent(commodityID)
    if response:
        amazonParser = amazonBeautifulParser()
        amazonParser.amazon_parser(response)
