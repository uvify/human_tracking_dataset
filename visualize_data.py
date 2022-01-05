
import glob
from os import truncate

import cv2 as cv
import re
import random
import argparse

from pandas.core import frame

parser = argparse.ArgumentParser()
parser.add_argument('--dir' , help='root directroy path')
parser.add_argument('--type', help='data type (train < 450) , (test >= 450)')
parser.add_argument('--seq' , help='sequence number')


args = parser.parse_args()
seq_path = args.dir + "/" + args.type + "/sequence_" + ("%05d" % int(args.seq))

txt_files = glob.glob(seq_path + '/**/*.txt', recursive=True)
img_files = glob.glob(seq_path + '/**/*.png', recursive=True)

img_files = sorted(img_files)
id_color_map = dict()

def get_pick_color(model):
    model_id = model
    r = int(model_id/(256**3))
    g = int(model_id%(256**3)/(256**2))
    b = int(model_id%(256**2)/256)
    a = int(model_id%256)
    return (r, g, b, a)


cv.namedWindow("win")

f = open(txt_files[0] , 'r')
lines = f.readlines()

regex = re.compile(r'\d+.png')

i  = 0
while True:
    
    mat = cv.imread(img_files[i])

    path_tokens = img_files[i].split(sep="/")

    sub_string = '/'.join(path_tokens[-5:-1])
    
    img_file_name = path_tokens[-1]
    frame_number = int(re.search(r"(\d+).png",img_file_name).group(1))
    
    for line in lines:
        line = line.strip()
        line_tokens = line.split(',')
        if(frame_number == int(line_tokens[0])):
            box_top_left_x = int(line_tokens[3])
            box_top_left_y = int(line_tokens[4])
            box_width = int(line_tokens[5])
            box_hegiht = int(line_tokens[6])


            person_id  = "person id: " + line_tokens[1]
            tracking_id = "tracking id: " + line_tokens[2]
            is_valid = "is_valid: " + line_tokens[7]            
            pose_class = "pose_class: " + line_tokens[8]
            occlusion = "occlusion: " + line_tokens[9]
            truncated = "truncated: "+ line_tokens[10]
            visibiltiy = "visibility: "+ line_tokens[11]
            
            try:
                color = id_color_map[line_tokens[1]]
            except KeyError:
                color  = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                id_color_map[line_tokens[1]] = color

            cv.rectangle(mat, (box_top_left_x, box_top_left_y), (box_top_left_x+box_width, box_top_left_y+box_hegiht), color, 3)
            cv.putText(mat, person_id, (box_top_left_x+10 + box_width, box_top_left_y+ 10)  ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, tracking_id, (box_top_left_x+10 + box_width, box_top_left_y + 25) ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, is_valid, (box_top_left_x+10 + box_width, box_top_left_y+ 40)  ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, pose_class, (box_top_left_x+10 + box_width, box_top_left_y + 55) ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, occlusion, (box_top_left_x+10 + box_width, box_top_left_y + 70) ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, truncated, (box_top_left_x+10 + box_width, box_top_left_y + 85) ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)
            cv.putText(mat, visibiltiy, (box_top_left_x+10 + box_width, box_top_left_y + 100) ,cv.FONT_HERSHEY_COMPLEX, 0.4, color, 1, cv.LINE_AA)


            cv.putText(mat, line_tokens[0] ,(30,30), cv.FONT_HERSHEY_COMPLEX, 1.0 , (255,255,255), 1, cv.LINE_AA)

    


    cv.imshow("win", mat)  
    key = cv.waitKey(0)
    if(key == 27 or key == 113):
        exit()

    elif(key==112 or key == 81):
        if(i >1 ):
            i = i-1

    else:
        i = i+1

    
