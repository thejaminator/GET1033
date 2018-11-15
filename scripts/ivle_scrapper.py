import urllib.request
import shutil
import cgi
import requests
import os
import pandas as pd


df = pd.read_csv('clean.csv')
storage = "C:/test/"

def get_stuid(stuid):
	len_front = 58 #58 characters before student id
	len_stunum = 7 #gets 7 numbers of the student id
	stunum = stuid[len_front:]
	stunum = stunum[:len_stunum]
	stunum = int(stunum)
	return stunum

def incrementloop(stuid):
	global success
	global fail
	success = 0
	fail = 0
	url_begin = stuid[:58] #"https://ivle.nus.edu.sg/ClassManagement/stuphoto.ashx?id=e"
	url_end = stuid[-31:]  #sequence following stuid e.g. ca95250234283f0fd0&AccountType=S
	hexadecimal = url_end[:17] #gets hash? following stuid e.g. ca9525007583f0fd0
	directory = storage + hexadecimal #creates hash? folder in diretory You can change the directory here
	if not os.path.exists(directory):  
		os.makedirs(directory)
	else: 
		print("dir alr exists!")
		wait = input("PRESS ENTER TO CONTINUE.")

	start = (get_stuid(stuid)) - 300 #start from how many number ID ago
	end = start + 150000
	print ("Starting ID is " + str(start))
	
	while (start < end):
		url = url_begin + str(start).zfill(7) + url_end #zfill makes sure it is 7 digits long with 0 infront
		print ("Try ID:", start)
		print ("Try url" , url)
		download_url(url, directory, start)
		start = start + 1
	
def download_url(url, directory, start):
	"""Download file from url to directory

	URL is expected to have a Content-Disposition header telling us what
	filename to use.

	Returns filename of downloaded file.

	"""
	response = requests.get(url, stream=True)
	global success
	global fail
	params = cgi.parse_header(
		response.headers.get('Content-Disposition', ''))[-1]	
	filename = os.path.basename(params['filename']) 
	if filename == "nophoto.jpg":
		fail += 1 
		print (success , " successes. " , fail , " failures.")
	else:
		filename = "E" + str(start).zfill(7) + "_" + os.path.basename(params['filename'])
		success += 1 
		print (success , " successes. " , fail , " failures.")
		abs_path = os.path.join(directory, filename)
		with open(abs_path, 'wb') as target:
			response.raw.decode_content = True
			shutil.copyfileobj(response.raw, target)

	return filename

	

incrementloop(input("Paste image url"))
