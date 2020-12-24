import csv,os
# print(os.path.dirname(__file__))
# res=os.path.join(os.path.dirname(__file__), '/data/route.csv')
# print(res)
# with open(r'C:\tools\git\git-cangku\RF_demo\data\route.csv') as f:
#     reader=csv.reader(f,delimiter=',')
#     print(reader,type(reader))
#     for line in reader:
#         print(line)


with open('some.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(['','user1','123456'])#写入多行
    writer.writerow(['','user1','123456'])#写到一行中