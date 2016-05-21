import random,string

def get_random_str(length = 1):
	ascii_char = string.letters + string.digits
	len = ascii_char.__len__()
	result = ''
	for x in range(length):
		result += ascii_char[random.randint(0,len-1)]
	print result
	return result

if __name__ == '__main__':
	for x in range(200):
		get_random_str(15);