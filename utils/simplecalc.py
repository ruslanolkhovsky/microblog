#
# Simple Calculator
#

removeSpaces = lambda a: a.replace(" ", "")

def SimpleCalc(expression):

    if expression != "":

        try:
            result = eval(removeSpaces(expression))

        except NameError:
            result = "Error! Wrong expression"

        except SyntaxError:
            result = "Error! Wrong expression"

        except ZeroDivisionError:
            result = "Error! Division by Zerro"

        else:
            result = str(expression) + " = " + str(result)
    else:
        result = ""

    return result

if __name__ == "__main__":
     print (SimpleCalc(input ("\nEnter expression > ")))
