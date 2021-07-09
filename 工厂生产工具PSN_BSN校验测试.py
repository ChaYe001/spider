
from com.dtmilano.android.viewclient import ViewClient
import time
import os, subprocess, sys
import random
import itertools
import argparse

def generate_random_str1(base_str):
    nonum = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    noAC = 'DEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    capsletter = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    Lowletter = 'abcdefghigklmnopqrstuvwxyz'
    ACletter = 'ABC'
    num = '0123456789'
    random_str = ''
    # length = len(capsletter) - 1
    # Pnum = (Lowletter + num)[random.randint(0, len(Lowletter + num) - 1)]
    # fePnum = (Lowletter + num)[random.randint(0, len(Lowletter + num)-1)]
    # datanum1 = num[random.randint(0, len(num)-1)]
    if base_str == 'datanum2':
        random_str = ACletter[random.randint(0, 2)]
    if base_str == 'fedatanum2':
        random_str = noAC[random.randint(0, len(noAC) - 1)]
    if base_str == 'Facnum':
        random_str = capsletter[random.randint(0, len(capsletter) - 1)]
    if base_str == 'feFacnum':
        random_str = (Lowletter + num)[random.randint(0, len(Lowletter + num) - 1)]
    if base_str == 'serialnum':
        random_str = num[random.randint(0, len(num) - 1)]
    if base_str == 'feserialnum':
        random_str = nonum[random.randint(0, len(nonum) - 1)]
    return random_str
def generate_random_str(i):
  """
  生成一个指定长度的随机字符串
  """
  # nonum = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
  # noAC = 'DEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  # capsletter  = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
  # Lowletter = 'abcdefghigklmnopqrstuvwxyz'
  # ACletter = 'ABC'
  # num = '0123456789'
  # # length = len(capsletter) - 1
  # # Pnum = (Lowletter + num)[random.randint(0, len(Lowletter + num) - 1)]
  # # fePnum = (Lowletter + num)[random.randint(0, len(Lowletter + num)-1)]
  # # datanum1 = num[random.randint(0, len(num)-1)]
  # datanum2 = ACletter[random.randint(0,2)]
  # fedatanum2 = noAC[random.randint(0,len(noAC)-1)]
  # Facnum = capsletter[random.randint(0, len(capsletter)-1)]
  # feFacnum = (Lowletter + num)[random.randint(0, len(Lowletter + num)-1)]
  # serialnum = num[random.randint(0, len(num)-1)]
  # feserialnum = nonum[random.randint(0, len(nonum)-1)]
  if i == 11:
      random_str = 'G20' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1(
          'datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')

  if i == 14:
      random_str = 'G26' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1(
          'datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')

  if i == 12:
      random_str = '140' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1(
          'datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 13:
      random_str = 'G41' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1(
          'datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1(
          'serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')

  if i ==15:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 0:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('feserialnum')
  if i == 1:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('feserialnum') + generate_random_str1('serialnum')
  if i == 2:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('feserialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 3:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('feserialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 4:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('feserialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 5:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('feserialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 6:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('feFacnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 7:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('feFacnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 8:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('fedatanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 9:
    random_str = 'G40' + generate_random_str1('Facnum') + generate_random_str1('feserialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
  if i == 10:
    random_str = 'G40' + generate_random_str1('feFacnum') + generate_random_str1('serialnum') + generate_random_str1('datanum2') + generate_random_str1('Facnum') + generate_random_str1('Facnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum') + generate_random_str1('serialnum')
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