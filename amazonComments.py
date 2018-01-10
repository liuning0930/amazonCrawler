from bs4 import BeautifulSoup

class amazonComments:

    def __init__(self,comments):
        self.origin_comments = comments

    def parser(origin_comments):
        soup = BeautifulSoup(origin_comments,"lxml")
        comments = soup.find_all("div",{"class":"a-section review"})


class amazonCommentObj:

    soup = None

    def __init__(self):
        print("amazonCommentObj")
        self.comment_id = ""
        self.comment_text = ""
        self.comment_date = ""
        self.comment_rate = 0

    def set_soup(self,soup):
        self.soup = soup
# tag.has_attr("class") and
    def parser(self,comments):
        commentsArray = self.soup.find_all("div",{"data-hook":"review"})
        import pdb; pdb.set_trace();
        print(len([commentsArray]))
