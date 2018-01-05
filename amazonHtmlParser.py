from html.parser import HTMLParser
from html.entities import name2codepoint

class amazonHtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self._startAttrs = set()

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            self._startAttrs.add(attr)

    def getStartTag(self):
        return self.startTag

    def getStartAttrs(self):
        return self._startAttrs
    


#     endTag = None
#     def handle_endtag(self, tag):
#         self.endTag = tag

#     bodyData = None 
#     def handle_data(self, data):
#         self.bodyData = data

# # 后面几个都没啥用
#     def handle_comment(self, data):
#         self.comment = data

#     entityref = None
#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         self.entityref = name

#     name = None
#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#             self.name = c
#         else:
#             c = chr(int(name))
#             self.name = c

#     decl = None
#     def handle_decl(self, data):
#         self.decl = data
