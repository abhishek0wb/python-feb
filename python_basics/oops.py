class Car:
   
   totalcar = 0

   def __init__(self, brand, model, fuel_type):
      self.__brand = brand
      self.__model = model
      self.fuel = fuel_type
      Car.totalcar += 1

# to private any attribute we have put "__" before the name of it.
   
   def get_brand(self):
      return self.__brand + " !"

# get_ method is to access the private attributes.


   def fullname(self):
     return f"{self.__brand} {self.__model} "
  
   
#  brand, model which are pass inside __init__ are parameters.
#  self.brand means, variable from inside class.
          
   @staticmethod  
   def general_description():
      return "car are mean of transport"  

   @property
   def model(self):
      return self.__model

# property decorater used to make a attribute private. 
   # access it only thought my method.

class ElectricCar(Car):
#  we can access car class in the electriccar class by just passing it inside brackets.
     def __init__(self, brand, model,fuel):
        super().__init__(brand, model, fuel)
#  super() keyword help us access the above attributes.


# mytesla = ElectricCar("Tesla", "Model S", "85kh", "Electricitys", "fuel")

# print(mytesla.model)
# print(isinstance(mytesla, Car))
# print(isinstance(mytesla, ElectricCar))


# print(mytesla.get_brand(), mytesla.fuel)
# print(mytesla.battery_size)
# print(mytesla.general_description())
# print(mytesla.fullname())
# print(mytesla.get_brand())

mycar = Car("maruti", "autok10", "Petrol")  
# print(mycar.get_brand(), mycar.fuel)  
# print(Car.totalcar)

# mycar.model = "city"
# print( mycar.model)
# print( mycar.fullname())
# print(mycar.fuel)

  
#  after so many error message finally get_ worked. 
# get_brand() can only work, neither brand and __brand because both are private.

class Battery:
  def battery_info(self):
     return "this is battery"

class Engine:
   def engine_info(self):
      return "this is engine"


class EV(Car, Battery, Engine):
   pass


testingcar = EV("mg", "comet", "fuel_type")
print(testingcar.engine_info())