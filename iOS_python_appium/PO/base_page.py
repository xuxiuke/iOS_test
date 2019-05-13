#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年02月21日

@author: Duke    公共类
"""

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC ,\
#      expected_conditions
import time
from appium.webdriver.mobilecommand import MobileCommand
# from appium.webdriver.common.touch_action import TouchAction
from appiumframework.PO import excel
# from operator import eq

class Action(object):
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 屏幕向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 左划拉出网关解除绑定按钮,换手机需要重新填数据-------------------------ios
    def left_stroke(self, t):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # l = self.getSize()
        self.driver.swipe(300, 150, 150, 150, t)

    # 场景编辑页面，左划拉出删除按钮，换手机需要重新填数据ios
    def leftswip_editscene(self, t):
        self.driver.swipe(300, 330, 150, 330, t)

    # 我的管家页面，左划，删除管家ios
    def leftswip_housekeeper(self, t):
        self.driver.swipe(300, 100, 150, 100, t)

    # 定时任务编辑页面，左划，删除执行任务ios
    def leftswip_delaytask(self, t):
        self.driver.swipe(300, 380, 150, 380, t)

    # 情景任务编辑页面-条件任务，左划，拉出删除按钮ios
    def leftswip_condition(self, t):
        self.driver.swipe(300, 250, 150, 250, t)

    # 情景任务编辑页面-执行任务，左划，拉出删除按钮（未设置条件任务ios
    def leftswip_implement(self, t):
        self.driver.swipe(300, 300, 150, 300, t)

    # 场景-延时编辑框，点击增加1s,换手机需要重新填数据-------------------------
    def tap_scene_delay(self):
        self.driver.tap([(597, 828), (810, 915)], 500)  # 点击坐标，增加1s

    # 点击管理分区ios
    def tap_zoning_management(self):
        self.driver.tap([(290, 110), (360, 130)], 500)

    # 点击添加设备ios
    def tap_add_device(self):
        self.driver.tap([(290, 70), (360, 90)], 500)

    # 长按封装,例子：el = self.find_xpath(excel.xpath_con('first_scene'))ios
    def long_press_custom(self, el):
        # TouchAction(self.driver).long_press(el, None, None, 5000).perform()  # ios不执行
        elx = el.location.get('x')
        ely = el.location.get('y')
        self.driver.swipe(elx, ely, elx, ely, 2000)

    # 重写元素定位的方法，速度第一ios
    def find_ios_predicate(self, loc):
        try:
            print("查找元素： %s" % loc)
            return self.driver.find_element_by_ios_predicate(loc)  #  "type == 'XCUIElementTypeButton' AND value == 'ClearEmail'"
        except Exception as e:
            print(e)
            print("未找到： %s" % loc)
            return False

    # 速度第二ios
    def find_name(self, loc):
        try:
            print("查找元素： %s" % loc)
            return self.driver.find_element_by_accessibility_id(loc)  # label或name
        except Exception as e:
            print(e)
            print("未找到：%s" % loc)
            return False

    # 速度并列第二ios
    def find_class_name(self, loc):
        try:
            print("查找元素： %s" % loc)
            return self.driver.find_element_by_class_name(loc)  # 不唯一情况较多，少用
        except Exception as e:
            print(e)
            print("未找到： %s" % loc)
            return False

    # 速度最慢ios
    def find_xpath(self, loc):
        try:
            print("查找元素： %s" % loc)
            return self.driver.find_element_by_xpath(loc)
        except Exception as e:
            print(e)
            print("未找到： %s" % loc)
            return False

    # 输入内容ios
    def input_content(self, loc, name):
        self.find_ios_predicate(loc).send_keys(name)

    # 判断是否是包涵这个xpath的页面ios
    def page_xpath(self, xpath1):
        if self.find_xpath(xpath1):
            print('页面包涵元素： ' + xpath1)
            return True
        else:
            print('页面没有元素： ' + xpath1)
            return False

    # 获取控件的text.ios
    def get_text(self, xpath1):
        return self.find_xpath(xpath1).text

    """
    # 判断页面元素是否存在
    def is_element(self, identifyBy, c):
        flag = None
        try:
            if identifyBy == 'id':
                self.driver.find_element_by_id(c)
            elif identifyBy == 'xpath':
                self.driver.find_element_by_xpath(c)
            elif identifyBy == 'class':
                self.driver.find_element_by_class_name(c)
            elif identifyBy == 'link_text':
                self.driver.find_element_by_link_text(c)
            elif identifyBy == 'partial_link_text':
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == 'name':
                self.driver.find_element_by_name(c)
            elif identifyBy == 'tag_name':
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == 'css_selector':
                self.driver.find_element_by_css_selector(c)
            flag = True
            print('找到元素： ' + c)
        except ValueError:
            flag = False
            print('未找到元素： ' + c)
        finally:
            return flag

    # 版本更新点击取消按钮
    def update_button(self):
        result = self.is_element('id', "cc.wulian.smarthomev6:id/btn_negative")
        if result:
            self.find_xpath("cc.wulian.smarthomev6:id/btn_negative").click()

    # 抛异常message
    def message_show(self, msg):
        raise NameError(msg)

    # 判断toast是否存在
    def find_toast(self, message):
        try:
            toast_loc = ("xpath", ".//*[contains(@text, '%s')]" % message)
            WebDriverWait(self.driver, 17).until(EC.presence_of_all_elements_located(toast_loc))
            print('找到toast： ' + message)
            return True
        except ValueError:
            print('未找到toast： ' + message)
            return False

    # 等待activity
    def wait_ac(self, activityName):
        s = self.driver.wait_activity(activityName, 3)
        if s:
            print('找到页面： ' + activityName)
            return True
        else:
            print('未找到页面： ' + activityName)
            return False

    # 输入验证码1-6
    def input_validation_code(self):
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(11)
        self.driver.press_keycode(12)
        self.driver.press_keycode(13)

    # 输入错误验证码
    def input_error_validation_code(self):
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(11)
        self.driver.press_keycode(12)
        self.driver.press_keycode(14)

    # 设备列表页面点击设备
    def click_device(self, deviceName):
        for i in range(10):
            if self.find_name(deviceName):
                time.sleep(1)
                self.driver.find_element_by_android_uiautomator('text(\"%s\")' % deviceName).click()
                break
            else:
                self.swipeUp(1000)
                time.sleep(1)
    """

    # 切换至H5界面ios
    def switch_h5(self):
        print (self.driver.contexts)
        d = self.driver.contexts
        # print (self.driver.current_context)
        # print (self.driver.page_source)  # 打印H5源码
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_cc.wulian.smarthomev6"})
        # self.driver.switch_to.context('WEBVIEW_cc.wulian.smarthomev6')
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": d[-1]})
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_1"})
        # print (self.driver.page_source)  # 打印H5源码
        print (self.driver.current_context)

    # 切换至原生ios
    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        print (self.driver.current_context)

    # ------------------------------------------------------------------------------------------------------------------
    # 前置条件：退出登陆，登录页面ios
    def log_out(self):
        if self.find_name('登录/注册'):
            print('未登陆！')
            self.find_name('登录/注册').click()  # 点击登录/注册
        else:
            self.find_name('设置').click()  # 点击设置
            self.find_name('退出登录').click()  # 点击退出登录
        time.sleep(2)

    # 前置条件：账号登陆，我的页面ios
    def account_login(self):
        self.find_name('我的').click()  # 点击我的按钮
        if self.find_name('登录/注册'):
            self.find_name('登录/注册').click()  # 点击登录/注册
            self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
            self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('18013986382')  # 输入账号
            self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl123456789')  # 输入密码
            self.find_name('登录').click()  # 点击登录
            time.sleep(2)

    # 前置条件：账号登陆，解绑所有网关，我的页面ios
    def untie(self):
        self.account_login()  # 登陆
        self.find_name('网关中心').click()  # 点击网关中心
        while True:
            if self.find_name('未登录网关'):
                print('未登陆网关！')
                break
            else:
                self.find_name('网关列表').click()  # 点击网关列表
                time.sleep(1)
                self.left_stroke(2000)  # 左划拉出解除绑定按钮
                self.find_name('解除绑定').click()  # 点击解除绑定按钮
                self.find_name('确定').click()  # 点击确定按钮
                self.find_name('common icon back').click()  # 点击左上返回按钮
                print('解绑一个网关！')
        print('没有绑定网关了！')
        self.find_name('common icon back').click()  # 点击左上返回按钮

    # 前置条件：账号登陆，如果未绑定网关，绑定网关，网关中心页面ios
    def old_gateway(self):
        self.account_login()  # 登陆
        self.find_name('网关中心').click()  # 点击网关中心
        if self.find_name('未登录网关'):
            self.find_name('网关列表').click()  # 点击网关列表
            self.find_name('common icon add').click()  # 点击网关列表页面右上+按钮
            self.find_ios_predicate("value == '请输入网关账号'").send_keys('50294D20B1FC')  # 输入网关ID
            self.find_ios_predicate("value == '输入密码'").send_keys('qazwsx1234')  # 输入密码
            self.find_name('绑定').click()  # 点击绑定按钮
            self.driver.back()
            print('网关绑定成功！')
        else:
            print('已经绑定网关！')

    # 前置条件：账号登陆，解绑原来所有网关，重新绑定网关，我的页面
    def bound_newgateway(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_xpath(excel.xpath_con('home')).click()
        self.find_xpath(excel.ios_predicate_con('scene_icon')).click()  # 点击场景，弹窗提示尚未绑定网关
        time.sleep(1)
        self.find_xpath(excel.ios_predicate_con('dialog_btn_positive')).click()  # 点击去绑定按钮
        self.find_xpath(excel.ios_predicate_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys('50294D20B1FC')  # 输入网关ID
        self.find_xpath(excel.ios_predicate_con('et_gateway_password')).send_keys('qazwsx1234')  # 输入网关密码
        self.find_xpath(excel.ios_predicate_con('btn_gateway_login')).click()  # 点击绑定网关按钮
        time.sleep(2)
        self.find_xpath(excel.ios_predicate_con('img_left')).click()
        self.find_xpath(excel.xpath_con('mine')).click()

    # 前置条件：账号登陆，绑定网关，全部场景页面，删除原有场景ios
    def scene_page(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()  # 点击智能
        while True:
            if self.find_name('暂无场景'):  # 验证是否有场景
                break
            else:
                self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
                self.find_name('删除场景').click()  # 点击删除场景
                time.sleep(1)
                self.find_name('确定').click()  # 点击确定按钮
                time.sleep(1)

    # 前置条件：账号登陆，绑定网关，分区管理页面,删除已有分区ios
    def zoning_management_page(self):
        self.old_gateway()  # 账号登陆，网关绑定，网关中心页面
        self.driver.back()
        self.find_name('设备').click()  # 点击设备
        self.find_name('common icon add').click()  # 点击右上+按钮
        time.sleep(1)
        self.tap_zoning_management()  # 点击管理分区
        while True:
            if self.find_name('device group more'):  # 验证是否有分区右侧更多按钮
                self.find_name('device group more').click()  # 点击第一个分区更多按钮
                self.find_name('删除').click()  # 点击删除按钮
                time.sleep(1)
                self.find_name('确定').click()  # 点击确定按钮
                self.find_name('处理中...')  # 过渡
                time.sleep(1)
            else:
                break

    # 前置条件，分区管理页面创建一个分区
    def creat_zone(self, name):
        self.find_name('common icon add').click()  # 点击右键角+按钮，新增分区
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(name)  # 输入新分区名称，呵呵
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)

    # 前置条件，至少有一个分区，设备列表页面ios
    def least_one_zone(self):
        self.old_gateway()  # 账号登陆，网关绑定，网关中心页面
        self.driver.back()
        time.sleep(2)
        self.find_name('设备').click()  # 点击设备
        self.find_name('common icon add').click()  # 点击右上+按钮
        time.sleep(1)
        self.tap_zoning_management()  # 点击管理分区
        if self.find_ios_predicate("name CONTAINS '个设备'"):
            self.driver.back()  # 返回设备列表页面
        else:
            self.creat_zone('自动化测试')
            self.driver.back()  # 返回设备列表页面
