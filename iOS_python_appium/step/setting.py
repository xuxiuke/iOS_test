#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年03月22日

@author: Duke    设置
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Setting(base_page.Action):

    # 前置条件：更改手机号页面
    def change_cell_phone_number_page(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('手机号').click()  # 点击手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('123456')  # 输入验证码
        self.find_name('验证成功后即可换绑手机号').click()  # 点击验证成功后即可换绑手机号按钮
        time.sleep(1)

    # 前置条件：修改密码身份验证页面
    def change_password_page(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('修改密码').click()  # 点击修改密码

    # 1、设置-账号安全，身份验证，不填验证码，验证成功后即可换绑手机号按钮不可点击(点击提示验证码错误)
    def authentication_button(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('手机号').click()  # 点击手机号
        self.find_name('验证成功后即可换绑手机号').click()  # 点击验证成功后即可换绑手机号按钮
        time.sleep(1)
        return self.find_name('验证码错误')

    # 2、设置-账号按钮，身份验证，错误验证码，toast提示：验证码错误
    def authentication_wrong_code(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('手机号').click()  # 点击手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('175862')  # 输入错误验证码
        self.find_name('验证成功后即可换绑手机号').click()  # 点击验证成功后即可换绑手机号按钮
        time.sleep(1)
        return self.find_name('验证码错误')

    # 3、设置-账号按钮，身份验证，小于6位验证码，toast提示：验证码错误
    def authentication_code_6(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('手机号').click()  # 点击手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('12345')  # 输入验证码5位
        self.find_name('验证成功后即可换绑手机号').click()  # 点击验证成功后即可换绑手机号按钮
        time.sleep(1)
        return self.find_name('验证码错误')

    # 4、设置-账号按钮，更改手机号，不输入手机号，直接点击获取验证码按钮，弹窗提示：手机号格式错误
    def phonepage_no_phone(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_name('获取验证码').click()  # 点击获取验证码
        return self.find_name('手机号格式错误')  # 验证弹窗是否存在

    # 5、手机号格式错误弹窗，点击我知道了，弹窗消失
    def phone_format_wrong(self):
        self.phonepage_no_phone()  # 手机号格式错误弹窗
        self.find_name('我知道了').click()  # 点击我知道了
        return self.find_name('手机号格式错误')  # 验证弹窗是否存在
    """
    # 6、设置-账号按钮，更改手机号，输入手机号，不输入验证码，更改手机号按钮不可点击
    def phonepage_button_no_code(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        # 输入手机号
        # 验证更改手机号按钮是否可点击

    # 7、设置-账号按钮，更改手机号，输入验证码，不输入手机号，更改手机号按钮不可点击
    def phonepage_button_no_phone(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        # 输入验证码
        # 验证更改手机号按钮是否可点击

    # 8、设置-账号按钮，更改手机号，输入错误手机号，输入验证码，点击更改手机号按钮，toast提示：手机号格式错误
    def phonepage_wrong_phone(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        # 输入错误手机号
        # 输入验证码
        # 点击更改手机号按钮
        return self.find_name('手机号格式错误')
    """
    # 9、设置-账号按钮，更改手机号，输入手机号，输入错误验证码，点击更改手机号按钮，toast提示：验证码错误
    def phonepage_wrong_code(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_ios_predicate("value == '手机号'").send_keys('18013986382')  # 输入手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('175862')  # 输入错误验证码
        self.find_xpath(excel.xpath_con('change_phone')).click()  # 点击更改手机号按钮
        time.sleep(1)
        return self.find_name('验证码错误')

    # 10、设置-账号按钮，更改手机号，输入手机号，输入小于6位验证码，点击更改手机号按钮，toast提示：验证码错误
    def phonepage_code_6(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_ios_predicate("value == '手机号'").send_keys('18013986382')  # 输入手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('12345')  # 输入验证码前5位
        self.find_xpath(excel.xpath_con('change_phone')).click()  # 点击更改手机号按钮
        time.sleep(1)
        return self.find_name('验证码错误')

    # 11、设置-账号按钮，更改手机号，输入已注册手机号，输入验证码，点击更改手机号按钮，toast提示：用户已存在
    def phonepage_old_user(self):
        self.change_cell_phone_number_page()  # 账号登陆，进入更改手机号页面
        self.find_ios_predicate("value == '手机号'").send_keys('18013986382')  # 输入手机号
        self.find_xpath(excel.xpath_con('verification_code')).send_keys('123456')  # 输入验证码
        self.find_xpath(excel.xpath_con('change_phone')).click()  # 点击更改手机号按钮
        time.sleep(1)
        return self.find_name('用户已存在')
    """
    # 12、设置-账号安全-邮箱，不输入验证码，验证成功后即可换绑邮箱（邮箱验证码没有设置为123456，大部分用例不可翻译，省略，同更改手机号）按钮，不可点击
    def mail_no_code(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('邮箱').click()  # 点击邮箱
        return self.find_name('获取邮件验证码').is_enabled()  # 验证验证成功后即可换绑邮箱按钮是否可点击
    """
    # 13、设置-账号安全-邮箱，输入错误验证码，toast提示：验证码失效
    def mail_wrong_code(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('邮箱').click()  # 点击邮箱
        self.find_ios_predicate("value == '邮箱地址'").send_keys('fgyeugfv@dssfs.com')  # 输入未注册邮箱
        self.find_name('获取邮件验证码').click()  # 点击获取邮件验证码按钮
        self.find_xpath(excel.xpath_con('change_email')).send_keys('123456')  # 输入错误验证码
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('验证码错误')
    """
    # 14、设置-账号安全-绑定邮箱-验证邮箱，未输入验证码，确定按钮不可点击
    """
    # 15、设置-账号安全-邮箱，输入邮箱格式错误，弹窗提示：电子邮箱无效
    def wrong_email(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('邮箱').click()  # 点击邮箱
        self.find_ios_predicate("value == '邮箱地址'").send_keys('xxkmtyx@126')  # 输入邮箱格式错误
        self.find_name('获取邮件验证码').click()  # 点击获取邮件验证码按钮
        time.sleep(1)
        return self.find_name('电子邮箱无效')  # 验证弹窗是否无效

    # 16、设置-账号安全-邮箱，输入邮箱已注册，toast提示：用户已存在
    def email_old_user(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('账号安全').click()  # 点击账号安全
        self.find_name('邮箱').click()  # 点击邮箱
        self.find_ios_predicate("value == '邮箱地址'").send_keys('xxkmtyx@126.com')  # 输入邮箱格式错误
        self.find_name('获取邮件验证码').click()  # 点击获取邮件验证码按钮
        time.sleep(1)
        return self.find_name('用户已存在')  # 验证toast是否正确

    # 17、设置-账号安全-修改密码，不输入验证码，验证成功后即可修改密码按钮，不可点击
    def password_no_code(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        return self.find_name('验证成功后即可修改密码').is_enabled()  # 验证验证成功后即可修改密码按钮是否可点击

    # 18、设置-账号安全-修改密码，输入错误密码，点击验证成功后即可修改密码按钮，toast提示：验证码错误
    def password_wrong_code(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('635241')  # 输入错误的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        time.sleep(1)
        return self.find_name('验证码不正确，请重新输入')

    # 19、设置-账号安全-修改密码-修改密码，不输入新密码，修复密码按钮不可点击
    def password_no_new_password(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('123456')  # 输入正确的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        return self.find_xpath(excel.xpath_con('change_password')).is_enabled()  # 验证确定按钮是否可点击

    # 20、设置-账号安全-修改密码-修改密码，输入少于8位新密码，toast提示：密码长度不能小于8个字符
    def password_new_password_6(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('123456')  # 输入正确的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        self.find_xpath(excel.xpath_con('change_password_input')).send_keys('1234567')  # 输入少于8位新密码
        self.find_xpath(excel.xpath_con('change_password')).click()  # 点击修改密码按钮
        time.sleep(1)
        return self.find_name('密码长度不能小于8个字符')

    # 21、设置-账号安全-修改密码-修改密码，输入全数字新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def password_new_number_password(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('123456')  # 输入正确的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('change_password_input')).send_keys('12345678')  # 输入8位全数字密码
        self.find_xpath(excel.xpath_con('change_password')).click()  # 点击修改密码按钮
        time.sleep(1)
        return self.find_name('密码至少有数字、字母或符号的2种组合')

    # 22、设置-账号安全-修改密码-修改密码，输入全字母新密码，toast提示：密码至少有数字、字母或符号的2种组合
    def password_new_letter_password(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('123456')  # 输入正确的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('change_password_input')).send_keys('qazwsxed')  # 输入8位全字母密码
        self.find_xpath(excel.xpath_con('change_password')).click()  # 点击修改密码按钮
        time.sleep(1)
        return self.find_name('密码至少有数字、字母或符号的2种组合')

    # 23、设置-账号安全-修改密码-修改密码，输入正确的新密码，返回我的页面
    def new_password(self):
        self.change_password_page()  # 账号登陆，修改密码验证身份页面
        self.find_ios_predicate("value == '请输入验证码'").send_keys('123456')  # 输入正确的验证码
        self.find_name('验证成功后即可修改密码').click()  # 点击验证成功后即可修改密码按钮
        self.find_xpath(excel.xpath_con('change_password_input')).send_keys('wl123456789')  # 输入8位全字母密码
        self.find_xpath(excel.xpath_con('change_password')).click()  # 点击修改密码按钮
        self.find_name('加载中...')  # 过渡
        time.sleep(2)
        return self.find_name('设置')  # 验证是否在我的页面,密码修改成功跳转我的页面(修改成功toast获取成功概率太低)

    # 24、设置-推送通知，关闭按钮，设备推送管理等隐藏
    def close_push(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_xpath(excel.xpath_con('push_notification_open')).click()  # 点击关闭推送通知
        return self.find_name('设备推送管理')

    # 25、设置-推送通知，打开按钮，推送时间等展开
    def open_push(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_xpath(excel.xpath_con('push_notification_open')).click()  # 点击关闭推送通知
        time.sleep(1)
        self.find_xpath(excel.xpath_con('push_notification_close')).click()  # 点击打开推送通知
        return self.find_name('推送时间')

    # 26、设置-报警语音-报警语音，关闭按钮，语速等隐藏
    def closing_alarm_speech(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('报警语音').click()  # 点击报警语音
        self.find_xpath(excel.xpath_con('alarm_speech_open')).click()  # 点击报警语音开关按钮，关闭
        return self.find_name('语速')

    # 27、设置-报警语音-报警语音，打开按钮，语种等展开
    def open_alarm_speech(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('报警语音').click()  # 点击报警语音
        self.find_xpath(excel.xpath_con('alarm_speech_open')).click()  # 点击报警语音开关按钮，关闭
        time.sleep(1)
        self.find_xpath(excel.xpath_con('alarm_speech_close')).click()  # 点击报警语音开关按钮，打开
        return self.find_name('语种')

    # 28、设置，点击退出登陆
    def drop_out(self):
        self.account_login()  # 账号登陆
        self.find_name('设置').click()  # 点击设置
        self.find_name('退出登录').click()  # 点击退出登录
        self.find_name('处理中...')  # 过渡
        time.sleep(2)
        return self.find_name('局域网登录')  # 验证是否退出成功，登录包含局域网登录按钮

