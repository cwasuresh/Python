class MultipleFunction():
      def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

      def OddEven():
          try:  
            Num=int(input("Enter a Number :"))
          except ValueError:
            print("It Must be a number")
            return
          if(Num%2==0):
            print(Num," is Even Number")
          else:
            print(Num," is Odd Number:") 

      def Eligible():
            Gen = input("Your Gender :") 
            try:
               Age = int(input("Your Age :"))
            except ValueError:  
                  print("Age Must be a Number")
                  return          
      
            if Gen == "Male" and Age >= 21:
                    print("ELIGIBLE")
            elif Gen == "Female" and Age >= 18:
                    print("ELIGIBLE")
            elif Gen in ["Male", "Female"]:
                    print("NOT ELIGIBLE")
            else:
                    print("Enter Correct data")  

      def Percentage():
          try:
              Sub1=int(input("Subject1="))
          except ValueError:  
              print("It Must be a Number")
              return  
          try:
              Sub2=int(input("Subject2="))
          except ValueError:  
              print("It Must be a Number")
              return
          try:
              Sub3=int(input("Subject3="))
          except ValueError:  
              print("It Must be a Number")
              return
          try:
              Sub4=int(input("Subject4="))
          except ValueError:  
              print("It Must be a Number")
              return
          try:
              Sub5=int(input("Subject5="))
          except ValueError:  
              print("It Must be a Number")
              return
          Total=Sub1+Sub2+Sub3+Sub4+Sub5
          print("Total=",Total)
          percent=(Total/500*100)
          print("Percentage=",percent) 

      def triangle():
          try:
            Hight=float(input("Height:"))
          except ValueError:  
            print("Value Must be a Number")
            return 
          try:
            Brdth=float(input("Breadth"))
          except ValueError:  
            print("Value Must be a Number")
            return 
          AOT=((Hight*Brdth)/2)
          print("Area of Triangle:",AOT)
          try:
             Hight1=float(input("Height1:"))
          except ValueError:  
            print("Value Must be a Number")
            return
          try:
             Hight2=float(input("Height2:"))
          except ValueError:  
            print("Value Must be a Number")
            return
          try:
             Brdth1=float(input("Breadth:"))
          except ValueError:  
            print("Value Must be a Number")
            return
          Trigle=(Hight1+Hight2+Brdth1)
          print("Perimeter of Triangle:",Trigle)
    