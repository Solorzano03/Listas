
from Listas.Figuras_geometricas import Tfiguras , Ttriangulo ,Trectanglo,Trombo, Toctoedro
print("***Menu de Opciones***")
print("1.perimetro y area de un rectangulo: ")
print("2.perimertro, hipotenusa y area de un triangulo rectangulo: ")
print("3.perimetro y area de un rombo: ")
print("4.Area y Volumen de un ortoedro: ")
print("5.salir ")
op = int(input("digite la opcion a realizar: "))
match op:
     case 1:
         _base=int(input("ingrese un valor para la base: "))
         _altura=int(input("ingrese un valor para la altura: "))
         c=Ttriangulo(_base,_altura)
         print("el perimetro del rectanglo es: ", c.perimetro())
         print("el area del rectangulo es: ", c.area())
     case 2:
         _base=int(input("ingrese la base del triangulo: "))
         _altura=int(input("ingrese la altura del triangulo: "))
         b=Trectanglo(_base,_altura,)
         print("el area del trianglo es: ", b.area())
         print("el perimetro del triangualo ", b.perimetro())
     case 3:
          _base=int(input("ingrese valor del diametro mayor del rombo: "))
          _altura=int(input("ingrese valor del diametro mayor del rombo: "))
          r=int(input("ingrese valor del diametro menor del rombo: "))
          lado=int(input("ingrese el tamaño del lado: "))
          a=Trombo(_base,_altura,lado)
          print("el area del trianglo es: ", a.area())
          print("el perimetro del triangualo ", a.perimetro())
     case 4:
          _base=int(input("digite la base del ortoedro:"))
          _altura=int(input("digite la altura del ortoedro: "))
          prof=int(input("digite la profundidad del ortoedro:")) 
          d=Toctoedro(_base,_altura,prof)
          print("el area del ortoedro es: ", d.area())
          print("el volumen del ortoedro es: ", d.volumen())   
     case 5:
          print("salir")    

