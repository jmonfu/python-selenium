import openpyxl

path="C:\SeleniumTest\Test.xlsx"

workBook = openpyxl.load_workbook(path)
sheet = workBook.get_sheet_by_name("Sheet1")

for r in range(1,6): #5 rows
    for c in range(1,4): #3 cols
        sheet.cell(row=r, column=c).value = "welcome"

workBook.save(path)