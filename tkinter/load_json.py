import json


def load_file(name):
    # Initializing the points that define the geometry of the elements
    #  item ( eye_left_x[], eye_right[], eyes_y[], iris_left_x[], iris_right_x[], iris_y[], pupil_left_x[], pupil_right_x[], pupils_y[],
    #  brightness_left_x[], brightness_right_x[], brightness_y[], brightness_left_x2[], brightness_right_x2[], brightness_y2[],
    #  eyebrow_left_x[], eyebrow_right_x[], eyebrow_y[], mouth_x[], mouth_y[], tongue_x[], tongue_y[]
    item = [[] for i in range(214)]

    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        # print eye_left["cozmo"][0]["eye_left"][2]["x"][1]["1"]

        item[0].append(file[name][0]["eye_left"][3]["x"])
        item[1].append(file[name][0]["eye_left"][4]["y"])
        item[2].append(file[name][1]["eye_right"][3]["x"])
        item[3].append(file[name][1]["eye_right"][4]["y"])

        item[4].append(file[name][2]["eyelid_up_left"][3]["x"])
        item[5].append(file[name][2]["eyelid_up_left"][4]["y"])
        item[6].append(file[name][3]["eyelid_up_right"][3]["x"])
        item[7].append(file[name][3]["eyelid_up_right"][4]["y"])

        item[8].append(file[name][4]["eyelid_down_left"][3]["x"])
        item[9].append(file[name][4]["eyelid_down_left"][4]["y"])
        item[10].append(file[name][5]["eyelid_down_right"][3]["x"])
        item[11].append(file[name][5]["eyelid_down_right"][4]["y"])

        item[12].append(file[name][6]["iris_left"][3]["x"])
        item[13].append(file[name][6]["iris_left"][4]["y"])
        item[14].append(file[name][7]["iris_right"][3]["x"])
        item[15].append(file[name][7]["iris_right"][4]["y"])

        item[16].append(file[name][8]["pupil_left"][3]["x"])
        item[17].append(file[name][8]["pupil_left"][4]["y"])
        item[18].append(file[name][9]["pupil_right"][3]["x"])
        item[19].append(file[name][9]["pupil_right"][4]["y"])

        item[20].append(file[name][10]["reflex_pupil_left"][3]["x"])
        item[21].append(file[name][10]["reflex_pupil_left"][4]["y"])
        item[22].append(file[name][11]["reflex_pupil_right"][3]["x"])
        item[23].append(file[name][11]["reflex_pupil_right"][4]["y"])

        item[24].append(file[name][12]["reflex_pupil_left_2"][3]["x"])
        item[25].append(file[name][12]["reflex_pupil_left_2"][4]["y"])
        item[26].append(file[name][13]["reflex_pupil_right_2"][3]["x"])
        item[27].append(file[name][13]["reflex_pupil_right_2"][4]["y"])

        item[28].append(file[name][14]["eyebrow_left"][3]["x"])
        item[29].append(file[name][14]["eyebrow_left"][4]["y"])
        item[30].append(file[name][15]["eyebrow_right"][3]["x"])
        item[31].append(file[name][15]["eyebrow_right"][4]["y"])

        item[32].append(file[name][16]["mouth"][3]["x"])
        item[33].append(file[name][16]["mouth"][4]["y"])

        item[34].append(file[name][17]["tongue"][3]["x"])
        item[35].append(file[name][17]["tongue"][4]["y"])

        item[36].append(file[name][18]["angry"][0]["eyelid_up_left"][0]["x"])
        item[37].append(file[name][18]["angry"][0]["eyelid_up_left"][1]["y"])
        item[38].append(file[name][18]["angry"][1]["eyelid_up_right"][0]["x"])
        item[39].append(file[name][18]["angry"][1]["eyelid_up_right"][1]["y"])
        item[40].append(file[name][18]["angry"][2]["eyelid_down_left"][0]["x"])
        item[41].append(file[name][18]["angry"][2]["eyelid_down_left"][1]["y"])
        item[42].append(file[name][18]["angry"][3]["eyelid_down_right"][0]["x"])
        item[43].append(file[name][18]["angry"][3]["eyelid_down_right"][1]["y"])

        item[44].append(file[name][18]["angry"][4]["iris_left"][0]["x"])
        item[45].append(file[name][18]["angry"][4]["iris_left"][1]["y"])
        item[46].append(file[name][18]["angry"][5]["iris_right"][0]["x"])
        item[47].append(file[name][18]["angry"][5]["iris_right"][1]["y"])

        item[48].append(file[name][18]["angry"][6]["pupil_left"][0]["x"])
        item[49].append(file[name][18]["angry"][6]["pupil_left"][1]["y"])
        item[50].append(file[name][18]["angry"][7]["pupil_right"][0]["x"])
        item[51].append(file[name][18]["angry"][7]["pupil_right"][1]["y"])

        item[52].append(file[name][18]["angry"][8]["reflex_pupil_left"][0]["x"])
        item[53].append(file[name][18]["angry"][8]["reflex_pupil_left"][1]["y"])
        item[54].append(file[name][18]["angry"][9]["reflex_pupil_right"][0]["x"])
        item[55].append(file[name][18]["angry"][9]["reflex_pupil_right"][1]["y"])
        item[56].append(file[name][18]["angry"][10]["reflex_pupil_left_2"][0]["x"])
        item[57].append(file[name][18]["angry"][10]["reflex_pupil_left_2"][1]["y"])
        item[58].append(file[name][18]["angry"][11]["reflex_pupil_right_2"][0]["x"])
        item[59].append(file[name][18]["angry"][11]["reflex_pupil_right_2"][1]["y"])

        item[60].append(file[name][18]["angry"][12]["eyebrow_left"][0]["x"])
        item[61].append(file[name][18]["angry"][12]["eyebrow_left"][1]["y"])
        item[62].append(file[name][18]["angry"][13]["eyebrow_right"][0]["x"])
        item[63].append(file[name][18]["angry"][13]["eyebrow_right"][1]["y"])

        item[64].append(file[name][18]["angry"][14]["mouth"][0]["x"])
        item[65].append(file[name][18]["angry"][14]["mouth"][1]["y"])

        item[66].append(file[name][18]["angry"][15]["tongue"][0]["x"])
        item[67].append(file[name][18]["angry"][15]["tongue"][1]["y"])

        item[68].append(file[name][19]["happiness"][0]["eyelid_up_left"][0]["x"])
        item[69].append(file[name][19]["happiness"][0]["eyelid_up_left"][1]["y"])
        item[70].append(file[name][19]["happiness"][1]["eyelid_up_right"][0]["x"])
        item[71].append(file[name][19]["happiness"][1]["eyelid_up_right"][1]["y"])
        item[72].append(file[name][19]["happiness"][2]["eyelid_down_left"][0]["x"])
        item[73].append(file[name][19]["happiness"][2]["eyelid_down_left"][1]["y"])
        item[74].append(file[name][19]["happiness"][3]["eyelid_down_right"][0]["x"])
        item[75].append(file[name][19]["happiness"][3]["eyelid_down_right"][1]["y"])

        item[76].append(file[name][19]["happiness"][4]["iris_left"][0]["x"])
        item[77].append(file[name][19]["happiness"][4]["iris_left"][1]["y"])
        item[78].append(file[name][19]["happiness"][5]["iris_right"][0]["x"])
        item[79].append(file[name][19]["happiness"][5]["iris_right"][1]["y"])

        item[80].append(file[name][19]["happiness"][6]["pupil_left"][0]["x"])
        item[81].append(file[name][19]["happiness"][6]["pupil_left"][1]["y"])
        item[82].append(file[name][19]["happiness"][7]["pupil_right"][0]["x"])
        item[83].append(file[name][19]["happiness"][7]["pupil_right"][1]["y"])

        item[84].append(file[name][19]["happiness"][8]["reflex_pupil_left"][0]["x"])
        item[85].append(file[name][19]["happiness"][8]["reflex_pupil_left"][1]["y"])
        item[86].append(file[name][19]["happiness"][9]["reflex_pupil_right"][0]["x"])
        item[87].append(file[name][19]["happiness"][9]["reflex_pupil_right"][1]["y"])
        item[88].append(file[name][19]["happiness"][10]["reflex_pupil_left_2"][0]["x"])
        item[89].append(file[name][19]["happiness"][10]["reflex_pupil_left_2"][1]["y"])
        item[90].append(file[name][19]["happiness"][11]["reflex_pupil_right_2"][0]["x"])
        item[91].append(file[name][19]["happiness"][11]["reflex_pupil_right_2"][1]["y"])

        item[92].append(file[name][19]["happiness"][12]["eyebrow_left"][0]["x"])
        item[93].append(file[name][19]["happiness"][12]["eyebrow_left"][1]["y"])
        item[94].append(file[name][19]["happiness"][13]["eyebrow_right"][0]["x"])
        item[95].append(file[name][19]["happiness"][13]["eyebrow_right"][1]["y"])

        item[96].append(file[name][19]["happiness"][14]["mouth"][0]["x"])
        item[97].append(file[name][19]["happiness"][14]["mouth"][1]["y"])

        item[98].append(file[name][19]["happiness"][15]["tongue"][0]["x"])
        item[99].append(file[name][19]["happiness"][15]["tongue"][1]["y"])

        item[100].append(file[name][20]["sadness"][0]["eyelid_up_left"][0]["x"])
        item[101].append(file[name][20]["sadness"][0]["eyelid_up_left"][1]["y"])
        item[102].append(file[name][20]["sadness"][1]["eyelid_up_right"][0]["x"])
        item[103].append(file[name][20]["sadness"][1]["eyelid_up_right"][1]["y"])
        item[104].append(file[name][20]["sadness"][2]["eyelid_down_left"][0]["x"])
        item[105].append(file[name][20]["sadness"][2]["eyelid_down_left"][1]["y"])
        item[106].append(file[name][20]["sadness"][3]["eyelid_down_right"][0]["x"])
        item[107].append(file[name][20]["sadness"][3]["eyelid_down_right"][1]["y"])

        item[108].append(file[name][20]["sadness"][4]["iris_left"][0]["x"])
        item[109].append(file[name][20]["sadness"][4]["iris_left"][1]["y"])
        item[110].append(file[name][20]["sadness"][5]["iris_right"][0]["x"])
        item[111].append(file[name][20]["sadness"][5]["iris_right"][1]["y"])

        item[112].append(file[name][20]["sadness"][6]["pupil_left"][0]["x"])
        item[113].append(file[name][20]["sadness"][6]["pupil_left"][1]["y"])
        item[114].append(file[name][20]["sadness"][7]["pupil_right"][0]["x"])
        item[115].append(file[name][20]["sadness"][7]["pupil_right"][1]["y"])

        item[116].append(file[name][20]["sadness"][8]["reflex_pupil_left"][0]["x"])
        item[117].append(file[name][20]["sadness"][8]["reflex_pupil_left"][1]["y"])
        item[118].append(file[name][20]["sadness"][9]["reflex_pupil_right"][0]["x"])
        item[119].append(file[name][20]["sadness"][9]["reflex_pupil_right"][1]["y"])
        item[120].append(file[name][20]["sadness"][10]["reflex_pupil_left_2"][0]["x"])
        item[121].append(file[name][20]["sadness"][10]["reflex_pupil_left_2"][1]["y"])
        item[122].append(file[name][20]["sadness"][11]["reflex_pupil_right_2"][0]["x"])
        item[123].append(file[name][20]["sadness"][11]["reflex_pupil_right_2"][1]["y"])

        item[124].append(file[name][20]["sadness"][12]["eyebrow_left"][0]["x"])
        item[125].append(file[name][20]["sadness"][12]["eyebrow_left"][1]["y"])
        item[126].append(file[name][20]["sadness"][13]["eyebrow_right"][0]["x"])
        item[127].append(file[name][20]["sadness"][13]["eyebrow_right"][1]["y"])

        item[128].append(file[name][20]["sadness"][14]["mouth"][0]["x"])
        item[129].append(file[name][20]["sadness"][14]["mouth"][1]["y"])

        item[130].append(file[name][20]["sadness"][15]["tongue"][0]["x"])
        item[131].append(file[name][20]["sadness"][15]["tongue"][1]["y"])

        item[132].append(file[name][21]["scared"][0]["eyelid_up_left"][0]["x"])
        item[133].append(file[name][21]["scared"][0]["eyelid_up_left"][1]["y"])
        item[134].append(file[name][21]["scared"][1]["eyelid_up_right"][0]["x"])
        item[135].append(file[name][21]["scared"][1]["eyelid_up_right"][1]["y"])
        item[136].append(file[name][21]["scared"][2]["eyelid_down_left"][0]["x"])
        item[137].append(file[name][21]["scared"][2]["eyelid_down_left"][1]["y"])
        item[138].append(file[name][21]["scared"][3]["eyelid_down_right"][0]["x"])
        item[139].append(file[name][21]["scared"][3]["eyelid_down_right"][1]["y"])

        item[140].append(file[name][21]["scared"][4]["iris_left"][0]["x"])
        item[141].append(file[name][21]["scared"][4]["iris_left"][1]["y"])
        item[142].append(file[name][21]["scared"][5]["iris_right"][0]["x"])
        item[143].append(file[name][21]["scared"][5]["iris_right"][1]["y"])

        item[144].append(file[name][21]["scared"][6]["pupil_left"][0]["x"])
        item[145].append(file[name][21]["scared"][6]["pupil_left"][1]["y"])
        item[146].append(file[name][21]["scared"][7]["pupil_right"][0]["x"])
        item[147].append(file[name][21]["scared"][7]["pupil_right"][1]["y"])

        item[148].append(file[name][21]["scared"][8]["reflex_pupil_left"][0]["x"])
        item[149].append(file[name][21]["scared"][8]["reflex_pupil_left"][1]["y"])
        item[150].append(file[name][21]["scared"][9]["reflex_pupil_right"][0]["x"])
        item[151].append(file[name][21]["scared"][9]["reflex_pupil_right"][1]["y"])
        item[152].append(file[name][21]["scared"][10]["reflex_pupil_left_2"][0]["x"])
        item[153].append(file[name][21]["scared"][10]["reflex_pupil_left_2"][1]["y"])
        item[154].append(file[name][21]["scared"][11]["reflex_pupil_right_2"][0]["x"])
        item[155].append(file[name][21]["scared"][11]["reflex_pupil_right_2"][1]["y"])

        item[156].append(file[name][21]["scared"][12]["eyebrow_left"][0]["x"])
        item[157].append(file[name][21]["scared"][12]["eyebrow_left"][1]["y"])
        item[158].append(file[name][21]["scared"][13]["eyebrow_right"][0]["x"])
        item[159].append(file[name][21]["scared"][13]["eyebrow_right"][1]["y"])

        item[160].append(file[name][21]["scared"][14]["mouth"][0]["x"])
        item[161].append(file[name][21]["scared"][14]["mouth"][1]["y"])

        item[162].append(file[name][21]["scared"][15]["tongue"][0]["x"])
        item[163].append(file[name][21]["scared"][15]["tongue"][1]["y"])

        item[164].append(file[name][22]["disgust"][0]["eyelid_up_left"][0]["x"])
        item[165].append(file[name][22]["disgust"][0]["eyelid_up_left"][1]["y"])
        item[166].append(file[name][22]["disgust"][1]["eyelid_up_right"][0]["x"])
        item[167].append(file[name][22]["disgust"][1]["eyelid_up_right"][1]["y"])
        item[168].append(file[name][22]["disgust"][2]["eyelid_down_left"][0]["x"])
        item[169].append(file[name][22]["disgust"][2]["eyelid_down_left"][1]["y"])
        item[170].append(file[name][22]["disgust"][3]["eyelid_down_right"][0]["x"])
        item[171].append(file[name][22]["disgust"][3]["eyelid_down_right"][1]["y"])

        item[172].append(file[name][22]["disgust"][4]["iris_left"][0]["x"])
        item[173].append(file[name][22]["disgust"][4]["iris_left"][1]["y"])
        item[174].append(file[name][22]["disgust"][5]["iris_right"][0]["x"])
        item[175].append(file[name][22]["disgust"][5]["iris_right"][1]["y"])

        item[176].append(file[name][22]["disgust"][6]["pupil_left"][0]["x"])
        item[177].append(file[name][22]["disgust"][6]["pupil_left"][1]["y"])
        item[178].append(file[name][22]["disgust"][7]["pupil_right"][0]["x"])
        item[179].append(file[name][22]["disgust"][7]["pupil_right"][1]["y"])

        item[180].append(file[name][22]["disgust"][8]["reflex_pupil_left"][0]["x"])
        item[181].append(file[name][22]["disgust"][8]["reflex_pupil_left"][1]["y"])
        item[182].append(file[name][22]["disgust"][9]["reflex_pupil_right"][0]["x"])
        item[183].append(file[name][22]["disgust"][9]["reflex_pupil_right"][1]["y"])
        item[184].append(file[name][22]["disgust"][10]["reflex_pupil_left_2"][0]["x"])
        item[185].append(file[name][22]["disgust"][10]["reflex_pupil_left_2"][1]["y"])
        item[186].append(file[name][22]["disgust"][11]["reflex_pupil_right_2"][0]["x"])
        item[187].append(file[name][22]["disgust"][11]["reflex_pupil_right_2"][1]["y"])

        item[188].append(file[name][22]["disgust"][12]["eyebrow_left"][0]["x"])
        item[189].append(file[name][22]["disgust"][12]["eyebrow_left"][1]["y"])
        item[190].append(file[name][22]["disgust"][13]["eyebrow_right"][0]["x"])
        item[191].append(file[name][22]["disgust"][13]["eyebrow_right"][1]["y"])

        item[192].append(file[name][22]["disgust"][14]["mouth"][0]["x"])
        item[193].append(file[name][22]["disgust"][14]["mouth"][1]["y"])

        item[194].append(file[name][22]["disgust"][15]["tongue"][0]["x"])
        item[195].append(file[name][22]["disgust"][15]["tongue"][1]["y"])

        item[196].append([file[name][0]["eye_left"][0]["identification"][0]["name"],
                          file[name][0]["eye_left"][0]["identification"][1]["id"]])
        item[197].append([file[name][1]["eye_right"][0]["identification"][0]["name"],
                          file[name][1]["eye_right"][0]["identification"][1]["id"]])
        item[198].append([file[name][2]["eyelid_up_left"][0]["identification"][0]["name"],
                          file[name][2]["eyelid_up_left"][0]["identification"][1]["id"]])
        item[199].append([file[name][3]["eyelid_up_right"][0]["identification"][0]["name"],
                          file[name][3]["eyelid_up_right"][0]["identification"][1]["id"]])
        item[200].append([file[name][4]["eyelid_down_left"][0]["identification"][0]["name"],
                          file[name][4]["eyelid_down_left"][0]["identification"][1]["id"]])
        item[201].append([file[name][5]["eyelid_down_right"][0]["identification"][0]["name"],
                          file[name][5]["eyelid_down_right"][0]["identification"][1]["id"]])
        item[202].append([file[name][6]["iris_left"][0]["identification"][0]["name"],
                          file[name][6]["iris_left"][0]["identification"][1]["id"]])
        item[203].append([file[name][7]["iris_right"][0]["identification"][0]["name"],
                          file[name][7]["iris_right"][0]["identification"][1]["id"]])
        item[204].append([file[name][8]["pupil_left"][0]["identification"][0]["name"],
                          file[name][8]["pupil_left"][0]["identification"][1]["id"]])
        item[205].append([file[name][9]["pupil_right"][0]["identification"][0]["name"],
                          file[name][9]["pupil_right"][0]["identification"][1]["id"]])
        item[206].append([file[name][10]["reflex_pupil_left"][0]["identification"][0]["name"],
                          file[name][10]["reflex_pupil_left"][0]["identification"][1]["id"]])
        item[207].append([file[name][11]["reflex_pupil_right"][0]["identification"][0]["name"],
                          file[name][11]["reflex_pupil_right"][0]["identification"][1]["id"]])
        item[208].append([file[name][12]["reflex_pupil_left_2"][0]["identification"][0]["name"],
                          file[name][12]["reflex_pupil_left_2"][0]["identification"][1]["id"]])
        item[209].append([file[name][13]["reflex_pupil_right_2"][0]["identification"][0]["name"],
                          file[name][13]["reflex_pupil_right_2"][0]["identification"][1]["id"]])
        item[210].append([file[name][14]["eyebrow_left"][0]["identification"][0]["name"],
                          file[name][14]["eyebrow_left"][0]["identification"][1]["id"]])
        item[211].append([file[name][15]["eyebrow_right"][0]["identification"][0]["name"],
                          file[name][15]["eyebrow_right"][0]["identification"][1]["id"]])
        item[212].append([file[name][16]["mouth"][0]["identification"][0]["name"],
                          file[name][16]["mouth"][0]["identification"][1]["id"]])
        item[213].append([file[name][17]["tongue"][0]["identification"][0]["name"],
                          file[name][17]["tongue"][0]["identification"][1]["id"]])

    return item


def checkPaint(name, item):
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        # Checking if each item wants to be painted
        if (file[name][0]["eye_left"][2]["exist"] == "yes"):
            eye_left = zip(item[0][0], item[1][0]) # (eye_left_x,eye_y)
            eye_left_colour = file[name][0]["eye_left"][1]["colour"]
        else:
            eye_left = [0, 0]
            eye_left_colour = None

        if (file[name][1]["eye_right"][2]["exist"] == "yes"):
            eye_right = zip(item[2][0], item[3][0])  # (eye_right_x,eye_y)
            eye_right_colour = file[name][1]["eye_right"][1]["colour"]
        else:
            eye_right = [0, 0]
            eye_right_colour = None

        if (file[name][2]["eyelid_up_left"][2]["exist"] == "yes"):
            eyelid_up_left = zip(item[4][0], item[5][0])  # (eyelid_up_left_x,eyelid_up_y)
            eyelid_up_left_colour = file[name][2]["eyelid_up_left"][1]["colour"]
            eyelid_up_left_angry = zip(item[36][0], item[37][0])
            eyelid_up_left_happiness = zip(item[68][0], item[69][0])
            eyelid_up_left_sadness = zip(item[100][0], item[101][0])
            eyelid_up_left_scared = zip(item[132][0], item[133][0])
            eyelid_up_left_disgust = zip(item[164][0], item[165][0])
        else:
            eyelid_up_left = [0, 0]
            eyelid_up_left_colour = None
            eyelid_up_left_angry = [0, 0]
            eyelid_up_left_happiness = [0, 0]
            eyelid_up_left_sadness = [0, 0]
            eyelid_up_left_scared = [0, 0]
            eyelid_up_left_disgust = [0, 0]

        if (file[name][3]["eyelid_up_right"][2]["exist"] == "yes"):
            eyelid_up_right = zip(item[6][0], item[7][0])  # (eyelid_up_right_x,eyelid_up_y)
            eyelid_up_right_colour = file[name][3]["eyelid_up_right"][1]["colour"]
            eyelid_up_right_angry = zip(item[38][0], item[39][0])
            eyelid_up_right_happiness = zip(item[70][0], item[71][0])
            eyelid_up_right_sadness = zip(item[102][0], item[103][0])
            eyelid_up_right_scared = zip(item[134][0], item[135][0])
            eyelid_up_right_disgust = zip(item[166][0], item[167][0])
        else:
            eyelid_up_right = [0, 0]
            eyelid_up_right_colour = None
            eyelid_up_right_angry = [0, 0]
            eyelid_up_right_happiness = [0, 0]
            eyelid_up_right_sadness = [0, 0]
            eyelid_up_right_scared = [0, 0]
            eyelid_up_right_disgust = [0, 0]

        if (file[name][4]["eyelid_down_left"][2]["exist"] == "yes"):
            eyelid_down_left = zip(item[8][0], item[9][0])  # (eyelid_down_left_x,eyelid_down_y)
            eyelid_down_left_colour = file[name][4]["eyelid_down_left"][1]["colour"]
            eyelid_down_left_angry = zip(item[40], item[41])
            eyelid_down_left_happiness = zip(item[72][0], item[73][0])
            eyelid_down_left_sadness = zip(item[104][0], item[105][0])
            eyelid_down_left_scared = zip(item[136][0], item[137][0])
            eyelid_down_left_disgust = zip(item[168][0], item[169][0])
        else:
            eyelid_down_left = [0, 0]
            eyelid_down_left_colour = None
            eyelid_down_left_angry = [0, 0]
            eyelid_down_left_happiness = [0, 0]
            eyelid_down_left_sadness = [0, 0]
            eyelid_down_left_scared = [0, 0]
            eyelid_down_left_disgust = [0, 0]

        if (file[name][5]["eyelid_down_right"][2]["exist"] == "yes"):
            eyelid_down_right = zip(item[10][0], item[11][0])  # (eyelid_down_right_x,eyelid_down_y)
            eyelid_down_right_colour = file[name][5]["eyelid_down_right"][1]["colour"]
            eyelid_down_right_angry = zip(item[42][0], item[43][0])
            eyelid_down_right_happiness = zip(item[74][0], item[75][0])
            eyelid_down_right_sadness = zip(item[106][0], item[107][0])
            eyelid_down_right_scared = zip(item[138][0], item[139][0])
            eyelid_down_right_disgust = zip(item[170][0], item[171][0])
        else:
            eyelid_down_right = [0, 0]
            eyelid_down_right_colour = None
            eyelid_down_right_angry = [0, 0]
            eyelid_down_right_happiness = [0, 0]
            eyelid_down_right_sadness = [0, 0]
            eyelid_down_right_scared = [0, 0]
            eyelid_down_right_disgust = [0, 0]

        if (file[name][6]["iris_left"][2]["exist"] == "yes"):
            iris_left = zip(item[12][0], item[13][0])  # (iris_left_x,iris_y)
            iris_left_colour = file[name][6]["iris_left"][1]["colour"]
            iris_left_angry = zip(item[76][0], item[77][0])
            iris_left_happiness = zip(item[76][0], item[77][0])
            iris_left_sadness = zip(item[108][0], item[109][0])
            iris_left_scared = zip(item[140][0], item[141][0])
            iris_left_disgust = zip(item[172][0], item[173][0])
        else:
            iris_left = [0, 0]
            iris_left_colour = None
            iris_left_angry = [0, 0]
            iris_left_happiness = [0, 0]
            iris_left_sadness = [0, 0]
            iris_left_scared = [0, 0]
            iris_left_disgust = [0, 0]

        if (file[name][7]["iris_right"][2]["exist"] == "yes"):
            iris_right = zip(item[14][0], item[15][0])  # (iris_left_x,iris_y)
            iris_right_colour = file[name][7]["iris_right"][1]["colour"]
            iris_right_angry = zip(item[46][0], item[47][0])
            iris_right_happiness = zip(item[78][0], item[79][0])
            iris_right_sadness = zip(item[110][0], item[111][0])
            iris_right_scared = zip(item[142][0], item[143][0])
            iris_right_disgust = zip(item[174][0], item[175][0])
        else:
            iris_right = [0, 0]
            iris_right_colour = None
            iris_right_angry = [0, 0]
            iris_right_happiness = [0, 0]
            iris_right_sadness = [0, 0]
            iris_right_scared = [0, 0]
            iris_right_disgust = [0, 0]

        if (file[name][8]["pupil_left"][2]["exist"] == "yes"):
            pupil_left = zip(item[16][0], item[17][0])  # (pupil_left_x,pupils_y)
            pupil_left_colour = file[name][8]["pupil_left"][1]["colour"]
            pupil_left_angry = zip(item[48][0], item[49][0])
            pupil_left_happiness = zip(item[80][0], item[81][0])
            pupil_left_sadness = zip(item[112][0], item[113][0])
            pupil_left_scared = zip(item[144][0], item[145][0])
            pupil_left_disgust = zip(item[176][0], item[177][0])
        else:
            pupil_left = [0, 0]
            pupil_left_colour = None
            pupil_left_angry = [0, 0]
            pupil_left_happiness = [0, 0]
            pupil_left_sadness = [0, 0]
            pupil_left_scared = [0, 0]
            pupil_left_disgust = [0, 0]

        if (file[name][9]["pupil_right"][2]["exist"] == "yes"):
            pupil_right = zip(item[18][0], item[19][0])  # (pupil_right_x,pupils_y)
            pupil_right_colour = file[name][9]["pupil_right"][1]["colour"]
            pupil_right_angry = zip(item[50][0], item[51][0])
            pupil_right_happiness = zip(item[82][0], item[83][0])
            pupil_right_sadness = zip(item[114][0], item[115][0])
            pupil_right_scared = zip(item[146][0], item[147][0])
            pupil_right_disgust = zip(item[178][0], item[179][0])
        else:
            pupil_right = [0, 0]
            pupil_right_colour = None
            pupil_right_angry = [0, 0]
            pupil_right_happiness = [0, 0]
            pupil_right_sadness = [0, 0]
            pupil_right_scared = [0, 0]
            pupil_right_disgust = [0, 0]

        if (file[name][10]["reflex_pupil_left"][2]["exist"] == "yes"):
            brightness_left = zip(item[20][0], item[21][0])  # (brightness_left_x,brightness_y)
            brightness_left_colour = file[name][10]["reflex_pupil_left"][1]["colour"]
            reflex_pupil_left_angry = zip(item[52][0], item[53][0])
            reflex_pupil_left_happiness = zip(item[84][0], item[85][0])
            reflex_pupil_left_sadness = zip(item[116][0], item[117][0])
            reflex_pupil_left_scared = zip(item[148][0], item[149][0])
            reflex_pupil_left_disgust = zip(item[180][0], item[181][0])
        else:
            brightness_left = [0, 0]
            brightness_left_colour = None
            reflex_pupil_left_angry = [0, 0]
            reflex_pupil_left_happiness = [0, 0]
            reflex_pupil_left_sadness = [0, 0]
            reflex_pupil_left_scared = [0, 0]
            reflex_pupil_left_disgust = [0, 0]

        if (file[name][11]["reflex_pupil_right"][2]["exist"] == "yes"):
            brightness_right = zip(item[22][0], item[23][0])  # (brightness_right_x,brightness_y)
            brightness_right_colour = file[name][11]["reflex_pupil_right"][1]["colour"]
            reflex_pupil_right_angry = zip(item[54][0], item[55][0])
            reflex_pupil_right_happiness = zip(item[86][0], item[87][0])
            reflex_pupil_right_sadness = zip(item[118][0], item[119][0])
            reflex_pupil_right_scared = zip(item[150][0], item[151][0])
            reflex_pupil_right_disgust = zip(item[182][0], item[183][0])
        else:
            brightness_right = [0, 0]
            brightness_right_colour = None
            reflex_pupil_right_angry = [0, 0]
            reflex_pupil_right_happiness = [0, 0]
            reflex_pupil_right_sadness = [0, 0]
            reflex_pupil_right_scared = [0, 0]
            reflex_pupil_right_disgust = [0, 0]

        if (file[name][12]["reflex_pupil_left_2"][2]["exist"] == "yes"):
            brightness_left2 = zip(item[24][0], item[25][0])  # (brightness_left_x2,brightness_y2)
            brightness_left2_colour = file[name][12]["reflex_pupil_left_2"][1]["colour"]
            reflex_pupil_left_2_angry = zip(item[56], item[57])
            reflex_pupil_left_2_happiness = zip(item[88][0], item[89][0])
            reflex_pupil_left_2_sadness = zip(item[120][0], item[121][0])
            reflex_pupil_left_2_scared = zip(item[152][0], item[153][0])
            reflex_pupil_left_2_disgust = zip(item[184][0], item[185][0])
        else:
            brightness_left2 = [0, 0]
            brightness_left2_colour = None
            reflex_pupil_left_2_angry = [0, 0]
            reflex_pupil_left_2_happiness = [0, 0]
            reflex_pupil_left_2_sadness = [0, 0]
            reflex_pupil_left_2_scared = [0, 0]
            reflex_pupil_left_2_disgust = [0, 0]

        if (file[name][13]["reflex_pupil_right_2"][2]["exist"] == "yes"):
            brightness_right2 = zip(item[26][0], item[27][0])  # (brightness_right_x2,brightness_y2)
            brightness_right2_colour = file[name][13]["reflex_pupil_right_2"][1]["colour"]
            reflex_pupil_right_2_angry = zip(item[58][0], item[59])
            reflex_pupil_right_2_happiness = zip(item[90][0], item[91][0])
            reflex_pupil_right_2_sadness = zip(item[122][0], item[123][0])
            reflex_pupil_right_2_scared = zip(item[154][0], item[155][0])
            reflex_pupil_right_2_disgust = zip(item[186][0], item[187][0])
        else:
            brightness_right2 = [0, 0]
            brightness_right2_colour = None
            reflex_pupil_right_2_angry = [0, 0]
            reflex_pupil_right_2_happiness = [0, 0]
            reflex_pupil_right_2_sadness = [0, 0]
            reflex_pupil_right_2_scared = [0, 0]
            reflex_pupil_right_2_disgust = [0, 0]

        if (file[name][14]["eyebrow_left"][2]["exist"] == "yes"):
            eyebrow_left = zip(item[28][0], item[29][0])  # (eyebrow_left_x,eyebrow_y2)
            eyebrow_left_colour = file[name][14]["eyebrow_left"][1]["colour"]
            eyebrow_left_angry = zip(item[60][0], item[61][0])
            eyebrow_left_happiness = zip(item[92][0], item[93][0])
            eyebrow_left_sadness = zip(item[124][0], item[125][0])
            eyebrow_left_scared = zip(item[156][0], item[157][0])
            eyebrow_left_disgust = zip(item[188][0], item[189][0])
        else:
            eyebrow_left = [0, 0]
            eyebrow_left_colour = None
            eyebrow_left_angry = [0, 0]
            eyebrow_left_happiness = [0, 0]
            eyebrow_left_sadness = [0, 0]
            eyebrow_left_scared = [0, 0]
            eyebrow_left_disgust = [0, 0]

        if (file[name][15]["eyebrow_right"][2]["exist"] == "yes"):
            eyebrow_right = zip(item[30][0], item[31][0])  # (eyebrow_right_x,eyebrow_y2)
            eyebrow_right_colour = file[name][15]["eyebrow_right"][1]["colour"]
            eyebrow_right_angry = zip(item[62][0], item[63][0])
            eyebrow_right_happiness = zip(item[94][0], item[95][0])
            eyebrow_right_sadness = zip(item[126][0], item[127][0])
            eyebrow_right_scared = zip(item[158][0], item[159][0])
            eyebrow_right_disgust = zip(item[190][0], item[191][0])
        else:
            eyebrow_right = [0, 0]
            eyebrow_right_colour = None
            eyebrow_right_angry = [0, 0]
            eyebrow_right_happiness = [0, 0]
            eyebrow_right_sadness = [0, 0]
            eyebrow_right_scared = [0, 0]
            eyebrow_right_disgust = [0, 0]

        if (file[name][16]["mouth"][2]["exist"] == "yes"):
            mouth = zip(item[32][0], item[33][0])  # (mouth_x,mouth_y)
            mouth_colour = file[name][16]["mouth"][1]["colour"]
            mouth_angry = zip(item[64][0], item[65][0])
            mouth_happiness = zip(item[96][0], item[97][0])
            mouth_sadness = zip(item[128][0], item[129][0])
            mouth_scared = zip(item[160][0], item[161][0])
            mouth_disgust = zip(item[192][0], item[193][0])
        else:
            mouth = [0, 0]
            mouth_colour = None
            mouth_angry = [0, 0]
            mouth_happiness = [0, 0]
            mouth_sadness = [0, 0]
            mouth_scared = [0, 0]
            mouth_disgust = [0, 0]

        if (file[name][17]["tongue"][2]["exist"] == "yes"):
            tongue = zip(item[34][0], item[35][0])  # (tongue_x,tongue_y)
            tongue_colour = file[name][17]["tongue"][1]["colour"]
            tongue_angry = zip(item[66][0], item[67][0])
            tongue_happiness = zip(item[98][0], item[99][0])
            tongue_sadness = zip(item[130][0], item[131][0])
            tongue_scared = zip(item[162][0], item[163][0])
            tongue_disgust = zip(item[194][0], item[195][0])
        else:
            tongue = [0, 0]
            tongue_colour = None
            tongue_angry = [0, 0]
            tongue_happiness = [0, 0]
            tongue_sadness = [0, 0]
            tongue_scared = [0, 0]
            tongue_disgust = [0, 0]

    to_paint = [eye_left,                       eye_left_colour,                eye_right,                      eye_right_colour,               eyelid_up_left,                 eyelid_up_left_colour,          eyelid_up_right,                eyelid_up_right_colour,         eyelid_down_left,               eyelid_down_left_colour,
                eyelid_down_right,              eyelid_down_right_colour,       iris_left,                      iris_left_colour,               iris_right,                     iris_right_colour,              pupil_left,                     pupil_left_colour,              pupil_right,                    pupil_right_colour,
                brightness_left,                brightness_left_colour,         brightness_right,               brightness_right_colour,        brightness_left2,               brightness_left2_colour,        brightness_right2,              brightness_right2_colour,       eyebrow_left,                   eyebrow_left_colour,
                eyebrow_right,                  eyebrow_right_colour,           mouth,                          mouth_colour,                   tongue,                         tongue_colour,                  eyelid_up_left_angry,           eyelid_up_left_happiness,       eyelid_up_left_sadness,         eyelid_up_left_scared,
                eyelid_up_left_disgust,         eyelid_up_right_angry,          eyelid_up_right_happiness,      eyelid_up_right_sadness,        eyelid_up_right_scared,         eyelid_up_right_disgust,        eyelid_down_left_angry,         eyelid_down_left_happiness,     eyelid_down_left_sadness,       eyelid_down_left_scared,
                eyelid_down_left_disgust,       eyelid_down_right_angry,        eyelid_down_right_happiness,    eyelid_down_right_sadness,      eyelid_down_right_scared,       eyelid_down_right_disgust,      iris_left_angry,                iris_left_happiness,            iris_left_sadness,              iris_left_scared,
                iris_left_disgust,              iris_right_angry,               iris_right_happiness,           iris_right_sadness,             iris_right_scared,              iris_right_disgust,             pupil_left_angry,               pupil_left_happiness,           pupil_left_sadness,             pupil_left_scared,
                pupil_left_disgust,             pupil_right_angry,              pupil_right_happiness,          pupil_right_sadness,            pupil_right_scared,             pupil_right_disgust,            reflex_pupil_left_angry,        reflex_pupil_left_happiness,    reflex_pupil_left_sadness,      reflex_pupil_left_scared,
                reflex_pupil_left_disgust,      reflex_pupil_right_angry,       reflex_pupil_right_happiness,   reflex_pupil_right_sadness,     reflex_pupil_right_scared,      reflex_pupil_right_disgust,     reflex_pupil_left_2_angry,      reflex_pupil_left_2_happiness,  reflex_pupil_left_2_sadness,    reflex_pupil_left_2_scared,
                reflex_pupil_left_2_disgust,    reflex_pupil_right_2_angry,     reflex_pupil_right_2_happiness, reflex_pupil_right_2_sadness,   reflex_pupil_right_2_scared,    reflex_pupil_right_2_disgust,   eyebrow_left_angry,             eyebrow_left_happiness,         eyebrow_left_sadness,           eyebrow_left_scared,
                eyebrow_left_disgust,           eyebrow_right_angry,            eyebrow_right_happiness,        eyebrow_right_sadness,          eyebrow_right_scared,           eyebrow_right_disgust,          mouth_angry,                    mouth_happiness,                mouth_sadness,                  mouth_scared,
                mouth_disgust,                  tongue_angry,                   tongue_happiness,               tongue_sadness,                 tongue_scared,                  tongue_disgust]

    return to_paint


def searchPositionPart(name, part):
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        for i in xrange(196, 214):
            if part == load_file(name)[i][0][0]:
                return i - 196


def delete_part(name, part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json', 'r+') as data_file:
        file = json.load(data_file)
        if file[name][searchPositionPart("cozmo", part)][part][2]["exist"] == "yes":
            file[name][searchPositionPart("cozmo", part)][part][2]["exist"] = "no"
            data_file.seek(0)
            json.dump(file, data_file, indent=4)
            data_file.truncate()


def create_part(name, part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json', 'r+') as data_file:
        file = json.load(data_file)
        if file[name][searchPositionPart("cozmo", part)][part][2]["exist"] == "no":
            file[name][searchPositionPart("cozmo", part)][part][2]["exist"] = "yes"
            data_file.seek(0)
            json.dump(file, data_file, indent=4)
            data_file.truncate()


