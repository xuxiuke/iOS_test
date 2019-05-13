#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年03月05日

@author: Duke    账号登陆+物联会员+意见反馈+关于+个人信息+网关中心    43条用例
"""

from appiumframework.PO.open_app import Open_app
from appiumframework.step import account_login
import unittest
import time
from appiumframework.PO import excel
import warnings

class Test004(unittest.TestCase, account_login.Account_login): # TestCase类，所有测试用例类继承的基本类
    """账号登陆+物联会员+意见反馈+关于+个人信息+网关中心测试"""
    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 屏蔽ResourceWarning报警
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、账号登陆，未绑定网关-首页
    def test_home_page(self):
        self.assertTrue(self.home_page())

    # 2、尚未登录网关编辑框，点击去登录，跳转到网关列表
    def test_go_to_land(self):
        self.assertTrue(self.go_to_land())

    # 3、尚未登录网关编辑框，点击取消按钮，编辑框消失
    def test_not_gateway_cancel(self):
        self.assertFalse(self.not_gateway_cancel())

    # 4、账号登陆，未绑定网关-查看小铃铛报警消息
    def test_alarm_message(self):
        self.assertTrue(self.alarm_message())

    # 5、账号登陆，未绑定网关-查看小铃铛日志消息
    def test_log_message(self):
        self.assertTrue(self.log_message())

    # 6、账号登陆，未绑定网关-点击设备，暂无设备
    def test_click_the_devide(self):
        self.assertTrue(self.clicl_the_device())

    # 7、账号登陆，未绑定网关-我的页面,物联会员
    def test_click_the_mine(self):
        self.assertTrue(self.click_the_mine())

    # 8、账号登陆，未绑定网关-绑定网关流程
    def test_bound_gateway(self):
        self.assertNotEqual(self.bound_gateway(), '未登录网关', '网关绑定失败')

    # 9、账号登陆，未绑定网关-绑定网关流程,不输入账号
    def test_bound_gateway_no_id(self):
        self.assertFalse(self.bound_gateway_no_id())

    # 10、账号登陆，未绑定网关-绑定网关流程,不输入密码
    def test_bound_gateway_no_password(self):
        self.assertFalse(self.bound_gateway_no_password())

    # 11、账号登陆，未绑定网关-绑定网关流程,输入密码少于6位
    def test_bound_gateway_password5(self):
        self.assertFalse(self.bound_gateway_password5())

    # 12、账号登陆，未绑定网关-绑定网关流程,输入错误密码
    def test_bound_gateway_wrong_password(self):
        self.assertTrue(self.bound_gateway_wrong_password())

    # 13、我的页面，进入物联会员
    def test_wulian_member(self):
        self.assertTrue(self.wulian_member())

    # 14、我的页面，物联会员，进入积分变动记录页面
    def test_integral_change(self):
        self.assertTrue(self.integral_change())

    # 15、我的页面，物联会员，签到规则
    def test_sign_in_rules(self):
        self.assertTrue(self.sign_in_rules())

    # 16、我的页面，物联会员，会员说明
    def test_member_description(self):
        self.assertTrue(self.member_description())

    # 17、我的页面，物联会员，积分说明
    def test_integral_explanation(self):
        self.assertTrue(self.integral_explanantion())

    # 18、我的页面，进入意见反馈页面
    def test_feed_back(self):
        self.assertTrue(self.feed_back())

    # 19、意见反馈，不输入内容，提交按钮不可点击
    def test_feed_back_submit(self):
        self.assertFalse(self.feed_back_submit())

    # 20、意见反馈，提交意见
    def test_feed_back_edit(self):
        self.assertTrue(self.feed_back_edit())

    # 21、关于页面
    def test_about_page(self):
        self.assertTrue(self.about_page())

    # 22、关于-功能介绍
    def test_about_introduction(self):
        self.assertTrue(self.about_introduction())

    # 23、关于-关于物联
    def test_about_wulian(self):
        self.assertTrue(self.about_wulian())

    # 24、个人信息页面
    def test_personal_information(self):
        self.assertTrue(self.personal_information())

    # 25、个人信息-点击头像
    def test_head_portrait(self):
        self.assertTrue(self.head_portrait())

    # 26、个人信息-点击头像,点击取消，编辑框消失
    def test_head_portrait_cancel(self):
        self.assertFalse(self.head_portrait_cancel())

    # 27、个人信息-修改名称
    def test_modify_the_name(self):
        self.assertTrue(self.modify_the_name())
        # 改回名称
        time.sleep(1)
        self.find_name('姓名').click()  # 点击名称
        self.find_xpath(excel.xpath_con('modify_name')).send_keys(u'Duke正式服')  # 输入新名称
        self.find_name('确定').click()  # 点击确定按钮

    # 28、个人信息-修改名称，取消
    def test_modify_the_name_cancel(self):
        self.assertFalse(self.modify_the_name_cancel())

    # 29、个人信息-修改名称，不输入点击确定，点击无效，修改名称弹窗还在
    def test_modify_the_name_determine(self):
        self.assertTrue(self.modify_the_name_determine())

    # 30、网关中心-已绑定网关
    def test_bound_gateway_list(self):
        self.assertTrue(self.bound_gateway_list())

    # 31、网关中心-已接受分享
    def test_acceptance_of_sharing(self):
        self.assertTrue(self.acceptance_of_sharing())

    # 32、网关设置-修改网关昵称
    def test_gateway_name(self):
        self.assertTrue(self.gateway_name())
        # 改回昵称
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关昵称').click()  # 点击网关昵称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('呵呵')  # 输入网关新昵称
        self.find_name('确定').click()  # 点击确定按钮

    # 33、网关设置-修改网关昵称，取消
    def test_gateway_name_cancel(self):
        self.assertFalse(self.gateway_name_cancel())

    # 34、网关设置-修改网关昵称，不输入点击确定
    def test_gateway_no_name(self):
        self.assertTrue(self.gateway_no_name())

    # 35、网关设置-修改密码
    def test_change_password(self):
        self.assertTrue(self.change_password())
        # 改回密码
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'123456abcd')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'qazwsx1234')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮

    # 36、网关设置-修改密码-未填写原始密码
    def test_change_no_old_password(self):
        self.assertFalse(self.change_no_old_password())

    # 37、网关设置-修改密码-未填写新密码
    def test_change_no_new_password(self):
        self.assertFalse(self.change_no_new_password())

    # 38、网关设置-修改密码-错错的原始密码，toast提示：修改失败
    def test_change_wrong_old_password(self):
        self.assertTrue(self.change_wrong_old_password())

    # 39、网关设置-修改密码-新密码全数字，toast提示：密码至少有数字、字母或符号的2种组合
    def test_change_number_password(self):
        self.assertTrue(self.change_number_password())

    # 40、网关设置-修改密码-新密码全字母，toast提示：密码至少有数字、字母或符号的2种组合
    def test_change_letter_password(self):
        self.assertTrue(self.change_letter_password())

    # 41、网关设置-修改密码-新密码小于6位，toast提示：密码长度不能小于6个字符
    def test_change_password_6(self):
        self.assertTrue(self.change_password_6())

    # 42、网关设置-修改密码-新密码与原始密码相同，toast提示：新密码不能和老密码相同
    def test_change_same_password(self):
        self.assertTrue(self.change_same_password())

    # 43、账号登陆，未绑定网关-点击智能
    def test_smart_page(self):
        self.assertTrue(self.smart_page())
