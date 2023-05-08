# IMPORTS:
# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtSql, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

# Custom PyQt5 animations
from animations import AnimatedToggleCheckbox

# System
import os
import sys
import webbrowser

# Math
import random

# Database Handling
import sqlite3

# Avatar system
import python_avatars as pa

pyvipsBinPath = os.path.abspath("vips-dev-8.14/bin")
dllDirectory = getattr(os, "dllDirectory", None)
if callable(dllDirectory):
    dllDirectory(pyvipsBinPath)
else:
    os.environ["PATH"] = os.pathsep.join((pyvipsBinPath, os.environ["PATH"]))

import pyvips
pyvips.cache_set_max(0)

global resolutionList, avatarSystemAssociations
resolutionList = ["1280x720", "1920x1080", "2560x1440", "3840x2160"]
avatarSystemAssociations = {
    'top': {
        'Short Waved': pa.HairType.SHORT_WAVED,
        'Big Hair': pa.HairType.BIG_HAIR,
        'Hat': pa.HairType.HAT,
        'Loose Hair': pa.HairType.LOOSE_HAIR,
        'Astronaut': pa.HairType.ASTRONAUT,
        'Bob': pa.HairType.BOB,
        'Braids': pa.HairType.BRAIDS,
        'Bun': pa.HairType.BUN,
        'Buzzcut': pa.HairType.BUZZCUT,
        'Caesar': pa.HairType.CAESAR,
        'Caesar Side Part': pa.HairType.CAESAR_SIDE_PART,
        'Cornrows': pa.HairType.CORNROWS,
        'Curly': pa.HairType.CURLY,
        'Curly 2': pa.HairType.CURLY_2,
        'Curvy': pa.HairType.CURVY,
        'Long Hair Curly': pa.HairType.LONG_HAIR_CURLY,
        'Short Curly': pa.HairType.SHORT_CURLY,
        'Dreadlocks': pa.HairType.DREADLOCKS,
        'Einstein': pa.HairType.EINSTEIN_HAIR,
        'Elvis': pa.HairType.ELVIS,
        'Evil Spike': pa.HairType.EVIL_SPIKE,
        'Frizzle': pa.HairType.FRIZZLE,
        'Pixie': pa.HairType.PIXIE,
        'Frida': pa.HairType.FRIDA,
        'Fro': pa.HairType.FRO,
        'Fro Band': pa.HairType.FRO_BAND,
        'Half Shaved': pa.HairType.HALF_SHAVED,
        'Mohawk': pa.HairType.MOHAWK,
        'Mowgli': pa.HairType.MOWGLI,
        'Straight 1': pa.HairType.STRAIGHT_1,
        'Straight 2': pa.HairType.STRAIGHT_2,
        'Shaved Sides': pa.HairType.SHAVED_SIDES,
        'Shaggy': pa.HairType.SHAGGY,
        'Shaggy Mullet': pa.HairType.SHAGGY_MULLET,
        'Wild': pa.HairType.WILD,
        'Sides': pa.HairType.SIDES,
        'Straight Strand': pa.HairType.STRAIGHT_STRAND,
        'Short Flat': pa.HairType.SHORT_FLAT,
        'Short Round': pa.HairType.SHORT_ROUND,
    },
    'accessory': {
        'None': pa.AccessoryType.NONE,
        'Eyepatch': pa.AccessoryType.EYEPATCH,
        'Glasses 1': pa.AccessoryType.KURT,
        'Glasses 2': pa.AccessoryType.PRESCRIPTION_1,
        'Glasses 3': pa.AccessoryType.PRESCRIPTION_2,
        'Glasses 4': pa.AccessoryType.ROUND,
        'Glasses 5': pa.AccessoryType.SUNGLASSES,
        'Glasses 6': pa.AccessoryType.SUNGLASSES_2,
        'Glasses 7': pa.AccessoryType.WAYFARERS,
        'Glasses 8': pa.AccessoryType.WAYFARERS_2,
    },
    'hairColour': {
        'Black': pa.HairColor.BLACK,
        'Red': pa.HairColor.RED,
        'Brown': pa.HairColor.BROWN,
        'Auburn': pa.HairColor.AUBURN,
        'Blonde': pa.HairColor.BLONDE,
        'Golden Blonde': pa.HairColor.BLONDE_GOLDEN,
        'Dark Brown': pa.HairColor.BROWN_DARK,
        'Silver Grey': pa.HairColor.SILVER_GRAY,
        'Pink': pa.HairColor.PASTEL_PINK,
        'Platinum': pa.HairColor.PLATINUM,
    },
    'facialHair': {
        'None': pa.FacialHairType.NONE,
        'Light Beard': pa.FacialHairType.BEARD_LIGHT,
        'Majestic Beard': pa.FacialHairType.BEARD_MAGESTIC,
        'Medium Beard': pa.FacialHairType.BEARD_MEDIUM,
        'Einstein Moustache': pa.FacialHairType.EINSTEIN_MOUSTACHE,
        'Fancy Moustache': pa.FacialHairType.MOUSTACHE_FANCY,
        'Magnum Moustache': pa.FacialHairType.MOUSTACHE_MAGNUM,
        'Wick Beard': pa.FacialHairType.WICK_BEARD,
    },
    'facialHairColour': {
        'Black': pa.HairColor.BLACK,
        'Red': pa.HairColor.RED,
        'Brown': pa.HairColor.BROWN,
        'Auburn': pa.HairColor.AUBURN,
        'Blonde': pa.HairColor.BLONDE,
        'Golden Blonde': pa.HairColor.BLONDE_GOLDEN,
        'Dark Brown': pa.HairColor.BROWN_DARK,
        'Silver Grey': pa.HairColor.SILVER_GRAY,
        'Pink': pa.HairColor.PASTEL_PINK,
        'Platinum': pa.HairColor.PLATINUM,
    },
    'clothes': {
        'Hoodie': pa.ClothingType.HOODIE,
        'Astronaut Suit': pa.ClothingType.ASTRONAUT_SUIT,
        'Blazer Shirt': pa.ClothingType.BLAZER_SHIRT,
        'Blazer Sweater': pa.ClothingType.BLAZER_SWEATER,
        'Bond Suit': pa.ClothingType.BOND_SUIT,
        'Collar Sweater': pa.ClothingType.COLLAR_SWEATER,
        'Chef': pa.ClothingType.CHEF,
        'Gladiator': pa.ClothingType.GLADIATOR,
        'Graphic Shirt': pa.ClothingType.GRAPHIC_SHIRT,
        'Overall': pa.ClothingType.OVERALL,
        'Jedi Robe': pa.ClothingType.JEDI_ROBE,
        'Crew Neck': pa.ClothingType.SHIRT_CREW_NECK,
        'Scoop Neck': pa.ClothingType.SHIRT_SCOOP_NECK,
        'V Neck': pa.ClothingType.SHIRT_V_NECK,
        'Wick Shirt': pa.ClothingType.SHIRT_WICK,
    },
    'clothesColour': {
        'Red': pa.ClothingColor.RED,
        'Black': pa.ClothingColor.BLACK,
        'Blue 1': pa.ClothingColor.BLUE_01,
        'Blue 2': pa.ClothingColor.BLUE_02,
        'Blue 3': pa.ClothingColor.BLUE_03,
        'Grey 1': pa.ClothingColor.GRAY_01,
        'Grey 2': pa.ClothingColor.GRAY_02,
        'Pastel Blue': pa.ClothingColor.PASTEL_BLUE,
        'Pastel Green': pa.ClothingColor.PASTEL_GREEN,
        'Pastel Orange': pa.ClothingColor.PASTEL_ORANGE,
        'Pastel Yellow': pa.ClothingColor.PASTEL_YELLOW,
        'Heather': pa.ClothingColor.HEATHER,
        'Pink': pa.ClothingColor.PINK,
        'White': pa.ClothingColor.WHITE,
    },
    'eyes': {
        'Squint': pa.EyeType.SQUINT,
        'Happy': pa.EyeType.HAPPY,
        'Eye Roll': pa.EyeType.EYE_ROLL,
        'Default': pa.EyeType.DEFAULT,
        'Closed': pa.EyeType.CLOSED,
        'Cry': pa.EyeType.CRY,
        'Heart': pa.EyeType.HEART,
        'Side': pa.EyeType.SIDE,
        'Surprised': pa.EyeType.SURPRISED,
        'Wink': pa.EyeType.WINK,
        'Dizzy': pa.EyeType.X_DIZZY,
        'Wacky': pa.EyeType.WINK_WACKY,
    },
    'eyebrows': {
        'Default': pa.EyebrowType.DEFAULT,
        'Angry': pa.EyebrowType.ANGRY,
        'Default Natural': pa.EyebrowType.DEFAULT_NATURAL,
        'Angry Natural': pa.EyebrowType.ANGRY_NATURAL,
        'Flat Natural': pa.EyebrowType.FLAT_NATURAL,
        'Frown Natural': pa.EyebrowType.FROWN_NATURAL,
        'Raised Excited': pa.EyebrowType.RAISED_EXCITED,
        'Raised Natural': pa.EyebrowType.RAISED_EXCITED_NATURAL,
        'None': pa.EyebrowType.NONE,
        'Sad Concerned': pa.EyebrowType.SAD_CONCERNED,
        'Sad Concerned 2': pa.EyebrowType.SAD_CONCERNED_NATURAL,
        'Up Down': pa.EyebrowType.UP_DOWN,
        'Up Down 2': pa.EyebrowType.UP_DOWN_NATURAL,
        'Unibrow': pa.EyebrowType.UNIBROW_NATURAL,
    },
    'mouth': {
        'Smile': pa.MouthType.SMILE,
        'Sad': pa.MouthType.SAD,
        'Big Smile': pa.MouthType.BIG_SMILE,
        'Concerned': pa.MouthType.CONCERNED,
        'Default': pa.MouthType.DEFAULT,
        'Disbelief': pa.MouthType.DISBELIEF,
        'Serious': pa.MouthType.SERIOUS,
        'Eating': pa.MouthType.EATING,
        'Grimace': pa.MouthType.GRIMACE,
        'Tongue': pa.MouthType.TONGUE,
        'Twinkle': pa.MouthType.TWINKLE,
        'Scream': pa.MouthType.SCREAM_OPEN,
    },
    'skinTone': {
        'Skin Tone 1': pa.SkinColor.LIGHT,
        'Skin Tone 2': pa.SkinColor.PALE,
        'Skin Tone 3': pa.SkinColor.BROWN,
        'Skin Tone 4': pa.SkinColor.DARK_BROWN,
        'Skin Tone 5': pa.SkinColor.BLACK,
        'Skin Tone 6': pa.SkinColor.TANNED,
        'Skin Tone 7': pa.SkinColor.YELLOW,
    }
}

#
def moveScreenElement(element, newPositionX, newPositionY, easingType, iterations, animationLength):
    # For equations of the curves used to calculate the multiplier, see https://www.desmos.com/calculator/2lormzlbhu
    if easingType == "Linear":
        print("Mode set to Linear")
        # Note: Due to pixel values being integers, the actual iterations taken and the amount moved in each iteration
        # are automatically rounded to ensure the animation finishes as close as possible to the target value. A higher
        # number of iterations will lead to a more precise and smooth transition!
        originalPositionX = round(element.x())
        originalPositionY = round(element.y())
        differenceX = newPositionX - originalPositionX
        differenceY = newPositionY - originalPositionY
        iterationXDifference = round(differenceX / iterations)
        iterationYDifference = round(differenceY / iterations)
        iterationsActual = round(differenceX / iterationXDifference)
        for i in range(1, iterationsActual + 1):
            currentPositionX = element.x()
            currentPositionY = element.y()
            element.move(round(currentPositionX + iterationXDifference), round(currentPositionY + iterationYDifference))
            loop = QEventLoop()
            QTimer.singleShot(round(animationLength/iterationsActual), loop.quit)
            loop.exec_()
        element.move(round(newPositionX), round(newPositionY))
    elif easingType == "Bezier":
        print("Mode set to Bezier")
        # Uses the Bezier curve to apply a multiplier to the element's position, which allows for a smooth transition
        # with an ease in/out appearance.
        originalPositionX = round(element.x())
        originalPositionY = round(element.y())
        for i in range(1, iterations + 1):
            completionValue = i/iterations * i/iterations * (3 - 2*(i/iterations))
            element.move(round(originalPositionX + (newPositionX - originalPositionX)*completionValue), round(originalPositionY + (newPositionY - originalPositionY)*completionValue))
            loop = QEventLoop()
            QTimer.singleShot(round(animationLength/iterations), loop.quit)
            loop.exec_()
        element.move(round(newPositionX), round(newPositionY))
    elif easingType == "EaseIn":
        print("Mode set to Ease In")
        # Uses a cubic curve to create an ease in multiplier for the transition.
        originalPositionX = round(element.x())
        originalPositionY = round(element.y())
        for i in range(1, iterations + 1):
            completionValue = pow(i/iterations, 3)
            element.move(round(originalPositionX + (newPositionX - originalPositionX)*completionValue), round(originalPositionY + (newPositionY - originalPositionY)*completionValue))
            loop = QEventLoop()
            QTimer.singleShot(round(animationLength/iterations), loop.quit)
            loop.exec_()
        element.move(round(newPositionX), round(newPositionY))
    elif easingType == "EaseOut":
        print("Mode set to Ease Out")
        # Uses the curve y = 1 - (1-x)^3 to create an ease out multiplier.
        originalPositionX = round(element.x())
        originalPositionY = round(element.y())
        for i in range(1, iterations + 1):
            completionValue = 1 - pow((1-(i/iterations)),3)
            element.move(round(originalPositionX + (newPositionX - originalPositionX)*completionValue), round(originalPositionY + (newPositionY - originalPositionY)*completionValue))
            loop = QEventLoop()
            QTimer.singleShot(round(animationLength/iterations), loop.quit)
            loop.exec_()
        element.move(round(newPositionX), round(newPositionY))
    else:
        print("Invalid easing type! Must be either:\nLinear, Bezier, EaseIn, EaseOut")

# Generate screen elements functions
def generateNewButton(parent, type, positionX, positionY, sizeX, sizeY, autoCenter, text):
    global buttonFontSize
    button = QPushButton(parent)
    # Set text
    button.setText(text)
    # Resize
    button.resize(sizeX, sizeY)
    # Move
    if autoCenter == True:
        button.move(positionX - round(sizeX / 2), positionY - round(sizeY / 2))
    else:
        button.move(positionX, positionY)
    # Set styling
    if type == "RedEnabled":
        style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                "#d60210, stop: 1 #780008); border: 2px solid black; font-family: " \
                "'Arial'; font-size: " + str(buttonFontSize) + "px; font-style: bold; color: white;" \
                                                               "border-radius: 14px}" \
                                                               "QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                                                               "#707070, stop: 1 #171717); border: 2px solid black; font-family: 'Arial';" \
                                                               "font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px}" \
                              "QPushButton:hover:!pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#e60000, stop: 1 #960000); border: 2px solid black; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize + 2) + "px; font-style: bold; color: white; border-radius: 20px}"
        button.setStyleSheet(style)
    elif type == "GreyBasicEnabled":
        style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                "#ffffff, stop: 1 #595959); border: 2px solid black; font-family: " \
                "'Arial'; font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: black; border-radius: 14px;}" \
                              "QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#707070, stop: 1 #171717); border: 2px solid black; border-size: 10px; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                              "QPushButton:hover:!pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#ffffff, stop: 1 #6b6a6a); border: 2px solid black; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize + 1) + "px; font-style: bold; color: black; border-radius: 20px;}"
    elif type == "GreyBasicDisabled":
        style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                "#8c8c8c, stop: 1 #595959); border: 2px solid grey; font-family: " \
                "'Arial'; font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: black; border-radius: 14px;}"
    elif type == "IconButtonSettings":
        style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                "#707070, stop: 1 #171717); border: 2px solid black; font-family: " \
                "'Arial'; font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                              "QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#707070, stop: 1 #171717); border: 2px solid black; border-size: 10px; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                              "QPushButton:hover:!pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#595959, stop: 1 #424242); border: 2px solid black; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize + 1) + "px; font-style: bold; color: white; border-radius: 20px;}"
        button.setFlat(True)
        button.setAutoFillBackground(True)
        icon = QIcon("OmniMathAssets/ImageAssets/settingsIcon.png")
        button.setIcon(icon)
        button.setIconSize(QSize(round(sizeX / 1.5), round(sizeY / 1.5)))
    elif type == "Random":
        style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                "#707070, stop: 1 #171717); border: 2px solid black; font-family: " \
                "'Arial'; font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                              "QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#707070, stop: 1 #171717); border: 2px solid black; border-size: 10px; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                              "QPushButton:hover:!pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                              "#595959, stop: 1 #424242); border: 2px solid black; font-family: 'Arial';" \
                              "font-size: " + str(
            buttonFontSize + 1) + "px; font-style: bold; color: white; border-radius: 20px;}"
        button.setFlat(True)
        button.setAutoFillBackground(True)
        icon = QIcon("OmniMathAssets/ImageAssets/diceIcon.png")
        button.setIcon(icon)
        button.setIconSize(QSize(round(sizeX / 1.8), round(sizeY / 1.8)))
    button.setStyleSheet(style)
    return button


def calculateFontSize():
    global screenWidth, screenHeight, mainFontSize, buttonFontSize
    # Calculate the appropriate font size by taking into account both the width and the height of the window and
    # averaging them
    if screenHeight <= 1440 and screenWidth <= 2640:
        mainFontWidth = screenWidth * 0.009
        mainFontHeight = screenHeight * 0.016
    else:
        mainFontWidth = screenWidth * 0.008
        mainFontHeight = screenHeight * 0.014
    mainFontSize = round((mainFontHeight + mainFontWidth) / 2)
    print(mainFontSize)
    buttonFontSize = mainFontSize


def playSound(soundName):
    global soundEnabled
    if soundEnabled:
        try:
            filePath = f"OmniMathAssets/AudioAssets/{soundName}"
            QSound.play(filePath)
            print(f"Played sound {filePath}")
        except Exception as e:
            print(f"Failed to play sound with name: {soundName}\nError reason: {e}")
    else:
        return


def loadAllAccounts():
    print("Loading all accounts into dictionary...")
    global allAccounts
    allAccounts = {}
    accountDirectories = []
    for _, dirs, files in os.walk("OmniMathUserProfiles"):
        for accountDirectory in dirs:
            accountDirectories.append(f"OmniMathUserProfiles/{accountDirectory}")
        print(accountDirectories)
        # Stop scanning at first level of directory
        break


def renderAvatar(avatarInfo):
    print(avatarInfo)
    global avatarSystemAssociations
    top = None
    accessory = None
    hairColour = None
    facialHair = None
    facialHairColour = None
    clothes = None
    clothesColour = None
    eyes = None
    eyebrows = None
    mouth = None
    skinTone = None
    for attribute, selectedValue in avatarInfo.items():
        for attributeList, attributeItems in avatarSystemAssociations.items():
            for name, association in attributeItems.items():
                if name == selectedValue and attribute == attributeList:
                    match attributeList:
                        case "top":
                            top = association
                        case "accessory":
                            accessory = association
                        case "hairColour":
                            hairColour = association
                        case "facialHair":
                            facialHair = association
                        case "facialHairColour":
                            facialHairColour = association
                        case "clothes":
                            clothes = association
                        case "clothesColour":
                            clothesColour = association
                        case "eyes":
                            eyes = association
                        case "eyebrows":
                            eyebrows = association
                        case "mouth":
                            mouth = association
                        case "skinTone":
                            skinTone = association
                        case _:
                            print(f"Invalid association category!")
    # print(f"Generating avatar with traits:\nTop: {top}\nAccessory: {accessory}\nHair colour: {hairColour}\n"
    #       f"Facial hair: {facialHair}\nClothes: {clothes}\nClothes colour: {clothesColour}\nEyes: {eyes}\n"
    #       f"Eyebrows: {eyebrows}\nMouth: {mouth}\nSkin tone: {skinTone}")
    avatar = pa.Avatar()
    avatar.top = top
    avatar.accessory = accessory
    avatar.hair_color = hairColour
    avatar.facial_hair = facialHair
    print(facialHairColour)
    avatar.facial_hair_color = facialHairColour
    avatar.clothing = clothes
    avatar.clothing_color = clothesColour
    avatar.eyes = eyes
    avatar.eyebrows = eyebrows
    avatar.mouth = mouth
    avatar.skin_color = skinTone
    avatar.style = pa.AvatarStyle.CIRCLE
    avatar.background_color = "#525252"
    print(avatar)
    try:
        previousResult = os.path.exists("OmniMathAssets/TemporaryAssets/avatar.png")
        previousResult2 = os.path.exists("OmniMathAssets/TemporaryAssets/avatar.svg")
        if previousResult and previousResult2:
            os.remove("OmniMathAssets/TemporaryAssets/avatar.png")
            os.remove("OmniMathAssets/TemporaryAssets/avatar.svg")
            print("Deleted previous avatar render")
        avatar.render("OmniMathAssets/TemporaryAssets/avatar.svg")
        image = pyvips.Image.new_from_file("OmniMathAssets/TemporaryAssets/avatar.svg")
        image.write_to_file("OmniMathAssets/TemporaryAssets/avatar.png")
        image.invalidate()
        print("Rendered successfully!")
        result = True
        return result
    except Exception as e:
        print(f"Error rendering avatar - {e}")
        result = False
        return result


account = {
    'basicInfo': {
        'firstName': 'Thomas',
        'lastName': 'Abbott',
        'passwordEnabled': True,
        'password': 'verySecurePassword123',
        'accountCreationDate': '16/01/2023',
        'role': 'Student',
    },
    'avatarInfo': {
        'top': 'Short Curly',
        'accessory': 'Glasses 2',
        'hairColour': 'Black',
        'facialHair': 'None',
        'clothes': 'Chef',
        'clothesColour': 'White',
        'eyes': 'Eye Roll',
        'eyebrows': 'Angry',
        'mouth': 'Concerned',
        'skinTone': 'Skin Tone 1'
    }
}

# renderAvatar(account['avatarInfo'])


# Application code
class OmnimathUserInterface(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        global screenWidth, screenHeight, desktopGeometry, buttonFontSize, currentPath, mainFontSize, isFullscreen, \
            resolutionString, autoScaleDisabled, soundEnabled, allAccounts
        print("Initialising PyQt5 application... Hello world!")
        super(OmnimathUserInterface, self).__init__()
        self.setWindowTitle("OmniMath")
        print(f"User screen width: {screenWidth}\nUser screen height (not including taskbar): {screenHeight}")
        self.setGeometry(desktopGeometry)
        self.showFullScreen()
        isFullscreen = True
        soundEnabled = True
        resolutionString = str(screenWidth) + "x" + str(screenHeight)
        calculateFontSize()
        allAccounts = {}
        autoScaleDisabled = False
        self.move(8, 0)
        self.resized.connect(self.rebuildScreen)
        #self.openLoginScreen(skipIntroVideo=True)
        #self.tweenTestScreen()
        self.openAvatarCreationScreen(name="FirstName LastName")
    def resizeEvent(self, event):
        self.resized.emit()
        return super(OmnimathUserInterface, self).resizeEvent(event)

    def openLoginScreen(self, skipIntroVideo):
        global screenWidth, screenHeight, currentPath, currentPage
        loadAllAccounts()
        print("Window initialised.")
        currentPage = "mainMenu"
        if not skipIntroVideo:
            videoWidget = QVideoWidget(self)
            videoWidget.resize(screenWidth, screenHeight)
            videoWidget.move(0, 0)
            self.setCentralWidget(videoWidget)
            mediaPlayer = QMediaPlayer(self, QMediaPlayer.VideoSurface)
            mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("OmniMathAssets/VideoAssets/MenuScreenBG.wmv")))
            mediaPlayer.setVideoOutput(videoWidget)
            mediaPlayer.play()
            loop = QEventLoop()
            QTimer.singleShot(8500, loop.quit)
            loop.exec_()
            videoWidget.close()
        menuWidget = QWidget(self)
        menuWidget.resize(screenWidth, screenHeight)
        menuWidget.move(0, 0)
        staticBG = QPixmap("OmniMathAssets/ImageAssets/MenuScreenBGStatic.png")
        staticBG = staticBG.scaled(screenWidth, screenHeight)
        self.setCentralWidget(menuWidget)
        menuWidget.backgroundLabel = QLabel(menuWidget)
        menuWidget.backgroundLabel.resize(screenWidth, screenHeight)
        menuWidget.backgroundLabel.move(0, 0)
        menuWidget.backgroundLabel.setStyleSheet("background-color: red;")
        menuWidget.backgroundLabel.setPixmap(staticBG)
        menuWidget.exitButton = generateNewButton(menuWidget, type="RedEnabled", positionX=round(screenWidth / 2),
                                                  positionY=round(18 * (screenHeight / 20)),
                                                  sizeX=round(screenWidth / 11),
                                                  sizeY=round(screenWidth / 26), autoCenter=True, text="Exit")
        menuWidget.settingsButton = generateNewButton(menuWidget, type="IconButtonSettings",
                                                      positionX=round(screenWidth / 2),
                                                      positionY=round(16 * (screenHeight / 20)),
                                                      sizeX=round(screenWidth / 11),
                                                      sizeY=round(screenWidth / 26), autoCenter=True,
                                                      text="  Settings")
        currentPath = os.getcwd()
        accountDirectoryPath = os.path.join(currentPath, "OmniMathUserProfiles")
        accountDirectory = os.listdir(accountDirectoryPath)
        numberOfValidAccountFiles = 0

        menuWidget.newAccountButton = generateNewButton(menuWidget, type="GreyBasicEnabled",
                                                        positionX=round(screenWidth / 2),
                                                        positionY=round(14 * (screenHeight / 20)),
                                                        sizeX=round(screenWidth / 11),
                                                        sizeY=round(screenWidth / 26), autoCenter=True,
                                                        text="Create account")
        menuWidget.selectAccountButton = generateNewButton(menuWidget, type="GreyBasicEnabled",
                                                           positionX=round(screenWidth / 2),
                                                           positionY=round(12 * (screenHeight / 20)),
                                                           sizeX=round(screenWidth / 11),
                                                           sizeY=round(screenWidth / 26), autoCenter=True,
                                                           text="Select account")

        def exitFunction():
            print("Exiting directly from menu.")
            sys.exit()

        def openSettings():
            print("Opening settings from menu screen.")
            playSound("buttonPress.wav")
            self.openSettingsScreen()

        menuWidget.settingsButton.clicked.connect(openSettings)
        menuWidget.exitButton.clicked.connect(exitFunction)

    def rebuildScreen(self):
        print("Screen size adjusted - Updating scaling values")
        global screenWidth, screenHeight, isFullscreen, app, currentPage, buttonFontSize, mainFontSize, resolutionString, autoScaleDisabled
        if not autoScaleDisabled:
            if isFullscreen:
                screenWidth = self.width()
                screenHeight = self.height()
                resolutionString = str(screenWidth) + "x" + str(screenHeight)
                buttonFontSize = round(screenWidth * 0.01)
                mainFontSize = round(screenWidth * 0.01 + 2)
                print(f"Fullscreen resolution is now {resolutionString}")
            else:
                screenWidth = self.width()
                screenHeight = self.height()
                resolutionString = str(screenWidth) + "x" + str(screenHeight)
                buttonFontSize = round(screenWidth * 0.01)
                mainFontSize = round(screenWidth * 0.01)
                print(f"Normal resolution is now {resolutionString}")
            calculateFontSize()
            print(
                f"Updated screen width and height values:\nW: {screenWidth}\nH: {screenHeight}\nNew font size: {mainFontSize}")
            if currentPage == "settings":
                self.openSettingsScreen()
            elif currentPage == "mainMenu":
                self.openLoginScreen(skipIntroVideo=True)
            elif currentPage == "avatarCreation":
                self.openAvatarCreationScreen()
        else:
            print("Ignored resize")

    def tweenTestScreen(self):
        global screenWidth, screenHeight, currentPath, mainFontSize, currentPage, isFullscreen, resolutionString, \
            resolutionList, soundEnabled
        currentPage = "settings"
        tWidget = QWidget(self)
        self.setCentralWidget(tWidget)
        tWidget.resize(screenWidth, screenHeight)
        tWidget.move(0, 0)
        tBGLabel = QLabel(tWidget)
        tBGLabel.resize(screenWidth, screenHeight)
        tBGLabel.move(0, 0)
        tBGLabel.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #808080, "
                                      "stop: 1 #242323);")
        testObject = QLabel(tWidget)
        testObject.resize(300,300)
        testObject.move(round(3*(screenWidth/4)), 1000)
        testObject.setStyleSheet("background: red;")
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        moveScreenElement(testObject, 0, 1000, "Bezier", 1000, 1500)
        print("Done")


    def openSettingsScreen(self):
        global screenWidth, screenHeight, currentPath, mainFontSize, currentPage, isFullscreen, resolutionString, \
            resolutionList, soundEnabled
        currentPage = "settings"
        settingsWidget = QWidget(self)
        self.setCentralWidget(settingsWidget)
        settingsWidget.resize(screenWidth, screenHeight)
        settingsWidget.move(0, 0)
        settingsBGLabel = QLabel(settingsWidget)
        settingsBGLabel.resize(screenWidth, screenHeight)
        settingsBGLabel.move(0, 0)
        settingsBGLabel.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #808080, "
                                      "stop: 1 #242323);")
        settingsHolderArea = QLabel(settingsWidget)
        settingsHolderArea.resize(round(screenWidth / 3), round(screenHeight / 1.5))
        settingsHolderArea.move(round(screenWidth / 2) - round(screenWidth / 6),
                                round(screenHeight / 2) - round(screenHeight / 3))
        settingsHolderArea.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #ededed,"
                                         "stop: 1 #949494); border: 2px solid black; border-radius: " + str(
            mainFontSize + 20) + "px;")
        settingsTitleLabel = QLabel(settingsWidget)
        settingsTitleLabel.resize(round(screenWidth / 3), round(screenHeight / 20))
        settingsTitleLabel.move(round(screenWidth / 2) - round(screenWidth / 6), round(4 * (screenHeight / 20)))
        settingsTitleLabel.setText("OmniMath Application Settings")
        settingsTitleLabel.setAlignment(Qt.AlignCenter)
        titleFont = QFont("Arial", mainFontSize)
        settingsFont = QFont("Arial", round(mainFontSize * 0.7))
        settingsTitleLabel.setFont(titleFont)
        fullscreenHolder = QLabel(settingsWidget)
        fullscreenHolder.resize(round(screenWidth / 4), round(screenHeight / 14))
        fullscreenHolder.move(round(screenWidth / 2) - round(screenWidth / 8),
                              round(6 * (screenHeight / 20)) - round(screenHeight / 28))
        fullscreenHolder.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #363636," \
                                       "stop: 1 #171717); border: 2px solid black; border-radius: " + str(
            mainFontSize) + "px;")
        fullscreenLabel = QLabel(settingsWidget)
        fullscreenLabel.setFont(settingsFont)
        fullscreenLabel.setStyleSheet("color: white;")
        fullscreenLabel.move(round(screenWidth / 3) + round(screenWidth / 20),
                             round(6 * (screenHeight / 20)) - round(screenHeight / 28))
        fullscreenLabel.resize(round(screenWidth / 5), round(screenHeight / 14))
        fullscreenLabel.setText("Enable Fullscreen Mode:")
        fullscreenToggle = AnimatedToggleCheckbox(settingsWidget, sizeX=round(screenWidth / 24),
                                                  sizeY=round(screenHeight / 14))
        fullscreenToggle.move(round(5.9 * (screenWidth / 10)) - round(screenWidth / 48),
                              round(6 * (screenHeight / 20)) - round(screenHeight / 28))
        if isFullscreen:
            fullscreenToggle.click()

        def updateFullscreenMode():
            print("Updating fullscreen mode...")
            global isFullscreen, resolutionString
            isFullscreen = fullscreenToggle.isChecked()
            print(f"Fullscreen mode: {isFullscreen}")
            if isFullscreen:
                self.showFullScreen()
                isFullscreen = True
                # rebuild screen size
                self.rebuildScreen()
                playSound("toggleOn.wav")
            else:
                self.showMaximized()
                isFullscreen = False
                self.rebuildScreen()
                playSound("toggleOff.wav")

        fullscreenToggle.toggled.connect(updateFullscreenMode)
        resolutionHolder = QLabel(settingsWidget)
        resolutionHolder.resize(round(screenWidth / 4), round(screenHeight / 14))
        resolutionHolder.move(round(screenWidth / 2) - round(screenWidth / 8),
                              round(8 * (screenHeight / 20)) - round(screenHeight / 28))
        resolutionHolder.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #363636,"
                                       "stop: 1 #171717); border: 2px solid black; border-radius: " + str(mainFontSize)
                                       + "px;")
        resolutionLabel = QLabel(settingsWidget)
        resolutionLabel.setFont(settingsFont)
        resolutionLabel.setStyleSheet("color: white;")
        resolutionLabel.move(round(screenWidth / 3) + round(screenWidth / 20),
                             round(8 * (screenHeight / 20)) - round(screenHeight / 28))
        resolutionLabel.resize(round(screenWidth / 5), round(screenHeight / 14))
        resolutionLabel.setText("Application resolution:")
        resolutionDropdown = QComboBox(settingsWidget)
        resolutionDropdown.resize(round(screenWidth / 16), round(screenHeight / 18))
        resolutionDropdown.move(round(5.7 * (screenWidth / 10)) - round(screenWidth / 48),
                                round(8 * (screenHeight / 20)) - round(screenHeight / 36))
        resolutionDropdown.addItem(resolutionString)
        resolutionDropdown.setStyleSheet(
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #d6d6d6, stop: 1 #737373); border-radius: 8px;")
        for resolution in resolutionList:
            resolutionArray = resolution.split("x")
            resolutionWidth = int(resolutionArray[0])
            resolutionHeight = int(resolutionArray[1])
            screen = app.desktop()
            monitorGeometry = screen.screenGeometry()
            maxWidth = monitorGeometry.width()
            maxHeight = monitorGeometry.height()
            if resolution != resolutionString and resolutionHeight <= maxHeight and resolutionWidth <= maxWidth:
                resolutionDropdown.addItem(resolution)

        def selectNewResolution():
            global screenWidth, screenHeight, autoScaleDisabled, currentPage, isFullscreen
            autoScaleDisabled = True
            playSound("toggleOff.wav")
            if isFullscreen:
                self.showNormal()
            selectedString = resolutionDropdown.currentText()
            resolutions = selectedString.split("x")
            screenWidth = int(resolutions[0])
            screenHeight = int(resolutions[1])
            print(screenWidth, screenHeight)
            resizeWidget = QWidget(self)
            self.setCentralWidget(resizeWidget)
            self.setGeometry(50, 50, screenWidth, screenHeight)
            self.showNormal()
            isFullscreen = False
            autoScaleDisabled = False
            currentPage = "settings"
            self.rebuildScreen()

        resolutionDropdown.currentTextChanged.connect(selectNewResolution)

        soundHolder = QLabel(settingsWidget)
        soundHolder.resize(round(screenWidth / 4), round(screenHeight / 14))
        soundHolder.move(round(screenWidth / 2) - round(screenWidth / 8),
                         round(screenHeight / 2) - round(screenHeight / 28))
        soundHolder.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #363636,"
                                  "stop: 1 #171717); border: 2px solid black; border-radius: " + str(mainFontSize)
                                  + "px;")
        soundLabel = QLabel(settingsWidget)
        soundLabel.setFont(settingsFont)
        soundLabel.setStyleSheet("color: white;")
        soundLabel.move(round(screenWidth / 3) + round(screenWidth / 20),
                        round((screenHeight / 2)) - round(screenHeight / 28))
        soundLabel.resize(round(screenWidth / 5), round(screenHeight / 14))
        soundLabel.setText("Sound Effects:")
        soundToggle = AnimatedToggleCheckbox(settingsWidget, sizeX=round(screenWidth / 24),
                                             sizeY=round(screenHeight / 14))
        soundToggle.move(round(5.9 * (screenWidth / 10)) - round(screenWidth / 48),
                         round(screenHeight / 2) - round(screenHeight / 28))
        if soundEnabled:
            soundToggle.click()

        def updateSoundSettings():
            print("Updating sound mode...")
            global soundEnabled
            soundEnabled = soundToggle.isChecked()
            print(f"Sound enabled: {soundEnabled}")
            if soundEnabled:
                playSound("toggleOn.wav")

        soundToggle.toggled.connect(updateSoundSettings)

        def goBackToMenu():
            self.openLoginScreen(skipIntroVideo=True)
        settingsWidget.exitBtn = generateNewButton(settingsWidget,"RedEnabled",round(screenWidth/2),round(screenHeight/1.3),round(screenWidth/11),round(screenWidth/26),autoCenter=True,text="Go back")
        settingsWidget.exitBtn.clicked.connect(goBackToMenu)


    def openAvatarCreationScreen(self, name):
        global screenWidth, screenHeight, currentPage, mainFontSize
        currentPage = "avatarCreation"
        avatarWidget = QWidget(self)
        self.setCentralWidget(avatarWidget)
        avatarWidget.resize(screenWidth, screenHeight)
        avatarWidget.move(0, 0)
        gradientBG = QLabel(avatarWidget)
        gradientBG.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0  #232526,"
                                 "stop: 1 #414345);")
        gradientBG.resize(screenWidth, screenHeight)
        gradientBG.move(0, 0)
        sidePanel = QLabel(avatarWidget)
        sidePanel.resize(round(screenWidth / 3), round(screenHeight / 1.2))
        sidePanel.move(round(screenWidth / 16), round(screenHeight / 2) - round(screenHeight / 2.4))
        sidePanel.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0  #e8e8e8,"
                                "stop: 1 #a8a8a8); border: 2px solid black; border-radius: " + str(mainFontSize + 10))
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 0)
        shadow.setBlurRadius(120)
        shadow.setColor(QColor("#000000"))
        sidePanel.setGraphicsEffect(shadow)

        titleLabel = QLabel(avatarWidget)
        titleLabel.resize(round(screenWidth / 3), round(screenHeight / 20))
        font = QFont("Arial", mainFontSize + 7)
        font.setBold(True)
        titleLabel.setFont(font)
        titleLabel.setText("Create your avatar:")
        titleLabel.setAlignment(Qt.AlignCenter)
        titleLabel.move(round(screenWidth / 16), round(screenHeight / 10))

        optionArea = QWidget(avatarWidget)
        optionArea.resize(round(screenWidth / 3), round(screenHeight / 1.4))
        optionArea.move(round(screenWidth / 16), round(screenHeight / 2 - screenHeight / 3))
        # optionArea.setStyleSheet("background-color: red")
        optionLayout = QVBoxLayout(optionArea)
        optionArea.setLayout(optionLayout)

        scrollArea = QScrollArea(avatarWidget)
        scrollArea.resize(round(screenWidth / 3), round(screenHeight / 1.4))
        scrollArea.move(round(screenWidth / 16), round(screenHeight / 2 - screenHeight / 3))
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(optionArea)
        scrollArea.setStyleSheet("background: transparent; border: 0px solid black")

        avatarPreviewLabel = QLabel(avatarWidget)
        avatarPreviewLabel.resize(round(screenWidth/5),round(screenHeight/3.125))
        avatarPreviewLabel.move(round(screenWidth/1.72), round(screenHeight/2 - screenHeight/6.25))
        placeholderPixmap = QPixmap("OmniMathAssets/ImageAssets/avatarPending.png")
        placeholderPixmap = placeholderPixmap.scaled(round(avatarPreviewLabel.width()), round(avatarPreviewLabel.height()))
        avatarPreviewLabel.setPixmap(placeholderPixmap)
        avatarShadow = QGraphicsDropShadowEffect()
        avatarShadow.setOffset(0, 0)
        avatarShadow.setBlurRadius(120)
        avatarShadow.setColor(QColor("#000000"))
        avatarPreviewLabel.setGraphicsEffect(avatarShadow)

        avatarNameLabel = QLabel(avatarWidget)
        avatarNameLabel.resize(round(screenWidth/2),round(screenHeight/6))
        avatarNameLabel.move(round(screenWidth/2 - screenWidth/14.9), round(screenHeight/1.6))
        avatarNameLabel.setFont(font)
        avatarNameLabel.setStyleSheet("color: white;")
        avatarNameLabel.setText(name)
        avatarNameLabel.setAlignment(Qt.AlignCenter)

        def randomiseAvatar():
            print("Randomising avatar...")
            topLabel.setText(random.choice(list(avatarSystemAssociations['top'])))
            accessoryLabel.setText(random.choice(list(avatarSystemAssociations['accessory'])))
            hairColourLabel.setText(random.choice(list(avatarSystemAssociations['hairColour'])))
            facialHairLabel.setText(random.choice(list(avatarSystemAssociations['facialHair'])))
            facialHairColourLabel.setText(random.choice(list(avatarSystemAssociations['facialHairColour'])))
            clothesLabel.setText(random.choice(list(avatarSystemAssociations['clothes'])))
            clothesColourLabel.setText(random.choice(list(avatarSystemAssociations['clothesColour'])))
            clothesLabel.setText(random.choice(list(avatarSystemAssociations['clothes'])))
            eyesLabel.setText(random.choice(list(avatarSystemAssociations['eyes'])))
            eyebrowsLabel.setText(random.choice(list(avatarSystemAssociations['eyebrows'])))
            mouthLabel.setText(random.choice(list(avatarSystemAssociations['mouth'])))
            skinToneLabel.setText(random.choice(list(avatarSystemAssociations['skinTone'])))
            updateAvatarPreview()

        randomiseAvatarButton = generateNewButton(parent=avatarWidget,type="Random",positionX=round(screenWidth/1.6),
                                                  positionY=round(screenHeight/1.2),sizeX=round(screenWidth / 11),sizeY=round(screenWidth / 26),autoCenter=True,
                                                  text="  Randomise")
        randomiseAvatarButton.clicked.connect(randomiseAvatar)

        def updateAvatarPreview():
            print("Updating avatar preview label...")
            placeholderPixmap = QPixmap("OmniMathAssets/ImageAssets/avatarPending.png")
            placeholderPixmap = placeholderPixmap.scaled(round(avatarPreviewLabel.width()),
                                                         round(avatarPreviewLabel.height()))
            avatarPreviewLabel.setPixmap(placeholderPixmap)
            # Construct the avatar dictionary
            avatarInfo = {
                'top': topLabel.text(),
                'accessory': accessoryLabel.text(),
                'hairColour': hairColourLabel.text(),
                'facialHair': facialHairLabel.text(),
                'facialHairColour': facialHairColourLabel.text(),
                'clothes': clothesLabel.text(),
                'clothesColour': clothesColourLabel.text(),
                'eyes': eyesLabel.text(),
                'eyebrows': eyebrowsLabel.text(),
                'mouth': mouthLabel.text(),
                'skinTone': skinToneLabel.text()
            }
            print(avatarInfo)
            result = renderAvatar(avatarInfo)
            if result == True:
                placeholderPixmap = QPixmap("OmniMathAssets/TemporaryAssets/avatar.png")
                placeholderPixmap = placeholderPixmap.scaled(round(avatarPreviewLabel.width()),
                                                             round(avatarPreviewLabel.height()))
                avatarPreviewLabel.setPixmap(placeholderPixmap)
            else:
                print("Not updating avatar preview (render failed)")


        def addNewOption(descriptionLabel, category):
            global mainFontSize, avatarSystemAssociations
            optionWidget = QWidget()
            optionWidget.setFixedSize(round(screenWidth / 3.16), round(screenHeight / 14))
            optionFont = QFont("Arial", mainFontSize-2)
            optionTitle = QLabel(optionWidget)
            optionTitle.setText(descriptionLabel)
            optionTitle.setFont(optionFont)
            optionTitle.setAlignment(Qt.AlignVCenter)
            optionTitle.resize(round(optionWidget.width()), round(optionWidget.height()))
            optionTitle.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 #363636,"
                                      "stop: 1 #171717); border: 2px solid black; border-radius: " +
                                      str(mainFontSize + 5) + "px; color: white")
            style = "QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                    "#ffffff, stop: 1 #595959); border: 2px solid black; font-family: 'Arial'; font-size: " \
                    + str(buttonFontSize) + "px; font-style: bold; color: black; border-radius: 14px;}" \
                                            "QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1," \
                                            "stop: 0 #707070, stop: 1 #171717); border: 2px solid black; border-size: 10px;" \
                                            "font-family: 'Arial';" \
                                            "font-size: " + str(
                buttonFontSize) + "px; font-style: bold; color: white; border-radius: 14px;}" \
                                  "QPushButton:hover:!pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 " \
                                  "#ffffff, stop: 1 #6b6a6a); border: 2px solid black; font-family: 'Arial';" \
                                  "font-size: " + str(
                buttonFontSize + 1) + "px; font-style: bold; color: black; border-radius: 16px;}"

            optionLabel = QLabel(optionWidget)
            optionLabel.setText(list(avatarSystemAssociations[category].items())[0][0])
            optionLabel.resize(round(optionWidget.width()/2),round(optionWidget.height()))
            optionLabel.setAlignment(Qt.AlignCenter)
            optionLabel.move(round(1.34*(optionWidget.width()/3)), 0)
            optionLabel.setFont(optionFont)
            optionLabel.setStyleSheet("color: white;")
            def cycleOptionsRight(category=category):
                # Get all category options from the association table and collect them in an array to cycle through
                options = []
                for option in avatarSystemAssociations[category]: options.append(option)
                currentOptionIndex = -1
                numberOfOptions = len(options)
                currentOption = optionLabel.text()
                for item in options:
                    currentOptionIndex += 1
                    if item == currentOption:
                        break
                currentOptionLabel = (options[currentOptionIndex])
                if currentOptionIndex + 1 < numberOfOptions:
                    # increment 1 more
                    currentOptionIndex += 1
                    currentOption = options[currentOptionIndex]
                    optionLabel.setText(currentOption)
                    print(f"Updated text to: {currentOption}")
                    updateAvatarPreview()
                else:
                    # reset back to start
                    currentOptionIndex = 0
                    currentOption = options[0]
                    optionLabel.setText(currentOption)
                    print(f"Updated text to: {currentOption}")
                    updateAvatarPreview()
            def cycleOptionsLeft(category=category):
                # Get all category options from the association table and collect them in an array to cycle through
                options = []
                for option in avatarSystemAssociations[category]: options.append(option)
                currentOptionIndex = -1
                numberOfOptions = len(options)
                currentOption = optionLabel.text()
                for item in options:
                    currentOptionIndex += 1
                    if item == currentOption:
                        break
                currentOptionLabel = (options[currentOptionIndex])
                if currentOptionIndex - 1 >= 0:
                    # increment 1 more
                    currentOptionIndex -= 1
                    currentOption = options[currentOptionIndex]
                    optionLabel.setText(currentOption)
                    print(f"Updated text to: {currentOption}")
                    updateAvatarPreview()
                else:
                    # reset back to start
                    currentOptionIndex = numberOfOptions - 1
                    currentOption = options[numberOfOptions-1]
                    optionLabel.setText(currentOption)
                    print(f"Updated text to: {currentOption}")
                    updateAvatarPreview()

            buttonLeft = QPushButton(optionWidget)
            buttonLeft.resize(round(optionWidget.width() / 11), round(optionWidget.height() / 2))
            buttonLeft.move(round(1.25*(optionWidget.width() / 3)), round(optionWidget.height() / 4))
            buttonLeft.setStyleSheet(style)
            iconLeft = QIcon("OmniMathAssets/ImageAssets/arrowLeft.png")
            buttonLeft.setIcon(iconLeft)
            buttonLeft.setIconSize(QSize(round(buttonLeft.width() / 1.2), round(buttonLeft.height() / 1.2)))
            buttonLeft.clicked.connect(lambda: cycleOptionsLeft(category=category))
            buttonRight = QPushButton(optionWidget)
            buttonRight.resize(round(optionWidget.width() / 11), round(optionWidget.height() / 2))
            buttonRight.move(round(2.65*(optionWidget.width() / 3)), round(optionWidget.height() / 4))
            buttonRight.setStyleSheet(style)
            iconRight = QIcon("OmniMathAssets/ImageAssets/arrowRight.png")
            buttonRight.setIcon(iconRight)
            buttonRight.setIconSize(QSize(round(buttonLeft.width() / 1.2), round(buttonLeft.height() / 1.2)))
            buttonRight.clicked.connect(lambda: cycleOptionsRight(category=category))
            optionLayout.addWidget(optionWidget)
            return optionLabel

        topLabel = addNewOption("Hair Style: ", "top")
        hairColourLabel = addNewOption("Hair Colour: ", "hairColour")
        accessoryLabel = addNewOption("Accessory: ", "accessory")
        facialHairLabel = addNewOption("Facial Hair: ", "facialHair")
        facialHairColourLabel = addNewOption("Facial Hair Colour:", "facialHairColour")
        clothesLabel = addNewOption("Clothes:", "clothes")
        clothesColourLabel = addNewOption("Clothes Colour:", "clothesColour")
        eyesLabel = addNewOption("Eyes:", "eyes")
        eyebrowsLabel = addNewOption("Eyebrows:", "eyebrows")
        mouthLabel = addNewOption("Mouth:", "mouth")
        skinToneLabel = addNewOption("Skin Tone:", "skinTone")
        updateAvatarPreview()



def main():
    print("Starting OmniMath...")
    global screenWidth, screenHeight, desktopGeometry, app
    app = QApplication(sys.argv)
    desktop = app.desktop()
    resolution = desktop.screenGeometry()
    desktopGeometry = resolution
    screenWidth = resolution.width()
    screenHeight = resolution.height()
    win = OmnimathUserInterface()
    win.show()
    sys.exit(app.exec_())


main()
