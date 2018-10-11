"""
Author: Armand Erasmus

	This is the main file for the Mars Rover Coding Problem.

	This will contain:

		- The main Class - main_MarsRvr
		- The main() function

"""

import math as math
import os
import sys
import rotatemove 

class main_MarsRvr(object):
	
	#This is the dictionary that would handle rover headings. They will be related to North, East, South and West.
	Headings = {'N':mt.pi/2, 'S':3*mt.pi, 'E':0, 'W':mt.pi}

	#The allowed rover commands array(Rover Language if you will):
	#L for Left
	#R for Right
	#M for Movement
	Commands = ['L', 'R', 'M']

	def __init__(self):
		
		self.commander = None
		self.Commands = []
		self.rovers = []

	def welcomeScreen(self):

		print '     '
		print '*' *40
		print '*'
		print '* 	WELCOME TO THE MARS ROVER COMMAND CENTRE	'
		print '*'
		print '*' *40
		print '		'

		print 'The Rovers uderstand the following'
		print 'Headings'
		print 'N - North'
		print 'S - South'
		print 'E - East'
		print 'W - West'
		print '			'
		print 'Commands'
		print 'L - Left'
		print 'R - Right'
		print 'M - Movement'

	def  move(self, rover_id):
		self.commander.move(rover_id, 1)

	def L_rotate(self, rover_id):
		self.commander.rotate(rover_id, mt.pi/2, 0)

	def R_rotate(self, rover_id):
		self.commander.rotate(rover_id, -mt.pi/2, 0)

	def input_parser(self, input):

		input = input.split('\n')
		corner = self.corner_parser(input[0])
		self.commander = rotatemove.RotateMove(((0, 0, 0),corner))

		for line in input[1::2]:
			self.parse_add_rover(line)

		for line in input[2::2]:
			self.instruction_parser(line)

	def instruction_parser(self, input):
		self.Commands.append([strg for strg in input.strip()])

	def corner_parser(self, corner):

		try:
			return tuple([int (uc) for uc in corner.strip().split('  ')] + [0])

		except Exception, e:
			print 'Whoops, seems like the corner hasnt been correctly specified :('
			raise Exception ('Corner must be a pair of integers')

	def controller_heading_check(self, heading_val):

		if not heading_val in self.Headings.values:
			print 'Hmmm, the Rover does not understand what you were trying to do there'

			raise Exception ('Controller heading incorrect')

		else:
			for heading_key in self.Headings.keys():
				if self.Headings[heading_key] == heading_val:
					return heading_key

	def heading_checker(self, heading):

		if not heading in self.Headings.keys();
			print 'The Rover doesnt seem to think that heading is valid'

		raise Exception ('The Heading provided by the user is not valid')

	else:
		return self.Headings[heading]

	def parse_add_rover(self, input):

		#This will give you more rovers

		rover = input.strip().split(' ')
		rover[2] = rover[2].upper()

		if len(rover) == 3:
			try:
				position = tuple([int(v) for v in rover[0:2]] + [0])

			except ValueError:
				print '		The Rover Position has not been correctly specified	'

			raise ValueError('Rover has been incorrectly positioned')

		heading = (self.heading_checker(rover[-1]), mt.pi/2)
			self.commander.add_rover(input, position, heading)
			self.rovers.append(input)

		elif len(rover) <> 3:
			print 'Oh no, the rover has not been correctly specified'

			raise Exception('Confirm coordinates and heading')

	def dispatch_input(self):
		for rover, Commands in zip(self.rovers, self.Commands):
			for instruction in Commands:
				if instruction == 'L':
					self.L_rotate(rover)
				elif instruction == 'R':
					self.R_rotate(rover)
				elif instruction == 'M':
					self.move(rover)
				else:
					print 'Incorrect instruction, the rover has no idea what you want it to do'

					raise Exception ('Incorrect Instruction')

	def display_output(self):
		output = ""

		for rover in self.rovers:
			r = self.commander.get_rover(rover)
			heading = self.controller_heading_check(r.heading[0])
			output += '%d %d %s\n' % (r.position[0], r.position[1], heading)

		return output

	def main():
		os.system('clear')

		dispatcher = main_MarsRvr()
		dispatcher.welcomeScreen()

		raw_input("Press enter to begin the mission...")

		os.system('clear')

		input = ''

		print 'Please provide upper-right grid corner as a pair'
		print 'Something like: 4 4'

		corner = raw_input('Enter upper-right corner of grid  (X Y): ')

		input += corner + '\n'

		while(True): 
			print 'Please enter rover position and heading,'  
			print 'Something like 1 2 N OR 3 3 E'
			print ' '
			print 'If you have already entered at least one set'
			print 'of position and heading you can hit enter to'
			print 'see final position of rovers. Otherwise,'
			print 'you can add more rovers, more rovers always = more fun'

			r = raw_input('Enter (xCoord yCoord Headg.):')

			if r == '':
				break
			else:
				input += r + '\n'

			print 'Time to give your rovers some commands'
			print 'Eg - LMLMLMLMM OR MMRMMRMRRM'

			Commands = raw_input('Enter commands for this rover:').upper()
			input += Commands + '\n'

			if input[-1] == '\n':
				input = input[:-1]
			else:
				input = input

			dispatcher.input_parser(input)
			dispatcher.dispatch_input()
			os.system('clear')

			print 'Your Final Rover(s) Position(s)'
			print dispatcher.display_output()

	if __name__ == '__main__':
	main()