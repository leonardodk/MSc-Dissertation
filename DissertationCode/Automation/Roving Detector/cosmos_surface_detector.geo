//----------------
// Bar definitions
{
  name: "VARIABLE",
  index: "simconstants",
  source_size: "30.0*m",
  world_box_width: "40.0*m",
  world_box_length: "40.0*m",
  world_box_depth: "15.0*m",
  water_thickness_target: "550*cm", 
  thickness_det: "100.0*cm", 
  acquifer_depth: "100.0*cm" ,
  detector_y_pos: "-500*cm"
}

// --------------------------------------------------
// Detector
{
  name: "DETECTOR",
  index: "scintillator",
  type: "scintillator"
}

// ---------------------------------------------------
// World Geometry
// Then air and carbon base
{
  name: "GEO",
  index: "world",
  material: "G4_AIR",
  size: ["world_box_length", "world_box_width", "world_box_depth"],
  type: "box",
  color: [0.9,0.9,0.99,0.9],
  drawstyle: "solid",
  force_auxedge: 1,
}

{
  name: "GEO",
  index: "particles_background",
  type: "box",
  mother: "world",
  material: "SiO2_Air_Pore_0p5_H20_0p0",// change this, find in /home/leonardo/Code/cosmicraysim/data/materials
  size: ["world_box_length", "world_box_width", "water_thickness_target"],
  position: ["0.0","0.0","-0.5*world_box_depth+0.5*water_thickness_target"],
  color: [0.99,0.88,0.21,0.3],
  drawstyle: "solid",
  force_auxedge: 1
}

{
  name: "GEO",
  index: "particles_target_acquifer",
  type: "box",
  mother: "particles_background",
  material: "G4_WATER",
  size: ["world_box_length", "5.0*m", "50.0*cm"],
  position: ["0.0","0.0","0.5*water_thickness_target-0.5*50.0*cm-acquifer_depth"],
  color: [0.1,0.1,1.0,0.8],
  drawstyle: "solid",
  force_auxedge: 1
}



{
  name: "GEO",
  index: "det",
  type: "box",
  mother: "world",
  material: "G4_BENZENE", //material: "G4_PLASTIC_SC_VINYLTOLUENE",
  size: ["thickness_det", "thickness_det", "thickness_det"],
  position: ["0.0","detector_y_pos","-0.5*world_box_depth+0.5*thickness_det+water_thickness_target+10.0*cm"],
  color: [0.99,0.3,1.0,0.8],
  drawstyle: "solid",
  sensitive: "scintillator",
  force_auxedge: 1
}
//+0.5*water_thickness_target+0.5*thickness_det+10*cm+



{
  name: "FLUX",
  index: "source_box",
  size: ["source_size", "source_size", "1.*mm"],
  position: ["0.0","0.0","0.5*world_box_depth-2*mm"]
}

// Target for the main detector stack
{
  name: "FLUX",
  index: "target_box_0",
  size: ["world_box_length", "world_box_width", "1.*mm"], //  size: ["20*m","20*m","1*mm"],
  position: ["0.0","0.0","0.0"],

}
