import xlwt
import sys
sys.path.append("..")

COMMENT_HEADER_NUMBER = 5


class commentsToExcel:

    def __init__(self):
        print("Start to create Excel")

    def createExcel(self, comments, commodityID):
        file = xlwt.Workbook()
        table = file.add_sheet(commodityID)
        for col in range(6):
            table_col = table.col(col)
            if col == 0:
                table_col.width = 256*20
            elif col == 1:
                table_col.width = 256*20
            elif col == 2:
                table_col.width = 256*20*2
            elif col == 3:
                table_col.width = 256*20
            elif col == 4:
                table_col.width = 256*20

        # 36pt
        tall_style = xlwt.easyxf('font:height 720;')
        first_row = table.row(0)
        first_row.set_style(tall_style)
        # excel style
        style = xlwt.XFStyle()
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
        alignment.wrap = 1
        # Add Alignment to Style
        style.alignment = alignment
        # 先写编号, comment header
        for i in range(COMMENT_HEADER_NUMBER):
            if i == 0:
                table.write(0, i, 'number', style)
            elif i == 1:
                table.write(0, i, 'id', style)
            elif i == 2:
                table.write(0, i, 'text', style)
            elif i == 3:
                table.write(0, i, 'date', style)
            elif i == 4:
                table.write(0, i, 'rate', style)

        # 填写内容
        for num in range(len(comments)):
            comment_obj = comments[num]
            table.write(num+1, 0, num+1, style)
            table.write(num+1, 1, comment_obj.comment_id, style)
            table.write(num+1, 2, comment_obj.comment_text, style)
            table.write(num+1, 3, comment_obj.comment_date, style)
            table.write(num+1, 4, comment_obj.comment_rate, style)

        path = "./excelfiles/" + commodityID + ".xls"
        print(commodityID + "comments file save: " + path)
        file.save(path)
