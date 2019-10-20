#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


def delwrtchmodsim(text_det_pos_sim):
    subprocess.call(["rm", "det_pos_sim.sh"], shell=True)  # del .sh file

    with open("det_pos_sim.sh", "w") as file:  # open new sh file with same name
        file.write(text_det_pos_sim)  # write in altered file text

    subprocess.call(["./changemod.sh"], shell=True)  # give new .sh file correct permissions


def delwrtgeo(geo_lines):
    subprocess.call(["rm", "cosmos_surface_detector.geo"])  # del old one

    with open("cosmos_surface_detector.geo", "w") as file:  # open new one
        for line_geo in geo_lines:  # write new doc using lines
            file.write(line_geo)
#######################################################################################################
det_pos = [500, 400, 350, 300, 250, 200, 150, 100, 50, 0, -50, -100, -150,
           -200, -250, -300, -350, -400, -500]

initial = 'p500'
initial2 = '500*cm'


for i in range(len(det_pos)):
     
    subprocess.call(["./det_pos_sim.sh"], shell=True)
    
    if i == (len(det_pos)-1):
        break
    
    
    with open("det_pos_sim.sh", "r") as file:
        text = file.read()
        replacement = str(det_pos[i+1])
        
        if int(replacement) < 0:
            replacement = 'n'+replacement[1:]
        elif int(replacement) > 0:
            replacement = 'p' + replacement
        elif int(replacement) == 0:
            replacement = replacement+'cm'
       
        text = text.replace(initial, replacement, 1)
        initial = replacement
        
        
    delwrtchmodsim(text)

    
    with open("cosmos_surface_detector.geo", "r") as file:
        lines = file.readlines()
        replacement2 = str(det_pos[i+1])+'*cm'
        lines[12] = lines[12].replace(initial2, str(det_pos[i+1])+'*cm')
    
        initial2 = replacement2
        
       
    delwrtgeo(lines)
  

