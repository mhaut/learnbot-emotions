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

            item[36].append(file[name][18]["angry"][0]["eyelid_up_left"][0]["x"][i][str(i)])
            item[37].append(file[name][18]["angry"][0]["eyelid_up_left"][1]["y"][i][str(i)])
            item[38].append(file[name][18]["angry"][1]["eyelid_up_right"][0]["x"][i][str(i)])
            item[39].append(file[name][18]["angry"][1]["eyelid_up_right"][1]["y"][i][str(i)])
            item[40].append(file[name][18]["angry"][2]["eyelid_down_left"][0]["x"][i][str(i)])
            item[41].append(file[name][18]["angry"][2]["eyelid_down_left"][1]["y"][i][str(i)])
            item[42].append(file[name][18]["angry"][3]["eyelid_down_right"][0]["x"][i][str(i)])
            item[43].append(file[name][18]["angry"][3]["eyelid_down_right"][1]["y"][i][str(i)])

            item[44].append(file[name][18]["angry"][4]["iris_left"][0]["x"][i][str(i)])
            item[45].append(file[name][18]["angry"][4]["iris_left"][1]["y"][i][str(i)])
            item[46].append(file[name][18]["angry"][5]["iris_right"][0]["x"][i][str(i)])
            item[47].append(file[name][18]["angry"][5]["iris_right"][1]["y"][i][str(i)])

            item[48].append(file[name][18]["angry"][6]["pupil_left"][0]["x"][i][str(i)])
            item[49].append(file[name][18]["angry"][6]["pupil_left"][1]["y"][i][str(i)])
            item[50].append(file[name][18]["angry"][7]["pupil_right"][0]["x"][i][str(i)])
            item[51].append(file[name][18]["angry"][7]["pupil_right"][1]["y"][i][str(i)])

            item[52].append(file[name][18]["angry"][8]["reflex_pupil_left"][0]["x"][i][str(i)])
            item[53].append(file[name][18]["angry"][8]["reflex_pupil_left"][1]["y"][i][str(i)])
            item[54].append(file[name][18]["angry"][9]["reflex_pupil_right"][0]["x"][i][str(i)])
            item[55].append(file[name][18]["angry"][9]["reflex_pupil_right"][1]["y"][i][str(i)])
            item[56].append(file[name][18]["angry"][10]["reflex_pupil_left_2"][0]["x"][i][str(i)])
            item[57].append(file[name][18]["angry"][10]["reflex_pupil_left_2"][1]["y"][i][str(i)])
            item[58].append(file[name][18]["angry"][11]["reflex_pupil_right_2"][0]["x"][i][str(i)])
            item[59].append(file[name][18]["angry"][11]["reflex_pupil_right_2"][1]["y"][i][str(i)])

            item[60].append(file[name][18]["angry"][12]["eyebrow_left"][0]["x"][i][str(i)])
            item[61].append(file[name][18]["angry"][12]["eyebrow_left"][1]["y"][i][str(i)])
            item[62].append(file[name][18]["angry"][13]["eyebrow_right"][0]["x"][i][str(i)])
            item[63].append(file[name][18]["angry"][13]["eyebrow_right"][1]["y"][i][str(i)])

            item[64].append(file[name][18]["angry"][14]["mouth"][0]["x"][i][str(i)])
            item[65].append(file[name][18]["angry"][14]["mouth"][1]["y"][i][str(i)])

            item[66].append(file[name][18]["angry"][15]["tongue"][0]["x"][i][str(i)])
            item[67].append(file[name][18]["angry"][15]["tongue"][1]["y"][i][str(i)])

            item[68].append(file[name][19]["happiness"][0]["eyelid_up_left"][0]["x"][i][str(i)])
            item[69].append(file[name][19]["happiness"][0]["eyelid_up_left"][1]["y"][i][str(i)])
            item[70].append(file[name][19]["happiness"][1]["eyelid_up_right"][0]["x"][i][str(i)])
            item[71].append(file[name][19]["happiness"][1]["eyelid_up_right"][1]["y"][i][str(i)])
            item[72].append(file[name][19]["happiness"][2]["eyelid_down_left"][0]["x"][i][str(i)])
            item[73].append(file[name][19]["happiness"][2]["eyelid_down_left"][1]["y"][i][str(i)])
            item[74].append(file[name][19]["happiness"][3]["eyelid_down_right"][0]["x"][i][str(i)])
            item[75].append(file[name][19]["happiness"][3]["eyelid_down_right"][1]["y"][i][str(i)])

            item[76].append(file[name][19]["happiness"][4]["iris_left"][0]["x"][i][str(i)])
            item[77].append(file[name][19]["happiness"][4]["iris_left"][1]["y"][i][str(i)])
            item[78].append(file[name][19]["happiness"][5]["iris_right"][0]["x"][i][str(i)])
            item[79].append(file[name][19]["happiness"][5]["iris_right"][1]["y"][i][str(i)])

            item[80].append(file[name][19]["happiness"][6]["pupil_left"][0]["x"][i][str(i)])
            item[81].append(file[name][19]["happiness"][6]["pupil_left"][1]["y"][i][str(i)])
            item[82].append(file[name][19]["happiness"][7]["pupil_right"][0]["x"][i][str(i)])
            item[83].append(file[name][19]["happiness"][7]["pupil_right"][1]["y"][i][str(i)])

            item[84].append(file[name][19]["happiness"][8]["reflex_pupil_left"][0]["x"][i][str(i)])
            item[85].append(file[name][19]["happiness"][8]["reflex_pupil_left"][1]["y"][i][str(i)])
            item[86].append(file[name][19]["happiness"][9]["reflex_pupil_right"][0]["x"][i][str(i)])
            item[87].append(file[name][19]["happiness"][9]["reflex_pupil_right"][1]["y"][i][str(i)])
            item[88].append(file[name][19]["happiness"][10]["reflex_pupil_left_2"][0]["x"][i][str(i)])
            item[89].append(file[name][19]["happiness"][10]["reflex_pupil_left_2"][1]["y"][i][str(i)])
            item[90].append(file[name][19]["happiness"][11]["reflex_pupil_right_2"][0]["x"][i][str(i)])
            item[91].append(file[name][19]["happiness"][11]["reflex_pupil_right_2"][1]["y"][i][str(i)])

            item[92].append(file[name][19]["happiness"][12]["eyebrow_left"][0]["x"][i][str(i)])
            item[93].append(file[name][19]["happiness"][12]["eyebrow_left"][1]["y"][i][str(i)])
            item[94].append(file[name][19]["happiness"][13]["eyebrow_right"][0]["x"][i][str(i)])
            item[95].append(file[name][19]["happiness"][13]["eyebrow_right"][1]["y"][i][str(i)])

            item[96].append(file[name][19]["happiness"][14]["mouth"][0]["x"][i][str(i)])
            item[97].append(file[name][19]["happiness"][14]["mouth"][1]["y"][i][str(i)])

            item[98].append(file[name][19]["happiness"][15]["tongue"][0]["x"][i][str(i)])
            item[99].append(file[name][19]["happiness"][15]["tongue"][1]["y"][i][str(i)])

            item[100].append(file[name][20]["sadness"][0]["eyelid_up_left"][0]["x"][i][str(i)])
            item[101].append(file[name][20]["sadness"][0]["eyelid_up_left"][1]["y"][i][str(i)])
            item[102].append(file[name][20]["sadness"][1]["eyelid_up_right"][0]["x"][i][str(i)])
            item[103].append(file[name][20]["sadness"][1]["eyelid_up_right"][1]["y"][i][str(i)])
            item[104].append(file[name][20]["sadness"][2]["eyelid_down_left"][0]["x"][i][str(i)])
            item[105].append(file[name][20]["sadness"][2]["eyelid_down_left"][1]["y"][i][str(i)])
            item[106].append(file[name][20]["sadness"][3]["eyelid_down_right"][0]["x"][i][str(i)])
            item[107].append(file[name][20]["sadness"][3]["eyelid_down_right"][1]["y"][i][str(i)])

            item[108].append(file[name][20]["sadness"][4]["iris_left"][0]["x"][i][str(i)])
            item[109].append(file[name][20]["sadness"][4]["iris_left"][1]["y"][i][str(i)])
            item[110].append(file[name][20]["sadness"][5]["iris_right"][0]["x"][i][str(i)])
            item[111].append(file[name][20]["sadness"][5]["iris_right"][1]["y"][i][str(i)])

            item[112].append(file[name][20]["sadness"][6]["pupil_left"][0]["x"][i][str(i)])
            item[113].append(file[name][20]["sadness"][6]["pupil_left"][1]["y"][i][str(i)])
            item[114].append(file[name][20]["sadness"][7]["pupil_right"][0]["x"][i][str(i)])
            item[115].append(file[name][20]["sadness"][7]["pupil_right"][1]["y"][i][str(i)])

            item[116].append(file[name][20]["sadness"][8]["reflex_pupil_left"][0]["x"][i][str(i)])
            item[117].append(file[name][20]["sadness"][8]["reflex_pupil_left"][1]["y"][i][str(i)])
            item[118].append(file[name][20]["sadness"][9]["reflex_pupil_right"][0]["x"][i][str(i)])
            item[119].append(file[name][20]["sadness"][9]["reflex_pupil_right"][1]["y"][i][str(i)])
            item[120].append(file[name][20]["sadness"][10]["reflex_pupil_left_2"][0]["x"][i][str(i)])
            item[121].append(file[name][20]["sadness"][10]["reflex_pupil_left_2"][1]["y"][i][str(i)])
            item[122].append(file[name][20]["sadness"][11]["reflex_pupil_right_2"][0]["x"][i][str(i)])
            item[123].append(file[name][20]["sadness"][11]["reflex_pupil_right_2"][1]["y"][i][str(i)])

            item[124].append(file[name][20]["sadness"][12]["eyebrow_left"][0]["x"][i][str(i)])
            item[125].append(file[name][20]["sadness"][12]["eyebrow_left"][1]["y"][i][str(i)])
            item[126].append(file[name][20]["sadness"][13]["eyebrow_right"][0]["x"][i][str(i)])
            item[127].append(file[name][20]["sadness"][13]["eyebrow_right"][1]["y"][i][str(i)])

            item[128].append(file[name][20]["sadness"][14]["mouth"][0]["x"][i][str(i)])
            item[129].append(file[name][20]["sadness"][14]["mouth"][1]["y"][i][str(i)])

            item[130].append(file[name][20]["sadness"][15]["tongue"][0]["x"][i][str(i)])
            item[131].append(file[name][20]["sadness"][15]["tongue"][1]["y"][i][str(i)])

            item[132].append(file[name][21]["scared"][0]["eyelid_up_left"][0]["x"][i][str(i)])
            item[133].append(file[name][21]["scared"][0]["eyelid_up_left"][1]["y"][i][str(i)])
            item[134].append(file[name][21]["scared"][1]["eyelid_up_right"][0]["x"][i][str(i)])
            item[135].append(file[name][21]["scared"][1]["eyelid_up_right"][1]["y"][i][str(i)])
            item[136].append(file[name][21]["scared"][2]["eyelid_down_left"][0]["x"][i][str(i)])
            item[137].append(file[name][21]["scared"][2]["eyelid_down_left"][1]["y"][i][str(i)])
            item[138].append(file[name][21]["scared"][3]["eyelid_down_right"][0]["x"][i][str(i)])
            item[139].append(file[name][21]["scared"][3]["eyelid_down_right"][1]["y"][i][str(i)])

            item[140].append(file[name][21]["scared"][4]["iris_left"][0]["x"][i][str(i)])
            item[141].append(file[name][21]["scared"][4]["iris_left"][1]["y"][i][str(i)])
            item[142].append(file[name][21]["scared"][5]["iris_right"][0]["x"][i][str(i)])
            item[143].append(file[name][21]["scared"][5]["iris_right"][1]["y"][i][str(i)])

            item[144].append(file[name][21]["scared"][6]["pupil_left"][0]["x"][i][str(i)])
            item[145].append(file[name][21]["scared"][6]["pupil_left"][1]["y"][i][str(i)])
            item[146].append(file[name][21]["scared"][7]["pupil_right"][0]["x"][i][str(i)])
            item[147].append(file[name][21]["scared"][7]["pupil_right"][1]["y"][i][str(i)])

            item[148].append(file[name][21]["scared"][8]["reflex_pupil_left"][0]["x"][i][str(i)])
            item[149].append(file[name][21]["scared"][8]["reflex_pupil_left"][1]["y"][i][str(i)])
            item[150].append(file[name][21]["scared"][9]["reflex_pupil_right"][0]["x"][i][str(i)])
            item[151].append(file[name][21]["scared"][9]["reflex_pupil_right"][1]["y"][i][str(i)])
            item[152].append(file[name][21]["scared"][10]["reflex_pupil_left_2"][0]["x"][i][str(i)])
            item[153].append(file[name][21]["scared"][10]["reflex_pupil_left_2"][1]["y"][i][str(i)])
            item[154].append(file[name][21]["scared"][11]["reflex_pupil_right_2"][0]["x"][i][str(i)])
            item[155].append(file[name][21]["scared"][11]["reflex_pupil_right_2"][1]["y"][i][str(i)])

            item[156].append(file[name][21]["scared"][12]["eyebrow_left"][0]["x"][i][str(i)])
            item[157].append(file[name][21]["scared"][12]["eyebrow_left"][1]["y"][i][str(i)])
            item[158].append(file[name][21]["scared"][13]["eyebrow_right"][0]["x"][i][str(i)])
            item[159].append(file[name][21]["scared"][13]["eyebrow_right"][1]["y"][i][str(i)])

            item[160].append(file[name][21]["scared"][14]["mouth"][0]["x"][i][str(i)])
            item[161].append(file[name][21]["scared"][14]["mouth"][1]["y"][i][str(i)])

            item[162].append(file[name][21]["scared"][15]["tongue"][0]["x"][i][str(i)])
            item[163].append(file[name][21]["scared"][15]["tongue"][1]["y"][i][str(i)])

            item[164].append(file[name][22]["disgust"][0]["eyelid_up_left"][0]["x"][i][str(i)])
            item[165].append(file[name][22]["disgust"][0]["eyelid_up_left"][1]["y"][i][str(i)])
            item[166].append(file[name][22]["disgust"][1]["eyelid_up_right"][0]["x"][i][str(i)])
            item[167].append(file[name][22]["disgust"][1]["eyelid_up_right"][1]["y"][i][str(i)])
            item[168].append(file[name][22]["disgust"][2]["eyelid_down_left"][0]["x"][i][str(i)])
            item[169].append(file[name][22]["disgust"][2]["eyelid_down_left"][1]["y"][i][str(i)])
            item[170].append(file[name][22]["disgust"][3]["eyelid_down_right"][0]["x"][i][str(i)])
            item[171].append(file[name][22]["disgust"][3]["eyelid_down_right"][1]["y"][i][str(i)])

            item[172].append(file[name][22]["disgust"][4]["iris_left"][0]["x"][i][str(i)])
            item[173].append(file[name][22]["disgust"][4]["iris_left"][1]["y"][i][str(i)])
            item[174].append(file[name][22]["disgust"][5]["iris_right"][0]["x"][i][str(i)])
            item[175].append(file[name][22]["disgust"][5]["iris_right"][1]["y"][i][str(i)])

            item[176].append(file[name][22]["disgust"][6]["pupil_left"][0]["x"][i][str(i)])
            item[177].append(file[name][22]["disgust"][6]["pupil_left"][1]["y"][i][str(i)])
            item[178].append(file[name][22]["disgust"][7]["pupil_right"][0]["x"][i][str(i)])
            item[179].append(file[name][22]["disgust"][7]["pupil_right"][1]["y"][i][str(i)])

            item[180].append(file[name][22]["disgust"][8]["reflex_pupil_left"][0]["x"][i][str(i)])
            item[181].append(file[name][22]["disgust"][8]["reflex_pupil_left"][1]["y"][i][str(i)])
            item[182].append(file[name][22]["disgust"][9]["reflex_pupil_right"][0]["x"][i][str(i)])
            item[183].append(file[name][22]["disgust"][9]["reflex_pupil_right"][1]["y"][i][str(i)])
            item[184].append(file[name][22]["disgust"][10]["reflex_pupil_left_2"][0]["x"][i][str(i)])
            item[185].append(file[name][22]["disgust"][10]["reflex_pupil_left_2"][1]["y"][i][str(i)])
            item[186].append(file[name][22]["disgust"][11]["reflex_pupil_right_2"][0]["x"][i][str(i)])
            item[187].append(file[name][22]["disgust"][11]["reflex_pupil_right_2"][1]["y"][i][str(i)])

            item[188].append(file[name][22]["disgust"][12]["eyebrow_left"][0]["x"][i][str(i)])
            item[189].append(file[name][22]["disgust"][12]["eyebrow_left"][1]["y"][i][str(i)])
            item[190].append(file[name][22]["disgust"][13]["eyebrow_right"][0]["x"][i][str(i)])
            item[191].append(file[name][22]["disgust"][13]["eyebrow_right"][1]["y"][i][str(i)])

            item[192].append(file[name][22]["disgust"][14]["mouth"][0]["x"][i][str(i)])
            item[193].append(file[name][22]["disgust"][14]["mouth"][1]["y"][i][str(i)])

            item[194].append(file[name][22]["disgust"][15]["tongue"][0]["x"][i][str(i)])
            item[195].append(file[name][22]["disgust"][15]["tongue"][1]["y"][i][str(i)])

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
            eyelid_up_left_angry = zip(item[36], item[37])
            eyelid_up_left_happiness = zip(item[68], item[69])
            eyelid_up_left_sadness = zip(item[100], item[101])
            eyelid_up_left_scared = zip(item[132], item[133])
            eyelid_up_left_disgust = zip(item[164], item[165])
        else:
            eyelid_up_left = [0, 0]
            eyelid_up_left_colour = None
            eyelid_up_left_angry = [0, 0]
            eyelid_up_left_happiness = [0, 0]
            eyelid_up_left_sadness = [0, 0]
            eyelid_up_left_scared = [0, 0]
            eyelid_up_left_disgust = [0, 0]

        if (file[name][3]["eyelid_up_right"][2]["exist"] == "yes"):
            eyelid_up_right = zip(item[6], item[7])  # (eyelid_up_right_x,eyelid_up_y)
            eyelid_up_right_colour = file[name][3]["eyelid_up_right"][1]["colour"]
            eyelid_up_right_angry = zip(item[38], item[39])
            eyelid_up_right_happiness = zip(item[70], item[71])
            eyelid_up_right_sadness = zip(item[102], item[103])
            eyelid_up_right_scared = zip(item[134], item[135])
            eyelid_up_right_disgust = zip(item[166], item[167])
        else:
            eyelid_up_right = [0, 0]
            eyelid_up_right_colour = None
            eyelid_up_right_angry = [0, 0]
            eyelid_up_right_happiness = [0, 0]
            eyelid_up_right_sadness = [0, 0]
            eyelid_up_right_scared = [0, 0]
            eyelid_up_right_disgust = [0, 0]

        if (file[name][4]["eyelid_down_left"][2]["exist"] == "yes"):
            eyelid_down_left = zip(item[8], item[9])  # (eyelid_down_left_x,eyelid_down_y)
            eyelid_down_left_colour = file[name][4]["eyelid_down_left"][1]["colour"]
            eyelid_down_left_angry = zip(item[40], item[41])
            eyelid_down_left_happiness = zip(item[72], item[73])
            eyelid_down_left_sadness = zip(item[104], item[105])
            eyelid_down_left_scared = zip(item[136], item[137])
            eyelid_down_left_disgust = zip(item[168], item[169])
        else:
            eyelid_down_left = [0, 0]
            eyelid_down_left_colour = None
            eyelid_down_left_angry = [0, 0]
            eyelid_down_left_happiness = [0, 0]
            eyelid_down_left_sadness = [0, 0]
            eyelid_down_left_scared = [0, 0]
            eyelid_down_left_disgust = [0, 0]

        if (file[name][5]["eyelid_down_right"][2]["exist"] == "yes"):
            eyelid_down_right = zip(item[10], item[11])  # (eyelid_down_right_x,eyelid_down_y)
            eyelid_down_right_colour = file[name][5]["eyelid_down_right"][1]["colour"]
            eyelid_down_right_angry = zip(item[42], item[43])
            eyelid_down_right_happiness = zip(item[74], item[75])
            eyelid_down_right_sadness = zip(item[106], item[107])
            eyelid_down_right_scared = zip(item[138], item[139])
            eyelid_down_right_disgust = zip(item[170], item[171])
        else:
            eyelid_down_right = [0, 0]
            eyelid_down_right_colour = None
            eyelid_down_right_angry = [0, 0]
            eyelid_down_right_happiness = [0, 0]
            eyelid_down_right_sadness = [0, 0]
            eyelid_down_right_scared = [0, 0]
            eyelid_down_right_disgust = [0, 0]

        if (file[name][6]["iris_left"][2]["exist"] == "yes"):
            iris_left = zip(item[12], item[13])  # (iris_left_x,iris_y)
            iris_left_colour = file[name][6]["iris_left"][1]["colour"]
            iris_left_angry = zip(item[44], item[45])
            iris_left_happiness = zip(item[76], item[77])
            iris_left_sadness = zip(item[108], item[109])
            iris_left_scared = zip(item[140], item[141])
            iris_left_disgust = zip(item[172], item[173])
        else:
            iris_left = [0, 0]
            iris_left_colour = None
            iris_left_angry = [0, 0]
            iris_left_happiness = [0, 0]
            iris_left_sadness = [0, 0]
            iris_left_scared = [0, 0]
            iris_left_disgust = [0, 0]

        if (file[name][7]["iris_right"][2]["exist"] == "yes"):
            iris_right = zip(item[14], item[15])  # (iris_left_x,iris_y)
            iris_right_colour = file[name][7]["iris_right"][1]["colour"]
            iris_right_angry = zip(item[46], item[47])
            iris_right_happiness = zip(item[78], item[79])
            iris_right_sadness = zip(item[110], item[111])
            iris_right_scared = zip(item[142], item[143])
            iris_right_disgust = zip(item[174], item[175])
        else:
            iris_right = [0, 0]
            iris_right_colour = None
            iris_right_angry = [0, 0]
            iris_right_happiness = [0, 0]
            iris_right_sadness = [0, 0]
            iris_right_scared = [0, 0]
            iris_right_disgust = [0, 0]

        if (file[name][8]["pupil_left"][2]["exist"] == "yes"):
            pupil_left = zip(item[16], item[17])  # (pupil_left_x,pupils_y)
            pupil_left_colour = file[name][8]["pupil_left"][1]["colour"]
            pupil_left_angry = zip(item[48], item[49])
            pupil_left_happiness = zip(item[80], item[81])
            pupil_left_sadness = zip(item[112], item[113])
            pupil_left_scared = zip(item[144], item[145])
            pupil_left_disgust = zip(item[176], item[177])
        else:
            pupil_left = [0, 0]
            pupil_left_colour = None
            pupil_left_angry = [0, 0]
            pupil_left_happiness = [0, 0]
            pupil_left_sadness = [0, 0]
            pupil_left_scared = [0, 0]
            pupil_left_disgust = [0, 0]

        if (file[name][9]["pupil_right"][2]["exist"] == "yes"):
            pupil_right = zip(item[18], item[19])  # (pupil_right_x,pupils_y)
            pupil_right_colour = file[name][9]["pupil_right"][1]["colour"]
            pupil_right_angry = zip(item[50], item[51])
            pupil_right_happiness = zip(item[82], item[83])
            pupil_right_sadness = zip(item[114], item[115])
            pupil_right_scared = zip(item[146], item[147])
            pupil_right_disgust = zip(item[178], item[179])
        else:
            pupil_right = [0, 0]
            pupil_right_colour = None
            pupil_right_angry = [0, 0]
            pupil_right_happiness = [0, 0]
            pupil_right_sadness = [0, 0]
            pupil_right_scared = [0, 0]
            pupil_right_disgust = [0, 0]

        if (file[name][10]["reflex_pupil_left"][2]["exist"] == "yes"):
            brightness_left = zip(item[20], item[21])  # (brightness_left_x,brightness_y)
            brightness_left_colour = file[name][10]["reflex_pupil_left"][1]["colour"]
            reflex_pupil_left_angry = zip(item[52], item[53])
            reflex_pupil_left_happiness = zip(item[84], item[85])
            reflex_pupil_left_sadness = zip(item[116], item[117])
            reflex_pupil_left_scared = zip(item[148], item[149])
            reflex_pupil_left_disgust = zip(item[180], item[181])
        else:
            brightness_left = [0, 0]
            brightness_left_colour = None
            reflex_pupil_left_angry = [0, 0]
            reflex_pupil_left_happiness = [0, 0]
            reflex_pupil_left_sadness = [0, 0]
            reflex_pupil_left_scared = [0, 0]
            reflex_pupil_left_disgust = [0, 0]

        if (file[name][11]["reflex_pupil_right"][2]["exist"] == "yes"):
            brightness_right = zip(item[22], item[23])  # (brightness_right_x,brightness_y)
            brightness_right_colour = file[name][11]["reflex_pupil_right"][1]["colour"]
            reflex_pupil_right_angry = zip(item[54], item[55])
            reflex_pupil_right_happiness = zip(item[86], item[87])
            reflex_pupil_right_sadness = zip(item[118], item[119])
            reflex_pupil_right_scared = zip(item[150], item[151])
            reflex_pupil_right_disgust = zip(item[182], item[183])
        else:
            brightness_right = [0, 0]
            brightness_right_colour = None
            reflex_pupil_right_angry = [0, 0]
            reflex_pupil_right_happiness = [0, 0]
            reflex_pupil_right_sadness = [0, 0]
            reflex_pupil_right_scared = [0, 0]
            reflex_pupil_right_disgust = [0, 0]

        if (file[name][12]["reflex_pupil_left_2"][2]["exist"] == "yes"):
            brightness_left2 = zip(item[24], item[25])  # (brightness_left_x2,brightness_y2)
            brightness_left2_colour = file[name][12]["reflex_pupil_left_2"][1]["colour"]
            reflex_pupil_left_2_angry = zip(item[56], item[57])
            reflex_pupil_left_2_happiness = zip(item[88], item[89])
            reflex_pupil_left_2_sadness = zip(item[120], item[121])
            reflex_pupil_left_2_scared = zip(item[152], item[153])
            reflex_pupil_left_2_disgust = zip(item[184], item[185])
        else:
            brightness_left2 = [0, 0]
            brightness_left2_colour = None
            reflex_pupil_left_2_angry = [0, 0]
            reflex_pupil_left_2_happiness = [0, 0]
            reflex_pupil_left_2_sadness = [0, 0]
            reflex_pupil_left_2_scared = [0, 0]
            reflex_pupil_left_2_disgust = [0, 0]

        if (file[name][13]["reflex_pupil_right_2"][2]["exist"] == "yes"):
            brightness_right2 = zip(item[26], item[27])  # (brightness_right_x2,brightness_y2)
            brightness_right2_colour = file[name][13]["reflex_pupil_right_2"][1]["colour"]
            reflex_pupil_right_2_angry = zip(item[58], item[59])
            reflex_pupil_right_2_happiness = zip(item[90], item[91])
            reflex_pupil_right_2_sadness = zip(item[122], item[123])
            reflex_pupil_right_2_scared = zip(item[154], item[155])
            reflex_pupil_right_2_disgust = zip(item[186], item[187])
        else:
            brightness_right2 = [0, 0]
            brightness_right2_colour = None
            reflex_pupil_right_2_angry = [0, 0]
            reflex_pupil_right_2_happiness = [0, 0]
            reflex_pupil_right_2_sadness = [0, 0]
            reflex_pupil_right_2_scared = [0, 0]
            reflex_pupil_right_2_disgust = [0, 0]

        if (file[name][14]["eyebrow_left"][2]["exist"] == "yes"):
            eyebrow_left = zip(item[28], item[29])  # (eyebrow_left_x,eyebrow_y2)
            eyebrow_left_colour = file[name][14]["eyebrow_left"][1]["colour"]
            eyebrow_left_angry = zip(item[60], item[61])
            eyebrow_left_happiness = zip(item[92], item[93])
            eyebrow_left_sadness = zip(item[124], item[125])
            eyebrow_left_scared = zip(item[156], item[157])
            eyebrow_left_disgust = zip(item[188], item[189])
        else:
            eyebrow_left = [0, 0]
            eyebrow_left_colour = None
            eyebrow_left_angry = [0, 0]
            eyebrow_left_happiness = [0, 0]
            eyebrow_left_sadness = [0, 0]
            eyebrow_left_scared = [0, 0]
            eyebrow_left_disgust = [0, 0]

        if (file[name][15]["eyebrow_right"][2]["exist"] == "yes"):
            eyebrow_right = zip(item[30], item[31])  # (eyebrow_right_x,eyebrow_y2)
            eyebrow_right_colour = file[name][15]["eyebrow_right"][1]["colour"]
            eyebrow_right_angry = zip(item[62], item[63])
            eyebrow_right_happiness = zip(item[94], item[95])
            eyebrow_right_sadness = zip(item[126], item[127])
            eyebrow_right_scared = zip(item[158], item[159])
            eyebrow_right_disgust = zip(item[190], item[191])
        else:
            eyebrow_right = [0, 0]
            eyebrow_right_colour = None
            eyebrow_right_angry = [0, 0]
            eyebrow_right_happiness = [0, 0]
            eyebrow_right_sadness = [0, 0]
            eyebrow_right_scared = [0, 0]
            eyebrow_right_disgust = [0, 0]

        if (file[name][16]["mouth"][2]["exist"] == "yes"):
            mouth = zip(item[32], item[33])  # (mouth_x,mouth_y)
            mouth_colour = file[name][16]["mouth"][1]["colour"]
            mouth_angry = zip(item[64], item[65])
            mouth_happiness = zip(item[96], item[97])
            mouth_sadness = zip(item[128], item[129])
            mouth_scared = zip(item[160], item[161])
            mouth_disgust = zip(item[192], item[193])
        else:
            mouth = [0, 0]
            mouth_colour = None
            mouth_angry = [0, 0]
            mouth_happiness = [0, 0]
            mouth_sadness = [0, 0]
            mouth_scared = [0, 0]
            mouth_disgust = [0, 0]

        if (file[name][17]["tongue"][2]["exist"] == "yes"):
            tongue = zip(item[34], item[35])  # (tongue_x,tongue_y)
            tongue_colour = file[name][17]["tongue"][1]["colour"]
            tongue_angry = zip(item[66], item[67])
            tongue_happiness = zip(item[98], item[99])
            tongue_sadness = zip(item[130], item[131])
            tongue_scared = zip(item[162], item[163])
            tongue_disgust = zip(item[194], item[195])
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
