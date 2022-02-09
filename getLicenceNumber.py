import string

def getNumberCleared(input):
    if input.startswith("B"):
        licenceNo = input
    elif input.startswith("8"):
        licenceNo = input.replace("8", "B")
    else:
        licenceNo = "Error in Licence Number"
    return licenceNo


def getLicenceNumber(array):
    licenceNo = ""

    for i in range(len(array)):
        if array[i] == '5' or array[i] == '5.' or array[i] == '5_':
            if array[i + 1] != "" and array[i + 1] != "." and array[i + 1] != "_":
                licenceNo = getNumberCleared(array[i + 1])
                break
            elif array[i + 2] != "" and array[i + 2] != "." and array[i + 2] != "_":
                licenceNo = getNumberCleared(array[i + 2])
                break
            else:
                licenceNo = "nah"
        elif array[i].startswith("5."):
            identifiedNumber = array[i].split(".")[1].strip()
            if identifiedNumber:
                licenceNo = getNumberCleared(identifiedNumber)
                break
        elif array[i].startswith("5_"):
            identifiedNumber = array[i].split("_")[1].strip()
            if identifiedNumber:
                licenceNo = getNumberCleared(identifiedNumber)
                break
        elif (array[i].startswith("B") or array[i].startswith("8")) and (len(array[i].strip()) == 7 or len(array[i].strip()) == 8 or len(array[i].strip()) == 9):
            identifiedNumber = array[i].strip()
            licenceNo = getNumberCleared(identifiedNumber)
            break
        else:
            licenceNo = "netha"
    return {
        "licenceNo": licenceNo
    }
