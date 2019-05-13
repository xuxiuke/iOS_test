# coding=utf-8
'''
Created on 2018年11月07日

@author: Duke    智尚金属两路开关
'''
from appiumframework.PO import base_page
from PO import excel
import time

class Metal_two_way_switch(base_page.Action):

    # 前置条件，开关1为开关模式
    def switch_mode1(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'智尚金属两路开关')  # 点击智尚金属两路开关
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        if self.is_element('xpath', excel.xpath_con('divMode_Switch')):  # 如果是开关模式就返回，不是就切换为开关模式
            self.find_xpath(excel.xpath_con('divMode_Switch')).click()  # 选择开关模式
            time.sleep(1)
            self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
            time.sleep(3)
        else:
            self.find_xpath(excel.xpath_con('magnetic_back')).click()  # 点击左上返回按钮
            time.sleep(1)

    # 进入设备详情页
    def metal_page(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'智尚金属两路开关')  # 点击智尚金属两路开关
        self.wait_ac(excel.activity_con('device_detail_activity'))
        return self.is_element('xpath', excel.xpath_con('metal_switch_mode_2'))  # 验证页面是否有元素开关模式2

    # 进入设备详情页，点击左上返回按钮，返回设备列表
    def metal_page_back(self):
        self.metal_page()  # 设备详情页
        self.find_xpath(excel.xpath_con('magnetic_back')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_item('搜索设备')

    # 详情页，长按开关1，弹出编辑框----用例只写开关1，开关2省略，下同
    def name1_press(self):
        self.switch_mode1()  # 设备详情页，开关1为开关模式
        self.long_press_custom(self.find_xpath(excel.xpath_con('metal_switch_name_1')))  # 长按开关1名称
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('metal_name_edit'))  # 验证编辑框元素是否存在

    # 详情页-编辑框，点击取消按钮，编辑框消失
    def name1_press_cancel(self):
        self.name1_press()  # 长按开关1弹出编辑框
        self.find_xpath(excel.xpath_con('metal_name_edit_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('metal_name_edit'))  # 验证编辑框元素是否存在

    # 详情页-编辑框，点击修改开关名称，弹出修改名称弹窗
    def name1_press_modify(self):
        self.name1_press()  # 长按开关1弹出编辑框
        self.find_xpath(excel.xpath_con('metal_name_edit_modify')).click()  # 点击修改开关名称按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('metal_modify_switch_name'))  # 验证修改名称弹窗元素是否存在

    # 详情页-修改名称弹窗，输入新名称呵呵1，点击取消按钮，弹窗消失，名称未修改
    def name1_modify_cancel(self):
        self.name1_press_modify()  # 修改子开关名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'呵呵1')  # 输入新名称呵呵1
        self.find_xpath(excel.xpath_con('giveup_edit_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('呵呵1')

    # 详情页-修改名称弹窗，输入新名称呵呵1，点击确定按钮，弹窗消失，名称修改成功----名称需要修改回来
    def name1_modify_sure(self):
        self.name1_press_modify()  # 修改子开关名称弹窗
        self.find_xpath(excel.xpath_con('renameInput')).send_keys(u'呵呵1')  # 输入新名称呵呵1
        self.find_xpath(excel.xpath_con('giveup_edit_sure')).click()  # 点击确定按钮
        return self.find_item('呵呵1')

    # 详情页，点击开关模式，进入切换模式页面
    def mode_page(self):
        self.metal_page()  # 设备详情页
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        return self.find_item('切换模式')

    # 详情页-切换模式页面，点击绑定模式，右上显示出确定按钮
    def mode_submit(self):
        self.switch_mode1()  # 设备详情页，开关1为开关模式
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        self.find_xpath(excel.xpath_con('divMode_binding')).click()  # 选择绑定模式
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('submit'))  # 验证确定按钮是否出现

    # 详情页-切换模式页面，点击绑定模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页
    def mode_submit_sure(self):
        self.mode_submit()  # 切换模式页面，选择绑定模式
        self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
        time.sleep(3)
        return self.find_item('绑定模式')

    # 详情页-绑定模式，点击开关按钮，进入绑定设备页面
    def binding_page(self):
        self.mode_submit_sure()  # 开关模式切换为绑定模式
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(1)
        return self.find_item('绑定设备')

    # 详情页-切换模式页面，点击场景模式，右上显示出确定按钮
    def mode_scene_submit(self):
        self.switch_mode1()  # 设备详情页，开关1为开关模式
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        self.find_xpath(excel.xpath_con('divMode_secne')).click()  # 选择绑定模式
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('submit'))  # 验证确定按钮是否出现

    # 详情页-切换模式页面，点击场景模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页
    def mode_scene_submit_sure(self):
        self.mode_scene_submit()  # 切换模式页面，选择场景模式
        self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
        time.sleep(3)
        return self.find_item('场景模式')

    # 详情页-场景模式，点击开关按钮，进入选择场景页面
    def scenemode_page(self):
        self.mode_scene_submit_sure()  # 开关1模式为场景模式
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(1)
        return self.find_item('选择场景')

    # 详情页-场景模式，点击场景模式，进入切换模式页面
    def mode_page_by_scene(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'智尚金属两路开关')  # 点击智尚金属两路开关
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        if self.is_element('xpath', excel.xpath_con('divMode_secne')):  # 如果是场景模式就返回，不是就切换为场景模式
            self.find_xpath(excel.xpath_con('divMode_secne')).click()  # 选择场景模式
            time.sleep(1)
            self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
            time.sleep(3)
        else:
            self.find_xpath(excel.xpath_con('magnetic_back')).click()  # 点击左上返回按钮
            time.sleep(1)
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击场景模式
        time.sleep(1)
        return self.find_item('切换模式')

    # 详情页-绑定模式，点击绑定模式，进入切换模式页面
    def mode_page_by_binding(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'智尚金属两路开关')  # 点击智尚金属两路开关
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        if self.is_element('xpath', excel.xpath_con('divMode_binding')):  # 如果是绑定模式就返回，不是就切换为绑定模式
            self.find_xpath(excel.xpath_con('divMode_binding')).click()  # 选择绑定模式
            time.sleep(1)
            self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
            time.sleep(3)
        else:
            self.find_xpath(excel.xpath_con('magnetic_back')).click()  # 点击左上返回按钮
            time.sleep(1)
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击绑定模式
        time.sleep(1)
        return self.find_item('切换模式')

    # 详情页-切换模式页面，点击开关模式，右上显示出确定按钮
    def mode_binding_submit(self):
        self.mode_page_by_binding()  # 开关1绑定模式，切换模式页面
        self.find_xpath(excel.xpath_con('divMode_Switch')).click()  # 选择开关模式
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('submit'))  # 验证确定按钮是否出现

    # 详情页-切换模式页面，点击开关模式，右上显示出确定按钮，点击确定按钮，保存成功，跳转详情页----开关2默认开关模式，不能使用查找text开关模式
    def mode_binding_submit_sure(self):
        self.mode_binding_submit()  # 开关1绑定模式，切换模式页面选择开关模式
        self.find_xpath(excel.xpath_con('submit')).click()  # 点击确定按钮
        time.sleep(3)
        self.find_xpath(excel.xpath_con('metal_switch_mode_1')).click()  # 详情页点击开关模式
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('divMode_Switch'))  # 验证是否有开关模式元素，应该没有

    # 详情页，点击右上更多按钮，进入更多页面
    def more_page(self):
        self.metal_page()  # 详情页
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证页面是否有删除设备按钮

    # 更多页面，点击左上返回按钮，返回详情页
    def more_page_back(self):
        self.more_page()  # 更多页面
        self.find_xpath(excel.xpath_con('metal_more_back')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('metal_switch_mode_2'))  # 验证页面是否有元素开关模式2

    # 更多页面，点击重命名，弹出修改名称弹窗
    def rename(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证是否有重命名弹窗元素

    # 更多页面-修改名称弹窗，输入名称呵呵123，点击取消按钮，弹窗消失，名称未修改
    def rename_cancel(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵123')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('呵呵123')

    # 更多页面-修改名称弹窗，输入名称呵呵123，点击确定按钮，弹窗消失，名称修改成功----名称需要修改回来
    def rename_sure(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵123')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('修改设备名称成功')

    # 更多页面-重命名弹窗，不输入名称，点击确定无效，查找：请输入设备名
    def rename_none(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys('')  # 不输入名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_item('请输入设备名')

    # 重命名设备名称，再次设置设备名称为名称重复，toast提示：设备名称重复！
    def rename_repeat(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'名称重复')  # 输入名称重复
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('设备名称重复！')

    # 更多页面，点击分区，进入分区页面
    def zone_page(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('no_zone'))  # 验证页面是否有未分区元素

    # 更多页面-分区页面，点击左上返回按钮，返回更多页面
    def zone_page_back(self):
        self.zone_page()  # 更多，分区页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-分区页面，点击管理分区，进入分区管理页面
    def zone_manage_page(self):
        self.zone_page()  # 更多，分区页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击管理分区
        time.sleep(1)
        return self.find_item('分区管理')

    # 更多页面-分区页面-分区管理页面，点击左上返回按钮，返回分区页面
    def zone_manage_page_back(self):
        self.zone_manage_page()  # 分区管理页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('no_zone'))  # 验证页面是否有未分区元素

    # 更多页面-分区页面，前置条件至少一个分区，点击第一个分区，跳转更多页面，toast提示：修改设备区域成功
    def change_zone(self):
        self.least_one_zone()  # 至少一个分区
        time.sleep(1)
        self.click_device(u'智尚金属两路开关')  # 点击智尚金属两路开关
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more_first_zone')).click()  # 点击第一个分区
        return self.find_toast('修改设备区域成功')

    # 更多页面-分区页面，前置条件修改区域成功，点击未分区，跳转更多页面，查找未分区
    def zone_page_non(self):
        self.zone_page()  # 更多，分区页面
        self.find_xpath(excel.xpath_con('no_zone')).click()  # 点击未分区
        time.sleep(2)
        return self.find_item('未分区')

    # 更多页面，点击设备信息，进入设备信息页面
    def device_information(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_info')).click()  # 点击设备信息
        time.sleep(1)
        return self.find_item('产品名称')

    # 更多页面-设备信息页面，点击左上返回按钮，返回更多页面
    def device_information_back(self):
        self.device_information()  #  设备信息页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面，点击找设备，弹出找设备弹窗
    def finddevice(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_find')).click()  # 点击找设备
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面-找设备弹窗，点击已找到按钮，弹窗消失
    def finddevice_found(self):
        self.finddevice()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击已找到
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面-找设备弹窗，点击再闪一次，弹窗还在
    def finddevice_again(self):
        self.finddevice()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击再闪烁一次
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面，点击日志，进入日志页面
    def log_message_page(self):
        self.more_page()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.wait_ac(excel.activity_con('message_log_activity'))

    # 更多页面-日志页面，点击左上返回按钮，返回更多页面
    def log_message_page_back(self):
        self.log_message_page()  # 日志消息页面
        self.find_id(excel.id_con('img_left')).click()  # 点击返回按钮
        time.sleep(1)
        return self.find_item('更多')

    # 更多页面-日志页面，点击按日期查找，弹窗日期编辑框
    def log_search_by_time(self):
        self.log_message_page()  # 日志消息页面
        self.find_id(excel.id_con('log_image_arrow')).click()  # 点击按日期查找
        time.sleep(2)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 判断元素是否存在

    # 更多页面-日志页面-弹窗日期编辑框，点击其他任意地方，编辑框消失----点击返回操作
    def log_search_by_time_hide(self):
        self.log_search_by_time()  # 按日期查找弹窗
        self.driver.back()
        time.sleep(2)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 判断元素是否存在

    # 更多页面-日志页面，点击清空记录，弹出清空记录弹窗
    def log_empty(self):
        self.log_message_page()  # 日志消息页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-日志页面-清空记录弹窗，点击取消按钮，弹窗消失
    def log_empty_cancel(self):
        self.log_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-日志页面-清空记录弹窗，点击确定按钮，弹窗消失，返回更多页面
    def log_empty_sure(self):
        self.log_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面，前置条件清空了记录，进入日志页面，查找：没有日志消息
    def log_empty_sure_again(self):
        self.log_empty_sure()  # 清空记录
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('没有日志消息')

    # 更多页面，前置条件清空了记录,开关1为开关模式，返回详情页，点击开关按钮两次，查找已打开
    def metal_open(self):
        self.switch_mode1()  # 设备详情页，开关1为开关模式
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('metal_more_back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已打开')

    # 更多页面，前置条件清空了记录,开关1为开关模式，返回详情页，点击开关按钮两次，查找已关闭
    def metal_close(self):
        self.switch_mode1()  # 设备详情页，开关1为开关模式
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('metal_more_back')).click()  # 点击左上返回按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('metal_switch_1')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已关闭')

    # 更多页面，点击删除设备按钮，弹出删除确认弹窗
    def delete_device(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_delete')).click()  # 点击删除设备按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-删除确认弹窗，点击取消按钮，弹窗消失----确定按钮，用例省略
    def delete_device_cancel(self):
        self.delete_device()  # 删除设备弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在
