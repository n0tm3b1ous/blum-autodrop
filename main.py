import time
import pyautogui
import win32api, win32con

tickets = 0

def click(pic):
    x, y = pyautogui.center(pic)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main():
    print("How many tickets do you want to use?")
    tickets = int(input())
    print("Starting in 5 seconds, swap to your bluestacks window and start the game!")
    time.sleep(5)
    print("Dropping...")
    for i in range(tickets):
        timeEnd = time.time() + 30
        while time.time() < timeEnd:
            try:
                bpPic = pyautogui.locateOnScreen("img/blum.png", confidence=0.75) # Blum point recognition confidence
            except pyautogui.ImageNotFoundException:
                continue
            click(bpPic)
            # time.sleep(0.01) # delay between clicks
        time.sleep(1)
        try:
            playButtonPic = pyautogui.locateOnScreen("img/playbutton.png", confidence=0.9)
        except pyautogui.ImageNotFoundException:
            print("Play button not found, exiting!")
            exit(1)
        click(playButtonPic)
        
if __name__ == "__main__":
    main()