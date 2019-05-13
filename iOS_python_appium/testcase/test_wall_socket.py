#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月22日

@author: Duke    墙面插座+场景    ？条用例
"""

from appiumframework.PO.open_app import Open_app
from appiumframework.step import wall_socket
import unittest
import time
from appiumframework.PO import excel
import warnings

class Test009(unittest.TestCase, wall_socket.Wall_socket): # TestCase类，所有测试用例类继承的基本类
    """墙面插座测试"""
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

    # 1、设备，进入墙面插座详情页
    def test_details_page(self):
        self.assertTrue(self.details_page())

    # 2、设备-插座详情页，点击返回按钮，返回设备列表页面
    def test_details_page_back(self):
        self.assertTrue(self.details_page_back())

    # 3、设备-插座详情页，关闭状态，点击开关按钮，打开插座
    def test_open_socket(self):
        self.assertTrue(self.open_socket())

    # 4、设备-插座详情页，打开状态，点击开关按钮，关闭插座
    def test_close_socket(self):
        self.assertTrue(self.close_socket())

    # 5、设备-插座详情页，点击更多按钮，进入更多页面
    def test_more_pages(self):
        self.assertTrue(self.more_pages())

    # 6、设备-插座详情页-更多，点击返回按钮，进入设备详情页
    def test_more_pages_back(self):
        self.assertTrue(self.more_pages_back())

    # 7、设备-插座详情页-更多，重命名哈哈123-确定
    def test_rename(self):
        self.assertTrue(self.rename())
        # 恢复设备名称
        time.sleep(1)
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('墙面插座')  # 输入新名称
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('确定').click()  # 点击确定按钮

    # 8、设备-插座详情页-更多，重命名哈哈123-确定，返回设备列表，可以查找到新设备名称
    def test_rename_back(self):
        self.assertTrue(self.rename_back())
        # 恢复设备名称
        self.switch_h5()
        self.find_xpath(excel.xpath_con('socket_more')).click()  # 点击右上更多按钮
        self.switch_app()
        time.sleep(1)
        self.find_name('重命名').click()  # 点击重命名
        self.find_name('清除文本').click()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('墙面插座')  # 输入新名称
        self.find_name('Done').click()  # 点击完成按钮
        self.find_name('确定').click()  # 点击确定按钮

    # 9、设备-插座详情页-更多，重命名哈哈123-取消
    def test_rename_cancel(self):
        self.assertFalse(self.rename_cancel())

    # 10、设备-插座详情页-更多，命名已有的设备名称，toast提示：设备名称重复！
    def test_zzz_raname_repeat(self):
        self.assertTrue(self.zzz_rename_repeat())

    # 11、设备-插座详情页-更多，重命名-不输入名称，确定按钮点击无效，重命名弹窗还在
    def test_rename_none(self):
        self.assertTrue(self.rename_none())

    # 12、设备-插座详情页-更多，点击分区，进入分区页面
    def test_zone_pages(self):
        self.assertTrue(self.zone_pages())

    # 13、设备-插座详情页-更多-分区，点击返回按钮，返回更多页面
    def test_zone_pages_back(self):
        self.assertTrue(self.zone_pages_back())

    # 14、设备-插座详情页-更多，前置条件至少有一个分区，点击分区，返回更多页面
    def test_modify_zone(self):
        self.assertTrue(self.modify_zone())

    # 15、设备-插座详情页-更多，点击未分区，返回更多页面，未分区可以查找到
    def test_non_zone(self):
        self.assertTrue(self.non_zone())

    # 16、设备-插座详情页-更多-分区，点击右上管理分区，进入分区管理页面
    def test_zoning_pages(self):
        self.assertTrue(self.zoning_pages())

    # 17、设备-插座详情页-更多-分区-分区管理，点击返回按钮，返回分区页面
    def test_zoning_pages_back(self):
        self.assertTrue(self.zoning_pages_back())

    # 18、设备-插座详情页-更多，点击设备信息，进入设备信息页面，产品名称
    def test_device_information(self):
        self.assertTrue(self.device_information())

    # 19、设备-插座详情页-更多-设备信息，点击返回按钮，返回更多页面
    def test_device_information_back(self):
        self.assertTrue(self.device_information_back())

    # 20、设备-插座详情页-更多，点击找设备，弹窗设备指示灯将闪烁10秒
    def test_find_device(self):
        self.assertTrue(self.find_device())

    # 21、设备-插座详情页-更多-找设备弹窗，点击已找到，弹窗消失
    def test_find_device_found(self):
        self.assertFalse(self.find_device_found())

    # 22、设备-插座详情页-更多-找设备弹窗，点击再闪一次，弹窗还在
    def test_find_device_find(self):
        self.assertTrue(self.find_device_find())

    # 23、设备-插座详情页-更多，点击删除设备，弹窗确定删除设备吗？
    def test_delete_device(self):
        self.assertTrue(self.delete_device())

    # 24、设备-插座详情页-更多-删除设备弹窗，点击取消按钮，弹窗消失（删除设备用例省略）
    def test_delete_device_cancel(self):
        self.assertFalse(self.delete_device_cancel())

    # 25、场景，设置场景打开插座    --------------------------------------------------------------
    def test_scene_open_socket(self):
        self.assertTrue(self.scene_open_socket())

    # 26、关闭插座，点击打开插座场景
    def test_click_scene_open_socket(self):
        self.assertTrue(self.click_scene_open_socket())

    # 27、场景，设置场景关闭插座
    def test_scene_close_socket(self):
        self.assertTrue(self.scene_close_socket())

    # 28、打开插座，点击关闭插座场景
    def test_click_scene_close_socket(self):
        self.assertTrue(self.click_scene_close_socket())

    # 29、场景，添加延时页面，点击延时按钮，弹出延时设置编辑框
    def test_scene_time(self):
        self.assertTrue(self.scene_time())

    # 30、场景，添加延时页面，点击延时按钮，弹出延时设置编辑框，再次点击延时按钮，编辑框隐藏
    def test_scene_time_off(self):
        self.assertFalse(self.scene_time_off())

    # 31、场景，添加延时页面，设置延时任务，编辑场景页面查找？秒后执行
    def test_scene_delay(self):
        self.assertTrue(self.scene_delay())

    # 32、场景，设置场景打开插座，点击返回按钮，弹窗：编辑的场景尚未保存，是否退出
    def test_editscene_back(self):
        self.assertTrue(self.editscene_back())

    # 33、场景，设置场景打开插座，点击返回按钮，点击取消，弹窗消失
    def test_editscene_back_cancel(self):
        self.assertFalse(self.editscene_back_cancel())

    # 34、场景，设置场景打开插座，点击返回按钮，点击退出，任务未保存
    def test_editscene_back_exit(self):
        self.assertFalse(self.editscene_back_exit())

    # 35、场景，设置场景打开插座，点击返回按钮，点击保存并退出，任务保存成功
    def test_editscene_back_exitsave(self):
        self.assertTrue(self.editscene_back_exitsave())

    # 36、场景，设置场景打开插座，左划拉出删除按钮
    def test_editscene_delete(self):
        self.assertTrue(self.editscene_delete())

    # 37、场景，设置场景打开插座，左划拉出删除按钮，点击删除，任务被删除
    def test_editscene_delete_click(self):
        self.assertFalse(self.editscene_delete_click())

    # 38、场景，设置场景打开插座，点击任务，可以重新设置任务，进入设置设备状态页面
    def test_editscene_edit(self):
        self.assertTrue(self.editscene_edit())

    # 39、场景，添加设备页面，点击全部分区，拉出所有分区
    def test_editscene_allzone(self):
        self.assertTrue(self.editscene_allzone())

    # 40、场景，添加设备页面，点击全部类别，拉出所有类别，查找智能门锁
    def test_editscene_allcategory(self):
        self.assertTrue(self.editscene_allcategory())

    # 41、场景，添加设备页面，点击批量添加，进入批量添加页面，查找全选
    def test_editscene_batchadd(self):
        self.assertTrue(self.editscene_batchadd())

