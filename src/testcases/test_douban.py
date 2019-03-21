import pytest
from selenium import webdriver
def test_douban_login():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com")
    print("open douban window~")
    login_frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(login_frame)
    driver.execute_script("arguments[0].style.background = 'rgb(138,43,226)';""login_frame")
    forget_passwd_els = driver.find_element_by_class_name('account-form-link')
    driver.execute_script("arguments[0].style.background = 'rgb(138,43,226)';""forget_passwd_els")
    forget_passwd_els.click()
    open_windows = driver.window_handles
    print("windows test:"+ str(open_windows))
    driver.switch_to.window(open_windows[1])
    driver.title == '帐号 使用帮助'


