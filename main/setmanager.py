"""
Author: Armand Erasmus

This file is the code used for managing your rovers. 
	It has the classes of SetRover and Manager
"""

import math as mt

class SetRover(object):

    def __init__(self, position, heading):
    	self.position = position
        self.heading = heading

    def get_heading(self):
    	return self._heading

    def get_position(self):
    	return self._position

    def set_heading(self, heading):
    	if isinstance(heading, tuple) and len(heading) == 2:
    		self._heading = (heading[0] % (2*mt.pi), heading[1] % (2*mt.pi))
    	else:
    		print 'Unexpect Heading'

    		raise ValueError('The heading needs a lengt of 2')

    def set_position(self, position):
    	if isinstance(position, tuple) and len(position) == 3:
    		self._position = position
    	else:
    		print 'Unexpected Position'

    		raise ValueError('The position needs a length of 3')

    position = property(get_position, set_position, None)
    heading = property(get_heading, set_heading, None)

class Manager(object):

    def __init__(self, corner):
    	self.rovers = {}
    	self.corner = corner

    def get_rover(self, rover_id):

    	if not rover_id in self.rovers.keys():
    		print 'Oh no! You seem to have lost a rover'

    		raise Exception ('We cannot find your rover')

    	else:
            return self.rovers[rover_id]

    def check_position(self, position):

    	if not isinstance(position, tuple) and len(corner) == 3:
    		print 'The Rover Position was Unexpected'

    		raise Exception('Rover position has the wrong shape')

    	if not (isinstance(position[0], int) and isinstance(position[1], int) 
            and isinstance(position[2], int)):

    		print 'Looks like the rover position is not an integer'

    		raise Exception('Rovers position is fractional')

    	if not self.available_position(position):
    		print 'Your rover is already in that position'

    		raise Exception('The rover is already in that position')

    	elif not self.rover_inside_grid(position):
    		pos2D = position[:2]
    		print 'Warning!!! The Rover is Outside the Grid'

    		raise Exception('The rover is outside the grid')

    def add_rover(self, rover_id, position, heading):

    	self.check_position(position)

    	if not rover_id in self.rovers.keys():
    		self.rovers[rover_id] = SetRover(position, heading)
    	else:
    		print 'A Rover with that ID already exists'

    		raise Exception ('That Rover ID is taken already')

    def rover_inside_grid(self, position):

    	x, y, z = position

    	x1 = self.corner[0][0] ; x2 = self.corner[1][0]
    	y1 = self.corner[0][1] ; y2 = self.corner[1][1]
    	z1 = self.corner[0][2] ; z2 = self.corner[1][2]

    	return (True if ( (x1 <= x <= x2 or x2 <= x <= x1) and 
                          (y1 <= y <= y2 or y2 <= y <= y1) and
                          (z1 <= z <= z2 or z2 <= z <= z1) ) 
                else False)

    def available_position(self, position):

    	return (False if position in [r.position for r in self.rovers.values()] 
                else True)

    def get_corner(self):
    	return self._corner

    def set_corner(self, corner):

    	if isinstance(corner, tuple) and len(corner) == 2:
            if (isinstance(corner[0], tuple) and len(corner[0]) == 3 and 
                isinstance(corner[1], tuple) and len(corner[1]) == 3):
                self._corner = corner

            else:
            	print 'Unexpected corner provided'

            	raise Exception('The Corner length is incorrect')

        else:
        	print 'Unexpected corner provided'

            raise Exception('The Corner length is incorrect')

    corner = property(get_corner, set_corner, None)






