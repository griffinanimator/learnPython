 import math

 class Circle(object):  # New style class
 	'An advanced cirle analytic toolkit'

 	version = '0.1'				# class variable

 	def __init__(self, radius):
 		self.radius = radius   # instance variable
 		# self is your instance.  an initializer

	# Method
	def area(self):
		' Perform a quadature on a shape of uniform radius'
		return math.pi * self.radius ** 2.0

	def perimeter(self):
		return 2.0 * math.pi * self.radius










# Tutorial

print 'Circuituous version', Circle.version
c = Circle(10)
print 'A circle of radius', c.radius
print 'has an area of', c.area()
print


# Example use 1

seed(8675309)
print 'Using Circuituous(tm) version', Circle.version
n = 10
circles [Circle(random()) for i in xrange(n)]
print 'The average area of', n, 'random circles'
avg = sum([c.area() for c in circles]) / n
print 'is %.1f' % avg
print

# Example use 2
cuts = [0.1, 0.7, 0.8]
circles = [Circle(r) for r in cuts]
for c in circles:
	print 'A circle with a radius of', c.radius
	print 'has a paremeter of', c.perimeter()
	print 'an a cold area of'. c.area()
	c.radius *= 1.1
	print 'and a warm area of', c.area()
	print
	

