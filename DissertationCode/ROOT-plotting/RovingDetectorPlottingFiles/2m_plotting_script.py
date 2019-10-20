#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:08:03 2019

@author: leonardo
"""

import matplotlib.pyplot as plt
import csv

x = []
water_table = []
water_table_error = []

no_water_table = []
no_water_table_err = []

sf = 1

with open('LT1mev.csv', 'r') as file:
    plots = csv.reader(file, delimiter=',')
    for plot in plots:
        x.append(float(plot[0]))
        water_table.append(float(plot[1]))
        water_table_error.append(float(plot[2]) * sf)
        no_water_table.append(float(plot[3]))
        no_water_table_err.append(float(plot[4]) * sf)
        
fig1 = plt.figure()
plt.title("Neutron counts at y positions with E < 1MeV")

plt.errorbar(x, water_table, yerr=water_table_error, capsize=2, label='With water table', 
             linestyle='--', c='navy', elinewidth=1, linewidth=1)
plt.errorbar(x, no_water_table, yerr=no_water_table_err, capsize=2, label='No water table',
             c='xkcd:coral', elinewidth=1, linewidth=1)

plt.ylabel('Counts of Neutrons with energy <1MeV')
plt.xlabel('y-position (cm)')
plt.axvspan(-250, 250, facecolor='k', alpha=0.2)


plt.legend()
plt.grid(True)
plt.savefig('/home/leonardo/Pictures/2m_LT_1p0_extended_wErrors.png', dpi = 300)
plt.show()

###############################################################################################
water_table2 = []
water_table_error2 = []

no_water_table2 = []
no_water_table_err2 = []


    
with open('LT0p1mev.csv', 'r') as file:
    plots2 = csv.reader(file, delimiter=',')
    for plot2 in plots2:
        water_table2.append(float(plot2[1]))
        water_table_error2.append(float(plot2[2]) * sf)
        no_water_table2.append(float(plot2[3]))
        no_water_table_err2.append(float(plot2[4]) * sf)
        
fig2 = plt.figure()
plt.title("Neutron counts at y positions with E < 0.1MeV")
plt.errorbar(x, water_table2, yerr=water_table_error2, capsize=2, label='With water table',
             linestyle='--', c='navy', elinewidth=1, linewidth=1)
plt.errorbar(x, no_water_table2, yerr=no_water_table_err2, capsize=2,
             label='No water table', c='xkcd:coral', elinewidth=1, linewidth=1 )
plt.ylabel('Counts of Neutrons with energy <0.1MeV')
plt.xlabel('y-position (cm)')

plt.axvspan(-250, 250, facecolor='k', alpha=0.2)

plt.legend()
plt.grid(True)
plt.savefig('/home/leonardo/Pictures/2m_LT_0p1_extended__wErrors.png', dpi = 300)

plt.show()


###############################################################################################
water_table3 = []
water_table_error3 = []

no_water_table3 = []
no_water_table_err3 = []


    
with open('LT0p05mev.csv', 'r') as file:
    plots3 = csv.reader(file, delimiter=',')
    for plot3 in plots3:
        water_table3.append(float(plot3[1]))
        water_table_error3.append(float(plot3[2]) * sf)
        no_water_table3.append(float(plot3[3]))
        no_water_table_err3.append(float(plot3[4]) * sf)
        
fig3 = plt.figure()
plt.title("Neutron counts at y positions with E < 0.05MeV")
plt.errorbar(x, water_table3, yerr=water_table_error3, capsize=2, label='With water table',
             linestyle='--', c='navy', elinewidth=1, linewidth=1)
plt.errorbar(x, no_water_table3, yerr=no_water_table_err3, capsize=2,
             label='No water table', c='xkcd:coral', elinewidth=1, linewidth=1 )
plt.ylabel('Counts of Neutrons with energy <0.05MeV')
plt.xlabel('y-position (cm)')

plt.axvspan(-250, 250, facecolor='k', alpha=0.2)

plt.legend()
plt.grid(True)
plt.savefig('/home/leonardo/Pictures/2m_LT_0p05_extended__wErrors.png', dpi = 300)

plt.show()


