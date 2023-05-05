def add(num1,num2):
    res = num1+num2
    return res
def sub(num1,num2):
    if num1>num2:
        res = num1-num2
    else:
        res = num2-num1
    return res 
def mul(num1,num2):
    res = num1*num2
    return res
def div(num1,num2):
    if num1>0 and num2>0:
        
        if num1>num2:
            res = num1%num2
        else:
            res = num2%num1
        return res

first_num = int(input("Enter first number\n"))
second_num = int(input("Enter second number\n"))

user_req = input("Enter the operations you want to perform:\n Add- 1\n Sub- 2\n Mul- 3\n Div- 4\n")

if user_req == "1":
    show_result = add(first_num,second_num)
    print(show_result)
if user_req == "2":
    show_result = sub(first_num,second_num)
    print(show_result)
if user_req == "3":
    show_result = mul(first_num,second_num)
    print(show_result)  
if user_req == "4":
    show_result = div(first_num,second_num)
    print(show_result) 
         
    