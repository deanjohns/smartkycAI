from getdob import getdob

def getNic(i, array):
    if "44." in i or "4d." in i or "Sd." in i or "49." in i or "46." in i or "4d-" in i or "4g." in i:
        if "44." in i:
            nicPart = i.split("44.")
        elif "4d." in i:
            nicPart = i.split("4d.")
        elif "Sd." in i:
            nicPart = i.split("Sd.")
        elif "49." in i:
            nicPart = i.split("49.")
        elif "46." in i:
            nicPart = i.split("46.")
        elif "4d-" in i:
            nicPart = i.split("4d-")
        elif "4g." in i:
            nicPart = i.split("4g.")
        else:
            nicPart = None

        if nicPart != None:
            nic = (nicPart[1].strip()).replace('.', '')
        else:
            nic = nicPart.replace('.', '')

        rawnicInt = nicPart[1].replace('.', '')
        nicInt = [int(s) for s in rawnicInt.strip().split() if s.isdigit()][0]
        dob = getdob(nicInt)["dateOfBirth"]
        gender = getdob(nicInt)["gender"]

        idIndex = array.index(i)
        dataObj = {
            "nic": nic,
            "dob": dob,
            "gender": gender,
            "idIndex": idIndex
        }
        return dataObj
    else:
        dataObj = {
            "nic": "",
            "dob": "",
            "gender": "",
            "idIndex": ""
        }
        return dataObj
