#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年03月05日

@author: Duke    账号登陆+物联会员+意见反馈+关于+个人信息+网关中心
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Account_login(base_page.Action):

    # 1、账号登陆，未绑定网关-首页
    def home_page(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_name('首页').click()  # 点击首页按钮
        self.find_name('离家').click()  # 点击离家场景
        return self.find_xpath(excel.xpath_con('go_to_land'))  # 验证弹出尚未登录网关编辑窗

    # 2、尚未登录网关编辑框，点击去登录，跳转到网关列表页面
    def go_to_land(self):
        self.home_page()  # 账号登录，网关未登录，首页
        self.find_xpath(excel.xpath_con('go_to_land')).click()  # 点击去登录
        return self.find_name('网关列表')  # 验证是否进入网关列表

    # 3、尚未登录网关编辑框，点击取消按钮，编辑框消失
    def not_gateway_cancel(self):
        self.home_page()  # 账号登录，网关未登录，首页
        self.find_xpath(excel.xpath_con('not_gateway_cancel')).click()  # 点击去取消
        return self.find_xpath(excel.xpath_con('go_to_land'))  # 验证弹出尚未登录网关编辑窗

    # 4、账号登陆，未绑定网关-查看小铃铛报警消息
    def alarm_message(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_name('首页').click()  # 点击首页按钮
        self.find_name('home message icon').click()  # 点击小铃铛
        self.find_name('报警消息').click()  # 点击小铃铛-报警消息
        return self.find_name('没有报警消息')

    # 5、账号登陆，未绑定网关-查看小铃铛日志消息
    def log_message(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_name('首页').click()  # 点击首页按钮
        self.find_name('home message icon').click()  # 点击小铃铛
        self.find_name('日志').click()  # 点击小铃铛-日志消息
        return self.find_name('没有日志消息')

    # 6、账号登陆，未绑定网关-点击设备，暂无设备
    def clicl_the_device(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_name('设备').click()  # 点击设备
        return self.find_name('空列表')  # 空列表（跟android不同）

    # 7、账号登陆，未绑定网关-我的页面,物联会员
    def click_the_mine(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        return self.find_name('物联会员')

    # 8、账号登陆，未绑定网关-绑定网关流程
    def bound_gateway(self):
        self.go_to_land()  # 尚未登录网关编辑框，点击去登录，跳转到网关列表页面
        self.find_name('common icon add').click()  # 点击网关列表右上角+按钮
        self.find_ios_predicate("value == '请输入网关账号'").send_keys('50294D20B1FC')  # 输入网关ID
        self.find_ios_predicate("value == '输入密码'").send_keys('qazwsx1234')  # 输入网关密码
        self.find_xpath(excel.xpath_con('bounding_gateway')).click()  # 点击绑定网关按钮
        time.sleep(2)
        self.find_name('common icon back').click()  # 点击左上返回按钮
        self.find_name('我的').click()  # 点击我的按钮
        self.find_name('网关中心').click()  # 点击网关中心
        text = self.get_text(excel.xpath_con('gateway_center_name'))  # 获取网关中心网关名
        return text

    # 9、账号登陆，未绑定网关-绑定网关流程,不输入账号
    def bound_gateway_no_id(self):
        self.go_to_land()  # 尚未登录网关编辑框，点击去登录，跳转到网关列表页面
        self.find_name('common icon add').click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_ios_predicate("value == '请输入网关账号'").send_keys('')  # 不输入网关ID
        self.find_ios_predicate("value == '输入密码'").send_keys('qazwsx1234')  # 输入网关密码
        return self.find_xpath(excel.xpath_con('bounding_gateway')).is_enabled()  # 验证绑定按钮是否可点击

    # 10、账号登陆，未绑定网关-绑定网关流程,不输入密码
    def bound_gateway_no_password(self):
        self.go_to_land()  # 尚未登录网关编辑框，点击去登录，跳转到网关列表页面
        self.find_name('common icon add').click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_ios_predicate("value == '请输入网关账号'").send_keys('50294D20B1FC')  # 输入网关ID
        self.find_ios_predicate("value == '输入密码'").send_keys('')  # 不输入网关密码
        return self.find_xpath(excel.xpath_con('bounding_gateway')).is_enabled()  # 验证绑定按钮是否可点击

    # 11、账号登陆，未绑定网关-绑定网关流程,输入密码少于6位
    def bound_gateway_password5(self):
        self.go_to_land()  # 尚未登录网关编辑框，点击去登录，跳转到网关列表页面
        self.find_name('common icon add').click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_ios_predicate("value == '请输入网关账号'").send_keys('50294D20B1FC')  # 输入网关ID
        self.find_ios_predicate("value == '输入密码'").send_keys('12345')  # 输入网关密码少于6位密码
        return self.find_xpath(excel.xpath_con('bounding_gateway')).is_enabled()  # 验证绑定按钮是否可点击

    # 12、账号登陆，未绑定网关-绑定网关流程,输入错误密码
    def bound_gateway_wrong_password(self):
        self.go_to_land()  # 尚未登录网关编辑框，点击去登录，跳转到网关列表页面
        self.find_name('common icon add').click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_ios_predicate("value == '请输入网关账号'").send_keys('50294D20B1FC')  # 输入网关ID
        self.find_ios_predicate("value == '输入密码'").send_keys('123456789')  # 输入错误网关密码
        self.find_xpath(excel.xpath_con('bounding_gateway')).click()  # 点击绑定网关按钮
        time.sleep(1)
        return self.find_name('设备密码错误')

    # 13、我的页面，进入物联会员
    def wulian_member(self):
        self.account_login()  # 账号登陆
        time.sleep(1)
        self.find_name('物联会员').click()  # 点击物联会员
        self.find_name('页面加载中...')
        time.sleep(1)
        # self.switch_h5()  # 定位xpath即可，不需要进入h5页面
        return self.find_xpath(excel.xpath_con('wulianmember_sign_in'))  # 签到图标是否存在验证会员页面

    # 14、我的页面，物联会员，进入积分变动记录页面
    def integral_change(self):
        self.wulian_member()  # 进入wulian会员页面
        time.sleep(1)
        self.find_name('积分变动记录').click()  # 点击积分变动记录
        time.sleep(7)
        return self.find_name('当前积分：')

    # 15、我的页面，物联会员，签到规则
    def sign_in_rules(self):
        self.wulian_member()  # 进入wulian会员页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('attendance_rules')).click()  # 点击签到规则？
        return self.find_name('签到规则')

    # 16、我的页面，物联会员，会员说明
    def member_description(self):
        self.wulian_member()  # 进入wulian会员页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('member_grade')).click()  # 点击xx会员
        time.sleep(1)
        return self.find_name('会员说明')

    # 17、我的页面，物联会员，积分说明
    def integral_explanantion(self):
        self.wulian_member()  # 进入wulian会员页面
        time.sleep(1)
        self.find_name('累积积分').click()  # 点击累积积分
        time.sleep(2)
        return self.find_name('积分说明')

    # 18、我的页面，进入意见反馈页面
    def feed_back(self):
        self.account_login()  # 账号登陆
        self.find_name('意见反馈').click()  # 点击意见反馈
        return self.find_ios_predicate("value == '输入您的邮箱（选填）'")

    # 19、意见反馈，不输入内容，提交按钮不可点击
    def feed_back_submit(self):
        self.feed_back()  # 意见反馈页面
        return self.find_name('提交').is_enabled()  # 验证提交按钮是否可点击

    # 20、意见反馈，提交意见
    def feed_back_edit(self):
        self.feed_back()  # 意见反馈页面
        self.find_xpath(excel.xpath_con('feedback_input')).send_keys(u'ios自动化测试')  # 输入
        self.find_name('提交').click()  # 点击提交按钮
        time.sleep(1)
        return self.find_name('提交成功')

    # 21、关于页面
    def about_page(self):
        self.account_login()  # 账号登陆
        self.find_name('关于').click()  # 点击关于
        return self.find_name('物联传感') and self.find_name('786779954') and self.find_name('www.wuliangroup.com')

    # 22、关于-功能介绍
    def about_introduction(self):
        self.about_page()  # 关于页面
        self.find_name('功能介绍').click()  # 点击功能介绍
        self.find_name('页面加载中...')
        time.sleep(1)
        return self.find_name('1. 全新风格') and self.find_name('2. 登录界面')

    # 23、关于-关于物联
    def about_wulian(self):
        self.about_page()  # 关于页面
        self.find_name('关于物联').click()  # 点击关于物联
        self.find_name('页面加载中...')
        time.sleep(1)
        return self.find_xpath(excel.xpath_con('about_page'))  # 验证是否进入关于物联页面

    # 24、个人信息页面
    def personal_information(self):
        self.account_login()  # 账号登陆
        self.find_xpath(excel.xpath_con('Login/Register')).click()  # 点击账号昵称
        return self.find_name('个人信息')  # 验证是否进入个人信息页面

    # 25、个人信息-点击头像
    def head_portrait(self):
        self.personal_information()  # 个人信息页面
        self.find_name('头像').click()  # 点击头像，弹出编辑框
        return self.find_name('拍照')

    # 26、个人信息-点击头像,点击取消，编辑框消失
    def head_portrait_cancel(self):
        self.head_portrait()  # 个人信息页面，弹出头像修改编辑框
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(1)
        return self.find_name('拍照')

    # 27、个人信息-修改名称
    def modify_the_name(self):
        self.personal_information()  # 个人信息页面
        self.find_name('姓名').click()  # 点击名称
        self.find_xpath(excel.xpath_con('modify_name')).send_keys(u'测试哈哈111')  # 输入新名称
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('测试哈哈111')

    # 28、个人信息-修改名称，取消
    def modify_the_name_cancel(self):
        self.personal_information()  # 个人信息页面
        self.find_name('姓名').click()  # 点击名称
        self.find_xpath(excel.xpath_con('modify_name')).send_keys(u'测试哈哈222')  # 输入新名称
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('测试哈哈222')

    # 29、个人信息-修改名称，不输入点击确定，点击无效，修改名称弹窗还在
    def modify_the_name_determine(self):
        self.personal_information()  # 个人信息页面
        self.find_name('姓名').click()  # 点击名称
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('修改名字')  # 验证修改名称弹窗还在

    # 30、网关中心-已绑定网关
    def bound_gateway_list(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关列表').click()  # 点击网关列表
        return self.find_ios_predicate("type == 'XCUIElementTypeCell'")  # 验证网关列表是否有网关

    # 31、网关中心-已接受分享
    def acceptance_of_sharing(self):
        self.account_login()  # 账号登陆
        self.find_name('网关中心').click()  # 点击网关中心
        self.find_name('网关列表').click()  # 点击网关列表
        self.find_name('已接受分享').click()  # 点击已接受分享
        return self.find_name('暂无他人分享')

    # 32、网关设置-修改网关昵称----自动化点击确定，没有修改昵称
    def gateway_name(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关昵称').click()  # 点击网关昵称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('自动化测试222')  # 输入网关新昵称
        self.find_name('确定').click()  # 点击确定按钮
        self.driver.back()  # 返回上一页
        return self.find_name('自动化测试222')

    # 33、网关设置-修改网关昵称，取消
    def gateway_name_cancel(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关昵称').click()  # 点击网关昵称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('自动化测试222')  # 输入网关新昵称
        self.find_name('取消').click()  # 点击取消按钮
        self.driver.back()  # 返回上一页
        return self.find_name('自动化测试222')

    # 34、网关设置-修改网关昵称，不输入点击确定
    def gateway_no_name(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关昵称').click()  # 点击网关昵称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('修改昵称')

    # 35、网关设置-修改密码
    def change_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123456abcd')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(2)
        return self.find_name('解除绑定')  # 修改成功，跳转网关设置页面，验证是否有解除绑定按钮

    # 36、网关设置-修改密码-未填写原始密码
    def change_no_old_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        # self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  不输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123456abcd')  # 输入新密码
        return self.find_name('确定').is_enabled()  # 验证确定按钮是否可点击

    # 37、网关设置-修改密码-未填写新密码
    def change_no_new_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        # self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123456abcd')  不输入新密码
        return self.find_name('确定').is_enabled()  # 验证确定按钮是否可点击

    # 38、网关设置-修改密码-错错的原始密码，toast提示：修改失败
    def change_wrong_old_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1256')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123456abcd')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('修改失败')

    # 39、网关设置-修改密码-新密码全数字，toast提示：密码至少有数字、字母或符号的2种组合
    def change_number_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123456789')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('密码至少有数字、字母或符号的2种组合')

    # 40、网关设置-修改密码-新密码全字母，toast提示：密码至少有数字、字母或符号的2种组合
    def change_letter_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'qweasdabcd')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('密码至少有数字、字母或符号的2种组合')

    # 41、网关设置-修改密码-新密码小于6位，toast提示：密码长度不能小于6个字符
    def change_password_6(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'123abcd')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('密码长度不能小于8个字符')

    # 42、网关设置-修改密码-新密码与原始密码相同，toast提示：新密码不能和老密码相同
    def change_same_password(self):
        self.old_gateway()  # 账号登陆，如果未绑定网关，绑定网关
        self.find_name('网关设置').click()  # 点击网关设置
        self.find_name('网关密码修改').click()  # 点击网关密码修改
        self.find_xpath(excel.xpath_con('gateway_original_password')).send_keys(u'qazwsx1234')  # 输入原始密码
        self.find_xpath(excel.xpath_con('gateway_new_password')).send_keys(u'qazwsx1234')  # 输入新密码
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('新密码不能与原密码相同')

    # 43、账号登陆，未绑定网关-点击智能
    def smart_page(self):
        self.untie()  # 登陆，如果绑定网关，解绑
        self.find_name('智能').click()  # 点击智能
        return self.find_xpath(excel.xpath_con('go_to_land'))  # 验证弹出尚未登录网关编辑窗
