#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script begins by calling CRsim.sh which sets off a simulation for 3e5 particles.
After completion,  CRsim.sh is then opened and read in as a string to a variable which
is then edited to change the name of the output ROOT file CRESTA outputs to, in
preparation for the next simulation. The old CRsim is then deleted and a new bash
script of the exact same name is created and written using the altered text. 
This new CRsim.sh is then given the correct permissions using the file chmod.sh.

Next the appropriate changes need to be made to the geometry file for the next simulation. 
This is done in a similar way to CRsim.sh; the text is read in, edited, the old file is 
deleted and a new one is written. No permission change is necessary here.

This is repeated until all required simulations have been run
"""

import subprocess  # allows python to interact with the terminal.



# Here I define some functions which will be used several times in the main body
# of my code.

# this function deletes the original CRsim.sh script,then it writes a 
# new updated script also called CRsim.sh using the text it's been passed,
# and then grants it the neccesary permissions.
def delwrtchmodCRsim(text_CRsim):
    subprocess.call(["rm", "CRsim.sh"], shell=True)  # delete old file

    with open("CRsim.sh", "w") as file:  # creates a new file with same name
        file.write(text_CRsim)  # write in updated text using text passed to function

    subprocess.call(["./changemod.sh"], shell=True)  # grant neccessary permissions


# this function deletes the old geometry file, and then writes a new updated one
# using text passed to the function permission changes are not required here
def delwrtgeo(geo_lines):
    subprocess.call(["rm", "cosmos_simple.geo"])  # delete old file

    with open("cosmos_simple.geo", "w") as file:  # create new file with same name
        for line_geo in geo_lines:  # write new doc using list of lines passed to function
            file.write(line_geo)


#
# main body of code
#

# Helow I have a list of soil thicknesses, moisture levels, and porosities used in the
# simulations. A simple substitution in the right place in CRsim.sh and the geometry file
# allows me to edit them in preparation to run them again with updated parameters.
thickness = ['10', '25', '50', '60', '75', '100', '125',
             '150', '175', '200', '225', '250', '275', '300',
             '325', '350', '375', '400', '425', '450', '475', '500',
             '525', '550', '575', '600']


mst_lvl = ["H20_0p0", "H20_0p01", "H20_0p02", "H20_0p05", "H20_0p1",
           "H20_0p2", "H20_0p3", "H20_0p4", "H20_0p5"]


porosities = ["Pore_0p5", "Pore_0p6", "Pore_0p75"]


# initial replacement variables set to the string of characters to first be 
# replaced in the files
currnt_thcknss = "10cm"  # initial thickness for substituion in  CRsim.sh
currnt_thcknss2 = "10*cm"  # initial thickness for substituion in the geo file
currnt_mst = "H20_0p0"  # initial moisture level for substituion in CRsim.sh and the geo file
currnt_por = "Pore_0p5"  #i nitial porosity  for substituion in CRsim.sh and the geo file

############################################# start of porosity loop
for i in range(len(porosities)):
    ############################################# start of saturation loop
    for j in range(len(mst_lvl)):
        ######################################### start of thicknesses loop
        for k in range(len(thickness)):
            subprocess.call(["./CRsim.sh"], shell=True)  # run simulation

            if k == (len(thickness) - 1):  # at the last one, break, as the final simulations have already run
                break

            with open("CRsim.sh", "r") as file:  # open CRsim in read mode
                text_k = file.read() # read file in as text
                nxt_thcknss = thickness[k + 1] + "cm"  # set replacement thickness to next one in the list
                
                text_k = text_k.replace(currnt_thcknss, nxt_thcknss)  # replace current thickness with next one
                currnt_thcknss = nxt_thcknss # prepare for next loop

            delwrtchmodCRsim(text_k)  # delete current CRsim.sh, write a new one and changes its permissions

            with open("cosmos_simple.geo", "r") as file: # open geometry file in read mode
                lines_k = file.readlines()  # read geometry file in as list of lines
                nxt_thcknss2 = thickness[k + 1] + '*cm'  
                lines_k[8] = lines_k[8].replace(currnt_thcknss2, nxt_thcknss2)  # replace correct bit with next bit

                currnt_thcknss2 = nxt_thcknss2

            delwrtgeo(lines_k)  # deletes current geo and writes new one

        ########################################## end of thicknesses loop

        if j == (len(mst_lvl) - 1):
            break

        with open("CRsim.sh", "r") as file:
            text_j = file.read()
            nxt_thcknss = "10cm"  
            text_j = text_j.replace(currnt_thcknss, nxt_thcknss)  # reset thickness in file name to 10cm
            currnt_thcknss = nxt_thcknss  

            
            nxt_mst = mst_lvl[j + 1]
            text_j = text_j.replace(currnt_mst, nxt_mst)

        delwrtchmodCRsim(text_j)  

        with open("cosmos_simple.geo", "r") as file:
            lines_j = file.readlines()

            nxt_thcknss2 = "10*cm"  
            lines_j[8] = lines_j[8].replace(currnt_thcknss2, nxt_thcknss2) # reset thickness in file name to 10cm

            currnt_thcknss2 = nxt_thcknss2  

            lines_j[39] = lines_j[39].replace(currnt_mst, nxt_mst)
            currnt_mst = nxt_mst

        delwrtgeo(lines_j)  
    ############################################### end of saturation loop

    if i == (len(porosities) - 1):
        break

    with open("CRsim.sh", "r") as file:
        text_i = file.read()
        nxt_thcknss = "10cm"
        nxt_mst = "H20_0p0"  

        text_i = text_i.replace(currnt_thcknss, nxt_thcknss)
        currnt_thcknss = nxt_thcknss

        text_i = text_i.replace(currnt_mst, nxt_mst)

        nxt_por = porosities[i + 1]
        text_i = text_i.replace(currnt_por, nxt_por)  # change the porosity to the next one along

    delwrtchmodCRsim(text_i)

    with open('cosmos_simple.geo', 'r') as file:
        lines_i = file.readlines()
        nxt_thcknss2 = "10*cm"

        lines_i[8] = lines_i[8].replace(currnt_thcknss2, nxt_thcknss2)  

        currnt_thcknss2 = nxt_thcknss2  # reprimes curret2

        lines_i[39] = lines_i[39].replace(currnt_mst, nxt_mst) 
        currnt_mst = nxt_mst  # moves current along one

        lines_i[39] = lines_i[39].replace(currnt_por, nxt_por)  
        currnt_por = nxt_por  # moves current along one

    delwrtgeo(lines_i)

    ############################################### end of porosity loop

