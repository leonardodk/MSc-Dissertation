//----------------
// Bar definitions
{
  name: "VARIABLE",
  index: "simconstants",
  world_box_width: "20.0*m",
  world_box_length: "20.0*m",
  world_box_depth: "15.0*m",
  water_thickness_target: "500*cm", //change this one 
  water_thickness_det: "450*cm", // ~0.5% still get through
} //10

// --------------------------------------------------
// Detector
{
  name: "DETECTOR",
  index: "scintillator",
  type: "scintillator"
}

// --------------------------------------------------- 20
// World Geometry
// Then air and carbon base
{
  name: "GEO",
  index: "world",
  material: "G4_AIR",
  size: ["world_box_length", "world_box_width", "world_box_depth"],
  type: "box",
  color: [0.9,0.9,0.99,0.9],
  drawstyle: "solid", //30
  force_auxedge: 5,
}

{
  name: "GEO",
  index: "particles_target",
  type: "box",
  mother: "world",
  material: "SiO2_Air_Pore_0p5_H20_0p0",// change this, find in /home/leonardo/Code/cosmicraysim/data/materials 39
  size: ["world_box_length", "world_box_width", "water_thickness_target"],
  position: ["0.0","0.0","0.0"],
  color: [0.694,0.619,0.369,0.9],
  drawstyle: "solid",
  force_auxedge: 1
}

{
  name: "GEO",
  index: "det",
  type: "box",
  mother: "world",
  material: "G4_WATER",
  size: ["world_box_length", "world_box_width", "water_thickness_det"],
  position: ["0.0","0.0","-0.5*water_thickness_target-0.5*water_thickness_det-10*cm"],
  color: [0.2,0.2,1.0,0.8],
  drawstyle: "solid",
  sensitive: "scintillator",
  force_auxedge: 1
}




{
  name: "FLUX",
  index: "source_box",
  size: ["world_box_length", "world_box_width", "1.*mm"],
  position: ["0.0","0.0","0.5*world_box_depth-2*mm"]
}

// Target for the main detector stack
{
  name: "FLUX",
  index: "target_box_0",
  size: ["world_box_length", "world_box_width", "1.*mm"], //  size: ["20*m","20*m","1*mm"],
  position: ["0.0","0.0","0.0"],

}
