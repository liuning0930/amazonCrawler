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

    def contains(self, item, array):
        for temp_item in array:
            if temp_item == item:
                return True
        return False

    def containsAttrs(self, attr, attrs):
        if isinstance(attrs, list):
            for temp_attr in attrs:
                attr_keys = temp_attr.keys()
                return self.contains(attr, attr_keys)
        return False

    def calculateRate(self, rate_string):
        split_rate = rate_string.split(" ")
        if len(split_rate) > 1:
            return split_rate[0]

        return '0'

    def parser_comments(self, comments, soup):
        str_comments = str(comments)
        soup = BeautifulSoup(str_comments, "lxml")
        soup_comments = soup.find_all("div", {"class": "a-section review"})
        parser_comments = []

        if (len(soup_comments) == 0):
            os.system("echo comments get fialed")
            sys.exit(0)

        for comment in soup_comments:
            soup = BeautifulSoup(str(comment), "lxml")
            review_div = soup.div
            comment_id = review_div["id"]
            comment_obj = amazonCommentObj()
            comment_obj.comment_id = comment_id
            celwidget_div = soup.div.div
            for child in celwidget_div.children:
                class_array = child["class"]
                # 找出comment data的div
                if child.name == "div" and self.contains('a-row', class_array) and self.contains('review-data', class_array) and len(class_array) == 2:
                    review_text_span = child.span
                    expander_collapsed_div = review_text_span.div
                    for expander_child in expander_collapsed_div.children:
                        # 当满足这个条件才是评论
                        if expander_child.name == "div" and self.containsAttrs("data-hook", child.attrs) and expander_child["data-hook"] == "review-collapsed":
                            comment_data = expander_child.string
                            comment_obj.comment_text = comment_data

                # 找到评论日期
                if child.name == "span" and self.containsAttrs("data-hook", child.attrs) and child["data-hook"] == "review-date":
                    comment_date = child.string
                    comment_obj.comment_date = comment_date

                # 找到rate
                if child.name == 'div' and self.contains('a-row', class_array) and len(class_array) == 1:
                    rate_a = child.a
                    rate_title = rate_a["title"]
                    comment_obj.comment_rate = self.calculateRate(rate_title)

            parser_comments.append(comment_obj)
