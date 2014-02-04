import numpy as np
from Solarsystem import Solarsystem

solarsystem = Solarsystem()
'''
double AU = 149597871000;       // [m]
double Gconst = 1.984e-29;      // [AU^3 kg^-1 y^-2]

double year = 31556926;         // [s]
double auy = year*1000/AU;      // converting factor between km/s to AU/year

double Msun = 1.98855e30;       // [kg]
double Mmercury = 3.30104e23;   // [kg]
double Mvenus = 4.86732e24;     // [kg]
double Mmars = 6.41693e23;      // [kg]
double Mearth = 5.97219e24;     // [kg]
double Mjupiter = 1.89813e27;   // [kg]
double Msaturn = 5.68319e26;    // [kg]
double Muranus = 8.68103e25;    // [kg]
double Mneptun = 1.0241e26;     // [kg]
double Mpluto = 1.30900e22;     // [kg]
  //                      Mass                                               x        y      vx        vy
planets[p] = new Planet(Msun,     N); planets[p] -> initial_condition(0        ,0      ,0       ,auy*13.1*Mjupiter/Msun); p++;
planets[p] = new Planet(Mmercury, N); planets[p] -> initial_condition(-Rmercury,0      ,0       ,-auy*47.9); p++;
planets[p] = new Planet(Mvenus,   N); planets[p] -> initial_condition(0        ,Rvenus ,auy*35.0,0        ); p++;
planets[p] = new Planet(Mearth,   N); planets[p] -> initial_condition(-Rearth  ,0      ,0       ,auy*29.8 ); p++;
planets[p] = new Planet(Mmars,    N); planets[p] -> initial_condition(0        ,Rmars  ,auy*24.1,0        ); p++;
planets[p] = new Planet(Mjupiter, N); planets[p] -> initial_condition(-Rjupiter,0      ,0       ,-auy*13.1); p++;
planets[p] = new Planet(Msaturn,  N); planets[p] -> initial_condition(Rsaturn  ,0      ,0       ,-9.7*auy ); p++;
planets[p] = new Planet(Muranus,  N); planets[p] -> initial_condition(Ruranus  ,0      ,0       ,6.8*auy  ); p++;
planets[p] = new Planet(Mneptun,  N); planets[p] -> initial_condition(0        ,Rneptun,-5.4*auy,0        ); p++;
planets[p] = new Planet(Mpluto,   N); planets[p] -> initial_condition(-Rpluto  ,0      ,0       ,auy*4.7  ); p++;
'''
year = 31556926
AU = 149597871000
auy = year*1000/AU
Planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uarnus","Nepune","Pluto"]
m = [3.30104e23,4.86732e24,5.97219e24,6.41693e23,1.89813e27,5.68319e26,8.68103e25,1.0241e26,1.30900e22]
r = [np.array([-0.39,0]),np.array([0,0.72]),np.array([-1.0,0]),np.array([0,1.52]),np.array([-5.2,0]),np.array([9.54,0]),np.array([19.19,0]),np.array([0,30.06]),np.array([-39.54,0])]
v = [np.array([0,-auy*47.9]),np.array([auy*35.0,0]),np.array([0,auy*29.8]),np.array([auy*24.1,0]),np.array([0,-auy*13.1]),np.array([0,-9.7*auy]),np.array([0,6.8*auy]),np.array([-5.4*auy,0]),np.array([0,auy*4.7])]
for i in range(len(Planets)):
	solarsystem.AddPlanet(m[i],r[i],v[i])

dt = 0.01

solarsystem.SetParams(dt)
# while True:
# 	if user_action:
# 		break
# 	solarsystem.Simulate()
# 	update_plot()
T = 1000
for i in xrange(T):
	solarsystem.Simulate()