# coding=utf-8
import os
import sys
import re
import json
import getopt
import requests
from amazonBeautifulParser import amazonBeautifulParser
from bs4 import BeautifulSoup
from amazonRequest import amazonRequest

# https://www.amazon.com/dp/B072JCVHF6


def systemExit(message):
    os.system('echo ' + message)
    sys.exit(0)


def getCurrentGoodsWebContent(commodityID):
    amazon_request = amazonRequest()
    response = amazon_request.request(amazon_request.commodityPrefix + commodityID)
    if response == "":
        print('No found the commodity')
    return response


def getAllReviewsCommentsContent(href):
    amazon_request = amazonRequest()
    response = amazon_request.request(amazon_request.commentPrefix + href)
    if response == "":
        print('No found the commodity')
    return response


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
    print("Get Goods Content successfully")
    if response:
        # 1. 解析总的comments的href
        soup = BeautifulSoup(response, 'lxml')
        all_reviews = soup.find_all("a", {"data-hook": "see-all-reviews-link-foot"})
        if len(all_reviews) > 0:
            all_reviews_href = all_reviews[0]["href"]
            if len(all_reviews_href) > 0:
                # 2.进入all reviews界面
                response = getAllReviewsCommentsContent(all_reviews_href)
                if response:
                    # 3. 解析comments
                    print("Get All Reviews Successfully, begin to parse")
                    amazonParser = amazonBeautifulParser()
                    amazonParser.amazon_parser(response)
                else:
                    print("Get All Reviews failed")
