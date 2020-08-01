import pyautogui as pyg
tys_path = "./image/333.png"


def seer():
    # 1.点击野怪  ok
    pyg.sleep(3)
    pyg.moveTo(528, 317)
    pyg.click()
    pyg.sleep(5)

    while 1:
        a = pyg.locateCenterOnScreen(tys_path)
        print(a)
        if a is not None:  # 判断技能在不在

            pyg.moveTo(436, 693)
            pyg.click()
            pyg.sleep(5)
        else:
            break
    pyg.moveTo(502, 653)
    pyg.click()


if __name__ == '__main__':
    for i in range(2):
        seer()
    # print(pyg.size())
