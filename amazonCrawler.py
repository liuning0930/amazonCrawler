# coding=utf-8
import os
import sys
import re
import json
import getopt
import requests
from amazonBeautifulParser import *

# https://www.amazon.com/dp/B072JCVHF6
commodityPrefix = "https://www.amazon.com/dp/"


def systemExit(message):
    os.system('echo ' + message)
    sys.exit(0)


def getCurrentGoodsWebContent(commodityID):
    user_agent = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(commodityPrefix + commodityID, headers=user_agent)
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
