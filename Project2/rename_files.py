import os

def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir("/Users/andreas.bechter/Udacity/Python_Basics/Project2/prank")
	print(file_list)

	#(2) for each file, rename filename

rename_files()
