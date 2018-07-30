# coding=utf-8
import os
import sys
import getopt
from amazonBeautifulParser import amazonBeautifulParser
from bs4 import BeautifulSoup
from amazonRequest import amazonRequest
sys.path.append("..")
from excel.commentsToExcel import commentsToExcel
import multiprocessing

# https://www.amazon.com/dp/B072JCVHF6
# B019T8Q426 B000N3SR22


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


def childProcess(commodityID):
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
                    comments = amazonParser.amazon_parser(response)
                    if len(comments) > 0:
                        excel_comments = commentsToExcel()
                        excel_comments.createExcel(comments, commodityID)
                else:
                    print("Get All Reviews failed")


def beginToParser(commodityIDs):
    print('Parent process %s.' % os.getpid())
    for commodityID in commodityIDs:
        p = multiprocessing.Process(target=childProcess, args=(commodityID,))
        print('Child process will start.')
        p.start()
        # p.join()
        print('Child process end.')


if __name__ == '__main__':
    try:
        opts, argvs = getopt.getopt(sys.argv[1:], 'l:', '')
    except getopt.GetoptError as err:
        print(str(err))
        systemExit('Please write commodity ID')

    if (len(opts) == 0):
        systemExit('Please write commodity ID')

    commodityIDs = ""
    for option, value in opts:
        if option == '-l':
            if value == "":
                print('CommodityID is empty')
                systemExit('Please write commodity ID')
            commodityIDs = value.split(" ")

    beginToParser(commodityIDs)
