from MasterDictionary import master
from DataManipulation import letters, lettersClearer, lettersBias, search
import time
import keyboard
import clipboard
import pynput
from pynput.mouse import Button
from pynput.keyboard import Key, Controller
import pyscreeze
import cv2

#pyscreeze.screenshot('1.jpg', region=(295, 948, 63, 62))
pic = cv2.imread('1.jpg')
keyboard_ = Controller()
mouse_ = pynput.mouse.Controller()

prevLetters = letters
run = True
print('Setup Complete')

while run:

    #if keyboard.is_pressed('esc'):


        turn = True
        while turn:
            pyscreeze.screenshot('2.jpg', region=(295, 948, 63, 62))
            pic2 = cv2.imread('2.jpg')
            b, g, r = cv2.split(cv2.subtract(pic, pic2))
            if keyboard.is_pressed('esc'):
                 turn = False
                 run = False
            if cv2.countNonZero(b) != 0 or cv2.countNonZero(g) != 0 or cv2.countNonZero(r) != 0:
                turn = False



        syllable, prevSyllable = "",""
        clipboard.copy("")


        mouse_.position = (753, 580)
        mouse_.click(Button.left, 2)
        with keyboard_.pressed(Key.ctrl):
            keyboard_.type('c')
        mouse_.position = (1072,514)
        mouse_.click(Button.left, 1)


        while syllable == prevSyllable:
            syllable = clipboard.paste()
        prevSyllable = syllable


        try:
            #word = lettersBias(master, letters, syllable)
            word = search(master[50000:],syllable)

            print(word)

            for letter in word:
                keyboard_.type(letter)
                #time.sleep(.05)
                time.sleep(.02)
            keyboard_.press(Key.enter)

            keyboard_.release(Key.enter)

            master.remove(word)

            #chat
            #mouse_.position = (1705, 978)
            #mouse_.click(Button.left, 1)

            # Test whether word was valid or not
            if cv2.countNonZero(b) != 0 or cv2.countNonZero(g) != 0 or cv2.countNonZero(r) != 0:
                letters = lettersClearer(word, letters)

            print(letters)

            time.sleep(.25)

        except:
            pass


