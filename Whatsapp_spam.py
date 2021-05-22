import pyautogui
import webbrowser as wb
import time
# at first copy the message you want to spam

count=input() # this is the number how many times you want to sapam

wb.open('https://web.whatsapp.com/')  # this will open whatsapp web 
time.sleep(60)   # here you will get a delay of 1 min to log in to whatsapp and select the chat where you want to spam

for i in range(count):
    ##################################
    pyautogui.hotkey('ctrl', 'v')   #1
    pyautogui.press("enter")        #2           this 2 line of codes will allow you to spam a message that you have copied.
    ##################################

    ################################
    # pyautogui.typewrite("string")#
    # pyautogui.typewrite("\n")    #            to use this code you have remove the # before the code and replace string with your message
    ################################

  # you should use any one code  or it will send 2 messages. First one is recomended.
  #-------------------------------------------------------------------------------------------------------------------#



