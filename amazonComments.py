import os
import sys
from amazonCommentObj import amazonCommentObj
from bs4 import BeautifulSoup


class amazonComments:

    def __init__(self, comments, soup):
        self.origin_comments = comments
        self.commentObjArray = []
        self.parser_comments(comments, soup)

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
        elif isinstance(attrs, dict):
            return self.contains(attr, attrs.keys())

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
            try:
                soup = BeautifulSoup(str(comment), "lxml")
                review_div = soup.div
                comment_id = review_div["id"]
                comment_obj = amazonCommentObj()
                comment_obj.comment_id = comment_id
                celwidget_div = soup.div.div
                for child in celwidget_div.children:
                    if not self.containsAttrs('class', child.attrs):
                        continue

                    class_array = child["class"]
                    # 找出comment data的div
                    if child.name == "div" and self.contains('a-row', class_array) and self.contains('review-data', class_array) and self.contains('a-spacing-small', class_array) and len(class_array) == 3:
                        expander_collapsed_span = child.span
                        if expander_collapsed_span["data-hook"] == "review-body":
                            comment_data = expander_collapsed_span.string
                            comment_obj.comment_text = comment_data

                    if child.name == 'div' and self.contains('a-row', class_array) and len(class_array) == 1:
                        for div_child in child.children:
                            # 找到rate
                            if div_child.name == 'a' and self.containsAttrs('class', div_child.attrs) and self.containsAttrs('title', div_child.attrs):
                                rate_a = div_child
                                rate_a_span = rate_a.span
                                rate_title = rate_a_span.string
                                comment_obj.comment_rate = self.calculateRate(rate_title)
                            # 找到评论日期
                            elif div_child.name == "span" and self.containsAttrs("data-hook", div_child.attrs) and div_child["data-hook"] == "review-date":
                                comment_date = div_child.string
                                comment_obj.comment_date = comment_date
                                parser_comments.append(comment_obj)
            except Exception as e:
                print(e)
                continue

        self.commentObjArray = parser_comments
        return parser_comments
