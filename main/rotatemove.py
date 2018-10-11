"""
Author: Armand Erasmus

This file contains the classes neccesary to move and rotate your rovers
"""
import math as mt
import setmanager

class RotateMove(setmanager.Manager):

	def rotate(self, rover_id, phi, theta):

		if ( theta == 0. ) and ( phi % (mt.pi/2) ) == 0.:
			r = self.get_rover(rover_id)
			lon, lat = r.heading
            lat += theta
            lon += phi
            r.heading = (lon, lat)
        else:
        	print 'The Rover is having some trouble rotating'

        	raise Exception ('Invalid rover rotation specified')

    def move(self, rover_id, displacement):

    	if isinstance(displacement, int) and displacement > 0:
    		r = self.get_rover(rover_id)
    		x, y, z = r.position
    		phi, theta = r.heading
    		x += int(mt.sin(theta)*mt.cos(phi))
    		y += int(mt.sin(theta)*mt.sin(phi))
    		z += int(mt.cos(theta))

    		self.check_position((x, y, z))
            r.position = (x, y, z)
            self.move(rover_id, displacement - 1)

        elif displacement < 0:
        	print 'Hmm, the Rover can only move forward'

        	raise Exception('The rover can only move forward')

        elif not isinstance(displacement, int):
        	print 'The Rover wont move in fractional ammounts'

        	raise Exception('Only integers are allowed for rover movement')