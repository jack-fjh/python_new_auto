*** Settings ***
Documentation               公共操作-登录
Library                     SeleniumLibrary


*** Keywords ***
with args
    [Arguments]         @{}          ${username}    ${pass}
    log to console      ${username}
    log to console      ****${pass}****
with dict
    &{dict} =   Create Dictionary   key=value   foo=bar
    log to console      ${dict}
with list
    @{list} =   Create List     a   b   c
    log to console      ${list}


*** Test Cases ***
test1
    with args           username=['alex','jack']        pass=2222

*** Test Cases ***
test2
    with dict
*** Test Cases ***
test3
    with list