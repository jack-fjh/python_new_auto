*** Settings ***
Documentation           如何使用自定义的库
Library                 ../common/uitils.py
Library                 SeleniumLibrary


*** Keywords ***




*** Test Cases ***
使用自定义库
    ${val}          get_topic_id            http://49.233.108.117:3000/topic/5fcb39a8617b0d7f5dce255b
    log to console      ${val}