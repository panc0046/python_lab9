from gfxhat import lcd,  fonts, backlight

def generateDictionary():
    files = open("font3.txt","r")
    charDictionary = {}
    for lines in files.readlines():
        stripped = lines.strip()
        # store key in variable
        keyDictionary = stripped[-1]
        valueDictionary = stripped[-18:-2]
        # Binary conversion
        valueList = []
        for i in range(0,len(valueDictionary),2):
            binNumber = format(int(valueDictionary[i]+valueDictionary[i+1],16),"08b")
            subList = list(map(int,binNumber))
            valueList.insert(i,subList)
        charDictionary[keyDictionary] = valueList
    return charDictionary

def displayObject(x,y,selectObject):
    lcd.clear()
    backlight.set_all(0,255,0)
    backlight.show()
    i = 0
    counter = 0
    while i < len(selectObject):
        j = 0
        temp_x = x
        temp_y = y + counter
        while j < len(selectObject[i]):
            lcd.set_pixel(temp_x,temp_y,selectObject[i][j])
            j = j+1
            temp_x = temp_x+1
        i = i+1
        counter = counter+1
        temp_y=temp_y+1
        lcd.show()

def displayCharacter():
    character = input("Enter character to display")
    dictionaryData = generateDictionary()
    if character in dictionaryData:
        x = int(input("Enter value of x"))
        y = int(input("Enter value of y"))
        displayObject(x,y,dictionaryData[character])
    else:
        print("Character is not found")
displayCharacter()
