#Klee Minty cube generator
import sys

def main():
	n = 5
	if len(sys.argv) > 1:
		n = int(sys.argv[1])

	m = n
	f = open("KleeMinty" + str(n) + ".dat", 'w')
	f.write(str(n) + '\n')
	f.write(str(n) + '\n')

	#generate objective
	c = ''
	for j in range(1,n+1):
		c += str(10**(n-j)) + ' '
	f.write(str(c) + '\n')

	b = ''
	for i in range(1,n+1):
		b += str(100**(i-1)) + ' '
	f.write(str(b) + '\n')

	for i in range(1,n+1):
		row = ''
		for j in range(1,i):
			row += str(2*(10**(i-j))) + ' '
		row += '1 '
		for j in range(i+1,n+1):
			row += '0 '
		f.write(row + '\n')

	f.close()


if __name__ == "__main__":
	main()