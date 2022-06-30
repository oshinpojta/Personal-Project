from idm import IDMan
import asyncio
from pyppeteer import launch
import time
import os
import re #regex
import pyautogui
import webbrowser
import random

def upload_tiktok():
  downloader = IDMan()
  tags = ["funny","anime","tiktok","challenge","cringe","foodie","hot","viral","football","haunted","wierd","trending","animeedits"]
  tag_name = tags[random.randint(0,len(tags)-1)]
  url_list = []
  async def main(tag_name):
      ssCount = 0
      print("Launching Browser....")
      # launch chromium browser in the background
      browser = await launch({"headless": False, "args": ["--start-maximized"]})
      # open a new tab in the browser
      page = await browser.newPage()
      tiktok_vid_url = "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-w4ewjk-DivShareLayoutV2.elmjn4l0 > div.tiktok-1hfe8ic-DivShareLayoutContentV2.elmjn4l1 > div.tiktok-1qb12g8-DivThreeColumnContainer.eegew6e2 > div.tiktok-yvmafn-DivVideoFeedV2.e5w7ny40 > div.tiktok-x6y88p-DivItemContainerV2.e19c29qe7 > div.tiktok-x6f6za-DivContainer-StyledDivContainerV2.e1gitlwo0 > div > div > a > div.tiktok-1wa52dp-DivPlayerContainer.e19c29qe4 > div.tiktok-1jxhpnd-DivContainer.e1yey0rl0 > div.tiktok-1h63bmc-DivBasicPlayerWrapper.e1yey0rl2"
      # add URL to a new page and then open it
      select = "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-w4ewjk-DivShareLayoutV2.elmjn4l0 > div.tiktok-1hfe8ic-DivShareLayoutContentV2.elmjn4l1 > div.tiktok-1qb12g8-DivThreeColumnContainer.eegew6e2 > div.tiktok-yvmafn-DivVideoFeedV2.e5w7ny40 > div.tiktok-x6y88p-DivItemContainerV2.e19c29qe7"
      await page.setViewport({"width": 1600, "height": 900})
      print("Getting Tiktok.com .....")
      pyautogui.screenshot().save("c:\\users\\sujan\\desktop\\python reddit youtube\\ss"+'{}'.format(ssCount)+".jpg")
      ssCount = ssCount+1
      pyautogui.screenshot().save("c:\\users\\sujan\\desktop\\python reddit youtube\\ss"+'{}'.format(ssCount)+".jpg")
      ssCount = ssCount+1
      pyautogui.screenshot().save("c:\\users\\sujan\\desktop\\python reddit youtube\\ss"+'{}'.format(ssCount)+".jpg")
      ssCount = ssCount+1
      await page.goto("https://www.tiktok.com/tag/"+tag_name)
      time.sleep(10)
      v = await page.querySelectorAll(
        select
      )
      print("Extracted URLs : ",len(v))
      ay = 0
      for vid in v:
        ay = ay+1
        await vid.hover()
        time.sleep(10)
        pyautogui.screenshot()
        s = await vid.querySelector("video")
        src = await s.getProperty("src")
        url = await src.jsonValue()
        print(url)
        print(ay)
        url_list.append(url)
      await browser.close()
      pyautogui.screenshot()
      print("URLs list ready...browser closed !")

  print("Starting : Tiktok Download .... tag : "+tag_name)
  asyncio.get_event_loop().run_until_complete(main(tag_name=tag_name))
  pyautogui.screenshot()
  #upload one by one 4 vids
  dir_path = "c:\\users\\sujan\\desktop\\python reddit youtube\\vids"
  print("Starting Upload to YouTube....")
  count_upload = 0
  count =  0
  '''
  for url in url_list:
    if count_upload == 4:
      break
    else:
      count_upload = count_upload+1
    downloader.download(url, dir_path, output="output.mp4", referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
    #keep count of videos
    file = open('CountTiktokVids.txt')
    for line in file:
        fields = line.strip().split()
        count = fields[0]
        print(count)
    file.close()
    num = int(count)+1
    string_count = '{}'.format(num)
    fileptr = open("CountTiktokVids.txt","w")  
    fileptr.write(string_count)
    fileptr.close()
    title = "Random TikTok Video #"+string_count
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
    pyautogui.write("Random TikTok Videos Only For You   \n")
    pyautogui.sleep(5)
    pyautogui.click(1378, 997) #next
    pyautogui.sleep(5)
    pyautogui.click(1378, 997) #next
    pyautogui.sleep(5)
    pyautogui.click(1378, 997) #next
    pyautogui.sleep(5)
    pyautogui.click(1378, 997) #next
    pyautogui.sleep(90)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.sleep(5)
    os.system("del /f /q vids\\output.mp4")
    print("deleted output.mp4")
    '''
  #upload 3-4 vids by merging
  for i in range(len(url_list)-5,len(url_list)-1):
    url = url_list[i]
    name = '{}'.format(i)+".mp4"
    downloader.download(url, dir_path, output=name, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
    time.sleep(10)
    fileptr = open("videonames.txt","a")  
    fileptr.write("file "+name+"\n")
    fileptr.close()
    time.sleep(2)

  os.system("move vids\\*.mp4")
  time.sleep(5)
  os.system("ffmpeg -f concat -i videonames.txt -c copy vids\\output.mp4")
  time.sleep(15)
  os.system("del /f /q *.mp4")
  os.system("del /f /q videonames.txt")
  print("deleting all downloaded tiktok files & videonames.txt...")
  #keep count of videos
  file = open('CountTiktokVids.txt')
  for line in file:
      fields = line.strip().split()
      count = fields[0]
      print(count)
  file.close()
  num = int(count)+1
  string_count = '{}'.format(num)
  fileptr = open("CountTiktokVids.txt","w")  
  fileptr.write(string_count)
  fileptr.close()
  title = "Random TikTok Video #"+string_count
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
  pyautogui.write("Random TikTok Videos Only For You   \n")
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

upload_tiktok()