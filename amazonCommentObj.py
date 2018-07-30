class amazonCommentObj:

    soup = None

    def __init__(self):
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
