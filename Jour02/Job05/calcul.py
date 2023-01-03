def calcule(num1,operator,num2):
    if operator == "+":
        result = num1+num2
    elif operator == "-":
        result = num1-num2
    elif operator == "*":
        result = num1*num2
    elif operator == "/":
        result = num1/num2
    elif operator == "%":
        result = num1%num2
    return result

print(calcule(2,"+",8))
print(calcule(7,"-",4))
print(calcule(8,"*",9))
print(calcule(6,"/",2))
print(calcule(8,"%",5))