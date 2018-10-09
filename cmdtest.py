#coding:utf-8
import os
import sys
import getopt


def main(argv):
	inputfile=''
	outputfile=''
	try:
		opts,args=getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('Error: cmdtest.py -i <infilename> -o <outputfilename>')
		sys.exit(2)
	for opt,arg in opts:
		if opt=='-h':
			print('usage: cmdtest.py -i <infilename> -o <outputfilename>')
			sys.exit(2)
		elif opt in ("-i","--ifile"):
			inputfile=arg
		elif opt in ("-o","--ofile"):
			outputfile=arg


	print("IN="+inputfile)
	print("OUT="+outputfile)
if __name__=="__main__":
	main(sys.argv[1:])