# coding:utf-8
import pyautogui
import time
import requests
import hashlib
import base64
import json
import pytesseract
from PIL import Image 
from PIL import ImageEnhance

def forward(num):
    pyautogui.keyDown('w')
    time.sleep(num)
    pyautogui.keyUp('w')
    time.sleep(0.1)
    print('前进结束')

def sideslip(direction,num):
    pyautogui.keyDown(str(direction))
    time.sleep(num)
    pyautogui.keyUp(str(direction))
    time.sleep(0.1)
    print('侧滑结束')

def turn(direction,num):
    pyautogui.keyDown(str(direction))
    time.sleep(num)
    pyautogui.keyUp(str(direction))
    print('转向结束')

def attack(num,interval):
    for i in range(num):
        pyautogui.press('tab')
        pyautogui.press('2')
        time.sleep(interval)
    print('击杀结束')

# 拾取物品
def pick_up(num,interval):
    pyautogui.press('esc')
    # 拾取中间
    for i in range(num):
        pyautogui.press('3')
        time.sleep(interval)
    # 拾取左边
    pyautogui.keyDown('q')
    time.sleep(0.70)
    pyautogui.keyUp('q')
    for i in range(num):
        pyautogui.press('3')
        time.sleep(interval)
    # 拾取右边
    pyautogui.keyDown('e')
    time.sleep(1.40)
    pyautogui.keyUp('e')
    for i in range(num):
        pyautogui.press('3')
        time.sleep(interval)
    # 返回中间
    pyautogui.keyDown('q')
    time.sleep(0.70)
    pyautogui.keyUp('q')

# 倾倒背包第一页右小角三个垃圾
def trash():
    pyautogui.press('f3')
    pyautogui.moveTo(2080,1080,0.1)
    pyautogui.click()
    pyautogui.moveTo(2080,580,0.1)
    pyautogui.click()
    pyautogui.moveTo(2150,1080,0.1)
    pyautogui.click()
    pyautogui.moveTo(2080,580,0.1)
    pyautogui.click()
    pyautogui.moveTo(2220,1080,0.1)
    pyautogui.click()
    pyautogui.moveTo(2080,580,0.1)
    pyautogui.click()
    pyautogui.press('f3')
    print('倒完垃圾')

def get_monster_name():
    global monster_name
    img = pyautogui.screenshot(region=(1220,200,300,50))
    time.sleep(0.1)
    print('截图成功')
    img.save(r'C:\Users\lrm\Desktop\one.png')
    time.sleep(0.1)

    # 印刷文字识别 webapi 接口地址
    URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/general"
    # 应用ID (必须为webapi类型应用，并印刷文字识别服务，参考帖子如何创建一个webapi应用：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=36481)
    APPID = "074593ae"
    # 接口密钥(webapi类型应用开通印刷文字识别服务后，控制台--我的应用---印刷文字识别---服务的apikey)
    API_KEY = "217bb29a4c86cfc6f22930489631ced9"
    def getHeader():
    #  当前时间戳
        curTime = str(int(time.time()))
    #  支持语言类型和是否开启位置定位(默认否)
        param = {"language": "en", "location": "false"}
        param = json.dumps(param)
        paramBase64 = base64.b64encode(param.encode('utf-8'))

        m2 = hashlib.md5()
        str1 = API_KEY + curTime + str(paramBase64,'utf-8')
        m2.update(str1.encode('utf-8'))
        checkSum = m2.hexdigest()
    # 组装http请求头
        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': APPID,
            'X-CheckSum': checkSum,
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        }
        return header
    # 上传文件并进行base64位编码
    with open(r'C:\Users\lrm\Desktop\one.png', 'rb') as f:
        f1 = f.read()

    f1_base64 = str(base64.b64encode(f1), 'utf-8')

        
    data = {
            'image': f1_base64
            }


    r = requests.post(URL, data=data, headers=getHeader())
    result = str(r.content, 'utf-8')

    # 错误码链接：https://www.xfyun.cn/document/error-code (code返回错误码时必看)
    monster_name = result[87:95]
    print(monster_name)

    time.sleep(0.2)
    

def attack_3(num,interval):
    for i in range(num):
        pyautogui.press('tab')
        time.sleep(1)
        get_monster_name()
        time.sleep(1)
        if '失控的' in monster_name:
            pyautogui.press('1')
            for i in range(13):
                pyautogui.press('2')
                time.sleep(2.20)
        else:
            pyautogui.press('2')
            time.sleep(interval)

num = [5,4,3,2,1]
for i in num:
    print('——请在 ' + str(i) + ' 秒内回到要挂机的窗口——')
    time.sleep(1)
print('主号已进入副本')

def go():
    pyautogui.press('i')
    time.sleep(2)

    sideslip('e',0.20)

    forward(2.90)
    print('————1————')

    turn('a',0.890)
    print('————2————')

    attack(4,4.0)
    print('————3————')

    forward(2.20)
    print('————4————')

    attack(3,4.0)
    print('————5————')

    forward(4.20)
    print('————6————')

    attack(3,4.0)
    print('————7————')

    forward(3.00)
    print('————8————')

    attack(8,4.0)
    print('————9————')

    forward(2.50)
    print('————10————')

    attack(8,4.0)
    print('————11————')

    forward(3.50)
    print('————12————')

    turn('d',1.50)
    print('————13————')

    attack(16,4.0)
    print('————14————')

    attack_3(6,4.0)
    print('————15————')

    turn('a',0.07)
    forward(4.70)
    pyautogui.press('esc')
    pick_up(5,0.1)
    print('————16————')

    turn('d',1.50)
    forward(4.20)
    turn('a',0.90)
    forward(12)
    print('————17————')

    trash()

go()
