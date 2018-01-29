from html.parser import HTMLParser
from html.entities import name2codepoint


class amazonHtmlParser(HTMLParser):

    flag = False
    comments = []

    def __init__(self):
        super().__init__()
        self._startAttrs = set()

    def handle_starttag(self, tag, attrs):

        def _attr(attrlist, attrname):
            for each in attrlist:
                if len(each) > 1:
                    if attrname == each[1]:
                        return True
            return False
        
        for attr in attrs:
            self._startAttrs.add(attr)

        if tag=="div" and _attr(attrs, "a-section review"):
            print("find div a-section review attrs")
            self.flag = True
            import pdb; pdb.set_trace();



    def getStartAttrs(self):
        return self._startAttrs


    def getComments(self):
        return self.comments
    

    # def handle_endtag(self, tag):
    #     if self.flag == True:
    #         self.flag = False
    #         import pdb; pdb.set_trace();

    def handle_data(self, data):
        if self.flag == True:
            self.comments.append(data)
            self.flag = False

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
