#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:30:54 2019

@author: leonardo
"""


import matplotlib.pyplot as plt
import csv

x = []
_0p4 = []
_0p5 = []
_0p6 = []
_0p75 = []

err_0p4 = []
err_0p5 = []
err_0p6 = []
err_0p75 = []


sf = 1

with open('att_plotting_data.csv', 'r') as file:
    plots = csv.reader(file, delimiter=',')
    for plot in plots:
        x.append(float(plot[0]))
        _0p4.append(float(plot[1]))
        _0p5.append(float(plot[2]) * sf)
        _0p6.append(float(plot[3]))
        _0p75.append(float(plot[4]) * sf)
        
with open('errors_for_plotting.csv', 'r') as file:
    plots = csv.reader(file, delimiter=',')
    for plot in plots:
        err_0p4.append(float(plot[0]))
        err_0p5.append(float(plot[1]) * sf)
        err_0p6.append(float(plot[2]))
        err_0p75.append(float(plot[3]) * sf)
        
"""plt.errorbar(x, water_table2, yerr=water_table_error2, capsize=2, label='With water table',
             linestyle='--', c='xkcd:azure', elinewidth=1, linewidth=1)"""
        
fig1 = plt.figure()
plt.title("Attenuation Lengths of cosmic ray neutrons in a SiO_2 soil")


plt.errorbar(x[:-1], _0p4[:-1], err_0p4[:-1], label='0.4 porosity', linewidth=1, capsize=2, elinewidth=1)
plt.errorbar(x, _0p5, err_0p5, label='0.5 porosity', linewidth=1, capsize=2, elinewidth=1)
plt.errorbar(x, _0p6, err_0p6, label='0.6 porosity', linewidth=1, capsize=2, elinewidth=1)
plt.errorbar(x, _0p75, err_0p75, label='0.75 porosity', linewidth=1, capsize=2, elinewidth=1)

plt.ylabel('Attenuaiton length (cm)')
plt.xlabel('Water saturation by volume (%)')
plt.legend()
plt.grid(True)
plt.savefig('/home/leonardo/Pictures/AttenuationLengthss.png', dpi = 300)
plt.show()