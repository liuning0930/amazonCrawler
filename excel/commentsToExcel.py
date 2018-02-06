import xlwt
import sys
sys.path.append("..")

COMMENT_HEADER_NUMBER = 5


class commentsToExcel:

    def __init__(self):
        print("self")

    def createExcel(self, comments, commodityID):
        file = xlwt.Workbook()
        table = file.add_sheet(commodityID)
        # 先写编号, comment header
        for i in range(COMMENT_HEADER_NUMBER):
            if i == 0:
                table.write(0, i, 'number')
            elif i == 1:
                table.write(0, i, 'id')
            elif i == 2:
                table.write(0, i, 'text')
            elif i == 3:
                table.write(0, i, 'date')
            elif i == 4:
                table.write(0, i, 'rate')

        # 填写内容
        for num in range(len(comments)):
            comment_obj = comments[num]
            table.write(num+1, 0, num+1)
            table.write(num+1, 1, comment_obj.comment_id)
            table.write(num+1, 2, comment_obj.comment_text)
            table.write(num+1, 3, comment_obj.comment_date)
            table.write(num+1, 4, comment_obj.comment_rate)

        path = "./excelfiles/" + commodityID + ".xls"
        print(commodityID + "comments file save: " + path)
        file.save(path)
