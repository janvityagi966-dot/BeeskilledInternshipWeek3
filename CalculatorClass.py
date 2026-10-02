class calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num1 = int(input("Enter Number: "))
        self.num2 = int(input("Enter Other Number: "))

    def Addition(self):
        return self.num1 + self.num2
    
    def Subtraction(self):
      if self.num1>self.num2:
        return self.num1 - self.num2
      else:
          return None
    
    def Multiplication(self):
        return self.num1 * self.num2
    
    def Division(self):
      try:
        return self.num1 / self.num2
      except ZeroDivisionError:
        return None
    
def main():
    Operations = calculator()

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Addition= ",Operations.Addition())
        elif choice == "2":
            print("Subtraction= ",Operations.Subtraction())
        elif choice == "3":
            print("Multiplication= ",Operations.Multiplication())
        elif choice == "4":
            print("Division= ",Operations.Division())
        elif choice == "5":
            print("Thank you for using the calculator.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
                        

        
    
    
       