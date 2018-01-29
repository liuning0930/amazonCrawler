import os
import sys
from bs4 import BeautifulSoup


class amazonCommentObj:

    soup = None

    def __init__(self):
        print("amazonCommentObj")
        self.comment_id = ""
        self.comment_text = ""
        self.comment_date = ""
        self.comment_rate = 0

    def set_soup(self, soup):
        self.soup = soup
# tag.has_attr("class") and

    def parser_comment_obj(self, comments):
        commentsArray = self.soup.find_all("div", {"data-hook": "review"})
        print(len([commentsArray]))


class amazonComments:

    def __init__(self, comments, soup):
        self.origin_comments = comments
        self.parser_comments(comments, soup)
        self.commentObjArray = []

    def contains(self, small, big):
        for i in range(len(big)-len(small)+1):
            for j in range(len(small)):
                if big[i+j] != small[j]:
                    break
                else:
                    return True
            return False

    def parser_comments(self, comments, soup):
        str_comments = str(comments)
        soup = BeautifulSoup(str_comments, "lxml")
        soup_comments = soup.find_all("div", {"class": "a-section review"})
        parser_comments = []

        if (len(soup_comments) == 0):
            os.sys("echo comments get fialed")

        for comment in soup_comments:
            soup = BeautifulSoup(str(comment), "lxml")
            review_div = soup.div
            comment_id = review_div["id"]
            comment_obj = amazonCommentObj()
            comment_obj.comment_id = comment_id
            celwidget_div = soup.div.div
            for child in celwidget_div.children:
                if child.name == "div" and self.contains(['a-row', 'review-data'], ['a-row', 'review-data']):
                    review_text_span = child.span
                    expander_collapsed_div = review_text_span.div
                    expander_content_div = expander_collapsed_div.div
                    comment_data = expander_content_div.content
                    comment_obj.comment_text = str(comment_data)

            parser_comments.append(comment_obj)
