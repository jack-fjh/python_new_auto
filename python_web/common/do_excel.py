from openpyxl import Workbook
import os

curr_dir=os.path.dirname(os.path.abspath(os.path.curdir))
file_path=os.path.join(curr_dir, 'data', 'helloworld.xlsx')

#1:实例化workbook对象
workbook=Workbook()
#2：创建一个sheet
worksheet=workbook.active
#3：给单元格设置值
worksheet['A1']='hello'
worksheet['B1']='world'
print(worksheet.title)
#更改sheet名字
worksheet.title='用户登录'
workbook.save(filename=file_path)
