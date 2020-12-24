*** Settings ***
Documentation  演示切换iframe
Library  SeleniumLibrary

*** Test Cases ***
安居客演示demo
    Open Browser    https://login.anjuke.com/login/form     chrome
    Select Frame   id:iframeLoginIfm
    Input Text      id:phoneIpt     18516735897
    Unselect Frame
    Click Element   css:div[id="footer"]>ul>li:nth-child(1)>a