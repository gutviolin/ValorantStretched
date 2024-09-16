import glob
path = "C:\\Users\\sionl\\AppData\\Local\\VALORANT\\Saved\\Config\\*\\Windows\\GameUserSettings.ini"
files = glob.glob(path)

desiredSettings = {
"bShouldLetterbox=" : "False",
"bLastConfirmedShouldLetterbox=" : "False",
"ResolutionSizeX=" : "1440",
"ResolutionSizeY=" : "1080",
"LastUserConfirmedResolutionSizeX=" : "1440",
"LastUserConfirmedResolutionSizeY=" : "1080",
"LastConfirmedFullscreenMode=" : "2",
"PreferredFullscreenMode=" : "2",
"DesiredScreenWidth=" : "1440",
"DesiredScreenHeight=" : "1080",
"LastUserConfirmedDesiredScreenWidth=" : "1440",
"LastUserConfirmedDesiredScreenHeight=" : "1080"
}

for file in files:
    #print(file)
    newLines = []
    with open(file) as readFile:
        lines = readFile.readlines()
        for line in lines:
            newLine = ""
            contains = False
            for i in desiredSettings:
                if line.startswith(i):
                    contains = True
                    newLine = i + desiredSettings[i] + "\n"
                    newLines.append(newLine)
                    break
            if (contains == False):
                newLine = line
                newLines.append(newLine)


    with open(file, "w") as fileWrite:
        for line in newLines:
            fileWrite.write(line)

