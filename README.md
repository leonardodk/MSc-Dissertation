# MSc-Dissertation
Code and data sets

This repo showcases the code I wrote, along with the results and dad for my dissertation in 2019.

Simulations were run to determine how effectively cosmic ray neutrons could be used to detect underground sources of water.

Each simulation generated and tracked 3x10^5 particles and took on average 4.3 minutes tocomplete. 
Initially, each simulation was prepared and set off manually, there is more detail on this in the dissertation itself which is in this repo 
under "Dissertation_Draft_Final.pdf" on pages 15 & 16. 

It quickly became apparent several hundred simulations would need to be run and if I were to be abel to compelte them fast enough,
I would need to automate every step of the process. To achieve this, a combination ofPython and Bash scripts were written, which could run all
the required simulations back to back, cycling through all the relavent conditions which I was testing within the simualtions.

The terminal command to start the sumulation software was written in a bash file that would be called by the Python script to start the first simulation. 
After finishing, Python would then read both the Bash script and the geometry file in as plain text, edit them, before overwriting them and saving new versions.

Python would then call the new Bash script and the process would repeat until all condiitons had been tested types had been done.

A much simplified flow chart, explaining how the script works is also shown in Fig. 8, the script itself is shown in full in Appendix B.

This combination of scripts allowed for work to be done on other tasks while simulations were running and also allowed for simulations to be run when it was not
possible to be at the desk, like overnight.
