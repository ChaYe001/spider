
from com.dtmilano.android.viewclient import ViewClient
import time
import os, subprocess, sys
import random
import itertools
import argparse


def generate_random_str(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str
def log(value):
    print(value)
def adb_shell(cmd):
    p = subprocess.getstatusoutput(cmd)
    return p
def start_test():
    global vc, device, cmd
    """采集指定抖音账号的关注推荐数据
    """
    # pic = 0
    log(u'准备测试SDK')
    # 连设备
    # serialno = argv.s
    serialno = '192.168.1.109:5555'
    if serialno:
        os.system('adb connect {}'.format(serialno or ''))
        time.sleep(3)

    device, serialno = ViewClient.connectToDeviceOrExit(serialno=serialno)
    vc = ViewClient(device, serialno, autodump=False)


    # op = adb_shell('adb shell getprop ro.build.version.release')
    # if int(op[0]) == 0:
    #     AndroidId = int(op[1])
    #     print(AndroidId)
    #     if AndroidId == 10:
    #         log(u'Android 10')
    #         cmd = "adb shell 'cd /sdcard/Android/data/com.llvision.glass3.api.test/files/Movies && ls -l |wc -l'"
    #     else:
    #         log(u'Android 9-')
    #         cmd = "adb shell 'cd sdcard/DCIM/LLVisionCamera && ls -l |wc -l'"
    # else:
    #     print('获取安卓版本失败，退出！！')
    # # 强制关闭SDK
    # log(u'强制关闭SDK.')
    # device.shell('am force-stop com.llvision.glass3.api.test')
    # time.sleep(2)
    # print(123)
    # #
    # # 启动SDK
    # log(u'启动SDK.')
    # device.shell('am start -n com.llvision.glass3.api.test/com.llvision.glass3.api.test.MainActivity')
    # time.sleep(10)
    # # 等待连接成功
    # log(u'等待连接成功.')

    # 点击搜索按钮
    time.sleep(1)
    vc.dump()

def powerkey():
    os.system('adb shell input keyevent 26')

def set_aes():

    vc.dump()

    btaes = vc.findViewById('com.llvision.glass3.api.test:id/btn_aes_key')
    if btaes:
        log(u'进入aes')
        btaes.touch()
        time.sleep(0.1)
        vc.dump()
    else:
        print(1)
    aes = generate_random_str(16)
    edt_aes = vc.findViewById('com.llvision.glass3.api.test:id/edt_aes_key')
    if edt_aes:
        log(u'写入aes.')
        edt_aes.touch()
        time.sleep(0.1)
        os.system('adb shell input text ' + str(aes))
        print(aes)
        vc.dump()
    else:
        print(2)
    for offset in range(9):

        edt_offset = vc.findViewById('com.llvision.glass3.api.test:id/edt_offset')
        if edt_offset:
            log(u'写入offset.')
            edt_offset.touch()
            time.sleep(0.1)
            os.system('adb shell input keyevent 67')
            os.system('adb shell input text ' + str(offset))
            vc.dump()
        else:

            print(3)
        btn_set_aes = vc.findViewById('com.llvision.glass3.api.test:id/btn_set_aes_key')
        if btn_set_aes:
            log(u'set offset.')
            btn_set_aes.touch()
            time.sleep(0.1)
            vc.dump()
        else:
            print(4)
        aeslist.insert(offset, str(aes))

    return aeslist

def checkaes():
    aeslist = set_aes()
    device.shell('input keyevent 4')
    device.shell('input keyevent 4')
    # device.drag((345,1550), (345, 1250), duration=100)
    vc.dump()
    btfac = vc.findViewById('com.llvision.glass3.api.test:id/id_factory_test')
    if btfac:
        log(u'进入fac')
        btfac.touch()
        time.sleep(0.1)
        vc.dump()
    btTEM = vc.findViewById('com.llvision.glass3.api.test:id/btn_temperature_frequency')
    if btTEM:
        log(u'进入TEM')
        btTEM.touch()
        time.sleep(0.1)
        vc.dump()
    for offset in range(9):
        edoffset = vc.findViewById('com.llvision.glass3.api.test:id/edt_offset')
        if edoffset:
            log(u'填入offset')
            edoffset.touch()
            time.sleep(0.1)
            vc.dump()
            # offset = random.randint(0, 8)
            os.system('adb shell input keyevent 67')
            os.system('adb shell input text ' + str(offset))
            print(offset)
            time.sleep(0.1)
            vc.dump()
        btsyncaes = vc.findViewById('com.llvision.glass3.api.test:id/btn_sync_aes_key')
        if btsyncaes:
            log(u'查看aes')
            btsyncaes.touch()
            time.sleep(0.1)
            vc.dump()
        showifo = vc.findViewWithText(aeslist[offset])
        if showifo:
            print(aeslist[offset])

        else:
            print('非正常结束')
            sys.exit()
    device.shell('input keyevent 4')
    device.shell('input keyevent 4')
    device.shell('input keyevent 4')


if __name__ == "__main__":
    start_test()
    aeslist = ['123','456','123','456','123','456','123','456','123','456','123','456']
    device.drag((345, 1550), (345, 1250), duration=100)
    for j in range(100):
        checkaes()