import sys

## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main():
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

	a = 1
	g = 1
	y = 0
	divisor_count = 0 

	x = int(sys.argv[1])

	while a <= x:
		if x % a == 0:
			divisor_count += 1
		a += 1

	while g < x:
		divisor_count2 = 0 
		b = 1
		while b <= g:
			if g % b == 0:
				divisor_count2 += 1
			b += 1
		if divisor_count2 >= y:
			y = divisor_count2
		g += 1

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

	if divisor_count > y:
		return ("anti-prime")
	else:
		return ("not anti-prime")
## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
