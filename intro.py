##最小可用id
##TEST CODE
#import random
#random.sample(xrange(N),n)
#testList = random.sample(xrange(100000),90000)
def minFree_brutForce(lst):
	x = 0
	while True:
		if x not in lst:
			return x
		x += 1

import numpy
def minFree1(lst):
	n = len(lst)
	flag = numpy.repeat(False, n+1)
	for x in lst:
		if x <= n :
			flag[x] = True
	for i in xrange(n+1):
		if flag[i] == False:
			return i

def minFree2(lst, start):
	n = len(lst)
	lstA = [x for x in lst if x <= start+n/2]
	lstB = [x for x in lst if x not in lstA]
	lenA = len(lstA)
	lenB = len(lstB)
	if lenA == 0:
		return start
	if lenB == 0:
		return lstA[0]+1
	if max(lstA)+1<= lenA+start : #lstA is full
		if max(lstB)+1<= n: #lstB is full
			return sorted(lstB)[-1]+1
		else:
			return minFree2(lstB,lenA)
	else :
		return minFree2(lstA,start)

##丑数
def get_uglyNum(n):
	x = 1
	i = 0
	while True:
		if uglyNum_brutForce(x) :
			i += 1
		if i == n:
			return x
		x += 1

def uglyNum_brutForce(num):
	while numpy.mod(num,2) == 0:
		num =num/2
	while numpy.mod(num,3) == 0:
		num = num/3
	while numpy.mod(num,5) == 0:
		num = num/5
	if num == 1:
		return True
	else:
		return False

def get_uglyNum2(n):
	if n == 1:
		return 1
	Q2 = [2]
	Q3 = [3]
	Q5 = [5]
	while n > 1:
		#print n
		x = min(Q2[0],Q3[0],Q5[0])
		#print "x = " +str(x)
		if x == Q2[0] :
			Q2=Q2[1:]
			Q2.append(x*2)
			Q3.append(x*3)
			Q5.append(x*5)
		elif x == Q3[0]:
			Q3=Q3[1:]
			Q3.append(x*3)
			Q5.append(x*5)
		else:
			Q5=Q5[1:]
			Q5.append(x*5)
		#print "Q2=" + str(Q2)
		#print "Q3=" + str(Q3)
		#print "Q5=" + str(Q5)
		n -= 1
	return x


