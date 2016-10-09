#!/usr/bin/env python3

import numpy as np
import pandas as pd
from abscplane import AbsComplexPlane



class ComplexPlaneNP(AbsComplexPlane):
	"""Abstract subclass that inherit from base class AbsComplexPlane for complex plane.
    
    A complex plane is a 2D grid of complex numbers, having
    the form (x + y*1j), where 1j is the unit imaginary number in
    Python, and one can think of x and y as the coordinates for
    the horizontal axis and the vertical axis of the plane, 
    respectively. Recall that (1j)*(1j) == -1. Also recall that 
    the FOIL rule for multiplication still works:
		(x + y*1j)*(v + w*1j) = (x*v - y*w + (x*w + y*v)*1j)
    You can check these results in an interpreter.
    
    In addition to generating the 2D grid of numbers (x + y*1j),
    we wish to easily support transformations of the plane with
    an arbitrary function f. Done properly, the attribute self.plane
    should store a 2D grid of numbers f(x + y*1j) such that the
    parameter x ranges from self.xmin to self.xmax with self.xlen
    total points, while the parameter y ranges from self.ymin to
    self.ymax with self.ylen total points. By default, the function
    f should be the identity function (lambda x : x), which does 
    nothing to the bare complex plane.
	"""
	def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen,plane=pd.DataFrame(), f=lambda x: x):
		"""
		Attributes:
		xmax (float) : maximum horizontal axis value
		xmin (float) : minimum horizontal axis value
		xlen (int)   : number of horizontal points
		ymax (float) : maximum vertical axis value
		ymin (float) : minimum vertical axis value
		ylen (int)   : number of vertical points
		plane        : stored complex plane implementation
		f    (func)  : function displayed in the plane
		""" 
		
		self.xmin = xmin
		self.xmax = xmax
		self.xlen = xlen
		self.ymin = ymin
		self.ymax = ymax
		self.ylen = ylen
		self.plane = plane 
		self.f = f

	def refresh(self):
		"""
		Regenerate complex plane.
		For every point (x + y*1j) in self.plane, replace
		the point with the value self.f(x + y*1j). 
		"""
		x = np.linspace(self.xmin, self.xmax, self.xlen)  #np.linspace(start, end, total points)
		y = np.linspace(self.ymin, self.ymax, self.ylen)
		for row in np.arange(self.xlen):				  #np.arange(num) will produce integers from 0 to num-1, same as range()
			self.plane[row]=pd.DataFrame({'points': self.f(x[row]+y*1j)})	
			#pd.DataFrame({'value': v, 'index': i}), it produce a dictionary, which include indexes and values.At here I omited the index.

		return 0

	def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
		"""
		Reset self.xmin, self.xmax, and/or self.xlen.
		Also reset self.ymin, self.ymax, and/or self.ylen.
		Zoom into the indicated range of the x- and y-axes.
		Refresh the plane as needed.
		"""
		self.xmin = xmin
		self.xmax = xmax
		self.xlen = xlen
		self.ymin = ymin
		self.ymax = ymax
		self.ylen = ylen
 
		self.refresh()
		return 0

	def set_f(self,f):
		"""
		Reset the transformation function f.
		Refresh the plane as needed.
		"""
		self.f = f
		self.refresh()
		return 0

def julia(c,max=100):
	'''
	input: complex parameter c and an optional positive integer max, return a the result of function func():
	In func(), when the absolute value of z(z=z^2+c) is greater than 2, then return 1. when it exceed max times, return 0. Otherwise, it returns the times of loop. 
	'''
	def func(z):
		n=0
		if np.absolute(z)>2:
			return 1
		while np.absolute(z)<=2:
			n=n+1
			z=z**2+c
			if n >= max:
				n=0
				break
		return n
	return func


'''
#test
p1=ComplexPlaneNP(1,2,3,4,6,4)
p1.refresh()
print(p1.plane)
'''

def test_julia1():
	'''
	test function julia. c=-1.037 + 0.17j, z=-1.00-0.2j
	'''
	f1 = julia( -1.037 + 0.17j )
	expected = 0
	computed = f1(-1.00-0.2j)
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_julia2():
	'''
	test function julia. c=-1.037 + 0.17j, z=-1.01 - 0.2j
	'''
	f1 = julia( -1.037 + 0.17j )
	expected = 20
	computed = f1(-1.01 - 0.2j)
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_julia3():
	'''
	test function julia. c=-1.037 + 0.17j, z=-1.02 - 0.2j
	'''
	f1 = julia( -1.037 + 0.17j )
	expected = 13
	computed = f1(-1.02 - 0.2j)
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

def test_julia4():
	'''
	test function julia. c=-1.037 + 0.17j, z=-1.03 - 0.2j
	'''
	f1 = julia( -1.037 + 0.17j )
	expected = 10
	computed = f1(-1.03 - 0.2j)
	success = computed == expected
	message = 'Computed %s, expected %s' % (computed, expected)
	assert success, message

test_julia1()
test_julia2()
test_julia3()
test_julia4()
