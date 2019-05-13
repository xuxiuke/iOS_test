#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月11日

@author: Duke    管家    78条用例
"""

from appiumframework.PO.open_app import Open_app
from appiumframework.step import housekeeper
import unittest
import time
import warnings

class Test008(unittest.TestCase, housekeeper.Housekeeper): # TestCase类，所有测试用例类继承的基本类
    """管家测试"""
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

    # 1、管家-我的管家页面，没有任务情况，提示：还没有创建管家任务，点击右上角“+”创建
    def test_no_housekeeper(self):
        self.assertTrue(self.no_housekeeper())

    # 2、管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框
    def test_add_housekeeper(self):
        self.assertTrue(self.add_housekeeper())

    # 3、管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框，点击右上“x”，编辑框消失
    def test_add_housekeeper_x(self):
        self.assertFalse(self.add_housekeeper_x())

    # 4、管家-创建管家任务编辑框，点击定时任务，进入定时任务编辑页面，查找：当时间到达-------------------------------------------------
    def test_timing_editpage(self):
        self.assertTrue(self.timing_editpage())

    # 5、管家-定时任务编辑页面，点击名称，弹出名称弹窗
    def test_timing_name(self):
        self.assertTrue(self.timing_name())

    # 6、管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击确定，弹窗消失，名称显示为：呵呵123
    def test_timing_name_sure(self):
        self.assertTrue(self.timing_name_sure())

    # 7、管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击取消，弹窗消失，名称显示未变
    def test_timing_name_cancel(self):
        self.assertFalse(self.timing_name_cancel())

    # 8、管家-定时任务编辑页面，点击时间，进入定时编辑页面，查找Sun
    def test_timing_time(self):
        self.assertTrue(self.timing_time())

    # 9、管家-定时编辑页面，点击保存，跳转定时任务编辑页面
    def test_timing_time_save(self):
        self.assertTrue(self.timing_time_save())

    # 10、管家-定时任务编辑页面，点击执行以下任务，进入添加任务页面
    def test_timetask_page(self):
        self.assertTrue(self.timetask_page())

    # 11、管家-添加任务页面，点击添加要执行的设备，进入选择设备页面
    def test_timetask_device_page(self):
        self.assertTrue(self.timetask_device_page())

    # 12、管家-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def test_timetask_allzone(self):
        self.assertTrue(self.timetask_allzone())

    # 13、管家-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def test_timetask_allclass(self):
        self.assertTrue(self.timetask_allclass())

    # 14、管家-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def test_timetask_alladd(self):
        self.assertTrue(self.timetask_alladd())

    # 15、管家-添加任务页面，点击添加要执行的场景，进入选择场景页面
    def test_timetask_scene_page(self):
        self.assertTrue(self.timetask_scene_page())

    # 16、管家-添加任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景
    def test_timetask_scene_finish(self):
        self.assertTrue(self.timetask_scene_finish())

    # 17、管家-选择设备页面，点击墙面插座，进入设置设备状态页面
    def test_setting_devide_status_page(self):
        self.assertTrue(self.setting_device_status_page())

    # 18、管家-设置设备状态页面，点击开，进入添加延时任务页面
    def test_delay_task_page(self):
        self.assertTrue(self.delay_task_page())

    # 19、管家-添加延时任务页面，点击打开添加延时按钮，弹出延时时间编辑框，查找00
    def test_delay_task_timeopen(self):
        self.assertTrue(self.delay_task_tiemopen())

    # 20、管家-添加延时任务页面，点击打开添加延时按钮，再次点击按钮，延时时间编辑框隐藏，查找不到00
    def test_delay_task_timeclose(self):
        self.assertFalse(self.delay_task_timeclose())

    # 21、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面
    def test_dekay_task_finish(self):
        self.assertTrue(self.delay_task_finish())

    # 22、管家-添加延时任务页面，左划任务，拉出删除按钮
    def test_task_leftswip(self):
        self.assertTrue(self.task_leftswip())

    # 23、管家-添加延时任务页面，左划任务，拉出删除按钮，点击删除按钮，任务删除
    def test_task_delete(self):
        self.assertFalse(self.task_delete())

    # 24、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗
    def test_giveup_edit(self):
        self.assertTrue(self.giveup_edit())

    # 25、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击取消，弹窗消失
    def test_giveup_edit_cancel(self):
        self.assertTrue(self.giveup_edit_cancel())

    # 26、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击确定，跳转我的管家页面，任务未保存
    def test_giveup_edit_sure(self):
        self.assertTrue(self.giveup_edit_sure())

    # 27、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击保存按钮，跳转我的页面，定时任务保存成功，查找呵呵123
    def test_timed_task(self):
        self.assertTrue(self.timed_task())

    # 28、管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加
    def test_timed_notask(self):
        self.assertTrue(self.timed_notask())

    # 29、管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def test_timed_notask_sure(self):
        self.assertFalse(self.timed_notask_sure())

    # 30、管家-新建一个定时任务，点击任务，进入定时任务编辑页面
    def test_click_timedtask(self):
        self.assertTrue(self.click_timedtask())

    # 31、管家-新建一个定时任务，左划任务，拉出编辑按钮
    def test_swip_timedtask(self):
        self.assertTrue(self.swip_firsttask())

    # 32、管家-新建一个定时任务，点击任务，进入设置设备状态页面
    def test_swip_timedtask_edit(self):
        self.assertTrue(self.firsttask_click())

    # 33、管家-新建一个定时任务，左滑删除第一个执行任务
    def test_swip_firsttask_delete(self):
        self.assertFalse(self.swip_firsttask_delete())

    # 34、管家-新建一个定时任务，左划任务，拉出删除按钮
    def test_swip_timedtask_delete(self):
        self.assertTrue(self.swip_timedtask_delete())

    # 35、管家-新建一个定时任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def test_swip_timedtask_deletesure(self):
        self.assertFalse(self.swip_timedtask_deletesure())

    # 36、管家-创建管家任务编辑框，点击情景任务，进入情景任务编辑页面-----------------------------------------------------------------
    def test_scenetask_page(self):
        self.assertTrue(self.scenetask_page())

    # 37、管家-情景任务编辑页面，点击名称，弹出名称弹窗
    def test_scenetask_name(self):
        self.assertTrue(self.scenetask_name())

    # 38、管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击确定，弹窗消失，名称显示为：哈哈123
    def test_scenetask_namesure(self):
        self.assertTrue(self.scenetask_namesure())

    # 39、管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击取消，弹窗消失，名称显示未变
    def test_scenetask_namecancel(self):
        self.assertFalse(self.scenetask_namecancel())

    # 40、管家-情景任务编辑，点击满足任一条件时，进入选择设备页面
    def test_condition_page(self):
        self.assertTrue(self.condition_page())

    # 41、管家-条件任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def test_conditionpage_zone(self):
        self.assertTrue(self.conditionpage_zone())

    # 42、管家-条件任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def test_conditionpage_categroy(self):
        self.assertTrue(self.conditionpage_category())

    # 43、管家-条件任务-选择设备页面，点击门窗磁探测器，进入设置设备状态页面
    def test_condition_magnetic_page(self):
        self.assertTrue(self.condition_mannetic_page())

    # 44、管家-条件任务-设置设备状态页面，点击设防时被打开，跳转下一页面
    def test_condition_magnetic_open(self):
        self.assertTrue(self.condition_magnetic_open())

    # 45、管家-条件任务-设置设备状态页面，点击设防时被关闭，跳转下一页面
    def test_condition_magnetic_close(self):
        self.assertTrue(self.condition_magnetic_close())

    # 46、管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除
    def test_condition_swip(self):
        self.assertTrue(self.condition_swip())

    # 47、管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除，点击删除，任务删除成功，查找不到门窗磁探测器
    def test_condition_swip_delete(self):
        self.assertFalse(self.condition_swip_delete())

    # 48、管家-情景任务编辑，点击执行以下任务，情景任务页面，查找添加要执行的设备
    def test_implement_page(self):
        self.assertTrue(self.implement_page())

    # 49、管家-执行任务-情景任务页面，点击添加要执行的设备，进入选择设备页面
    def test_implement_devicepage(self):
        self.assertTrue(self.implement_devicepage())

    # 50、管家-已设置条件-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面
    def test_implement_scenepage(self):
        self.assertTrue(self.implement_scenepage())

    # 51、管家-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景
    def test_implement_scenepage_finish(self):
        self.assertTrue(self.implement_scenepage_finish())

    # 52、管家-执行任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def test_implement_device_zone(self):
        self.assertTrue(self.implement_device_zone())

    # 53、管家-已设置条件-执行任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def test_implement_device_categroy(self):
        self.assertTrue(self.implement_device_categroy())

    # 54、管家-已设置条件-执行任务-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def test_implement_device_add(self):
        self.assertTrue(self.implement_device_add())

    # 55、管家-执行任务-选择设备页面，点击墙面插座，进入设置设备状态页面
    def test_implement_socket_setting(self):
        self.assertTrue(self.implement_socket_setting())

    # 56、管家-执行任务-设置设备状态页面，点击开，跳转添加延时页面
    def test_implement_socket_open(self):
        self.assertTrue(self.implement_socket_open())

    # 57、管家-执行任务-设置设备状态页面，点击关，跳转添加延时页面
    def test_implement_socket_close(self):
        self.assertTrue(self.implement_socket_close())

    # 58、管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，查找00
    def test_implement_time_open(self):
        self.assertTrue(self.implement_time_open())

    # 59、管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，再次点击开关按钮，延时时间编辑框隐藏，查找不到00
    def test_implement_time_close(self):
        self.assertFalse(self.implement_time_close())

    # 60、管家-执行任务-添加延时页面，点击完成按钮，跳转情景任务编辑页面，查找墙面插座
    def test_implement_finish(self):
        self.assertTrue(self.implement_finish())

    # 61、管家-已设置任务，点击执行任务，进入设置设备状态页面
    def test_implement_click_firsttask(self):
        self.assertTrue(self.implement_click_firsttask())

    # 62、管家-已设置任务，左划执行任务，拉出删除按钮，查找删除
    def test_implement_swip(self):
        self.assertTrue(self.implement_swip())

    # 63、管家-已设置任务，左划执行任务，拉出删除按钮，点击删除按钮，任务被删除，查找墙面插座
    def test_implement_swip_delete(self):
        self.assertFalse(self.implement_swip_delete())

    # 64、管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def test_condition_implement_allnone(self):
        self.assertTrue(self.condition_implement_allnone())

    # 65、管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def test_condition_implement_allnone_sure(self):
        self.assertFalse(self.condition_implement_allnone_sure())

    # 66、管家-情景任务编辑页面-已设置执行条件，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def test_implement_none(self):
        self.assertTrue(self.implement_none())

    # 67、管家-情景任务编辑页面-已设置执行任务，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def test_condition_none(self):
        self.assertTrue(self.condition_none())

    # 68、管家-已设置名称-已设置执行条件-已设置执行任务，点击保存，跳转我的管家页面，查找第一个管家任务元素
    def test_scenetask_creat(self):
        self.assertTrue(self.scenetask_creat())

    # 69、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑
    def test_giveup_edit2(self):
        self.assertTrue(self.giveup_edit2())

    # 70、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击取消，弹窗消失
    def test_giveup_edit2_cancel(self):
        self.assertTrue(self.giveup_edit2_cancel())

    # 71、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击确定，跳转我的管家页面，任务未保存
    def test_giveup_edit2_sure(self):
        self.assertTrue(self.giveup_edit2_sure())

    # 72、管家-情景任务编辑页面，点击生效条件，进入生效条件页面,查找：生效时间条件
    def test_precondition_page(self):
        self.assertTrue(self.precondition_page())

    # 73、管家-生效条件页面，点击生效时间条件，进入生效时段页面
    def test_precondition_time(self):
        self.assertTrue(self.precondition_time())

    # 74、管家-生效条件页面，点击生效设备条件，进入选择设备页面
    def test_precondition_device(self):
        self.assertTrue(self.precondition_device())

    # 75、管家-生效条件页面，点击生效场景条件，进入选择场景页面
    def test_precondition_scene(self):
        self.assertTrue(self.precondition_scene())

    # 76、管家-新建一个情景任务，点击情景任务，进入情景任务编辑页面
    def test_click_scenetask(self):
        self.assertTrue(self.click_scenetask())

    # 77、管家-新建一个情景任务，左划任务，拉出编辑按钮
    def test_scenetask_swip_delete(self):
        self.assertTrue(self.scenetask_swip_delete())

    # 78、管家-新建一个情景任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def test_scenetask_click_delete(self):
        self.assertTrue(self.scenetask_click_delete())
