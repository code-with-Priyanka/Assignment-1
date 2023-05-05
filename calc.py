class Calc:
    def __init__(self,first_num,second_num):
        self.first_num = first_num
        self.second_num = second_num
    def add(self):
        res = self.first_num+self.second_num
        return res
    def sub(self):
        res = self.first_num-self.second_num
        return res 
    def mul(self):
        res = self.first_num*self.second_num
        return res
    def div(self):
        res = self.first_num / self.second_num
        return res 
 
first_num = int(input("Enter first number\n"))
second_num = int(input("Enter second number\n"))
obj = Calc(first_num,second_num)
user_req = input("Enter the operations you want to perform:\n Add- 1\n Sub- 2\n Mul- 3\n Div- 4\n")
def main():
    while True:
        if user_req == "1":
            show_result = obj.add()
            print(show_result)
        elif user_req == "2":
            show_result = obj.sub()
            print(show_result)
        elif user_req == "3":
            show_result = obj.mul()
            print(show_result)  
        elif user_req == "4":
            show_result = obj.div()
            print(show_result)
        else:
            print("Invalid Options\n")     
            
            