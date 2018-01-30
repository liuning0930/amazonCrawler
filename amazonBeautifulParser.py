from bs4 import BeautifulSoup
from amazonComments import *


class amazonBeautifulParser:
    def __init__(self):
        self.soup = None

    def findAllComments(self, comments):
        print("find all comments")
        amazon_comments = amazonComments(comments, self.soup)

    def amazon_parser(self, html):
        self.soup = BeautifulSoup(html, "lxml")
        commentsSection = self.soup.find_all("div", {"class": "a-section review-views celwidget"})
        self.findAllComments(commentsSection)
        return


class amazonUserObj:
    def __init__(self):
        print("amazon User")
        self.user_id = ""
        self.user_name = ""
        self.user_picture = ""
        self.user_profile = ""
