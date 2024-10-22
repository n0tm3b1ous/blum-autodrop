import time
import pyautogui
import win32api, win32con

tickets = 0

def clickOnPic(pic):
    x, y = pyautogui.center(pic)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
    print("How many tickets do you want to use?")
    tickets = int(input())
    print("Starting in 5 seconds, swap to your bluestacks window and place your cursor on the Play button!")
    time.sleep(5)
    pyautogui.click()
    print("Dropping...")
    for i in range(tickets):
        timeEnd = time.time() + 30
        while time.time() < timeEnd:
            try:
                bpPic = pyautogui.locateOnScreen("img/blum.png", confidence=0.75) # Blum point recognition confidence
            except pyautogui.ImageNotFoundException:
                continue
            clickOnPic(bpPic)
            # time.sleep(0.01) # delay between clicks
        if i == tickets-1: break
        time.sleep(1)
        try:
            playButtonPic = pyautogui.locateOnScreen("img/playbutton.png", confidence=0.9)
        except pyautogui.ImageNotFoundException:
            print("Play button not found, exiting!")
            exit(1)
        clickOnPic(playButtonPic)
    print("Done!")
        
if __name__ == "__main__":
    main()