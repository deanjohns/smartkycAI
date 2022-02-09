import re

def getBloodGroup(i):
    if "Blood Group" in i:
        bloodGroupData = re.sub('[t]', '+', i.split("Blood Group")[1])
        bloodGroupData = re.sub('[8]', 'B', bloodGroupData)
        bloodGroupData = re.sub('[0]', 'O', bloodGroupData)

        return bloodGroupData.strip()
    return "Not detected"
