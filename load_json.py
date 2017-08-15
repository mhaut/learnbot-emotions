import json


def load_file(name):
    # Initializing the points that define the geometry of the elements
    #  item ( eye_left_x[], eye_right[], eyes_y[], iris_left_x[], iris_right_x[], iris_y[], pupil_left_x[], pupil_right_x[], pupils_y[],
    #  brightness_left_x[], brightness_right_x[], brightness_y[], brightness_left_x2[], brightness_right_x2[], brightness_y2[],
    #  eyebrow_left_x[], eyebrow_right_x[], eyebrow_y[], mouth_x[], mouth_y[], tongue_x[], tongue_y[]
    item = [[] for i in range(54)]

    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        # print eye_left["cozmo"][0]["eye_left"][2]["x"][1]["1"]
        for i in xrange(36):
            item[0].append(file[name][0]["eye_left"][3]["x"][i][str(i)])
            item[1].append(file[name][0]["eye_left"][4]["y"][i][str(i)])
            item[2].append(file[name][1]["eye_right"][3]["x"][i][str(i)])
            item[3].append(file[name][1]["eye_right"][4]["y"][i][str(i)])

            item[4].append(file[name][2]["eyelid_up_left"][3]["x"][i][str(i)])
            item[5].append(file[name][2]["eyelid_up_left"][4]["y"][i][str(i)])
            item[6].append(file[name][3]["eyelid_up_right"][3]["x"][i][str(i)])
            item[7].append(file[name][3]["eyelid_up_right"][4]["y"][i][str(i)])

            item[8].append(file[name][4]["eyelid_down_left"][3]["x"][i][str(i)])
            item[9].append(file[name][4]["eyelid_down_left"][4]["y"][i][str(i)])
            item[10].append(file[name][5]["eyelid_down_right"][3]["x"][i][str(i)])
            item[11].append(file[name][5]["eyelid_down_right"][4]["y"][i][str(i)])

            item[12].append(file[name][6]["iris_left"][3]["x"][i][str(i)])
            item[13].append(file[name][6]["iris_left"][4]["y"][i][str(i)])
            item[14].append(file[name][7]["iris_right"][3]["x"][i][str(i)])
            item[15].append(file[name][7]["iris_right"][4]["y"][i][str(i)])

            item[16].append(file[name][8]["pupil_left"][3]["x"][i][str(i)])
            item[17].append(file[name][8]["pupil_left"][4]["y"][i][str(i)])
            item[18].append(file[name][9]["pupil_right"][3]["x"][i][str(i)])
            item[19].append(file[name][9]["pupil_right"][4]["y"][i][str(i)])

            item[20].append(file[name][10]["reflex_pupil_left"][3]["x"][i][str(i)])
            item[21].append(file[name][10]["reflex_pupil_left"][4]["y"][i][str(i)])
            item[22].append(file[name][11]["reflex_pupil_right"][3]["x"][i][str(i)])
            item[23].append(file[name][11]["reflex_pupil_right"][4]["y"][i][str(i)])

            item[24].append(file[name][12]["reflex_pupil_left_2"][3]["x"][i][str(i)])
            item[25].append(file[name][12]["reflex_pupil_left_2"][4]["y"][i][str(i)])
            item[26].append(file[name][13]["reflex_pupil_right_2"][3]["x"][i][str(i)])
            item[27].append(file[name][13]["reflex_pupil_right_2"][4]["y"][i][str(i)])

            item[28].append(file[name][14]["eyebrow_left"][3]["x"][i][str(i)])
            item[29].append(file[name][14]["eyebrow_left"][4]["y"][i][str(i)])
            item[30].append(file[name][15]["eyebrow_right"][3]["x"][i][str(i)])
            item[31].append(file[name][15]["eyebrow_right"][4]["y"][i][str(i)])

            item[32].append(file[name][16]["mouth"][3]["x"][i][str(i)])
            item[33].append(file[name][16]["mouth"][4]["y"][i][str(i)])

            item[34].append(file[name][17]["tongue"][3]["x"][i][str(i)])
            item[35].append(file[name][17]["tongue"][4]["y"][i][str(i)])

        item[36].append([file[name][0]["eye_left"][0]["identification"][0]["name"],file[name][0]["eye_left"][0]["identification"][1]["id"]])
        item[37].append([file[name][1]["eye_right"][0]["identification"][0]["name"],file[name][1]["eye_right"][0]["identification"][1]["id"]])
        item[38].append([file[name][2]["eyelid_up_left"][0]["identification"][0]["name"],file[name][2]["eyelid_up_left"][0]["identification"][1]["id"]])
        item[39].append([file[name][3]["eyelid_up_right"][0]["identification"][0]["name"],file[name][3]["eyelid_up_right"][0]["identification"][1]["id"]])
        item[40].append([file[name][4]["eyelid_down_left"][0]["identification"][0]["name"],file[name][4]["eyelid_down_left"][0]["identification"][1]["id"]])
        item[41].append([file[name][5]["eyelid_down_right"][0]["identification"][0]["name"],file[name][5]["eyelid_down_right"][0]["identification"][1]["id"]])
        item[42].append([file[name][6]["iris_left"][0]["identification"][0]["name"],file[name][6]["iris_left"][0]["identification"][1]["id"]])
        item[43].append([file[name][7]["iris_right"][0]["identification"][0]["name"],file[name][7]["iris_right"][0]["identification"][1]["id"]])
        item[44].append([file[name][8]["pupil_left"][0]["identification"][0]["name"],file[name][8]["pupil_left"][0]["identification"][1]["id"]])
        item[45].append([file[name][9]["pupil_right"][0]["identification"][0]["name"],file[name][9]["pupil_right"][0]["identification"][1]["id"]])
        item[46].append([file[name][10]["reflex_pupil_left"][0]["identification"][0]["name"],file[name][10]["reflex_pupil_left"][0]["identification"][1]["id"]])
        item[47].append([file[name][11]["reflex_pupil_right"][0]["identification"][0]["name"],file[name][11]["reflex_pupil_right"][0]["identification"][1]["id"]])
        item[48].append([file[name][12]["reflex_pupil_left_2"][0]["identification"][0]["name"],file[name][12]["reflex_pupil_left_2"][0]["identification"][1]["id"]])
        item[49].append([file[name][13]["reflex_pupil_right_2"][0]["identification"][0]["name"],file[name][13]["reflex_pupil_right_2"][0]["identification"][1]["id"]])
        item[50].append([file[name][14]["eyebrow_left"][0]["identification"][0]["name"],file[name][14]["eyebrow_left"][0]["identification"][1]["id"]])
        item[51].append([file[name][15]["eyebrow_right"][0]["identification"][0]["name"],file[name][15]["eyebrow_right"][0]["identification"][1]["id"]])
        item[52].append([file[name][16]["mouth"][0]["identification"][0]["name"],file[name][16]["mouth"][0]["identification"][1]["id"]])
        item[53].append([file[name][17]["tongue"][0]["identification"][0]["name"],file[name][17]["tongue"][0]["identification"][1]["id"]])
    return item

def checkPaint(name,item):
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        # Checking if each item wants to be painted
        if (file[name][0]["eye_left"][2]["exist"] == "yes"):
            eye_left = zip(item[0], item[1])  # (eye_left_x,eye_y)
            eye_left_colour = file[name][0]["eye_left"][1]["colour"]
        else:
            eye_left = [0, 0]
            eye_left_colour = None

        if (file[name][1]["eye_right"][2]["exist"] == "yes"):
            eye_right = zip(item[2], item[3])  # (eye_right_x,eye_y)
            eye_right_colour = file[name][1]["eye_right"][1]["colour"]
        else:
            eye_right = [0, 0]
            eye_right_colour = None

        if (file[name][2]["eyelid_up_left"][2]["exist"] == "yes"):
            eyelid_up_left = zip(item[4], item[5])  # (eyelid_up_left_x,eyelid_up_y)
            eyelid_up_left_colour = file[name][2]["eyelid_up_left"][1]["colour"]
        else:
            eyelid_up_left = [0, 0]
            eyelid_up_left_colour = None

        if (file[name][3]["eyelid_up_right"][2]["exist"] == "yes"):
            eyelid_up_right = zip(item[6], item[7])  # (eyelid_up_right_x,eyelid_up_y)
            eyelid_up_right_colour = file[name][3]["eyelid_up_right"][1]["colour"]
        else:
            eyelid_up_right = [0, 0]
            eyelid_up_right_colour = None

        if (file[name][4]["eyelid_down_left"][2]["exist"] == "yes"):
            eyelid_down_left = zip(item[8], item[9])  # (eyelid_down_left_x,eyelid_down_y)
            eyelid_down_left_colour = file[name][4]["eyelid_down_left"][1]["colour"]
        else:
            eyelid_down_left = [0, 0]
            eyelid_down_left_colour = None

        if (file[name][5]["eyelid_down_right"][2]["exist"] == "yes"):
            eyelid_down_right = zip(item[10], item[11])  # (eyelid_down_right_x,eyelid_down_y)
            eyelid_down_right_colour = file[name][5]["eyelid_down_right"][1]["colour"]
        else:
            eyelid_down_right = [0, 0]
            eyelid_down_right_colour = None

        if (file[name][6]["iris_left"][2]["exist"] == "yes"):
            iris_left = zip(item[12], item[13])  # (iris_left_x,iris_y)
            iris_left_colour = file[name][6]["iris_left"][1]["colour"]
        else:
            iris_left = [0, 0]
            iris_left_colour = None

        if (file[name][7]["iris_right"][2]["exist"] == "yes"):
            iris_right = zip(item[14], item[15])  # (iris_left_x,iris_y)
            iris_right_colour = file[name][7]["iris_right"][1]["colour"]
        else:
            iris_right = [0, 0]
            iris_right_colour = None

        if (file[name][8]["pupil_left"][2]["exist"] == "yes"):
            pupil_left = zip(item[16], item[17])  # (pupil_left_x,pupils_y)
            pupil_left_colour = file[name][8]["pupil_left"][1]["colour"]
        else:
            pupil_left = [0, 0]
            pupil_left_colour = None

        if (file[name][9]["pupil_right"][2]["exist"] == "yes"):
            pupil_right = zip(item[18], item[19])  # (pupil_right_x,pupils_y)
            pupil_right_colour = file[name][9]["pupil_right"][1]["colour"]
        else:
            pupil_right = [0, 0]
            pupil_right_colour = None

        if (file[name][10]["reflex_pupil_left"][2]["exist"] == "yes"):
            brightness_left = zip(item[20], item[21])  # (brightness_left_x,brightness_y)
            brightness_left_colour = file[name][10]["reflex_pupil_left"][1]["colour"]
        else:
            brightness_left = [0, 0]
            brightness_left_colour = None

        if (file[name][11]["reflex_pupil_right"][2]["exist"] == "yes"):
            brightness_right = zip(item[22], item[23])  # (brightness_right_x,brightness_y)
            brightness_right_colour = file[name][11]["reflex_pupil_right"][1]["colour"]
        else:
            brightness_right = [0, 0]
            brightness_right_colour = None

        if (file[name][12]["reflex_pupil_left_2"][2]["exist"] == "yes"):
            brightness_left2 = zip(item[24], item[25])  # (brightness_left_x2,brightness_y2)
            brightness_left2_colour = file[name][12]["reflex_pupil_left_2"][1]["colour"]
        else:
            brightness_left2 = [0, 0]
            brightness_left2_colour = None

        if (file[name][13]["reflex_pupil_right_2"][2]["exist"] == "yes"):
            brightness_right2 = zip(item[26], item[27])  # (brightness_right_x2,brightness_y2)
            brightness_right2_colour = file[name][13]["reflex_pupil_right_2"][1]["colour"]
        else:
            brightness_right2 = [0, 0]
            brightness_right2_colour = None

        if (file[name][14]["eyebrow_left"][2]["exist"] == "yes"):
            eyebrow_left = zip(item[28], item[29])  # (eyebrow_left_x,eyebrow_y2)
            eyebrow_left_colour = file[name][14]["eyebrow_left"][1]["colour"]
        else:
            eyebrow_left = [0, 0]
            eyebrow_left_colour = None

        if (file[name][15]["eyebrow_right"][2]["exist"] == "yes"):
            eyebrow_right = zip(item[30], item[31])  # (eyebrow_right_x,eyebrow_y2)
            eyebrow_right_colour = file[name][15]["eyebrow_right"][1]["colour"]
        else:
            eyebrow_right = [0, 0]
            eyebrow_right_colour = None

        if (file[name][16]["mouth"][2]["exist"] == "yes"):
            mouth = zip(item[32], item[33])  # (mouth_x,mouth_y)
            mouth_colour = file[name][16]["mouth"][1]["colour"]
        else:
            mouth = [0, 0]
            mouth_colour = None

        if (file[name][17]["tongue"][2]["exist"] == "yes"):
            tongue = zip(item[34], item[35])  # (tongue_x,tongue_y)
            tongue_colour = file[name][17]["tongue"][1]["colour"]
        else:
            tongue = [0, 0]
            tongue_colour = None
    to_paint = [eye_left, eye_left_colour, eye_right, eye_right_colour, eyelid_up_left,
                eyelid_up_left_colour, eyelid_up_right, eyelid_up_right_colour, eyelid_down_left,
                eyelid_down_left_colour, eyelid_down_right, eyelid_down_right_colour, iris_left, iris_left_colour, iris_right,
                iris_right_colour, pupil_left, pupil_left_colour, pupil_right, pupil_right_colour, brightness_left,
                brightness_left_colour, brightness_right, brightness_right_colour, brightness_left2,
                brightness_left2_colour, brightness_right2, brightness_right2_colour, eyebrow_left, eyebrow_left_colour,
                eyebrow_right, eyebrow_right_colour, mouth, mouth_colour, tongue, tongue_colour]
    return to_paint

def searchPositionPart(name,part):
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        for i in xrange(36,54):
            if part == load_file(name)[i][0][0]:
                return i-36



def delete_part(name,part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json','r+') as data_file:
        file = json.load(data_file)
        if file[name][searchPositionPart("cozmo",part)][part][2]["exist"]=="yes":
            file[name][searchPositionPart("cozmo", part)][part][2]["exist"] = "no"
            data_file.seek(0)
            json.dump(file,data_file,indent=4)
            data_file.truncate()

def create_part(name,part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json','r+') as data_file:
        file = json.load(data_file)
        if file[name][searchPositionPart("cozmo",part)][part][2]["exist"]=="no":
            file[name][searchPositionPart("cozmo", part)][part][2]["exist"] = "yes"
            data_file.seek(0)
            json.dump(file,data_file,indent=4)
            data_file.truncate()

