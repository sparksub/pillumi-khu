import pandas as pd


def make_pictogram_list(pill_info):
    pictogram_info = pd.read_csv('/Users/sparksub/Documents/GitHub/pillumi-khu/server/assets/pictogram-info.csv')
    pictogram_info = pictogram_info.values
    pictogram_list = []

    group = ["용법", "부작용", "주의사항", "상호작용", "금지사항", "보관방법"]
    # Dosage = 4
    # AtpnWarnQesitm = 5
    # AtpnQesitm = 6
    # IntrcQesitm = 7
    # SeQesitm = 8
    # DepositMethodQesitm = 9

    for j, subgroup in enumerate(group):
        value_list = []
        for i in range(0, len(pictogram_info)):
            item = pictogram_info[i]
            if (item[1] == subgroup) and (pill_info[j+4] != ''):
                if not pd.isna(item[3]):
                    word_list = item[3].split(', ')
                    check = False
                    for word in range(0, len(word_list)):
                        result = pill_info[j+4].find(word_list[word])
                        if check:
                            break
                        if result != -1:
                            if not pd.isna(item[2]):
                                if pill_info[j+4].find(item[2]) != -1:
                                    value_list.append(item[0])
                                    check = True
                            else:
                                value_list.append(item[0])
                                check = True
        pictogram_list.append(value_list)
    return {
        "Dosage": pictogram_list[0],
        "AtpnWarnQesitm": pictogram_list[1],
        "AtpnQesitm": pictogram_list[2],
        "IntrcQesitm": pictogram_list[3],
        "SeQesitm": pictogram_list[4],
        "DepositMethodQesitm": pictogram_list[5]
    }