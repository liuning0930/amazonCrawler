from bs4 import BeautifulSoup

class amazonBeautifulParser:
    def __init__(self):
        print ("123456789")

    def findAllComments(self,soup):
        comments = soup.find_all("div",{"class":"a-section review"})
        print(len(comments))
        for reviewDiv in comments:
            

    def parser(self,html):
        soup = BeautifulSoup(html,"lxml")
        self.findAllComments(soup)

    
        
