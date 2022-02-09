def getdob(nic):
    nicInString = str(nic)
    month = ""
    day = ""

    if len(nicInString) != 9 and len(nicInString) != 12:
        return "Invalid NIC"
    else:
        if len(nicInString) == 9:
            birthYear = "19" + nicInString[:2]
            dayText = nicInString[2:5]
        else:
            birthYear = nicInString[:4]
            dayText = nicInString[4:7]

        if int(dayText) > 500:
            gender = "Female"
            dayText = int(dayText) - 500
        else:
            gender = "Male"
            dayText = int(dayText)

        if 1 > dayText > 366:
            return "Invalid NIC"
        else:
            if dayText > 335:
                day = dayText - 335
                month = "12"
            elif dayText > 305:
                day = dayText - 305
                month = "11"
            elif dayText > 274:
                day = dayText - 274
                month = "10"
            elif dayText > 244:
                day = dayText - 244
                month = "09"
            elif dayText > 213:
                day = dayText - 213
                month = "08"
            elif dayText > 182:
                day = dayText - 182
                month = "07"
            elif dayText > 152:
                day = dayText - 152
                month = "06"
            elif dayText > 121:
                day = dayText - 121
                month = "05"
            elif dayText > 91:
                day = dayText - 91
                month = "04"
            elif dayText > 60:
                day = dayText - 60
                month = "03"
            elif dayText < 32:
                day = dayText
                month = "01"
            elif dayText > 31:
                day = dayText - 31
                month = "02"
    return {"dateOfBirth": str(day) + "/" + month + "/" + birthYear, "gender": gender}
