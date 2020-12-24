def input_func():
    res_value1=input('请输入数字：')
    res_value2=input('请输入数字：')
    res_value3=input('请输入数字：')
    if res_value1 > res_value2:
        max=res_value1
        if max > res_value3:
            max=max
        else:
            max=res_value3
    else:
        if res_value2 < res_value3:
            max=res_value3
        else:
            max=res_value2
    return max

def max_func():
    res=input('请输入值1：')
    res1=input('请输入值2：')
    return max(res,res1)

def test1():
    pass
test1()