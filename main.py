import time
import threading
from tkinter import *
from pynput.mouse import Button, Controller
  
from pynput.keyboard import Listener, KeyCode

delay = 0.001
button = Button.left
toggleKey = KeyCode(char='`')
stopKey = KeyCode(char='\\')


window = Tk()
window.title("AutoClicker")
window.geometry("500x500")
window.grid()

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
  
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()
  

def on_press(key):
    if key == toggleKey:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stopKey:
        click_thread.exit()
        listener.stop()

window.mainloop()

with Listener(on_press=on_press) as listener:
    listener.join()


