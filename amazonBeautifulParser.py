from bs4 import BeautifulSoup
from amazonComments import *

class amazonBeautifulParser:
    def __init__(self):
        print ("123456789")

    def findAllComments(self,soup):
        commentsSection = soup.find_all("div",{"class":"a-section review-views celwidget"})
        print(len(commentsSection))
        comments = []
        for reviewSection in commentsSection:
            import pdb; pdb.set_trace();
            break
            

    def parser(self,html):
        soup = BeautifulSoup(html,"lxml")
        self.findAllComments(soup)

class amazonUserObj:
    def __init__(self):
        print("amazon User")
        self.user_id = ""
        self.user_name = ""
        self.user_picture = ""
        self.user_profile = ""
        
