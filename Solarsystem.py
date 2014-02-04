import numpy as np
from Planet import Planet

class Solarsystem:
	def __init__(self):
		solarmass = 1.98855e30
		self.planets = []
		self.sun = Planet(solarmass,np.zeros(2),np.zeros(2))
		self.t0 = self.t1 = 0
		self.G = 1.984e-29
		self.Gsm = self.G*self.sun.m

	def SetParams(self,dt):
		self.dt = dt
	def AddPlanet(self,mass,pos,vel):
		self.planets.append(Planet(mass,pos,vel))

	def Simulate(self):
		for planet in self.planets:
			self.t0,planet.v = self.ODESolver(self.t0,self.dt,planet.v,self.FG)
			self.t1,planet.r = self.ODESolver(self.t1,self.dt,planet.r,self.x)

	def FG(self,t,y):
		a = self.Gsm*y/(np.dot(y,y)*np.sqrt(np.dot(y,y)))
		return a

	def x(self,t,y):
		return y

	def ODESolver(self,t0,dt,y0,f):
		"RK4"
		k1 = dt*f(t0,y0)
		k2 = dt*f(t0+0.5*dt,y0+0.5*k1)
		k3 = dt*f(t0+0.5*dt,y0+0.5*k2)
		k4 = dt*f(t0+dt,y0+k3)
		return t0+dt,y0+(1./6)*(k1+2.*k2+2.*k3+k4)