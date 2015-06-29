#--------------------
# UXS - Compiler 0.1
#--------------------

OptionTable = []
ButtonTable = []
AnchorTable = []
DelimitingChar = ":"

_DebugCompiler = False

lineTypeList = [["Anchor","anchor","ANCHOR","a","A"], ...
                ["Button","button","BUTTON","b","B"], ...
                ["Radio","radio","RADIO","rb","RB"], ...
                ["CheckBox","checkbox","CHECKBOX","cb","CB"]]

class CButton:
    name            = ""
    cmdList         = []
    position        = (0,0)

class COption:
    optionType      = "Radio"
    name            = ""
    enableDefault   = False # no default option
    optionList      = []    # default goes first
    orientation     = "V"   # H or V
    gridWrap        = 4


def getDelimitingChar(line):
    # TODO : Use first non-ascii character as delimiter
    return "|"

def updateAnchorTable(line):
    return

def updateButtonTable(line):
    return

def updateRadioTable(line):
    return

def updateTable(line, lineType):
    if(lineType == "Anchor"):
        updateAnchorTable(line)
    elif(lineType == "Button"):
        updateButtonTable(line)
    elif(lineType == "Radio"):
        updateRadioTable(line)
        
        
    
def parseScript(scriptName):
    global DelimitingChar
    global OptionTable
    global ButtonTable
    global AnchorTable

    try:
        f = open(scriptName, "r")
    except:
        print "[ABORT] failed to open script : '%s'"%(scriptName)
        exit()

    lineNumber = 0
    for line in f:
        lineNumber += 1
        if not line:
            if _DebugCompiler : print "skipping line %d"%(lineNumber)
            continue
        DelimitingChar = getDelimitingChar(line)
        contents = line.split(DelimitingChar)
        for lineType in lineTypeList:
            if(contents[0] in lineType):
                updateTable(line,lineType[0])
        
if size(sys.argv) == 3:
    scriptName = sys.argv[1]
    outputName = sys.argv[2]
    if _DebugCompiler : print "[PARSING] %s"%(scriptName)
    parseScript(scriptName)
    if _DebugCompiler : print "[BUILDING-UX] "%(scriptName)
    buildUX(outputName)
    if _DebugCompiler : print "[FINISH]"

