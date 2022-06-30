import os
import re #regex
import re
import pyautogui
import webbrowser

hashtag_name = "#funny"

os.system("cd c:\\users\\sujan\\desktop\\python reddit youtube")   #move to video file location
os.system("del /f /q C:\\Users\\sujan\\AppData\\Local\\Instaloader\\session-sam.15_06")        #delete session file bcoz its causing error
os.system("instaloader --login=sam.15_06 --password=darkknight2785 \""+hashtag_name+"\" --no-pictures --no-captions --no-metadata-json --no-compress-json -c 5")   #download only hashtag vids - try upto 40

# folder path
dir_path = 'C:\\Users\\sujan\\Desktop\\Python Reddit Youtube'

os.system("move "+hashtag_name+"\\*.mp4")
# list to store files
list = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        list.append(path)
print(len(list))
print(list)
check = True
while check == True :
    for name in list:
        if re.search(".mp4$",name)==None:
            print("removing from list - "+name)
            list.remove(name)
            check = True
            break
        else:
            check = False
print(list)
for name in list:
        fileptr = open("videonames.txt","a")  
        fileptr.write("file "+name+"\n")
        fileptr.close()
#os.system("cd "+dir_path)
os.system("ffmpeg -f concat -i videonames.txt -c copy vids\\output.mp4")
os.system("del /f /q "+hashtag_name+"\\*.*")
os.system("del /f /q *.mp4")
os.system("del /f /q videonames.txt")
print("deleting all downloaded insta files & videonames.txt...")

file = open('CountInstaVids.txt')
count = 0
for line in file:
    fields = line.strip().split()
    count = fields[0]
    print(count)
file.close()
num = int(count)+1
string_count = '{}'.format(num)
fileptr = open("CountInstaVids.txt","w")  
fileptr.write(string_count)
fileptr.close()
title = "Random Insta Videos #"+string_count
print(title)

pyautogui.sleep(5)
webbrowser.open('https://studio.youtube.com/', new = 2)
pyautogui.sleep(5)
pyautogui.click(1800,99) #create
pyautogui.sleep(3)
pyautogui.click(1702, 145) #upload
pyautogui.sleep(5)
pyautogui.click(950,690) # select files
pyautogui.sleep(3)
pyautogui.click(250,185) # file choose
pyautogui.sleep(3)
pyautogui.click(700,669) # open
pyautogui.sleep(7)
pyautogui.click(x=540, y=357, clicks=2) #double click title paste
pyautogui.sleep(3) 
pyautogui.write(title)
pyautogui.sleep(3)
pyautogui.click(542, 464) #paste description
pyautogui.write("Random Instagram Videos Only For You   \n")
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(180)
pyautogui.hotkey('ctrl', 'w')
pyautogui.sleep(5)
os.system("del /f /q vids\\output.mp4")
print("deleted output.mp4")
print(list)
