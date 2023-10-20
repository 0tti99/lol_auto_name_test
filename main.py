import numpy as np
import os
import time
import pyautogui
import win32api
import win32con


def get_pos(filepath):
    position = pyautogui.locateOnScreen(filepath, confidence=0.8)
    while(position is None):
        print(f"{filepath} not on screen!")
        position = pyautogui.locateOnScreen(filepath, confidence=0.8)
        time.sleep(1)
    (left, top, width, height) = position
    print(f"{left} {top} {width} {height}")
    return ((left,top + 10))

def click(mouse_pos):
    win32api.SetCursorPos(mouse_pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def names_to_check():
    with open('names.txt', 'r') as f:
        lines = f.readlines()  
    lines = [line.strip() for line in lines]
    return lines
    
def main():
    # wait before the script starts
    time.sleep(1)
    
    # find and delete the ok_names file
    if(os.path.exists("ok_names.txt")):
        os.remove("ok_names.txt")
        
    # create it again
    ok_names = open("ok_names.txt", "w")
    
    # get the position of the check name button
    check_name = get_pos("images/check_name.png")
    
    # calculate the position of the text box
    text_box = tuple(np.subtract(check_name, (120,0)))
    
    # get the names to check from the file
    names = names_to_check()
    
    # steps for every name
    for name in names:
        
        # click the text box
        click(text_box)
        time.sleep(0.2)
        
        # write the name into the textbox
        # pyautogui.typewrite(name)
        time.sleep(0.2)
        
        # click the button
        click(check_name)
        time.sleep(0.2)
        
        # check the response
        response = pyautogui.locateOnScreen("images/name_ok.png", confidence=0.8)
        time.sleep(0.2)
        
        # name has been found
        if(response is not None):
            ok_names.write(name + "\n")
        time.sleep(0.2)
        
    ok_names.close()
    return 0

if __name__ == "__main__":
    exit_code = main()
    print(f"exit code: {exit_code}")