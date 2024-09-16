import glob
#Constatnts
path = "C:\\Users\\sionl\\AppData\\Local\\VALORANT\\Saved\\Config\\*\\Windows\\GameUserSettings.ini"
RES_X = "1440"
RES_Y = "1080"
FullScreenMode = "2" #Windowed

desiredSettings = {
"bShouldLetterbox=" : "False", #Removes Black bars
"bLastConfirmedShouldLetterbox=" : "False",
"ResolutionSizeX=" : RES_X,
"ResolutionSizeY=" : RES_Y,
"LastUserConfirmedResolutionSizeX=" : RES_X,
"LastUserConfirmedResolutionSizeY=" : RES_Y,
"LastConfirmedFullscreenMode=" : FullScreenMode,
"PreferredFullscreenMode=" : FullScreenMode,
"DesiredScreenWidth=" : RES_X,
"DesiredScreenHeight=" : RES_Y,
"LastUserConfirmedDesiredScreenWidth=" : RES_X,
"LastUserConfirmedDesiredScreenHeight=" : RES_Y,
"FullscreenMode=" : FullScreenMode,
}

files = glob.glob(path)
for file in files:
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

