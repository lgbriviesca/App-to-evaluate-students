import csv

"""Importé cada quiz por separado porque en repetidas ocasiones tuve el problema (:) 
y no pude usar panda para importar múltiples archivos de una vez. 
            ERROR: Failed cleaning build dir for numpy
            Successfully built pandas
            Failed to build numpy
            ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly 
"""

quiz1_dict = []
quiz2_dict = []
quiz3_dict = []
quiz4_dict = []

with open("quiz_1.csv", encoding="utf-8") as csv_file1:
    quiz1 = csv.DictReader(csv_file1)
    for i in quiz1:
        quiz1_dict.append({"Name": i["First Name"].lower().strip() + " " + i["Last Name"].lower(
        ).strip(), "Accuracy": int(i["Accuracy"].strip('%')), "Score": int(i["Score"])})

with open("quiz_2.csv", encoding="utf-8") as csv_file2:
    quiz2 = csv.DictReader(csv_file2)
    for i in quiz2:
        quiz2_dict.append({"Name": i["First Name"].lower().strip() + " " + i["Last Name"].lower(
        ).strip(), "Accuracy": int(i["Accuracy"].strip('%')), "Score": int(i["Score"])})

with open("quiz_3.csv", encoding="utf-8") as csv_file3:
    quiz3 = csv.DictReader(csv_file3)
    for i in quiz3:
        quiz3_dict.append({"Name": i["First Name"].lower().strip() + " " + i["Last Name"].lower(
        ).strip(), "Accuracy": int(i["Accuracy"].strip('%')), "Score": int(i["Score"])})

with open("quiz_4.csv", encoding="utf-8") as csv_file4:
    quiz4 = csv.DictReader(csv_file4)
    for i in quiz4:
        quiz4_dict.append({"Name": i["First Name"].lower().strip() + " " + i["Last Name"].lower(
        ).strip(), "Accuracy": int(i["Accuracy"].strip('%')), "Score": int(i["Score"])})

files = quiz1_dict, quiz2_dict, quiz3_dict, quiz4_dict

#print(files)