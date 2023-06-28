import pyautogui
from time import sleep
import colorama
from colorama import Fore
import keyboard

pyautogui.FAILSAFE = False

print(Fore.LIGHTRED_EX + """                               
         
  -#%%%%%%%%%%%%%%%%%%%%%%#=  
 :%%%%%%%%%%%%%%%%%%%%%%%%%%- 
 +%%%%%%%%%%*#%%%%%%%%%%%%%%+                            _             _   
 *%%%%%%%%%%:   *%%%%%%%%%%%*     ___   ___   _ __ ___  | |__    ___  | |_ 
 *%%%%%%%%%%:     =%%%%%%%%%#    / __| / _ \ | '_ ` _ \ | '_ \  / _ \ | __|
 *%%%%%%%%%%:   +%%%%%%%%%%%*   | (__ | (_) || | | | | || |_) || (_) || |_        
 +%%%%%%%%%%+#%%%%%%%%%%%%%%+    \___| \___/ |_| |_| |_||_.__/  \___/  \__|
 :%%%%%%%%%%%%%%%%%%%%%%%%%%- 
   %%%%%%%%%%%%%%%%%%%%%%%% 
   """ , Fore.LIGHTYELLOW_EX + "                                            by ABDALRAHMAN125141""")
print(Fore.LIGHTBLUE_EX + "Welcame to Insta-once© Tool" , Fore.LIGHTYELLOW_EX +"V1")
print("                                                                                                        ")     
print(Fore.LIGHTMAGENTA_EX + "------------------------------------------------------------")
comment = input(Fore.LIGHTYELLOW_EX + "Please put your comment: ")
print("                                                                                                        ") 
how_many = input(Fore.LIGHTYELLOW_EX + "Please put how many videos you want to comment: ")
print("                                                                                                        ") 
print(Fore.LIGHTMAGENTA_EX +"--------------------------------------------------------------------------------------") 
print(Fore.LIGHTGREEN_EX + "Starting after 10s, please go to the YouTube Shorts page")

sleep(10)

for i in range(int(how_many)):
    # Commenting
    sleep(2)
    pyautogui.click(1018, 455)
    
    sleep(1)
    pyautogui.click(987, 654)
    
    sleep(1)
    keyboard.write(comment)
    
    sleep(1)
    pyautogui.click(1208, 665)
    
    sleep(2)
    pyautogui.click(1277, 185)
    
    # Scrolling
    sleep(1)
    pyautogui.scroll(-20)

