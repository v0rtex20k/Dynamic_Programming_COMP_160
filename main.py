##########################################################################
#
#    Tufts University, Comp 160 wordInterpret coding assignment
#
#    main.py
#    wordInterpret
#
#    simple main to test wordInterpret
#    NOTE: this main is only for you to test wordInterpret. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from interpret import wordInterpret


def main():
	inputNums = "34212421214221219212244212142212192122464734651422121921224"
	result = wordInterpret(inputNums)
	print(result)


if __name__ == '__main__':
	main()