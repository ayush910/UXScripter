#--------------------
# UXS - Compiler 0.1
#--------------------

import re  # regex for parsing 
import sys # for command line args

OptionTable = {}
ButtonTable = []
AnchorTable = []
DelimitingChar = ":"

_DebugCompiler = False

lineTypeList = [["Anchor","anchor","ANCHOR","a","A"], ...
                ["Button","button","BUTTON","b","B"], ...
                ["Radio","radio","RADIO","rb","RB"], ...
                ["CheckBox","checkbox","CHECKBOX","cb","CB"]]
lineNumber = 0

HELPTEXT = """
[ERROR] Invalid Arguments !
Syntax >> uxs "script" "executable"
"""

# regex for parsing
rxAnchor   = r"pos/(((/d+),){2}(,/w+)*/)"
rxButton   = r"" #TODO
rxCBOption = r"" #TODO
rxRBOption = r"" #TODO

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
	# TODO : Handle negative relative positions
	# formats : a|pos(/d+,/d+)
	#			a|pos(/d+,/d+,/w+)

	posString = line.split(DelimitingChar)
	if len(posString) != 2:
		print "[ERROR][line:%d] anchor's position not specified"%(lineNumeber)
		exit()
	rxRes = re.findall(rxAnchor,posString[1])
	if _DebugCompiler :
		print "[DEBUG][line:%d] Anchor '%s'"%(lineNumber,posString[0])
		print rxRes
	rxN = len(rxRes)
	if rxN in [2,3]:
		# translate coords incase of relative position
		dx,dy = 0,0
		if rxN == 3:
			if rxRes[2] not in AnchorTable.Keys():
				print "[ERROR][line:%d] Anchor '%s' not defined"%(lineNumber, rxRes[2])
				exit()
			(dx,dy) = AnchorTable[rxRes[2]]
			
		(X,Y) = (int(rxRes[0]) + dx, int(rxRes[1]) + dy)
		AnchorTable[rxRes[2]] = (X,Y)
		if _DebugCompiler : 
			print "[DEBUG][line:%d] Added Anchor '%s':(%d,%d) to table"%(lineNumber,posString[0],rxRes[2],X,Y)
	else:
		print "[ERROR][line:%d] anchor's position could not be determined"%(lineNumeber)
		exit()
	
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
	else:
		print "[ERROR][line:%d] Well this is awkward. We have not yet implemented '%s'"%(lineNumber,lineType)
		exit()
    
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

	global lineNumber
    lineNumber = 0
    for line in f:
        lineNumber += 1
        if not line:
            if _DebugCompiler : print "skipping line %d"%(lineNumber)
            continue
        
		DelimitingChar = getDelimitingChar(line)
        contents = line.split(DelimitingChar)
		
		bRecognizedCmd = False
        
		for lineType in lineTypeList:
            if(contents[0] in lineType):
                updateTable(line,lineType[0])
				bRecognizedCmd = True
		
		if not bRecognizedCmd:
			print "[ERROR][line:%d] Could not recognize '%s'"%(contents[0])
			exit()
		

if size(sys.argv) == 3:
    scriptName = sys.argv[1]
    outputName = sys.argv[2]
    if _DebugCompiler : print "[PARSING] %s"%(scriptName)
    parseScript(scriptName)
    if _DebugCompiler : print "[BUILDING-UX] %s -> %s"%(scriptName, outputName)
    buildUX(outputName)
	if _DebugCompiler : print "[FINISHED] %s"%(outputName)
else:
	#TODO : use script name as output name incase second argument is missing
	print HELPTEXT

