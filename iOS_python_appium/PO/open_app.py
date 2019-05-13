#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年02月21日

@author: Duke    打开APP
"""

# from appiumframework.PO import excel
from appiumframework.step import login
from appium import webdriver

class Open_app(login.Login):

    def open(self):
        desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '12.1',
            'deviceName': 'iPhone 6 Plus',
            'noReset': True,  # 不用每次清除数据
            'resetKeyboard': True,
            'app': '/Users/test/ios_appium_python/appiumframework/SmartHomeV6/SmartHomeV6.app',
            'bundleID': 'WL.SmartHomeV6',
            'udid': 'f40887649324b63d0cbbfa9cec97606fcb1d1a9c',
            'newCommandTimeout': '120',
            'automationName': 'XCUITest',
            'startIWDP': True  # 调起ios-webkit-debug-proxy，进入h5页面
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        print('打开APP成功')

    def get_driver(self):
        driver = self.driver
        return driver

    def after(self):
        self.driver.quit()

    """
    def open(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'R8V5T15629001602',
            'noReset': True,  # 不用每次清除数据
            'resetKeyboard': True,
            "unicodeKeyboard": True,
            # 'app': 'F:\\SmartHome-wulian-release-6.2.1.apk',
            'appPackage': 'cc.wulian.smarthomev6',
            'appActivity': 'cc.wulian.smarthomev6.main.welcome.SplashActivity',
            'automationName': 'Uiautomator2'  # 定位toast元素
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    """
