import rstr
# psn = rstr.xeger(r'[A-Z]\d[A-Z] \d[A-Z]\d')
# print(psn)

from com.dtmilano.android.viewclient import ViewClient
import time
import os, subprocess, sys

def generate_random_str(i):
    """
    生成一个指定长度的随机字符串
    """
    if i == 11:
        random_str = 'G20' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{6}')

    if i == 14:
        random_str = 'G26' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{6}')

    if i == 12:
        random_str = '140' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{6}')
    if i == 13:
        random_str = 'G41' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{6}')

    if i ==15:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{6}')
    if i == 0:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{5}\D')
    if i == 1:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{4}\D\d')
    if i == 2:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{3}\D\d{2}')
    if i == 3:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d{2}\D\d{3}')
    if i == 4:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\d\D\d{4}')
    if i == 5:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z]{2}\D\d{5}')
    if i == 6:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][A-Z][^A-Z]\d{6}')
    if i == 7:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[A-C][^A-Z][A-Z]\d{6}')
    if i == 8:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\d[^A-C][A-Z]{2}\d{6}')
    if i == 9:
        random_str = 'G40' + rstr.xeger(r'[A-Z]\D[A-C][A-Z]{2}\d{6}')
    if i == 10:
        random_str = 'G40' + rstr.xeger(r'[^A-Z]\d[A-C][A-Z]{2}\d{6}')
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
    log(u'准备测试psn写入规则')
    # 连设备
    # serialno = argv.s
    serialno = '192.168.1.101:5555'
    if serialno:
        os.system('adb connect {}'.format(serialno or ''))
        time.sleep(1)

    device, serialno = ViewClient.connectToDeviceOrExit(serialno=serialno)
    vc = ViewClient(device, serialno, autodump=False)
    time.sleep(1)
    vc.dump()

def powerkey():
    os.system('adb shell input keyevent 26')

def set_psn(i):

    vc.dump()

    btpsn = vc.findViewById('com.llvision.cit.test:id/btn_psn')
    if btpsn:
        log(u'进入psn写入')
        btpsn.touch()
        time.sleep(0.1)
        vc.dump()
    else:
        print(1)
    psn = generate_random_str(i)
    # psn = 'G40T5COQ106111'
    edt_btpsn = vc.findViewById('com.llvision.cit.test:id/edt_psn')
    if edt_btpsn:
        log(u'写入psn.')
        edt_btpsn.touch()
        time.sleep(0.1)
        os.system('adb shell input text ' + str(psn))
        os.system('adb shell input keyevent 66')
        # print(psn)
        vc.dump()
    else:
        print(2)
    return psn


def checkpsn():
    # psn = 'G4012345678901'
    j = 1
    for i in range(16):
        psn = set_psn(i)
        # psn = '12345678912345'
        # print(psn)
        time.sleep(1)
        vc.dump()
        # print(123)
        # showifo = vc.findViewById('com.llvision.cit.test:id/tv_info')
        showifo = vc.findViewWithText('PSN写入成功：' + psn)
        # print(showifo)
        if showifo:
            print(psn)

        else:
            print('非正常psn_' + str(psn)+ '_' + str(j))
            j += 1
            device.shell('input keyevent 4')
            device.shell('input keyevent 4')


if __name__ == "__main__":
    start_test()
    checkpsn()