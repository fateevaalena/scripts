import os
import datetime
import random
path = "npdoc"

#get list np file
def enumeratefiles(path=path):
    """Returns all the files in a directory as a list"""
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_collection.append(file)
    return file_collection

#update date in string
def updatedate(text_file,newdate):
	#find date and replase current date
	index = text_file.find('<updated_date>',0)+14
	return text_file.replace(text_file[index:index+10],newdate)#replace all date

#update id
def updateid(text_file):
	#find id and replace it
	index = text_file.find('<article_id id="',0)+16
	text_file = text_file.replace(text_file[index:index+6],str(random.randint(1000000,9999999)))
	#find original id and replace it
	index = text_file.find('<original_article_id id="',0)+25
	return text_file.replace(text_file[index:index+6],str(random.randint(1000000,9999999)))


try:
	now = str(datetime.datetime.now())[0:10]#get current date
	file_collection = enumeratefiles(path) #get list np file
	if len(file_collection) == 0:
		print "empty dir - "+ path
	for  filenames in file_collection:
		if filenames.split(".")[1] == 'npdoc':
			f = open(path+'/'+filenames, 'r')
			text_file = f.read()
			text_file = updatedate(text_file,now)
			text_file = updateid(text_file)
			f = open(path+'/'+filenames, 'w')
			f.seek(0)
			f.write(text_file)
			f.close()
			print  "Update " + filenames
		else:
			print "Incorrect file: " + filenames
except IOError:
	print "File not open for reading"
finally:
	raw_input("Press enter")