# Script to print starts pattern
'''
    *
  * *
* * *
'''
import sys

def triangle_stars(lines=5 ):
	'''
	lines : int : count of lines to print the pattern
	'''
	for line in range(lines, 0, -1):
		# current line
		# 
		# lets counts stuffs
		n_prefix_double_spaces = line
		n_stars = (lines - line + 1)
		# concatenate and print
		print(
			'  '*n_prefix_double_spaces + 
			'* '*n_stars
		)
		

if __name__ == "__main__":
	# lets add cmd line arguments
	if len(sys.argv) > 1:
		lines = int(sys.argv[1]) # change string to int
		triangle_stars(lines)	# to print variale number of lines using cmdline
	else:
		triangle_stars() # default value 5 will be used

