#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月03日

@author: Duke    分区管理
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Zoning_management(base_page.Action):

    # 1、设备-管理分区，创建分区呵呵，确定
    def new_zoning(self):
        self.zoning_management_page()  # 账号登陆，绑定网关，分区管理页面，并删除已有分区
        self.find_name('common icon add').click()  # 点击右键角+按钮，新增分区
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(u'呵呵')  # 输入新分区名称，呵呵
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('呵呵')

    # 2、设备-管理分区，创建分区哈哈，取消
    def new_zoning_cancel(self):
        self.zoning_management_page()  # 账号登陆，绑定网关，分区管理页面，并删除已有分区
        self.find_name('common icon add').click()  # 点击右键角+按钮，新增分区
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(u'呵呵')  # 输入新分区名称，呵呵
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(1)
        return self.find_name('呵呵')

    # 3、设备-管理分区，不输入分区名，确定按钮点击无效，弹窗未消失
    def new_zoning_no_name(self):
        self.zoning_management_page()  # 账号登陆，绑定网关，分区管理页面，并删除已有分区
        self.find_name('common icon add').click()  # 点击右键角+按钮，新增分区
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('新建')

    # 4、设备-管理分区，点击编辑按钮，取消，编辑框消失
    def edit_cancel(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(1)
        return self.find_name('删除')

    # 5、设备-管理分区，点击编辑按钮，删除，确定
    def edit_delete(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('删除').click()  # 点击删除按钮
        time.sleep(1)
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(2)
        return self.find_name('呵呵')

    # 6、设备-管理分区，点击编辑按钮，删除，取消
    def edit_delete_cancel(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('删除').click()  # 点击删除按钮
        time.sleep(1)
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(2)
        return self.find_name('呵呵')

    # 7、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，确定
    def modefy_the_name(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('修改分区名称').click()  # 点击修改分区名称
        time.sleep(1)
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(u'哈哈')  # 输入新分区名称，哈哈
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('哈哈')

    # 8、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，取消
    def modefy_the_name_cancel(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('修改分区名称').click()  # 点击修改分区名称
        time.sleep(1)
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(u'哈哈')  # 输入新分区名称，哈哈
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(1)
        return self.find_name('哈哈')

    # 9、设备-管理分区，点击编辑按钮，修改分区名称，输入名称为空，确定按钮点击无效，弹窗修改分区还在
    def modefy_no_name(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('修改分区名称').click()  # 点击修改分区名称
        time.sleep(1)
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('修改分区')

    # 10、设备-管理分区，创建一个分区，添加一个设备
    def zone_add(self):
        self.new_zoning()  # 创建新区域，呵呵
        self.find_name('呵呵').click()  # 点击呵呵分区
        self.find_name('插入“门窗磁探测器”').click()  # 点击+按钮，插入“门窗磁探测器”
        self.driver.back()
        return self.find_name('1个设备')

    # 11、设备-管理分区，创建一个分区，添加一个设备，再删除一个设备
    def zone_reduce(self):
        self.zone_add()  # 创建一个分区，添加一个设备
        self.find_name('呵呵').click()  # 点击呵呵分区
        self.find_name('删除“门窗磁探测器”').click()  # 点击-按钮，删除“门窗磁探测器”
        self.find_name('删除').click()  # 点击删除按钮
        self.driver.back()
        return self.find_name('0个设备')

    # 12、设备-管理分区，创建一个分区，点击设备-全部分区可以找到
    def new_zoning_devide(self):
        self.new_zoning()  # 新建一个分区，呵呵
        self.driver.back()  # 返回设备列表
        time.sleep(1)
        self.find_xpath(excel.xpath_con('all_zone')).click()  # 点击全部分区
        time.sleep(2)
        return self.find_name('呵呵')

    # 13、设备-管理分区，创建一个分区，删除分区，点击设备-全部分区找不到
    def new_zoing_delete_devide(self):
        self.new_zoning_devide()
        self.find_xpath(excel.xpath_con('all_zone')).click()  # 点击全部分区
        self.find_name('common icon add').click()  # 点击右上+按钮
        time.sleep(1)
        self.tap_zoning_management()  # 点击管理分区
        self.find_name('device group more').click()  # 点击第一个分区更多按钮
        self.find_name('删除').click()  # 点击删除按钮
        time.sleep(1)
        self.find_name('确定').click()  # 点击确定按钮
        self.find_name('处理中...')  # 过渡
        time.sleep(1)
        self.driver.back()
        self.find_xpath(excel.xpath_con('all_zone')).click()  # 点击全部分区
        time.sleep(1)
        return self.find_name('呵呵')

