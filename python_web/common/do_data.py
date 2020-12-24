'''
解析数据文件
'''
import csv,os
data_file_path=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(data_file_path+'/','data/data1.csv')
def do_csv(csvpath):
    test_data=[]
    with open(csvpath,'r',encoding='utf-8') as f:
        reader=csv.reader(f)
        next(reader)
        for line in reader:
            # print(line)
            test_data.append(tuple(line))
    return test_data



