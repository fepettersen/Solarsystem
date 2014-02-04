import Planet

class Solarsystem:
	def __init__(self):
		self.planets = []

	def AddPlanet(self,mass,pos,vel):
		self.planets.append(Planet(mass,pos,vel))

	def Simulate(self):
		for planet in self.planets:
			planet.v = self.ODESolver(t0,dt,planet.v,self.FG)
			planet.r = self.ODESolver(t0,dt,planet.r,self.x)

	def FG(self,t,y):
		pass

	def x(self,t,y):
		pass

	def ODESolver(self,t0,dt,y0,f):
		"RK4"
		k1 = dt*f(t0,y0)
		k2 = dt*f(t0+0.5*dt,y0+0.5*k1)
		k3 = dt*f(t0+0.5*dt,y0+0.5*k2)
		k4 = dt*f(t0+dt,y0+k3)
		return t0+dt,y0+(1./6)*(k1+2.*k2+2.*k3+k4)