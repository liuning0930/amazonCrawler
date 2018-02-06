from bs4 import BeautifulSoup
from amazonComments import amazonComments
from amazonRequest import amazonRequest


class amazonBeautifulParser:
    def __init__(self):
        self.soup = None
        self.pages = []

    def findAllComments(self, comments):
        print("find all comments")
        amazon_comments = amazonComments(comments, self.soup)
        return amazon_comments.commentObjArray

    def parser_pages(self):
        pages_btm = self.soup.find_all("li", {"data-reftag": "cm_cr_arp_d_paging_btm"})
        for pages_btm_li in pages_btm:
            for child in pages_btm[0].children:
                page_href = child["href"]
                self.pages.append(page_href)
        print()

    def getPageComments(self, page):
        amazon_request = amazonRequest()
        response = amazon_request.request(amazon_request.commentPrefix + page)
        if response == "":
            print("Get page comments failed")
        return response

    def page_comments_parser(self, html):
        commentsSection = self.soup.find_all("div", {"class": "a-section a-spacing-none review-views celwidget"})
        comments = self.findAllComments(commentsSection)
        return comments

    # 第一步解析
    def amazon_parser(self, html):
        self.soup = BeautifulSoup(html, "lxml")
        # 解析pages
        self.parser_pages()
        # 解析第一页的内容
        # amazon_comments = amazonComments(html, self.soup)
        # comments = amazon_comments
        comments = []
        print("Get Page 1 comments")
        # 只有1页的时候
        if len(self.pages) <= 1:
            return comments
        else:
            # 大于1页的时候
            for page_num in range(len(self.pages)):
                print("Get Page page_num comments: " + str(page_num))
                if page_num > 0:
                    # 获取每一页的内容
                    page_response = self.getPageComments(self.pages[page_num])
                    if page_response == "":
                        print("Page response error")
                        continue
                    # 解析每一页的内容
                    self.soup = BeautifulSoup(page_response, "lxml")
                    amazon_comments_page = amazonComments(page_response, self.soup)
                    page_parser_comments = amazon_comments_page.commentObjArray
                    if len(page_parser_comments) > 0:
                        comments.extend(page_parser_comments)
                        continue
                    else:
                        continue
            return comments


class amazonUserObj:
    def __init__(self):
        print("amazon User")
        self.user_id = ""
        self.user_name = ""
        self.user_picture = ""
        self.user_profile = ""
