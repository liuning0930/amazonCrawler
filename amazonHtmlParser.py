from html.parser import HTMLParser
from html.entities import name2codepoint

# HTMLParser库的中心思想：每个tag来解析，进入handle_starttag，在这里面，判断是否是自己需要解析的tag，通过flag来表示。然后进入handle_data来获取数据，hanlde_endtag进入结尾

class amazonHtmlParser(HTMLParser):

    flag = False;

    def __init__(self):
        super().__init__()
        self._startAttrs = set()

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None
        
        for attr in attrs:
            self._startAttrs.add(attr)

        import pdb; pdb.set_trace();
        if tag=="div" and _attr(attrs, "a-expander-content a-expander-partial-collapse-content"):
            self.flag = True


    def getStartAttrs(self):
        return self._startAttrs
    

    def handle_endtag(self, tag):
        if self.flag == True:
            self.flag = False

    def handle_data(self, data):
        if self.flag == True:
            print("need to handle data")

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
