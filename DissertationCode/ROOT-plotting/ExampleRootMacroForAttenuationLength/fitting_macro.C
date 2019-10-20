// this is a file for experimenting with root
// Here I am fitting a line to y data to get some numbers

{

g = new TGraph("H20_0p4.txt");
// create a new graph called "g" from data in data2.txt
// this is for SiO2_Air_Pore_0p5_H20_0p0 from 10cm depth to 600cm depth

g->SetTitle("Neutron count vs soil thickness - dry SiO2 soil, 0.4 porosity;Thickness of soil (cm); Number of neutrons passing through soil");
g->SetMarkerStyle(8); //set to circles
g->SetMarkerSize(0.9); // nice size



f = new TF1("f", "[0]*e^(-x/[1])", 10, 600);
//create a new line called "f" which we will fit to g

f->SetParameter(1, 20); 
//intialise second parameter to 20 

f->SetParLimits(1, 1, 1000); //set second parameter limits to 1 and 1000, not too large and not negative

f->SetParameter(0, 250000);
f->SetParLimits(0, 1, 300000);


g->Fit(f);
//fit f to g


g->Draw("AP");
//draw
}
