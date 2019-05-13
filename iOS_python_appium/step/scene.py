#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月08日

@author: Duke    场景
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Scene(base_page.Action):

    # 1、智能页面，无场景，页面提示：暂无场景
    def no_scene(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        return self.find_name('暂无场景')

    # 2、智能页面，创建场景，默认离家名称，场景编辑页面点击保存
    def create_scene_save(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('editingscene_finishScene')).click()  # 点击右上保存按钮
        self.switch_app()
        return self.find_name('离家')

    # 3、智能页面，创建场景，默认离家名称，场景编辑页面返回
    def create_scene_back(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('editingscene_goback')).click()  # 点击左上返回按钮
        self.switch_app()
        return self.find_name('离家')  # 验证是否有场景

    # 4、智能页面，创建场景，默认离家名称，左上返回按钮
    def create_scene_cancel(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('scene_back')).click()  # 点击左上返回按钮
        self.switch_app()
        return self.find_name('离家')

    # 5、智能页面，创建场景自定义名称呵呵123
    def hehe123_scene(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys('呵呵123')  # 输入新场景名称呵呵123
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('editingscene_finishScene')).click()  # 点击右上保存按钮
        self.switch_app()
        return self.find_name('呵呵123')

    # 6、智能页面，创建场景，不输入名称，完成点击无效，还在场景名称与图标页面
    def no_name_scene(self):
        self.scene_page()  # 账号登陆，网关绑定，全部场景页面，删除全部已有场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('customScene_input_name')).clear()  # 清空输入框
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        time.sleep(1)
        return self.find_xpath(excel.xpath_con('finish_delay'))  # 完成按钮还能查到

    # 7、智能页面，创建场景，创建相同名称的场景，toast提示：该场景名称已存在，请换一个(H5页面toast获取不到，改用定位还在场景名称与图标页面)
    def same_name_scene(self):
        self.create_scene_save()  # 先创建一个离家场景
        self.find_name('common icon add').click()  # 点击+按钮创建场景
        self.find_name('页面加载中...')  # 过渡
        time.sleep(2)
        self.switch_h5()
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
        return self.find_xpath(excel.xpath_con('finish_delay'))  # 完成按钮还能查到

    # 8、智能页面，长按场景，取消，编辑框消失
    def longpress_cancel(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()  # 点击智能
        if self.find_name('暂无场景'):  # 验证是否有场景
            self.find_name('common icon add').click()  # 点击+按钮创建场景
            self.find_name('页面加载中...')  # 过渡
            time.sleep(2)
            self.switch_h5()
            self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
            self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
            time.sleep(1)
            self.find_xpath(excel.xpath_con('editingscene_finishScene')).click()  # 点击右上保存按钮
            self.switch_app()
            self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
            time.sleep(1)
            self.find_name('取消').click()  # 点击取消
        else:
            self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
            time.sleep(1)
            self.find_name('取消').click()  # 点击取消
        time.sleep(1)
        return self.find_name('取消')

    # 9、智能页面，长按场景，删除-取消
    def longpress_delete_cancel(self):
        self.create_scene_save()  # 先创建一个离家场景
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        self.find_name('删除场景').click()  # 点击删除
        time.sleep(1)
        self.find_name('取消').click()  # 点击取消
        time.sleep(1)
        return self.find_name('离家')

    # 10、智能页面，长按场景，删除-确定
    def longpress_delete(self):
        self.create_scene_save()  # 先创建一个离家场景
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        self.find_name('删除场景').click()  # 点击删除
        time.sleep(1)
        self.find_name('确定').click()  # 点击确定
        time.sleep(1)
        return self.find_name('离家')

    # 11、智能页面，长按场景，编辑场景
    def longpress_edit(self):
        self.old_gateway()  # 账号登陆，绑定网关，网关中心页面
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()  # 点击智能
        if self.find_name('暂无场景'):  # 验证是否有场景
            self.find_name('common icon add').click()  # 点击+按钮创建场景
            self.find_name('页面加载中...')  # 过渡
            time.sleep(2)
            self.switch_h5()
            self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
            self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击完成按钮
            time.sleep(1)
            self.find_xpath(excel.xpath_con('editingscene_finishScene')).click()  # 点击右上保存按钮
            self.switch_app()
            self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
            time.sleep(1)
            self.find_name('编辑场景').click()  # 点击编辑场景
            self.find_name('页面加载中...')  # 过渡
            time.sleep(2)
            self.switch_h5()
            return self.find_xpath(excel.xpath_con('editingscene_finishScene'))  # 验证是否有场景编辑页面保存按钮
        else:
            self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
            time.sleep(1)
            self.find_name('编辑场景').click()  # 点击编辑场景
            self.find_name('页面加载中...')  # 过渡
            time.sleep(2)
            self.switch_h5()
            return self.find_xpath(excel.xpath_con('editingscene_finishScene'))  # 验证是否有场景编辑页面保存按钮
