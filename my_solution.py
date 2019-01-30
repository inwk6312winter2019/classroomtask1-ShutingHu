#This is my sloution
import os
def traverse_folder(dict):
	res = []
	for files in os.listdir(dict):
		res.append(files)
		print(res)
