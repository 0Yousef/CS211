# front.py – a lexical analyzer system for simple arithmetic expressions

Import string

# Global declarations

# Variables
charClass = None
lexeme = [‘’] * 100
nextChar = ‘’
lexLen = 0
token = None
nextToken = None
in_fp = None

# Function declarations
Def addChar():
    Global lexLen, lexeme, nextChar
    If lexLen <= 98:
        Lexeme[lexLen] = nextChar
        lexLen += 1
        lexeme[lexLen] = ‘\0’
    else:
        print(“Error – lexeme is too long”)


def getChar():
    global nextChar, charClass, in_fp
    nextChar = in_fp.read(1)
    if nextChar == ‘’:
        charClass = ‘EOF’
    else:
        if nextChar.isalpha():
            charClass = ‘LETTER’
        elif nextChar.isdigit():
            charClass = ‘DIGIT’
        else:
            charClass = ‘UNKNOWN’


def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()


def lookup(ch):
    global nextToken
    if ch == ‘(‘:
        addChar()
        nextToken = 25  # LEFT_PAREN
    elif ch == ‘)’:
        addChar()
        nextToken = 26  # RIGHT_PAREN
    elif ch == ‘+’:
        addChar()
        nextToken = 21  # ADD_OP
    elif ch == ‘-‘:
        addChar()
        nextToken = 22  # SUB_OP
    elif ch == ‘*’:
        addChar()
        nextToken = 23  # MULT_OP
    elif ch == ‘/’:
        addChar()
        nextToken = 24  # DIV_OP
    else:
        addChar()
        nextToken = ‘EOF’
    return nextToken


def lex():
    global lexLen, nextToken, charClass
    lexLen = 0
    getNonBlank()

    if charClass == ‘LETTER’:
        addChar()
        getChar()
        while charClass == ‘LETTER’ or charClass == ‘DIGIT’:
            addChar()
            getChar()
        nextToken = 11  # IDENT

    elif charClass == ‘DIGIT’:
        addChar()
        getChar()
        while charClass == ‘DIGIT’:
            addChar()
            getChar()
        nextToken = 10  # INT_LIT

    elif charClass == ‘UNKNOWN’:
        lookup(nextChar)
        getChar()

    elif charClass == ‘EOF’:
        nextToken = ‘EOF’
        lexeme[0] = ‘E’
        lexeme[1] = ‘O’
        lexeme[2] = ‘F’
        lexeme[3] = ‘\0’

    print(f”Next token is: {nextToken}, Next lexeme is {‘’.join(lexeme)}”)
    return nextToken


# Main driver
Def main():
    Global in_fp
    In_fp = open(“front.in”, “r”)
    
    If in_fp is None:
        Print(“ERROR – cannot open front.in”)
    Else:
        getChar()
        while nextToken != ‘EOF’:
            lex()


if __name__ == ‘__main__’:
    main()
