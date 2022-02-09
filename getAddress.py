def getAddress(i, name=""):
    address = i
    if "8." in address:
        address = address.replace("8.", "")
    elif "B." in address:
        address = address.replace("B.", "")
    elif "5." in address:
        address = address.replace("5.", "")

    # nameList = name.split(" ")
    # allList = address.split(" ")
    #
    # addressList = list(set(allList) - set(nameList)) + list(set(nameList) - set(allList))
    # address = " ".join(reversed(addressList))

    return address
