*** Settings ***
Documentation  切换alert窗口
Library         SeleniumLibrary

*** Test Cases ***
切换alert窗口
    Set Selenium speed  0.5
    Open Browser        http://49.233.108.117:3000/signin       chrome
    Input Text          id:name         testuser1
    Input Password      id:pass         123456
    Click Element       css:[value="登录"]
    Go To               http://49.233.108.117:3000/user/testuser1
    Click Element       css:div:nth-child(2)[class="cell"] [class="topic_title_wrapper"] [title="12312312313231"]
    Click Element       css:div[id="manage_topic"] a:nth-child(2)>i
    ${message}          Handle Alert
    log to console      ${message}
