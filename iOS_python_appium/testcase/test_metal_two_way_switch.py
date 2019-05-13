#coding=utf-8
'''
Created on 2018年11月01日

@author: Duke    智尚金属两路开关    48条用例
'''
from PO.open_app import Open_app
from step import metal_two_way_switch
import unittest
import time
from PO import excel
@unittest.skip(u'添加场景、区域，跳过测试')
class Test012(unittest.TestCase, metal_two_way_switch.Metal_two_way_switch): # TestCase类，所有测试用例类继承的基本类
    """智尚金属两路开关"""
    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 进入设备详情页
    def test_metal_page(self):
        self.assertTrue(self.metal_page())

    # 进入设备详情页，点击左上返回按钮，返回设备列表
    def test_metal_page_back(self):
        self.assertTrue(self.metal_page_back())

    # 详情页，长按开关1，弹出编辑框----用例只写开关1，开关2省略，下同
    def test_name1_press(self):
        self.assertTrue(self.name1_press())

    # 详情页-编辑框，点击取消按钮，编辑框消失
    def test_name1_press_cancel(self):
        self.assertFalse(self.name1_press_cancel())

    # 详情页-编辑框，点击修改开关名称，弹出修改名称弹窗
    def test_name1_press_modify(self):
        self.assertTrue(self.name1_press_modify())

    # 详情页-修改名称弹窗，输入新名称呵呵1，点击取消按钮，弹窗消失，名称未修改
    def test_name1_modify_cancel(self):
        self.assertFalse(self.name1_modify_cancel())

    # 详情页-修改名称弹窗，输入新名称呵呵1，点击确定按钮，弹窗消失，名称修改成功----名称需要修改回来
    def test_name1_modify_sure(self):
        self.assertTrue(self.name1_modify_sure())
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('metal_switch_name_1')))  # 长按开关1名称
        time.sleep(1)
        self.find_xpath(excel.xpath_con('metal_name_edit_modify')).click()  # 点击修改开关名称按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'开关1')  # 输入新名称呵呵1
        self.find_xpath(excel.xpath_con('giveup_edit_sure')).click()  # 点击确定按钮

    # 详情页，点击开关模式，进入切换模式页面
    def test_mode_page(self):
        self.assertTrue(self.mode_page())

    # 详情页-切换模式页面，点击绑定模式，右上显示出确定按钮
    def test_mode_submit(self):
        self.assertTrue(self.mode_submit())

    # 详情页-切换模式页面，点击绑定模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页
    def test_mode_submit_sure(self):
        self.assertTrue(self.mode_submit_sure())

    # 详情页-绑定模式，点击开关按钮，进入绑定设备页面
    def test_binding_page(self):
        self.assertTrue(self.binding_page())

    # 详情页-切换模式页面，点击场景模式，右上显示出确定按钮
    def test_mode_scene_submit(self):
        self.assertTrue(self.mode_scene_submit())

    # 详情页-切换模式页面，点击场景模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页
    def test_mode_scene_submit_sure(self):
        self.assertTrue(self.mode_scene_submit_sure())

    # 详情页-场景模式，点击开关按钮，进入选择场景页面
    def test_scenemode_page(self):
        self.assertTrue(self.scenemode_page())

    # 详情页-场景模式，点击场景模式，进入切换模式页面
    def test_mode_page_by_scene(self):
        self.assertTrue(self.mode_page_by_scene())

    # 详情页-绑定模式，点击绑定模式，进入切换模式页面
    def test_mode_page_by_binding(self):
        self.assertTrue(self.mode_page_by_binding())

    # 详情页-切换模式页面，点击开关模式，右上显示出确定按钮
    def test_mode_binding_submit(self):
        self.assertTrue(self.mode_binding_submit())

    # 详情页-切换模式页面，点击开关模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页----开关2默认开关模式，不能使用查找text开关模式
    def test_mode_binding_submit_sure(self):
        self.assertFalse(self.mode_binding_submit_sure())

    # 详情页，点击右上更多按钮，进入更多页面
    def test_more_page(self):
        self.assertTrue(self.more_page())

    # 更多页面，点击左上返回按钮，返回详情页
    def test_more_page_back(self):
        self.assertTrue(self.more_page_back())

    # 更多页面，点击重命名，弹出修改名称弹窗
    def test_rename(self):
        self.assertTrue(self.rename())

    # 更多页面-修改名称弹窗，输入名称呵呵123，点击取消按钮，弹窗消失，名称未修改
    def test_rename_cancel(self):
        self.assertFalse(self.rename_cancel())

    # 更多页面-修改名称弹窗，输入名称呵呵123，点击确定按钮，弹窗消失，名称修改成功----名称需要修改回来
    def test_rename_sure(self):
        self.assertTrue(self.rename_sure())
        # 名称修改回来
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'智尚金属两路开关')  # 输入原名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)

    # 更多页面-重命名弹窗，不输入名称，点击确定无效，查找：请输入设备名
    def test_rename_none(self):
        self.assertTrue(self.rename_none())

    # 重命名设备名称，再次设置设备名称为名称重复，toast提示：设备名称重复！
    def test_rename_repeat(self):
        self.assertTrue(self.rename_repeat())

    # 更多页面，点击分区，进入分区页面
    def test_zone_page(self):
        self.assertTrue(self.zone_page())

    # 更多页面-分区页面，点击左上返回按钮，返回更多页面
    def test_zone_page_back(self):
        self.assertTrue(self.zone_page_back())

    # 更多页面-分区页面，点击管理分区，进入分区管理页面
    def test_zone_manage_page(self):
        self.assertTrue(self.zone_manage_page())

    # 更多页面-分区页面-分区管理页面，点击左上返回按钮，返回分区页面
    def test_zone_manage_page_back(self):
        self.assertTrue(self.zone_manage_page_back())

    # 更多页面-分区页面，前置条件至少一个分区，点击第一个分区，跳转更多页面，toast提示：修改设备区域成功
    def test_change_zone(self):
        self.assertTrue(self.change_zone())

    # 更多页面-分区页面，前置条件修改区域成功，点击未分区，跳转更多页面，查找未分区
    def test_zone_page_non(self):
        self.assertTrue(self.zone_page_non())

    # 更多页面，点击设备信息，进入设备信息页面
    def test_device_information(self):
        self.assertTrue(self.device_information())

    # 更多页面-设备信息页面，点击左上返回按钮，返回更多页面
    def test_device_information_back(self):
        self.assertTrue(self.device_information_back())

    # 更多页面，点击找设备，弹出找设备弹窗
    def test_finddevice(self):
        self.assertTrue(self.finddevice())

    # 更多页面-找设备弹窗，点击已找到按钮，弹窗消失
    def test_finddevice_found(self):
        self.assertFalse(self.finddevice_found())

    # 更多页面-找设备弹窗，点击再闪一次，弹窗还在
    def test_finddevice_again(self):
        self.assertTrue(self.finddevice_again())

    # 更多页面，点击日志，进入日志页面
    def test_log_message_page(self):
        self.assertTrue(self.log_message_page())

    # 更多页面-日志页面，点击左上返回按钮，返回更多页面
    def test_log_message_page_back(self):
        self.assertTrue(self.log_message_page_back())

    # 更多页面-日志页面，点击按日期查找，弹窗日期编辑框
    def test_log_search_by_time(self):
        self.assertTrue(self.log_search_by_time())

    # 更多页面-日志页面-弹窗日期编辑框，点击其他任意地方，编辑框消失----点击返回操作
    def test_log_search_by_time_hide(self):
        self.assertFalse(self.log_search_by_time_hide())

    # 更多页面-日志页面，点击清空记录，弹出清空记录弹窗
    def test_log_empty(self):
        self.assertTrue(self.log_empty())

    # 更多页面-日志页面-清空记录弹窗，点击取消按钮，弹窗消失
    def test_log_empty_cancel(self):
        self.assertFalse(self.log_empty_cancel())

    # 更多页面-日志页面-清空记录弹窗，点击确定按钮，弹窗消失，返回更多页面
    def test_log_empty_sure(self):
        self.assertTrue(self.log_empty_sure())

    # 更多页面，前置条件清空了记录，进入日志页面，查找：没有日志消息
    def test_log_empty_sure_again(self):
        self.assertTrue(self.log_empty_sure_again())

    # 更多页面，前置条件清空了记录,开关1为开关模式，返回详情页，点击开关按钮两次，查找已打开
    def test_metal_open(self):
        self.assertTrue(self.metal_open())

    # 更多页面，前置条件清空了记录,开关1为开关模式，返回详情页，点击开关按钮两次，查找已关闭
    def test_metal_close(self):
        self.assertTrue(self.metal_close())

    # 更多页面，点击删除设备按钮，弹出删除确认弹窗
    def test_delete_device(self):
        self.assertTrue(self.delete_device())

    # 更多页面-删除确认弹窗，点击取消按钮，弹窗消失----确定按钮，用例省略
    def test_delete_device_cancel(self):
        self.assertFalse(self.delete_device_cancel())

