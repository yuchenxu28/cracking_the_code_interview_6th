# Q1: Is Unique: Implement an algorithm to dtermine if a string has all unique characters. 

def isUnique(str):
	str_list = list()
	for i in range(len(str)):
		if str[i] not in str_list:
			str_list.append(str[i])
		else:
			return True
	return False

#print(isUnique("jeta")) 	#false
#print(isUnique("abab"))	#true

#Q2: Given two strings, write a method to decide if one is a permutation of the other
def permutation(str1, str2):
	if (str1 in str2 or str2 in str1):
		return True
	else:
		return False

#print(permutation("as", "aasas"))	#true
#print(permutation("aasas", "as"))	#true
#print(permutation("aase", "byu"))	#false

#Q3: Write a method to replace all spaces in a string with "%20". 
def replaceSpace(str):
	str = str.split()
	for i in range(len(str)):
		if (i != (len(str) - 1)):
			str[i] += "%20"
	str = ''.join(str)

#print(replaceSpace("we we qwewq sd"))

#Q4: Given a string, write a function to check if it is a permutation of a palindrome.
def isPalindromeofPermutation(str):
	odd = 0
	str = str.replace(" ", "")
	print(str)
	for i in range(len(str)):
		if (str.count(str[i]) % 2 == 1):
			odd += 1
		if (odd > 1):
			return False
	return True

#print(isPalindromeofPermutation(" taco cat"))

#Q5: There are three types of edits on a string: insert char, remove char or change char. 
# Given two strings, write a function to check if they are one edit (or zero edit) away
def deleteChar(str1, str2):
	for i in range(len(str1)):
		if (str1[:i] + str1[i+1:] == str2):
			return True
	return False

def replaceChar(str1, str2):
	for i in range(len(str1)):
		if (str1[:i] + str1[i+1:] == str2[:i] + str2[i+1:]):
			return True
	return False

def oneAway(str1, str2):
	if (len(str1) == len(str2)):
		if (str1 == str2):
			return True
		else:
			return replaceChar(str1, str2)
	else:
		return deleteChar(str1, str2) or deleteChar(str2, str1)
#print(oneAway("pale", "bae"))

#Q6: Implement a method to perform basic string compression using the counts of repeated characters.
def compress(str1):
	str1 = sorted(str1)
	compressstr = list()
	number = 0
	for i in range(len(str1)):
		letter = str1[i]
		if (str1[i] != str1[i-1]):
			number = 1
			compressstr.append(str1[i])
			compressstr.append(str(number))
		else:
			number += 1
			compressstr[len(compressstr)-1] = str(number)
	return ''.join(compressstr)

str1 = "asabsdabbs"
#print(compress(str1))

#Q7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90degrees. Can you do this in place?
"""
N = 5
matrix = [[x*y for x in range(N)] for y in range(N)] 
for x in range(N): 
	for y in range(N):
		print(matrix[x][y], end = "")

def rotateMatrix(matrix):
	temp = 0
	for x in range(N):
		for y in range(N):
			x
"""

#Q8: Write an algorithm such that if an element in an NxN is 0, its entire row and column are set to 0
# N = 5
# matrix1 = [[(x+1)*(y+1) for x in range(N)] for y in range(N)] 
# matrix1[1][2] = 0
# for x in range(N): 
# 	for y in range(N):
# 		print(matrix1[x][y], end = " ")
# 	print("\n")
def setRowColtoZero(matrix):
	xlist = list()
	ylist = list()
	for x in range(N):
		for y in range(N):
			if (matrix[x][y] == 0):
				xlist.append(x)
				ylist.append(y)

	for i in range(len(xlist)):
		for j in range(len(matrix)):
			matrix[xlist[i]][j] = 0
			matrix[j][ylist[i]] = 0

	return matrix

# newmatrix = setRowColtoZero(matrix1)
# for x in range(N): 
# 	for y in range(N):
# 		print(newmatrix[x][y], end = " ")
# 	print("\n")

#Q9: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
# using only one call to isSubstring

def isRotation(s1, s2):
	totals = s2 + s2
	if (s1 in totals):
		return True
	else:
		return False

print(isRotation("waterbottle", "terbottlewa"))