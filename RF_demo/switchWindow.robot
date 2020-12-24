*** Settings ***
Documentation           切换浏览器窗口

Library                 SeleniumLibrary


*** Test Cases ***
切换浏览器窗口
    Open Browser            https://www.baidu.com           chrome
    Set Selenium Implicit Wait      10
    Input Text              id:kw       hello world
    Click Element           id:su
    Click Element           css:div[id="content_left"] div[id="1"]>h3>a:nth-child(1)
    Switch Window           NEW
    Input Text              id:query            hello