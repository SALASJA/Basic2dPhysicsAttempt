from tkinter import *
from random import *
import math
import inspect


class Ball:
	def __init__(self, canvas, name, color = "grey", x = None, y = None, radius = None): #can put defaults in here and not in if statement
		if x != None:
			self.x = x
			self.initialX = x
		else:
			self.x = 720
			self.initialX = 720
		
		if y != None:
			self.y = y
			self.initialY = y
		else:
			self.y = 150
			self.initialY = 150
			
		if radius != None:
			self.radius = radius
		else:
			self.radius = 30
		
		self.canvas = canvas
		self.name = name
		self.color = color
		self.canvas.create_oval(self.x - self.radius, self.y - self.radius, \
		                        self.x + self.radius, self.y + self.radius, \
		                        tags = self.name, fill = self.color)
	def getY(self):
		return self.y
		
	def setY(self, y):
		self.y = y
	
	def getX(self):
		return self.x
		
	def setX(self, x):
		self.x = x
	
	def getRadius(self):
		return self.radius
	
	def moveUp(self, speed = 1):
		self.setY(self.y - speed) #this can implement speed 
		
	def drawPosition(self):
		self.canvas.delete(self.name)
		self.canvas.create_oval(self.x - self.radius, self.y - self.radius, \
								self.x + self.radius, self.y + self.radius, \
								tags = self.name, fill = self.color)
	def ballDistance(self, ball):
		return math.sqrt((ball.getX() - self.getX())**2 + \
						 (ball.getY() - self.getY())**2)
						 
	def ballRadiiSum(self, ball):
		return ball.getRadius() + self.getRadius()
	
	def getMidpoint(self, ball):
		return [(ball.getX() + self.getX())/2, \
		        (ball.getY() + self.getY())/2 ]
	
	def getSlope(self, ball):
		return (ball.getY() - self.getY()) / \
		       (ball.getX() - self.getX())
	
	def getName(self):
		return self.name
	
	def new(self):
		self.x = self.initialX
		self.y = self.initialY
		
	

class GUI:
	def __init__(self):
		self.window = Tk()
		
		canvas = Canvas(self.window, height = 720, width = 1440, bg = "black")
		self.ball  = Ball(canvas, "ball", y = 690, color = "pink", radius = 30)
		self.ballList = [self.ball]
		colorList = ["red", "green", "blue"]
		for i in range(30):
			coloR = colorList[randint(0, 2)]
			randx = randint(670, 780)
			randy = randint(0, 720)
			self.ballList.append(Ball(canvas, name = chr(64 + i), color = coloR,  x = randx, y = randy))
		canvas.pack()
		
		button = Button(self.window, text = "move", command = self.move)
		reset = Button(self.window, text = "reset", command = self.reset)
		button.pack()
		reset.pack()
		
		self.window.mainloop()
	
	def reset(self):
		for i in self.ballList:
			i.new()
			i.drawPosition()
		self.window.update()
	
	def move(self):
		while self.ball.getY() - 30 >= 0: #minus 30 represents outer edge 
			self.ball.moveUp(3)
			#if self.ballDistance() < self.ballRadiiSum():
			#	distanceLeft = self.ball.getRadius() - self.ballDistance()/2
			#	midpoint = self.getMidpoint()
			#	angle = math.atan(self.getSlope())
			#	ycomponent = math.sin(angle) * distanceLeft
			#	xcomponent = math.cos(angle) * distanceLeft
			#	self.ball2.setX(self.ball2.getX() - xcomponent)
			#	self.ball2.setY(self.ball2.getY() - ycomponent) #goal now is to generalized
			#	self.ball2.drawPosition()
			
			for i in self.ballList:
				if i.ballDistance(self.ball) < i.ballRadiiSum(self.ball) and i.getName() != "ball":
					distanceLeft = self.ball.getRadius() - i.ballDistance(self.ball)/2
					midpoint = i.getMidpoint(self.ball)
					angle = math.atan(i.getSlope(self.ball))
					ycomponent = math.sin(angle) * distanceLeft
					xcomponent = math.cos(angle) * distanceLeft
					if i.getSlope(self.ball) > 0:
						i.setX(i.getX() - xcomponent)
						i.setY(i.getY() - ycomponent)
					else:
						i.setX(i.getX() + xcomponent)
						i.setY(i.getY() + ycomponent) #another case other than this two is undefined slope
					i.drawPosition()
			self.ball.drawPosition()
			print("stack: " + str(len(inspect.stack())), 1000)
			self.window.update()
			
	def ballDistance(self):
		return math.sqrt((self.ball.getX() - self.ball2.getX())**2 + \
						 (self.ball.getY() - self.ball2.getY())**2)
	
	def ballRadiiSum(self):
		return self.ball.getRadius() + self.ball2.getRadius()
	
	def getMidpoint(self):
		return [(self.ball.getX() + self.ball2.getX())/2, \
		        (self.ball.getY() + self.ball2.getY())/2 ]
	
	def getSlope(self):
		return (self.ball.getY() - self.ball2.getY()) / \
		       (self.ball.getX() - self.ball2.getX())

GUI()