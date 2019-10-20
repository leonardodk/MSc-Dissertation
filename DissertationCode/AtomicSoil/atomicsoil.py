#!/usr/bin/env python3
"""
This script takes a user entered soil porosity and saturation level and returns the atomic
masses per cm^3 and mass fractions for each element present. Density is done in cm^3
and all volumes are 1cm^3 which allows for easy calculations of density as they are
effectively the same.

Only one soil composition was needed for this research but the use of dictionaries allows for
easy expansion to more soil types.

"""
Av = 6.02e23
# avogadros constant

Mr = {'H': 1, 'C': 12, 'N': 14, 'O': 16, 'Si': 28, 'Ar': 40}
# Mrs of relevant elements

rho = {'H20': 1, 'SiO2': 2.65}
# densities of relavent materials in g/cm^3

ppcm3Air = {'N': 4.1925e19, 'O': 1.1314e19, 'Ar': 2.5531e17, 'C': 1.3438e16}
# particles per cm^3 in air, calculated by hand assuming 1 mole of any gas occupies 22.4dm^3
# at rtp, and that the atmosphere is 78% Nitrogen gas (N2), 21% oxygen gas (O2), 0.95% Argon
# gas, 0.05% carbon dioxide CO2 gas


# this determines how much of the volume is empty space
porosity = float(input('Please enter a porosity in the form.\n'
                       '0.XXX...: '))

print(porosity)
# how much of the empty space is to be filled by water
saturation = float(input('How saturated is this soil (%): \n'
                         'Please enter a number percentage between 0 and 100: ')) / 100

print(saturation)

# work out how much volume the air, water and soil each has
total_vol = 1  # cm3
vol_space = (total_vol * porosity)
vol_solid = total_vol - vol_space
vol_H2O = (vol_space * saturation)
vol_air = vol_space - vol_H2O

# prints out volumes of air, water and soil (solid)
print('\n\nthis gives us:\n'
      '\t :-\t {0}cm3 air/cm3\n'  #
      '\t :-\t {1}cm3 water/cm3\n '
      '\t :-\t {2}cm3 SiO2\n\n'.format(vol_air, vol_H2O, vol_solid))

# masses of each elemeent in air
mass_N = (vol_air * ppcm3Air['N']) / Av * Mr['N']
mass_O_air = (vol_air * ppcm3Air['O']) / Av * Mr['O']
mass_Ar = (vol_air * ppcm3Air['Ar']) / Av * Mr['Ar']
mass_C = (vol_air * ppcm3Air['C']) / Av * Mr['C']


# masses of elements in water
massH = vol_H2O * (2 / 18)  # water is 2/18ths H by mass
massO_H2O = vol_H2O * (16 / 18)  # water is 16/18ths by mass

# masses of elements in soil
moles_solid = (vol_solid * rho['SiO2']) / (Mr['Si'] + (Mr['O'] * 2))
mass_Si = moles_solid * Mr['Si']
mass_O_solid = moles_solid * 2 * Mr['O']

total_mass_O = mass_O_air + massO_H2O + mass_O_solid

totalM = massH + total_mass_O + mass_N + mass_Si + mass_Ar + mass_C

masses = [massH, total_mass_O, mass_Si, mass_N, mass_Ar, mass_C]
elements = ['H', 'O', 'Si', 'N', 'Ar', 'C']

for i in range(len(masses)):
    if i == 0:
        print('This makes the soil:')
        print('\t {0:.3}g {1} atoms; mass fraction {2:.5}'.format(masses[i], elements[i], masses[i] / totalM))
    else:
        print('\t {0:.3}g {1} atoms; mass fraction {2:.5}'.format(masses[i], elements[i], masses[i] / totalM))

print(totalM) # prints total mass which is also the density as everything is done by cm3