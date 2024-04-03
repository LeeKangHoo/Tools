a = 'test'
print(a)
def test():
	global a
	a = 'good'
	print(a)
test()
print(a)
