*** Settings ***
Documentation           演示使用resource文件
Resource                resource.txt
Library                 SeleniumLibrary
#Suite Setup             用户登录到系统         testuser1       123456
Suite Setup             用户登录到系统
Suite Teardown          Close Browser
Test Setup              Log to Console      开始执行test
Test Teardown           Capture Page Screenshot

*** Test Cases ***
发帖测试
    Set Selenium Implicit Wait          10
    Log to console      **********
    用户发帖
