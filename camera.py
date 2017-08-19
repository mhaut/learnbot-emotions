import json


with open('prueba.json') as data_file:
	file = json.load(data_file)
	# print eye_left["cozmo"][0]["eye_left"][2]["x"][1]["1"]
	list=[]
	list.append(file['cozmo'][0]["eye_left"][3]["x"])
	print list