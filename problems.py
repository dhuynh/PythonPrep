
def front3(str):
	if len(str) >= 3:
		front = str[:3]
	else:
		front = str
	return front + front + front

def string_times(str, n):
	newStr = ""

	s = str
	charArray = list(s)

	for i in n:
		newStr.join(charArray)
	return newstr

def front_times(str, n):
	newStr = ""

	if len(str) >= 3:
		front = str[:3]
	else:
		front = str


	for i in range(n):
		newStr += front
	return newStr


def string_bits(str):
	newStr = ""
	s = str
	charArray = list(str)

	for i in range(0, len(charArray)):
		if i%2 == 0:
			newStr += charArray[i]
	return newStr

def string_splosion(str):

	result = ""

	for i in range(len(str)):
		result += str[:i+1]
	return result 
  
def array_count9(nums):
	count = ''

	for num in nums:
		if nums[i] == 9:
			count+=1
	return count

def array_front9(nums):
	end = len(nums)
	if len(nums > 4):
		end = 4

	for i in range(end):
		if nums[i] == 9:
			return True
	return False

def array123(nums):
	for i in range(len(nums)-2):
		if nums[i] == 1 and nums[i+1] == 2 and nums [i+2]==3:
			return True
	return False

def string_match(a,b):
	count=0
	for char in range(len(a)):
		if a[char] == b[char]:
			count +=1
	return count

def make_abba(a,b):
	return a + b + b + a

def mostCommonChar(str):
	charArray = list(str)

	charDict = {}

	for i in range(len(charArray)):
		if charArray[i] in charDict.keys():
			charDict[charArray[i]] += 1
		else:
			charDict[charArray[i]] = 1

	v =list(charDict.values())
	k =list(charDict.keys())


	return k[v.index(max(v))]



