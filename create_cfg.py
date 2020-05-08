import os
path='xxxxxxxxxxxxx/Data/data1/Dataseqthree'
yuv_filename=os.listdir(path)
for i,name in enumerate(yuv_filename):
    frams=name.split("_")[-1].split(".")[0]
    width=name.split("_")[-2].split("x")[0]
    height=name.split("_")[-2].split("x")[1]
    name_sub =name.split(".")[0]
    line1='#======== File I/O ===============\n'
    line2='FrameRate                     : 25          # Frame Rate per second\n'
    line3='SourceWidth                   : '+str(width)+'         # Input  frame width\n'
    line4='SourceHeight                  : '+str(height)+'         # Input  frame height\n'
    line5='FramesToBeEncoded             : '+str(frams)+'         # Number of frames to be coded\n\n'
    with open(name_sub+'.cfg','w') as f:
        f.write(line1) 
        f.write(line2)
        f.write(line3)
        f.write(line4)
        f.write(line5)   
