import requests,os
import praw #reddit
import re #regex
import pyautogui
import webbrowser
import time

#pyautogui.mouseInfo()

########################-------------------------------------------- REDDIT AUTH -----------------------------------#############################
webbrowser.open('https://studio.youtube.com/', new = 2)
pyautogui.sleep(50)
quit()
client_id = "XJ1vQ1MbsW7UMF0wczYvBw"
client_secret = "LqhIjW4PNHvLzCYVQxOZljB0JOkgTg"
user_agent = "megamind"
username = "LocksmithSuch8024"
password = "Lovely@2785"

reddit = praw.Reddit(client_id="XJ1vQ1MbsW7UMF0wczYvBw", 
                    client_secret="LqhIjW4PNHvLzCYVQxOZljB0JOkgTg",
                    user_agent = "megamind",
                    username = "LocksmithSuch8024",
                    password = "Lovely@2785",)


def create_reddit_object():
    reddit = praw.Reddit(client_id="XJ1vQ1MbsW7UMF0wczYvBw", 
                    client_secret="LqhIjW4PNHvLzCYVQxOZljB0JOkgTg",
                    user_agent = "megamind",
                    username = "LocksmithSuch8024",
                    password = "Lovely@2785",)
    return reddit

reddit = create_reddit_object()

subred = reddit.subreddit("funny")

hot = subred.hot(limit = 6)
new = subred.new(limit = 6)
count = 0
for i in hot:
    count = count+1
    if(re.findall("^https://v.redd.it/",i.url)!=[]) :
        title = re.sub(r'\W+', '', i.title)
        if(len(title)>12):
            title = title[:10]
        
        print(title, "https://www.reddit.com" + i.permalink[:-1])
        seconds = time.time()
        local_time = time.ctime(seconds)
        fileptr = open("log.txt","a")  
        fileptr.write("Title : "+i.title+" \nUploading Time : "+local_time+" \n\n")
        fileptr.close() 
        url = "https://www.reddit.com" + i.permalink[:-1]+".json"
   
        r = requests.get(url,headers={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"})
     
        data = r.json()[0]
        video_url = data["data"]['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        audio_url = "https://v.redd.it/"+video_url.split("/")[3]+"/DASH_audio.mp4"
        
        with open("vids\\video.mp4","wb") as f:
            g = requests.get(video_url,stream=True)
            f.write(g.content)
        with open("vids\\audio.mp3","wb") as f:
            g = requests.get(audio_url,stream=True)
            f.write(g.content)
        videooutputname = title
        os.system("ffmpeg -i vids\\video.mp4 -i vids\\audio.mp3 -c copy vids\\output.mp4")
        print("Created Output : "+i.title)
        pyautogui.sleep(5)
        os.system("del /f /q vids\\video.mp4")
        print("deleted video.mp4.....")
        pyautogui.sleep(5)
        os.system("del /f /q vids\\audio.mp3")
        print("deleted audio.mp3.....")
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
        pyautogui.write(i.title)
        pyautogui.sleep(3)
        pyautogui.click(542, 464) #paste description
        pyautogui.write(i.title+"   \n")
        pyautogui.sleep(5)
        pyautogui.click(1378, 997) #next
        pyautogui.sleep(5)
        pyautogui.click(1378, 997) #next
        pyautogui.sleep(5)
        pyautogui.click(1378, 997) #next
        pyautogui.sleep(5)
        pyautogui.click(1378, 997) #next
        pyautogui.sleep(120)
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.sleep(5)
        os.system("del /f /q vids\\output.mp4")
        print("deleted output.mp4 for : "+i.title)
        pyautogui.sleep(5)


















        #cmd2 = "python upload_video.py --file='c:/users/sujan/desktop/videoplayback.mp4' --title='Summer vacation in California' --description='Had fun surfing in Santa Cruz' --keywords='surfing,Santa Cruz' --category='22' --privacyStatus='public'"
        #os.system(cmd2)
'''
        request_body = {
            'snippet': {
                'categoryI': 19,
                'title': i.title,
                'description': '#cats #videos #viral #catvideos #funny #youtube #shorts /n '+i.name+' random videos /n strange video',
                'tags': ['Python', 'Youtube API', 'Google','Reddit', 'Videos', 'Viral', 'Shorts']
            },
            'status': { 
            },
            'notifySubscribers': False
        }
        mediaFile = MediaFileUpload(videooutputname+'.mp4')
        response_upload = youtube.videos().insert(
            part='snippet,status',
            body=request_body,
            media_body=mediaFile
        ).execute()
        print("here7 DONE "+i.title+' ..................')

'''
############################### ------------------- new youtube upload -------------------------###########################33
'''
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
pyautogui.write('Hello, world!')
pyautogui.sleep(3)
pyautogui.click(542, 464) #paste description
pyautogui.write('Hello, world! ')
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.click(1378, 997) #next
pyautogui.sleep(5)
pyautogui.hotkey('ctrl', 'w')
quit()

'''
###################---------------------------- youtube upload ---------------------------------#########################
'''
CLIENT_SECRET_FILE = 'client_secrets.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

upload_date_time = datetime.datetime(2020, 8, 25, 12, 30, 0).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing This is Private Video ',
        'description': 'Upload TEsting This is Private Video',
        'tags': ['Python', 'Youtube API', 'Google']
    },
    'status': {
        'privacyStatus': 'public',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('videoplayback.mp4')

response_upload = youtube.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

'''

"""
youtube.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('thumbnail.png')
).execute()
"""