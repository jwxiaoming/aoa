# coding:utf-8
import pyautogui
import time
import requests

# 自动模式
def mode_a():
    attack_key = '2'
    switch_key = 'tab'
    turn_key = 'd'
    turn_angle = 0.12
    interval_time = 0.15
    num = [5,4,3,2,1]

    for i in num:
        print('——请在 ' + str(i) + ' 秒内回到要挂机的窗口——')
        time.sleep(1)

    cishu = 0
    while(True):
        pyautogui.press(switch_key)
        time.sleep(interval_time)
        pyautogui.press(attack_key)
        time.sleep(interval_time)
        pyautogui.keyDown(turn_key)
        time.sleep(turn_angle)
        pyautogui.keyUp(turn_key)
        time.sleep(interval_time)
        cishu += 1
        print('已完成自动攻击:'+str(cishu)+'次，按 Ctrl+C 退出'+r["tips"])

# 高级模式
def mode_b():
    attack_key = str(input('请输入攻击技能键：'))
    switch_key = str(input('请输入怪物选择键(tab键请输入tab)：'))
    turn_key = str(input('请输入转向键：'))
    turn_angle = float(input('请输入转向角度值（建议0.1至0.15）：'))
    interval_time = 0.15
    num = [5,4,3,2,1]

    for i in num:
        print('——请在 ' + str(i) + ' 秒内回到要挂机的窗口——')
        time.sleep(1)

    cishu = 0
    while(True):
        pyautogui.press(switch_key)
        time.sleep(interval_time)
        pyautogui.press(attack_key)
        time.sleep(interval_time)
        pyautogui.keyDown(turn_key)
        time.sleep(turn_angle)
        pyautogui.keyUp(turn_key)
        time.sleep(interval_time)
        cishu += 1
        print('已完成自动攻击:'+str(cishu)+'次，按 Ctrl+C 退出'+ r["tips"])

# 选择模式
def select_mode():
    print('——————————————————————————————————————')
    print('欢迎使用机甲世纪定点刷怪脚本，请选择以下两种模式开始~')
    print('A：自动模式，请提前将攻击技能键放置在数字【2】')
    print('B：高级模式，可自定义技能键与转向方向、角度')
    print('——————————————————————————————————————')
    mode = input('请输入A或B（不区分大小写）按回车，进行下一步：')
    # mode_text = ['a','A','b','B']
        
    if mode == 'a'or mode=='A':
        print('您已选择自动模式')
        mode_a()
    elif mode == 'b'or mode=='B':
        print('您已选择高级模式')
        mode_b()
    else:
        print('你输入的不是A或B,请重新输入。')
        select_mode()
        # exit()

#查看开关
url = "https://jwxiaoming.github.io/aoa/Autokill/info.json"
r = requests.get(url).json()
if r["switch"] == 'on':
    select_mode()
    # print(r["tips"])
else:
    print('程序维护或已有新版本，可加微信客服（jwxiaoming）了解更多')
    exit()

