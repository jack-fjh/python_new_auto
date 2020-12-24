*** Settings ***
Documentation  test web app demo
...            fengjiahui
...            关键字驱动
Library        SeleniumLibrary

*** Test Cases ***
打开百度搜索          #测试用例标题，可以使用任意语言来描述
    Open Browser    https://www.baidu.com   chrome      #参数值之间使用tab健隔开
    Input Text      id:kw   hello world
    Click Element   id:su