import moviepy.editor as mp
import os

#using movepy, convert each gif to an mp4 video with the same name

for file in os.walk('.'):
    for f in file[2]:
        if f.endswith('.gif'):
            clip = mp.VideoFileClip(f)
            clip.write_videofile('videos/' + f.replace('.gif', '.mp4'))