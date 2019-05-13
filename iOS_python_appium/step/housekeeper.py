#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年04月11日

@author: Duke    管家
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Housekeeper(base_page.Action):

    # 前提条件，管家，进入我的管家页面
    def housekeeper_page(self):
        self.old_gateway()  # 账号登陆，绑定网关
        self.driver.back()
        time.sleep(1)
        self.find_name('智能').click()  # 点击智能
        self.find_name('管家').click()  # 点击管家

    # 前提条件，管家，删除所有管家
    def mine_housekeeper(self):
        self.housekeeper_page()  # 进入我的管家页面
        while True:
            if self.find_name('还没有创建管家任务，点击右上角“+”创建'):  # 验证是否有场景任务
                break
            else:
                self.leftswip_housekeeper(2000)  # 左划任务
                self.find_name('删除').click()  # 点击删除按钮
                time.sleep(1)

    # 前置条件，设置名称，传name参数
    def set_name(self, name):
        self.find_ios_predicate("type == 'XCUIElementTypeLink'" and "value == '5'").click()  # 点击名称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys(name)  # 名称输入框输入新名称 呵呵123
        self.find_name('确定').click()  # 点击确定按钮

    # 前置条件，定时任务编辑页面，查看是否有执行任务，有就删除
    def delete_task(self):
        while True:
            if self.find_ios_predicate("name CONTAINS '立即执行'"):
                self.leftswip_delaytask(2000)  # 左划执行任务
                self.find_name('删除').click()  # 删除任务
                time.sleep(1)
            else:
                break

    # 前置条件，创建执行任务
    def creat_task(self):
        self.find_name('执行以下任务').click()  # 点击执行以下任务
        self.find_name('添加要执行的设备').click()  # 点击添加要执行的设备
        time.sleep(1)
        self.find_name('墙面插座').click()  # 选择墙面插座
        time.sleep(1)
        self.find_name('开').click()  # 点击开
        time.sleep(1)
        self.find_name('完成').click()  # 点击完成按钮
        time.sleep(1)

    # 前置条件，创建满足条件
    def creat_condition(self):
        self.find_name('满足任一条件时').click()  # 点击满足任一条件时
        time.sleep(1)
        self.find_name('门窗磁探测器').click()  # 点击门窗磁探测器
        time.sleep(1)
        self.find_name('设防时被打开').click()  # 点击设防时被打开
        self.find_name('完成').click()  # 点击完成按钮
        time.sleep(1)

    # 前置条件，删除情景任务满足条件
    def delete_condition(self):
        while True:
            if self.find_xpath(excel.xpath_con('first_condition')):  # 查询是否有满足任务
                self.leftswip_condition(2000)  # 左划条件任务
                self.find_name('删除').click()  # 点击删除
                time.sleep(1)
            else:
                break

    # 前置条件，删除情景任务编辑页面执行任务
    def delete_implement(self):
        while True:  # 删除可能有的执行条件
            if self.find_ios_predicate("name CONTAINS '秒执行'"):
                self.leftswip_implement(2000)  # 左划任务
                self.find_name('删除').click()  # 点击删除
                time.sleep(1)
            else:
                break

    # 1、管家-我的管家页面，没有任务情况，提示：还没有创建管家任务，点击右上角“+”创建(实际有BUG)
    def no_housekeeper(self):
        self.mine_housekeeper()  # 我的管家页面，删除所有管家任务
        return self.find_name('还没有创建管家任务，点击右上角“+”创建')

    # 2、管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框
    def add_housekeeper(self):
        self.housekeeper_page()  # 进入我的管家页面
        self.find_name('common icon add').click()  # 点击右上+按钮
        return self.find_name('创建管家任务')

    # 3、管家-我的管家页面，点击右上角“+”，弹出创建管家任务编辑框，点击右上“x”，编辑框消失
    def add_housekeeper_x(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_name('butler close icon').click()  # 点击右上X按钮
        return self.find_name('创建管家任务')

    # 4、管家-创建管家任务编辑框，点击定时任务，进入定时任务编辑页面，查找：当时间到达-------------------------------------------------
    def timing_editpage(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_name('butler addtime icon').click()  # 点击定时任务
        time.sleep(1)
        return self.find_name('当时间到达')

    # 5、管家-定时任务编辑页面，点击名称，弹出名称弹窗
    def timing_name(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.find_ios_predicate("type == 'XCUIElementTypeLink'" and "value == '5'").click()  # 点击名称
        return self.find_ios_predicate("type == 'XCUIElementTypeTextField'")  # 验证是否有名称弹窗

    # 6、管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击确定，弹窗消失，名称显示为：名称 呵呵123
    def timing_name_sure(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.set_name('自动化测试6')
        return self.find_name('名称 自动化测试6')

    # 7、管家-定时任务编辑-名称弹窗，输入名称呵呵123，点击取消，弹窗消失，名称显示未变
    def timing_name_cancel(self):
        self.timing_name()  # 定时任务，名称弹窗
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('哈哈123')  # 名称输入框输入新名称 呵呵123
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('名称 哈哈123')

    # 8、管家-定时任务编辑页面，点击时间，进入定时编辑页面，查找定时
    def timing_time(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.find_ios_predicate("name CONTAINS 'Sun'").click()  # 点击时间事件
        return self.find_name('定时')

    # 9、管家-定时编辑页面，点击保存，跳转定时任务编辑页面
    def timing_time_save(self):
        self.timing_time()  # 定时任务，定时编辑页面
        self.find_name('保存').click()  # 点击保存按钮
        return self.find_name('定时任务')

    # 10、管家-定时任务编辑页面，点击执行以下任务，进入添加任务页面，查找添加要执行的设备
    def timetask_page(self):
        self.timing_editpage()  # 定时任务编辑页面
        self.find_name('执行以下任务').click()  # 点击执行以下任务
        return self.find_name('添加要执行的设备')

    # 11、管家-添加任务页面，点击添加要执行的设备，进入选择设备页面
    def timetask_device_page(self):
        self.timetask_page()  # 添加任务页面
        self.find_name('添加要执行的设备').click()  # 点击添加要执行的设备
        time.sleep(1)
        return self.find_name('选择设备')

    # 12、管家-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def timetask_allzone(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_name('全部分区').click()  # 点击全部分区
        return self.find_name('未分区')  # 延时是否有全部分区元素

    # 13、管家-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def timetask_allclass(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_name('全部类别').click()  # 点击全部类别
        return self.find_name('智能门锁')

    # 14、管家-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def timetask_alladd(self):
        self.timetask_device_page()  # 定时任务，选择设备页面
        self.find_name('批量添加').click()  # 点击批量添加
        return self.find_name('全选')

    # 15、管家-添加任务页面，点击添加要执行的场景，进入选择场景页面
    def timetask_scene_page(self):
        self.timetask_page()  # 添加任务页面
        self.find_name('添加要执行的场景').click()  # 点击添加要执行的场景
        return self.find_name('选择场景')

    # 16、管家-添加任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景
    def timetask_scene_finish(self):
        self.timetask_scene_page()  # 选择场景页面
        self.find_name('完成').click()  # 点击右上完成按钮
        return self.find_name('请选择一个场景')

    # 17、管家-选择设备页面，点击墙面插座，进入设置设备状态页面
    def setting_device_status_page(self):
        self.timetask_device_page()  # 选择设备页面
        self.find_name('墙面插座').click()  # 选择墙面插座
        return self.find_name('设置设备状态')

    # 18、管家-设置设备状态页面，点击开，进入添加延时任务页面
    def delay_task_page(self):
        self.setting_device_status_page()  # 设置设备状态页面
        self.find_name('开').click()  # 点击开
        return self.find_name('添加延时')

    # 19、管家-添加延时任务页面，点击打开添加延时按钮，弹出延时时间编辑框，查找00
    def delay_task_tiemopen(self):
        self.delay_task_page()  # 添加延时页面
        self.find_xpath(excel.xpath_con('add_delay')).click()  # 点击打开添加延时开关按钮
        return self.find_name('00')

    # 20、管家-添加延时任务页面，点击打开添加延时按钮，再次点击按钮，延时时间编辑框隐藏，查找不到00
    def delay_task_timeclose(self):
        self.delay_task_tiemopen()  # 添加延时页面，延时开关打开状态
        self.find_xpath(excel.xpath_con('add_delay')).click()  # 点击打开添加延时开关按钮
        return self.find_name('00')

    # 21、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面
    def delay_task_finish(self):
        self.housekeeper_page()  # 进入我的管家页面
        self.find_name('common icon add').click()  # 点击右上+按钮
        self.find_name('butler addtime icon').click()  # 点击定时任务
        time.sleep(1)
        self.delete_task()  # 删除执行任务
        self.creat_task()  # 创建执行任务
        time.sleep(1)
        return self.find_ios_predicate("name CONTAINS '立即执行'")

    # 22、管家-添加延时任务页面，左划任务，拉出删除按钮
    def task_leftswip(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.leftswip_delaytask(2000)  # 左划执行任务
        return self.find_name('删除')

    # 23、管家-添加延时任务页面，左划任务，拉出删除按钮，点击删除按钮，任务删除
    def task_delete(self):
        self.housekeeper_page()  # 进入我的管家页面
        self.find_name('common icon add').click()  # 点击右上+按钮
        self.find_name('butler addtime icon').click()  # 点击定时任务
        time.sleep(1)
        self.delete_task()  # 删除执行任务
        self.creat_task()  # 创建执行任务
        self.leftswip_delaytask(2000)  # 左划执行任务
        self.find_name('删除').click()  # 删除任务
        time.sleep(1)
        return self.find_ios_predicate("name CONTAINS '立即执行'")

    # 24、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗
    def giveup_edit(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        return self.find_name('是否放弃编辑')  # 验证是否有弹窗

    # 25、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击取消，弹窗消失
    def giveup_edit_cancel(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        self.find_name('取消').click()  # 点击取消按钮
        f1 = bool(self.find_name('是否放弃编辑'))
        f2 = bool(self.find_name('执行以下任务'))
        return f1 == False and f2 == True # 验证是否有弹窗和是否在任务编辑页面

    # 26、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击左上返回按钮，弹窗是否放弃编辑弹窗，点击确定，跳转我的管家页面，任务未保存
    def giveup_edit_sure(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.set_name('自动化测试26')
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        f1 = bool(self.find_name('是否放弃编辑'))
        f2 = bool(self.find_name('执行以下任务'))
        f3 = bool(self.find_name('自动化测试26'))
        return f1 == False and f2 == False and f3 == False  # 弹窗消失，没有停留在编辑页面

    # 27、管家-添加延时任务页面，点击完成按钮，跳转定时任务编辑页面，点击保存按钮，跳转我的页面，定时任务保存成功，查找呵呵123
    def timed_task(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.set_name('自动化测试27')
        self.find_name('保存').click()  # 点击右上保存按钮
        time.sleep(2)
        return self.find_name('自动化测试27')

    # 28、管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加
    def timed_notask(self):
        self.timing_editpage()  # 管家定时任务编辑页面
        self.delete_task()
        self.find_name('保存').click()  # 点击右上保存按钮
        time.sleep(1)
        return self.find_name('执行任务不能为空，请添加')  # 判断是否有弹窗这个元素

    # 29、管家-定时任务编辑页面，点击保存按钮，弹窗提示：执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def timed_notask_sure(self):
        self.timed_notask()  # 管家-定时任务-执行任务不能为空弹窗
        self.find_name('确定').click()  # 点击确定按钮
        return self.find_name('执行任务不能为空，请添加')  # 判断是否有弹窗这个元素

    # 30、管家-新建一个定时任务，点击任务，进入定时任务编辑页面
    def click_timedtask(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.set_name('自动化测试30')
        self.find_name('保存').click()  # 点击右上保存按钮
        time.sleep(2)
        self.find_name('自动化测试30').click()  # 点击新建管家
        time.sleep(2)
        return self.find_name('当时间到达')

    # 31、管家-新建一个定时任务，左划任务，拉出删除按钮
    def swip_firsttask(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.leftswip_delaytask(2000)  # 左划第一个管家任务
        return self.find_name('删除')

    # 32、管家-新建一个定时任务，点击任务，进入设置设备状态页面
    def firsttask_click(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.find_ios_predicate("name CONTAINS '立即执行'").click()  # 点击第一个任务
        time.sleep(1)
        return self.find_name('设置设备状态')

    # 33、管家-新建一个定时任务，左滑删除第一个执行任务
    def swip_firsttask_delete(self):
        self.delay_task_finish()  # 添加一个执行任务
        self.leftswip_delaytask(2000)  # 左划第一个管家任务
        self.find_name('删除').click()  # 点击删除
        return self.find_ios_predicate("name CONTAINS '立即执行'")

    # 34、管家-新建一个定时任务，左划任务，拉出删除按钮
    def swip_timedtask_delete(self):
        self.housekeeper_page()  # 我的管家页面
        self.find_name('common icon add').click()  # 点击右上+按钮
        self.find_name('butler addtime icon').click()  # 点击定时任务
        time.sleep(1)
        self.creat_task()  # 创建执行任务
        self.set_name('自动化测试34')
        self.find_name('保存').click()  # 点击右上保存按钮
        time.sleep(2)
        self.leftswip_housekeeper(2000)  # 左划第一个管家任务
        return self.find_name('删除')

    # 35、管家-新建一个定时任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def swip_timedtask_deletesure(self):
        self.mine_housekeeper()  # 我的管家页面，删除所有管家任务
        self.find_name('common icon add').click()  # 点击右上+按钮
        self.find_name('butler addtime icon').click()  # 点击定时任务
        time.sleep(1)
        self.creat_task()  # 创建执行任务
        self.set_name('自动化测试35')  # 设置名称
        self.find_name('保存').click()  # 点击右上保存按钮
        time.sleep(2)
        self.leftswip_housekeeper(2000)  # 左划第一个管家任务
        self.find_name('删除').click()  # 点击删除
        time.sleep(1)
        return self.find_name('自动化测试35')

    # 36、管家-创建管家任务编辑框，点击情景任务，进入情景任务编辑页面-----------------------------------------------------------------
    def scenetask_page(self):
        self.add_housekeeper()  # 创建管家任务编辑框页面
        self.find_name('butler addscene icon').click()  # 点击情景任务
        time.sleep(1)
        return self.find_name('满足任一条件时')

    # 37、管家-情景任务编辑页面，点击名称，弹出名称弹窗
    def scenetask_name(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_ios_predicate("type == 'XCUIElementTypeLink'" and "value == '5'").click()  # 点击名称
        return self.find_ios_predicate("type == 'XCUIElementTypeTextField'")  # 验证是否有名称弹窗

    # 38、管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击确定，弹窗消失，名称显示为：哈哈123
    def scenetask_namesure(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.set_name('自动化测试38')
        return self.find_name('名称 自动化测试38')

    # 39、管家-情景任务编辑-名称弹窗，输入名称哈哈123，点击取消，弹窗消失，名称显示未变
    def scenetask_namecancel(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_ios_predicate("type == 'XCUIElementTypeLink'" and "value == '5'").click()  # 点击名称
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('哈哈39')  # 名称输入框输入新名称 呵呵123
        self.find_name('取消').click()  # 点击取消按钮
        return self.find_name('名称 哈哈39')

    # 40、管家-情景任务编辑，点击满足任一条件时，进入选择设备页面
    def condition_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_name('满足任一条件时').click()  # 点击满足任一条件时
        time.sleep(1)
        return self.find_name('选择设备')

    # 41、管家-条件任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def conditionpage_zone(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_name('全部分区').click()  # 点击全部分区
        return self.find_name('未分区')  # 延时是否有全部分区元素

    # 42、管家-条件任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def conditionpage_category(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_name('全部类别').click()  # 点击全部类别
        return self.find_name('智能门锁')

    # 43、管家-条件任务-选择设备页面，点击门窗磁探测器，进入设置设备状态页面
    def condition_mannetic_page(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_name('门窗磁探测器').click()  # 点击门窗磁探测器
        time.sleep(1)
        return self.find_name('设置设备状态')

    # 44、管家-条件任务-设置设备状态页面，点击设防时被打开，跳转下一页面
    def condition_magnetic_open(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_name('门窗磁探测器').click()  # 点击门窗磁探测器
        time.sleep(1)
        self.find_name('设防时被打开').click()  # 点击设防时被打开
        return self.find_name('同时向我发送报警信息')  # 验证是否进入下一页面

    # 45、管家-条件任务-设置设备状态页面，点击设防时被关闭，跳转下一页面
    def condition_magnetic_close(self):
        self.condition_page()  # 情景任务-条件任务，选择设备页面
        self.find_name('门窗磁探测器').click()  # 点击门窗磁探测器
        time.sleep(1)
        self.find_name('设防时被关闭').click()  # 点击设防时被关闭
        return self.find_name('同时向我发送报警信息')  # 验证是否进入下一页面

    # 46、管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除
    def condition_swip(self):
        self.condition_magnetic_open()  # 创建一个条件任务
        self.find_name('完成').click()  # 点击完成按钮
        time.sleep(1)
        self.leftswip_condition(2000)  # 左划条件任务
        time.sleep(1)
        return self.find_name('删除')

    # 47、管家-条件任务成功-情景任务编辑页面，左划任务，拉出删除按钮，查找删除，点击删除，任务删除成功，查找不到门窗磁探测器
    def condition_swip_delete(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除满足条件
        self.creat_condition()  # 创建满足条件
        self.leftswip_condition(2000)  # 左划条件任务
        self.find_name('删除').click()  # 点击删除
        time.sleep(1)
        return self.find_xpath(excel.xpath_con('first_condition'))

    # 48、管家-情景任务编辑，点击执行以下任务，情景任务页面，查找添加要执行的设备
    def implement_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_name('执行以下任务').click()  # 点击执行以下任务
        return self.find_name('添加要执行的设备')

    # 49、管家-执行任务-情景任务页面，点击添加要执行的设备，进入选择设备页面
    def implement_devicepage(self):
        self.implement_page()  # 执行任务-情景任务页面
        self.find_name('添加要执行的设备').click()  # 点击添加要执行的设备
        return self.find_name('选择设备')

    # 50、管家-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面
    def implement_scenepage(self):
        self.implement_page()  # 执行任务-情景任务页面
        self.find_name('添加要执行的场景').click()  # 点击添加要执行的场景
        return self.find_name('选择场景')

    # 51、管家-执行任务-情景任务页面，点击添加要执行的场景，进入选择场景页面，点击完成，toast提示：请选择一个场景
    def implement_scenepage_finish(self):
        self.implement_scenepage()  # 情景任务-选择场景，场景选择页面
        self.find_name('完成').click()  # 点击完成按钮
        return self.find_name('请选择一个场景')

    # 52、管家-执行任务-选择设备页面，点击全部分区，下拉所以分区，查找元素全部分区
    def implement_device_zone(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_name('全部分区').click()  # 点击全部分区
        return self.find_name('未分区')  # 验证是否存在元素未分区

    # 53、管家-执行任务-选择设备页面，点击全部类别，下拉所以类别，查找智能门锁
    def implement_device_categroy(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_name('全部类别').click()  # 点击全部类别
        return self.find_name('智能门锁')

    # 54、管家-执行任务-选择设备页面，点击批量添加，进入批量添加页面，查找全选
    def implement_device_add(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_name('批量添加').click()  # 点击批量添加
        return self.find_name('全选')

    # 55、管家-执行任务-选择设备页面，点击墙面插座，进入设置设备状态页面
    def implement_socket_setting(self):
        self.implement_devicepage()  # 执行任务-选择设备页面
        self.find_name('墙面插座').click()  # 点击墙面插座
        return self.find_name('设置设备状态')

    # 56、管家-执行任务-设置设备状态页面，点击开，跳转添加延时页面
    def implement_socket_open(self):
        self.implement_socket_setting()  # 情景任务-执行任务，墙面插座设置设备状态页面
        self.find_name('开').click()  # 点击墙面插座开
        return self.find_name('添加延时')

    # 57、管家-执行任务-设置设备状态页面，点击关，跳转添加延时页面
    def implement_socket_close(self):
        self.implement_socket_setting()  # 情景任务-执行任务，墙面插座设置设备状态页面
        self.find_name('关').click()  # 点击墙面插座关
        return self.find_name('添加延时')

    # 58、管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，查找00
    def implement_time_open(self):
        self.implement_socket_open()  # 情景任务-执行任务，添加延时页面
        self.find_xpath(excel.xpath_con('add_delay')).click()  # 点击打开添加延时开关按钮
        return self.find_name('00')

    # 59、管家-执行任务-添加延时页面，点击添加延时开关按钮，弹出延时时间编辑框，再次点击开关按钮，延时时间编辑框隐藏，查找不到00
    def implement_time_close(self):
        self.implement_time_open()  # 打开延时按钮
        self.find_xpath(excel.xpath_con('add_delay')).click()  # 点击打开添加延时开关按钮
        return self.find_name('00')

    # 60、管家-执行任务-添加延时页面，点击完成按钮，跳转情景任务编辑页面，查找墙面插座
    def implement_finish(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除可能有的满足条件
        self.delete_implement()  # 删除可能有的执行条件
        self.creat_task()  # 创建执行任务
        return self.find_ios_predicate("name CONTAINS '秒执行'")

    # 61、管家-已设置任务，点击执行任务，进入设置设备状态页面
    def implement_click_firsttask(self):
        self.scenetask_page()  # 情景任务编辑页面
        if self.find_ios_predicate("name CONTAINS '秒执行'"):  # 查找任务，有任务直接点击，没有任务先添加再点击
            self.find_ios_predicate("name CONTAINS '秒执行'").click()  # 点击任务
        else:
            self.creat_task()  # 创建执行任务
            self.find_ios_predicate("name CONTAINS '秒执行'").click()  # 点击任务
        time.sleep(1)
        return self.find_name('设置设备状态')

    # 62、管家-已设置任务，左划执行任务，拉出删除按钮，查找删除
    def implement_swip(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除可能有的满足条件
        if self.find_ios_predicate("name CONTAINS '秒执行'"):  # 查找任务，有任务直接左滑，没有任务先添加再左滑
            self.leftswip_implement(2000)  # 左划任务
        else:
            self.creat_task()  # 创建执行任务
            self.leftswip_implement(2000)  # 左划任务
        return self.find_name('删除')

    # 63、管家-已设置任务，左划执行任务，拉出删除按钮，点击删除按钮，任务被删除，查找墙面插座
    def implement_swip_delete(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除可能有的满足条件
        self.delete_implement()  # 删除可能有的执行条件
        self.creat_task()  # 创建执行任务
        self.leftswip_implement(2000)
        self.find_name('删除').click()  # 点击删除
        return self.find_ios_predicate("name CONTAINS '秒执行'")

    # 64、管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或执行任务不能为空，请添加
    def condition_implement_allnone(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除可能有的满足条件
        self.delete_implement()  # 删除可能有的执行条件
        self.find_name('保存').click()  # 点击保存
        time.sleep(1)
        return self.find_name('执行条件或执行任务不能为空，请添加')  # 验证弹窗元素是否存在

    # 65、管家-情景任务编辑页面，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加，点击确定按钮，弹窗消失
    def condition_implement_allnone_sure(self):
        self.condition_implement_allnone()  # 执行条件或者执行任务不能为空弹窗
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        return self.find_name('执行条件或执行任务不能为空，请添加')  # 验证弹窗元素是否存在

    # 66、管家-情景任务编辑页面-已设置执行条件，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def implement_none(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除满足条件
        self.delete_implement()  # 删除可能有的执行条件
        self.creat_condition()  # 创建满足条件
        self.find_name('保存').click()  # 点击保存
        time.sleep(1)
        return self.find_name('执行条件或执行任务不能为空，请添加')  # 验证弹窗元素是否存在

    # 67、管家-情景任务编辑页面-已设置执行任务，点击保存按钮，弹窗提示：执行条件或者执行任务不能为空，请添加
    def condition_none(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.delete_condition()  # 删除可能有的满足条件
        while True:  # 验证是否有执行任务，有就过，没有就创建一个
            if self.find_ios_predicate("name CONTAINS '秒执行'"):
                break
            else:
                self.creat_task()
        self.find_name('保存').click()  # 点击保存
        time.sleep(1)
        return self.find_name('执行条件或执行任务不能为空，请添加')  # 验证弹窗元素是否存在

    # 68、管家-已设置名称-已设置执行条件-已设置执行任务，点击保存，跳转我的管家页面，查找第一个管家任务元素
    def scenetask_creat(self):
        self.scenetask_page()  # 情景任务编辑页面
        while True:  # 验证是否有满足条件，有就过，没有就创建一个
            if self.find_xpath(excel.xpath_con('first_condition')):  # 查询是否有满足任务
                break
            else:
                self.creat_condition()  # 创建满足条件
        while True:  # 验证是否有执行任务，有就过，没有就创建一个
            if self.find_ios_predicate("name CONTAINS '秒执行'"):
                break
            else:
                self.creat_task()
        self.set_name('自动化测试68')
        self.find_name('保存').click()  # 点击保存
        time.sleep(2)
        return self.find_name('自动化测试68')  # 验证管家是否新建成功

    # 69、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑
    def giveup_edit2(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.creat_task()
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        return self.find_name('是否放弃编辑')  # 验证是否有弹窗

    # 70、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击取消，弹窗消失
    def giveup_edit2_cancel(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.creat_condition()
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        self.find_name('取消').click()  # 点击取消按钮
        time.sleep(1)
        f1 = bool(self.find_name('是否放弃编辑'))
        f2 = bool(self.find_name('满足任一条件时'))
        return f1 == False and f2 == True # 验证是否有弹窗和是否在编辑页面

    # 71、管家-已设置执行任务，点击左上返回按钮，弹窗提示：是否放弃编辑，点击确定，跳转我的管家页面，任务未保存
    def giveup_edit2_sure(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.creat_task()
        self.set_name('自动化测试71')
        self.find_xpath(excel.xpath_con('time_back')).click()  # 点击左上返回按钮
        self.find_name('确定').click()  # 点击确定按钮
        time.sleep(1)
        f1 = bool(self.find_name('是否放弃编辑'))
        f2 = bool(self.find_name('满足任一条件时'))
        f3 = bool(self.find_name('自动化测试71'))
        return f1 == False and f2 == False and f3 == False  # 验证是否有弹窗和是否在编辑页面

    # 72、管家-情景任务编辑页面，点击生效条件，进入生效条件页面,查找：生效时间条件
    def precondition_page(self):
        self.scenetask_page()  # 情景任务编辑页面
        self.find_name('生效条件').click()  # 点击生效条件
        return self.find_name('生效时间条件')

    # 73、管家-生效条件页面，点击生效时间条件，进入生效时段页面
    def precondition_time(self):
        self.precondition_page()  # 生效条件页面
        self.find_name('生效时间条件').click()  # 点击生效时间条件
        return self.find_name('生效时段')

    # 74、管家-生效条件页面，点击生效设备条件，进入选择设备页面
    def precondition_device(self):
        self.precondition_page()  # 生效条件页面
        self.find_name('生效设备条件').click()  # 点击生效设备条件
        return self.find_name('选择设备')

    # 75、管家-生效条件页面，点击生效场景条件，进入选择场景页面
    def precondition_scene(self):
        self.precondition_page()  # 生效条件页面
        self.find_name('生效场景条件').click()  # 点击生效场景条件
        return self.find_name('选择场景')

    # 76、管家-新建一个情景任务，点击情景任务，进入情景任务编辑页面
    def click_scenetask(self):
        self.scenetask_page()  # 情景任务编辑页面
        while True:  # 验证是否有满足条件，有就过，没有就创建一个
            if self.find_xpath(excel.xpath_con('first_condition')):  # 查询是否有满足任务
                break
            else:
                self.creat_condition()  # 创建满足条件
        while True:  # 验证是否有执行任务，有就过，没有就创建一个
            if self.find_ios_predicate("name CONTAINS '秒执行'"):
                break
            else:
                self.creat_task()
        self.set_name('自动化测试76')
        self.find_name('保存').click()  # 点击保存
        time.sleep(2)
        self.find_name('自动化测试76').click()  # 点击第一个管家任务
        time.sleep(2)
        return self.find_name('满足任一条件时')

    # 77、管家-新建一个情景任务，左划任务，拉出删除按钮
    def scenetask_swip_delete(self):
        self.housekeeper_page()  # 管家页面
        if self.find_name('还没有创建管家任务，点击右上角“+”创建'):  # 验证是否有场景任务
            self.find_name('common icon add').click()  # 点击右上+按钮
            self.find_name('butler addscene icon').click()  # 点击情景任务
            time.sleep(1)
            while True:  # 验证是否有满足条件，有就过，没有就创建一个
                if self.find_xpath(excel.xpath_con('first_condition')):  # 查询是否有满足任务
                    break
                else:
                    self.creat_condition()  # 创建满足条件
            while True:  # 验证是否有执行任务，有就过，没有就创建一个
                if self.find_ios_predicate("name CONTAINS '秒执行'"):
                    break
                else:
                    self.creat_task()
            self.set_name('自动化测试77')
            self.find_name('保存').click()  # 点击保存
            time.sleep(2)
        self.leftswip_housekeeper(2000)  # 左划任务
        return self.find_name('删除')

    # 78、管家-新建一个情景任务，左划任务，拉出删除按钮，点击删除按钮，任务被删除
    def scenetask_click_delete(self):
        self.no_housekeeper()  # 管家页面，删除所有管家任务
        self.find_name('common icon add').click()  # 点击右上+按钮
        self.find_name('butler addscene icon').click()  # 点击情景任务
        time.sleep(1)
        while True:  # 验证是否有满足条件，有就过，没有就创建一个
            if self.find_xpath(excel.xpath_con('first_condition')):  # 查询是否有满足任务
                break
            else:
                self.creat_condition()  # 创建满足条件
        while True:  # 验证是否有执行任务，有就过，没有就创建一个
            if self.find_ios_predicate("name CONTAINS '秒执行'"):
                break
            else:
                self.creat_task()
        self.set_name('自动化测试78')
        self.find_name('保存').click()  # 点击保存
        time.sleep(2)
        self.leftswip_housekeeper(2000)  # 左划任务
        self.find_name('删除').click()  # 点击删除按钮
        time.sleep(2)
        return self.find_name('还没有创建管家任务，点击右上角“+”创建')  # 验证我的管家页面管家任务元素是否存在
