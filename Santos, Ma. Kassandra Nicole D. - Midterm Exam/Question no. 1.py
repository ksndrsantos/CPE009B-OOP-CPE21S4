def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp

 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9)/5 +32

 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15

 class FahrenheitToCelsius(TemperatureConversion):
     def conversion(self):
         return (self._temp - 32 ) * (5/9)

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print("Celsius to Kelvin")
 print(str(convert.conversion()) + " Kelvin")

 print("Celsius to Fahrenheit")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")

 tempInFahrenheit = float(input("Enter the temperature in fahrenheit: "))
 print("Fahrenheit to Celsius")
 convert = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + " celsius")


main()