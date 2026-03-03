import keyboard 
import pyautogui
import time

frame_idx = 0
frame_max = 6570
keyboard.wait("-")
while frame_idx < frame_max:
    try:
        with open (f"G:\Python\Bad Apple cs 2\Cfg\Frame_{frame_idx:04d}.cfg", "r", encoding="utf-8") as file:
            com = file.read().splitlines()
            keyboard.press_and_release("2")
            time.sleep(0.1)
            keyboard.press_and_release("`")
            time.sleep(0.1)

            for i in range(len(com)):
                keyboard.write(com[i])
                keyboard.press_and_release("enter")
                time.sleep(1.2 if i == 1 else 0.1)
            keyboard.press_and_release("`")
            time.sleep(0.1)
            screenshot = pyautogui.screenshot(f"G:\Python\Bad Apple cs 2\Screenshot\screen{frame_idx:04d}.png")
            time.sleep(0.1)
            keyboard.press_and_release("`")
            time.sleep(0.1)
            keyboard.write("mp_restartgame 1")
            keyboard.press_and_release("enter")
            keyboard.press_and_release("`")
            time.sleep(2)
            print ("frame {}".format(frame_idx))
    except FileNotFoundError:
        print(f"Файл {frame_idx} не найден, пропускаем...")
        continue
    frame_idx += 1





