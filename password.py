#!/usr/bin/python

import random

def application(environ, start_response):
	status = '200 OK'
	max_count = 15

	count = environ['REQUEST_URI'].rpartition('/')[2]

	if count.isdigit():
		count = int(count)
	else:
		count = 1

	random_passes = []
	for index in range(min(count,max_count)):
		random_passes.append(random_pass())

	output = "\n".join(random_passes)

	response_headers = [('Content-type', 'text/plain'),
				('Content-Length', str(len(output)))]
	start_response(status, response_headers)

	return [output]

def random_pass():
	adjectives = []
	animals = []
	skills = []
	names = []

	with open("./adjectives.txt","r") as words:
		 for line in words:
			  adjectives.append(line.rstrip())
		 words.close()

	with open("./animals.txt","r") as words:
		for line in words:
			animals.append(line.rstrip())
		words.close()

	with open("./skills.txt","r") as words:
		 for line in words:
			  skills.append(line.rstrip())
		 words.close()

	with open("./names.txt","r") as words:
		 for line in words:
			  names.append(line.rstrip())
		 words.close()

	random.seed()
	adjective = adjectives[random.randint(0,len(adjectives)-1)].title()
	name = names[random.randint(0,len(names)-1)].title()
	animal = animals[random.randint(0,len(animals)-1)].title()
	skill = skills[random.randint(0,len(skills)-1)].title().replace(" ","")
	return str(adjective+animal+skill+name+str(random.randint(10,99)))

if __name__ == "__main__":
	print(random_pass())
