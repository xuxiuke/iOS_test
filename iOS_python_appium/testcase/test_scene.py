#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月08日

@author: Duke    场景    11条用例
"""

from appiumframework.PO.open_app import Open_app
from appiumframework.step import scene
import unittest
import time
import warnings

class Test007(unittest.TestCase, scene.Scene): # TestCase类，所有测试用例类继承的基本类
    """场景测试"""
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

    # 1、智能页面，无场景，页面提示：暂无场景
    def test_no_scene(self):
        self.assertTrue(self.no_scene())

    # 2、智能页面，创建场景，默认离家名称，场景编辑页面点击保存
    def test_create_scene_save(self):
        self.assertTrue(self.create_scene_save())

    # 3、智能页面，创建场景，默认离家名称，场景编辑页面返回
    def test_create_scene_back(self):
        self.assertTrue(self.create_scene_back())

    # 4、智能页面，创建场景，默认离家名称，左上返回按钮
    def test_create_scene_cancel(self):
        self.assertFalse(self.create_scene_cancel())

    # 5、智能页面，创建场景自定义名称呵呵123
    def test_hehe123_scene(self):
        self.assertTrue(self.hehe123_scene())

    # 6、智能页面，创建场景，不输入名称，完成点击无效，还在场景名称与图标页面
    def test_no_name_scene(self):
        self.assertTrue(self.no_name_scene())

    # 7、智能页面，创建场景，创建相同名称的场景，toast提示：该场景名称已存在，请换一个(H5页面toast获取不到，改用定位还在场景名称与图标页面)
    def test_same_name_scene(self):
        self.assertTrue(self.same_name_scene())

    # 8、智能页面，长按场景，取消，编辑框消失
    def test_longpress_cancel(self):
        self.assertFalse(self.longpress_cancel())

    # 9、智能页面，长按场景，删除-取消
    def test_longpress_delete_cancel(self):
        self.assertTrue(self.longpress_delete_cancel())

    # 10、智能页面，长按场景，删除-确定
    def test_longpress_delete(self):
        self.assertFalse(self.longpress_delete())

    # 11、智能页面，长按场景，编辑场景
    def test_longpress_edit(self):
        self.assertTrue(self.longpress_edit())


