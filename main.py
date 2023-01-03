instructionsTypes = {
    "R": {
        "funct7": 7,
        "rs2": 5,
        "rs1": 5,
        "funct3": 3,
        "rd": 3
    },
    "I": {
        "IMM": 12,
        "rs1": 5,
        "funct3": 3,
        "rd": 5
    },
    "S": {
        "IMM1": 7,
        "rs2": 5,
        "rs1": 5,
        "funct3": 3,
        "IMM2": 5
    },
    "J": {
        "imm": 20,
        "rd": 5
    },
    "B": {
        "imm1": 7,
        "rs2": 5,
        "rs1": 5,
        "funct3": 3,
        "imm2": 5
    },
    "U": {
        "imm": 20,
        "rd": 5
    }
    
}

def separateBinaryIntoInstructions(binaryString, instructionTypeName):
    currentPlaceInStruction = 0

    instructionType = instructionsTypes[instructionTypeName]

    for section in instructionType:
        instructionSize = instructionType[section]
        instructionBinaryCode = binaryString[currentPlaceInStruction:currentPlaceInStruction + instructionSize]

        print(f"{section}: {instructionBinaryCode}")

        currentPlaceInStruction += instructionSize

    print(f"OPCODE: {getOpcode(binaryString)}")

def getOpcode(binaryString):
    return binaryString[25:32]

def printRightOrderOfJalImmediate(immStr):
    firstSequence = immStr[0] * 12
    redSequence = immStr[0:11]
    blueDigit = immStr[11]
    greenSequence = immStr[12: 20]

    hasMoreThan32Bits = len(f"{firstSequence}{greenSequence}{blueDigit}{redSequence}0")

    if hasMoreThan32Bits:
        print(f"{firstSequence} {greenSequence} {blueDigit} {redSequence}")
    else:
        print(f"{firstSequence} {greenSequence} {blueDigit} {redSequence} 0")


def formatIImmediate(immStr):
    firstSequence = immStr[0] * 20
    secondSequence = immStr

    print(f"{firstSequence}{secondSequence}")

def formatSImmediate(immStr1, immStr2):
    firstSequence = immStr1[0] * 20
    secondSequence = immStr1
    thirdSequence = immStr2

    print(f"{firstSequence}{secondSequence}{thirdSequence}")

def formatBImmediate(immStr1, immStr2):
    firstSequence = immStr1[0] * 20
    greenSequence = immStr1[1: 7]
    redSequence = immStr2[0:4]
    blueChar = immStr2[-1]

    print(f"{firstSequence} {blueChar} {greenSequence} {redSequence} 0")

def formatUImmediate(immStr):
    print(f"{immStr}000000000000")

###########################################################
#                    ÁREA DE TRABALHO
###########################################################

# print(getOpcode("00000001100000000000000011101111")) #printar opcode para descobrir o tipo de instrução

# separateBinaryIntoInstructions("00000001100000000000000011101111", "J") #printar a instrução dividida po seções

# getRightOrderOfJalImmediate("00000001100000000000") #pegar ordem certa do Imm de uma instrução jal (TIPO J)
# formatIImmediate("000011111111")
# formatBImmediate("1111111", "10101")
# formatUImmediate("00010010001101000101")

###########################################################
#                    ADICIONAIS
###########################################################

# print(0x00) # mostrar hexadecimal em decimal
# print(0b00)  # mostrar binario em decimal
# print(bin(00)) # mostrar decimal em forma binária
# print(len("11111111111111111111111111110100")) # descobrir tamanho de uma string


###########################################################
#                    LEGENDAS
###########################################################
"""
rd: registrador em que algo será armazenado
rs1 e rs2: registradores com informações para a instrução
"""
