#/usr/local/bin/python
#import random

## General binary tree node class. @property is not useful right now.
class Node(object):
	def __init__(self, value=None, left=None, right=None):
		self.__left = left
		self.__right = right
		self.__value = value 

	@property
	def right(self):
		return self.__right
	
	@right.setter
	def right(self, value):
		self.__right = value

	@right.deleter
	def right(self):
		del self.__right
	
	@property
	def left(self):
		return self.__left
	
	@left.setter
	def left(self, value):
		self.__left = value

	@left.deleter
	def left(self):
		del self.__left

def get_diameter(node):
	if not node:
		return (0, 0)

	if not isinstance(node, Node):
		raise Exception(" Invalid param type ")
	
	(left_height, left_diameter) = get_diameter(node.left)
	(right_height, right_diameter) = get_diameter(node.right)
	
	current_diameter = 0
	if node.right and node.left:
		current_diameter = left_height + right_height + 1


	return (max([left_height, right_height]) + 1, max([left_diameter, right_diameter, current_diameter]))

# Case 2: Diameter is not through root
#	
#		      1
#		2	   
#	       4  5        	
#            8
#           9		   
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.left.left = Node(9)

print "case 1 : Height : %s Diameter : %s" %  get_diameter(root)		


#     case 2: Diameter through root
#		      1
#		2	    3
#	       4  5        6 7	
#            8		    10
#          9               11   
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(10)
root.right.left.right.left = Node(11)
print "case 2 Height : %s Diameter : %s" %  get_diameter(root)		
