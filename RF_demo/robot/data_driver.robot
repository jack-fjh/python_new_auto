*** Settings ***
Documentation       数据驱动
Library         SeleniumLibrary
Library         DataDriver          ../data/data1.csv
Test Template   用户登录
Test Setup      Open Browser        ${LoginURL}     chrome
Test Teardown   Close Browser
*** Variables ***
${LoginURL}     http://49.233.108.117:3000/signin



*** Keywords ***
用户登录
    [Arguments]     ${username}     ${password}
#    Open Browser    ${LoginURL}       chrome
    Input Text      id:name      ${username}
    Input Password  id:pass     ${password}
    Click Element   css:div [class="form-actions"]>input

#*** Test Cases ***              UserName            password        [Tages]         [Documentation]

#用户名或密码错误                    test1               111111
#信息不完整                           test2               ${empty}        123         documentation内容
#用户登录成功                      testuser1           123456

*** Test Cases ***
使用用户名和密码进行登录 '${username}' '${password}'

