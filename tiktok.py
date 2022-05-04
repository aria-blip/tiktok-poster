import moviepy.editor as mp
import requests
import random

subreddits=["interestingasfuck","Damnthatsinteresting","mildlyinteresting","notinteresting","coolguides","GetMotivated","creepy","pics","Images",]
response = requests.get("https://meme-api.herokuapp.com/gimme/"+random.choice(subreddits)).json()

text=response["title"]
imagurl=response["url"]
print(imagurl)

r = requests.get(imagurl)
name="meme."+imagurl[-3:]

with open(name,"wb") as f:
	f.write(r.content)
        


print(response)

video=mp.VideoFileClip("vid.mp4")
imag=(mp.ImageClip(name) 
    .set_duration(video.duration)
    .resize(width=280)
    .set_pos((5,40))

)
txt_clip = mp.TextClip(text, fontsize = 12, color= 'white',bg_color='black',method='caption',size=(280,73)) 
txt_clip = txt_clip.set_pos((5,imag.size[1])).set_duration(7) 
# txt_clip=txt_clip.resize(height=200)

final=mp.CompositeVideoClip([video,imag,txt_clip])
final.subclip(0).write_videofile('Thoughts! #fyp #fact #theory #interesting.mp4')
print(str(video.w) +" j "+str(video.h)+"j"+ str(imag.size[1]))

