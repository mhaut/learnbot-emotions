import json

from PyQt4.QtCore import QPointF


def load_file(name):
    # Initializing the points that define the geometry of the elements
    #  item ( eye_left_x[], eye_right[], eyes_y[], iris_left_x[], iris_right_x[], iris_y[], pupil_left_x[], pupil_right_x[], pupils_y[],
    #  brightness_left_x[], brightness_right_x[], brightness_y[], brightness_left_x2[], brightness_right_x2[], brightness_y2[],
    #  eyebrow_left_x[], eyebrow_right_x[], eyebrow_y[], mouth_x[], mouth_y[], tongue_x[], tongue_y[]
    item = [[] for i in range(106)]

    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json') as data_file:
        file = json.load(data_file)
        # print eye_left["cozmo"][0]["eye_left"][2]["x"][1]["1"]
        for i in xrange(35):
            item[0].append(QPointF(file["eye_left"]["x"][i],file["eye_left"]["y"][i]))
            item[1].append(QPointF(file["eye_right"]["x"][i], file["eye_right"]["y"][i]))

            item[2].append(QPointF(file["eyelid_up_left"]["x"][i], file["eyelid_up_left"]["y"][i]))
            item[3].append(QPointF(file["eyelid_up_right"]["x"][i], file["eyelid_up_right"]["y"][i]))
            item[4].append(QPointF(file["eyelid_down_left"]["x"][i], file["eyelid_down_left"]["y"][i]))
            item[5].append(QPointF(file["eyelid_down_right"]["x"][i], file["eyelid_down_right"]["y"][i]))

            item[6].append(QPointF(file["iris_left"]["x"][i], file["iris_left"]["y"][i]))
            item[7].append(QPointF(file["iris_right"]["x"][i], file["iris_right"]["y"][i]))

            item[8].append(QPointF(file["pupil_left"]["x"][i], file["pupil_left"]["y"][i]))
            item[9].append(QPointF(file["pupil_right"]["x"][i], file["pupil_right"]["y"][i]))

            item[10].append(QPointF(file["reflex_pupil_left"]["x"][i], file["reflex_pupil_left"]["y"][i]))
            item[11].append(QPointF(file["reflex_pupil_right"]["x"][i], file["reflex_pupil_right"]["y"][i]))
            item[12].append(QPointF(file["reflex_pupil_left_2"]["x"][i], file["reflex_pupil_left_2"]["y"][i]))
            item[13].append(QPointF(file["reflex_pupil_right_2"]["x"][i], file["reflex_pupil_right_2"]["y"][i]))

            item[14].append(QPointF(file["eyebrow_left"]["x"][i], file["eyebrow_left"]["y"][i]))
            item[15].append(QPointF(file["eyebrow_right"]["x"][i], file["eyebrow_right"]["y"][i]))

            item[16].append(QPointF(file["mouth"]["x"][i], file["mouth"]["y"][i]))
            item[17].append(QPointF(file["tongue"]["x"][i], file["tongue"]["y"][i]))

        item[98].append(file["eye_left"]["colour"])
        item[99].append(file["eyelid_up_left"]["colour"])
        item[100].append(file["iris_left"]["colour"])
        item[101].append(file["pupil_left"]["colour"])
        item[102].append(file["reflex_pupil_left"]["colour"])
        item[103].append(file["eyebrow_left"]["colour"])
        item[104].append(file["mouth"]["colour"])
        item[105].append(file["tongue"]["colour"])


    with open('base_emotions.json') as data_file:
        file = json.load(data_file)
        for i in xrange(35):
            item[18].append(QPointF(file["angry"]["eyelid_up_left"]["x"][i], file["angry"]["eyelid_up_left"]["y"][i]))
            item[19].append(QPointF(file["angry"]["eyelid_up_right"]["x"][i], file["angry"]["eyelid_up_right"]["y"][i]))
            item[20].append(QPointF(file["angry"]["eyelid_down_left"]["x"][i], file["angry"]["eyelid_down_left"]["y"][i]))
            item[21].append(QPointF(file["angry"]["eyelid_down_right"]["x"][i], file["angry"]["eyelid_down_right"]["y"][i]))
            item[22].append(QPointF(file["angry"]["iris_left"]["x"][i], file["angry"]["iris_left"]["y"][i]))
            item[23].append(QPointF(file["angry"]["iris_right"]["x"][i], file["angry"]["iris_right"]["y"][i]))
            item[24].append(QPointF(file["angry"]["pupil_left"]["x"][i], file["angry"]["pupil_left"]["y"][i]))
            item[25].append(QPointF(file["angry"]["pupil_right"]["x"][i], file["angry"]["pupil_right"]["y"][i]))
            item[26].append(QPointF(file["angry"]["reflex_pupil_left"]["x"][i], file["angry"]["reflex_pupil_left"]["y"][i]))
            item[27].append(QPointF(file["angry"]["reflex_pupil_right"]["x"][i], file["angry"]["reflex_pupil_right"]["y"][i]))
            item[28].append(QPointF(file["angry"]["reflex_pupil_left_2"]["x"][i], file["angry"]["reflex_pupil_left_2"]["y"][i]))
            item[29].append(QPointF(file["angry"]["reflex_pupil_right_2"]["x"][i], file["angry"]["reflex_pupil_right_2"]["y"][i]))
            item[30].append(QPointF(file["angry"]["eyebrow_left"]["x"][i], file["angry"]["eyebrow_left"]["y"][i]))
            item[31].append(QPointF(file["angry"]["eyebrow_right"]["x"][i], file["angry"]["eyebrow_right"]["y"][i]))
            item[32].append(QPointF(file["angry"]["mouth"]["x"][i], file["angry"]["mouth"]["y"][i]))
            item[33].append(QPointF(file["angry"]["tongue"]["x"][i], file["angry"]["tongue"]["y"][i]))

            item[34].append(QPointF(file["happiness"]["eyelid_up_left"]["x"][i], file["happiness"]["eyelid_up_left"]["y"][i]))
            item[35].append(QPointF(file["happiness"]["eyelid_up_right"]["x"][i], file["happiness"]["eyelid_up_right"]["y"][i]))
            item[36].append(QPointF(file["happiness"]["eyelid_down_left"]["x"][i], file["happiness"]["eyelid_down_left"]["y"][i]))
            item[37].append(QPointF(file["happiness"]["eyelid_down_right"]["x"][i], file["happiness"]["eyelid_down_right"]["y"][i]))
            item[38].append(QPointF(file["happiness"]["iris_left"]["x"][i], file["happiness"]["iris_left"]["y"][i]))
            item[39].append(QPointF(file["happiness"]["iris_right"]["x"][i], file["happiness"]["iris_right"]["y"][i]))
            item[40].append(QPointF(file["happiness"]["pupil_left"]["x"][i], file["happiness"]["pupil_left"]["y"][i]))
            item[41].append(QPointF(file["happiness"]["pupil_right"]["x"][i], file["happiness"]["pupil_right"]["y"][i]))
            item[42].append(QPointF(file["happiness"]["reflex_pupil_left"]["x"][i], file["happiness"]["reflex_pupil_left"]["y"][i]))
            item[43].append(QPointF(file["happiness"]["reflex_pupil_right"]["x"][i], file["happiness"]["reflex_pupil_right"]["y"][i]))
            item[44].append(QPointF(file["happiness"]["reflex_pupil_left_2"]["x"][i], file["happiness"]["reflex_pupil_left_2"]["y"][i]))
            item[45].append(QPointF(file["happiness"]["reflex_pupil_right_2"]["x"][i], file["happiness"]["reflex_pupil_right_2"]["y"][i]))
            item[46].append(QPointF(file["happiness"]["eyebrow_left"]["x"][i], file["happiness"]["eyebrow_left"]["y"][i]))
            item[47].append(QPointF(file["happiness"]["eyebrow_right"]["x"][i], file["happiness"]["eyebrow_right"]["y"][i]))
            item[48].append(QPointF(file["happiness"]["mouth"]["x"][i], file["happiness"]["mouth"]["y"][i]))
            item[49].append(QPointF(file["happiness"]["tongue"]["x"][i], file["happiness"]["tongue"]["y"][i]))

            item[50].append(QPointF(file["sadness"]["eyelid_up_left"]["x"][i], file["sadness"]["eyelid_up_left"]["y"][i]))
            item[51].append(QPointF(file["sadness"]["eyelid_up_right"]["x"][i], file["sadness"]["eyelid_up_right"]["y"][i]))
            item[52].append(QPointF(file["sadness"]["eyelid_down_left"]["x"][i], file["sadness"]["eyelid_down_left"]["y"][i]))
            item[53].append(QPointF(file["sadness"]["eyelid_down_right"]["x"][i], file["sadness"]["eyelid_down_right"]["y"][i]))
            item[54].append(QPointF(file["sadness"]["iris_left"]["x"][i], file["sadness"]["iris_left"]["y"][i]))
            item[55].append(QPointF(file["sadness"]["iris_right"]["x"][i], file["sadness"]["iris_right"]["y"][i]))
            item[56].append(QPointF(file["sadness"]["pupil_left"]["x"][i], file["sadness"]["pupil_left"]["y"][i]))
            item[57].append(QPointF(file["sadness"]["pupil_right"]["x"][i], file["sadness"]["pupil_right"]["y"][i]))
            item[58].append(QPointF(file["sadness"]["reflex_pupil_left"]["x"][i], file["sadness"]["reflex_pupil_left"]["y"][i]))
            item[59].append(QPointF(file["sadness"]["reflex_pupil_right"]["x"][i], file["sadness"]["reflex_pupil_right"]["y"][i]))
            item[60].append(QPointF(file["sadness"]["reflex_pupil_left_2"]["x"][i], file["sadness"]["reflex_pupil_left_2"]["y"][i]))
            item[61].append(QPointF(file["sadness"]["reflex_pupil_right_2"]["x"][i], file["sadness"]["reflex_pupil_right_2"]["y"][i]))
            item[62].append(QPointF(file["sadness"]["eyebrow_left"]["x"][i], file["sadness"]["eyebrow_left"]["y"][i]))
            item[63].append(QPointF(file["sadness"]["eyebrow_right"]["x"][i], file["sadness"]["eyebrow_right"]["y"][i]))
            item[64].append(QPointF(file["sadness"]["mouth"]["x"][i], file["sadness"]["mouth"]["y"][i]))
            item[65].append(QPointF(file["sadness"]["tongue"]["x"][i], file["sadness"]["tongue"]["y"][i]))

            item[66].append(QPointF(file["scared"]["eyelid_up_left"]["x"][i], file["scared"]["eyelid_up_left"]["y"][i]))
            item[67].append(QPointF(file["scared"]["eyelid_up_right"]["x"][i], file["scared"]["eyelid_up_right"]["y"][i]))
            item[68].append(QPointF(file["scared"]["eyelid_down_left"]["x"][i], file["scared"]["eyelid_down_left"]["y"][i]))
            item[69].append(QPointF(file["scared"]["eyelid_down_right"]["x"][i], file["scared"]["eyelid_down_right"]["y"][i]))
            item[70].append(QPointF(file["scared"]["iris_left"]["x"][i], file["scared"]["iris_left"]["y"][i]))
            item[71].append(QPointF(file["scared"]["iris_right"]["x"][i], file["scared"]["iris_right"]["y"][i]))
            item[72].append(QPointF(file["scared"]["pupil_left"]["x"][i], file["scared"]["pupil_left"]["y"][i]))
            item[73].append(QPointF(file["scared"]["pupil_right"]["x"][i], file["scared"]["pupil_right"]["y"][i]))
            item[74].append(QPointF(file["scared"]["reflex_pupil_left"]["x"][i], file["scared"]["reflex_pupil_left"]["y"][i]))
            item[75].append(QPointF(file["scared"]["reflex_pupil_right"]["x"][i], file["scared"]["reflex_pupil_right"]["y"][i]))
            item[76].append(QPointF(file["scared"]["reflex_pupil_left_2"]["x"][i], file["scared"]["reflex_pupil_left_2"]["y"][i]))
            item[77].append(QPointF(file["scared"]["reflex_pupil_right_2"]["x"][i], file["scared"]["reflex_pupil_right_2"]["y"][i]))
            item[78].append(QPointF(file["scared"]["eyebrow_left"]["x"][i], file["scared"]["eyebrow_left"]["y"][i]))
            item[79].append(QPointF(file["scared"]["eyebrow_right"]["x"][i], file["scared"]["eyebrow_right"]["y"][i]))
            item[80].append(QPointF(file["scared"]["mouth"]["x"][i], file["scared"]["mouth"]["y"][i]))
            item[81].append(QPointF(file["scared"]["tongue"]["x"][i], file["scared"]["tongue"]["y"][i]))

            item[82].append(QPointF(file["disgust"]["eyelid_up_left"]["x"][i], file["disgust"]["eyelid_up_left"]["y"][i]))
            item[83].append(QPointF(file["disgust"]["eyelid_up_right"]["x"][i], file["disgust"]["eyelid_up_right"]["y"][i]))
            item[84].append(QPointF(file["disgust"]["eyelid_down_left"]["x"][i], file["disgust"]["eyelid_down_left"]["y"][i]))
            item[85].append(QPointF(file["disgust"]["eyelid_down_right"]["x"][i], file["disgust"]["eyelid_down_right"]["y"][i]))
            item[86].append(QPointF(file["disgust"]["iris_left"]["x"][i], file["disgust"]["iris_left"]["y"][i]))
            item[87].append(QPointF(file["disgust"]["iris_right"]["x"][i], file["disgust"]["iris_right"]["y"][i]))
            item[88].append(QPointF(file["disgust"]["pupil_left"]["x"][i], file["disgust"]["pupil_left"]["y"][i]))
            item[89].append(QPointF(file["disgust"]["pupil_right"]["x"][i], file["disgust"]["pupil_right"]["y"][i]))
            item[90].append(QPointF(file["disgust"]["reflex_pupil_left"]["x"][i], file["disgust"]["reflex_pupil_left"]["y"][i]))
            item[91].append(QPointF(file["disgust"]["reflex_pupil_right"]["x"][i], file["disgust"]["reflex_pupil_right"]["y"][i]))
            item[92].append(QPointF(file["disgust"]["reflex_pupil_left_2"]["x"][i], file["disgust"]["reflex_pupil_left_2"]["y"][i]))
            item[93].append(QPointF(file["disgust"]["reflex_pupil_right_2"]["x"][i], file["disgust"]["reflex_pupil_right_2"]["y"][i]))
            item[94].append(QPointF(file["disgust"]["eyebrow_left"]["x"][i], file["disgust"]["eyebrow_left"]["y"][i]))
            item[95].append(QPointF(file["disgust"]["eyebrow_right"]["x"][i], file["disgust"]["eyebrow_right"]["y"][i]))
            item[96].append(QPointF(file["disgust"]["mouth"]["x"][i], file["disgust"]["mouth"]["y"][i]))
            item[97].append(QPointF(file["disgust"]["tongue"]["x"][i], file["disgust"]["tongue"]["y"][i]))
    return item

def delete_part(name, part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json', 'r+') as data_file:
        file = json.load(data_file)
        if file[part]["exist"] == "yes":
            file[part]["exist"] = "no"
            data_file.seek(0)
            json.dump(file, data_file, indent=4)
            data_file.truncate()


def create_part(name, part):
    # Assigning the values of the files to the items in the list "item"
    with open(name + '.json', 'r+') as data_file:
        file = json.load(data_file)
        if file[part]["exist"] == "no":
            file[part]["exist"] = "yes"
            data_file.seek(0)
            json.dump(file, data_file, indent=4)
            data_file.truncate()