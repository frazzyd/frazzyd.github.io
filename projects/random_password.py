# Script:    passwordgenerator.py
# Desc:      Create a random password of a given length.
# Author:    Fraser Dumayne
# Created:   12/09/2014
# Updated:   04/01/2017 - Added boilerplate and main
######################################################################################################

import random, sys

# Create string with possible characters
passChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz0123456789!?_-@£$%^&*+="

def passCreate(passLength):
	
	password = [] # Create empty list
	
	for character in range(passLength): # Loop based on size given by user
		password.append(random.choice(passChars)) # Choose a random character from passChars and add to the empty list
	print ''.join(password) # Print the password by joining every item in the list into a string
	
	return password

def main():
	sys.argv.append(12)
	
	if len(sys.argv) != 2:
		print 'Please input the length of password you would like'
		return
		
	passCreate(sys.argv[1])

if __name__ == '__main__':
	main()

