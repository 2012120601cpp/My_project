import openpyxl
def do_Excel():
    wb = openpyxl.load_workbook(r"E:\My_project\testData\test_sql.xlsx")
    sheet1 = wb.get_sheet_by_name("Sheet1")
    sql = sheet1.cell(row=1,column=1).value
    print(sql)


if __name__ == '__main':
    do_Excel()





