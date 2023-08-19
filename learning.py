# angka = 1
# nama = "maman"

# Casting
# angka_str = str(angka)
# print(type(angka_str))

# input & output

# kelas = input("Kelas berapa: ")
# print(f"Selamat datang di kelas {kelas}")

# operator,operand & aritmatik
# angka1 = 9
# angka2 = 8

# print(angka1+angka2)
# print(angka1-angka2)
# print(angka1*angka2)
# print(angka1/angka2)
# print(angka1//angka2)
# print(angka1 % angka2)
# print(angka1**angka2)

# angka1 += 5
# print(angka1)

# library math
# import math

# print(math.pow(2, 3))  # pangkat
# print(math.ceil(2.3))  # bulat ke atas
# print(math.sqrt(25))  # akar

# Escape character
# print("\"Selamat Datang\"")

# String methods
# nama = "Dadang"
# nama_belakang = "arjuna"
# umur = 37

# print(nama.upper())
# print(nama.lower())
# print(nama.split())
# print(len(nama))
# print(nama.capitalize())
# print(nama.index("g"))
# # slicing
# print(nama[2:])
# print(nama[:2])
# print(nama[-2])
# print(nama[-4:-2])
# # concat
# print(nama + " " + nama_belakang)
# # format
# print(f"nama lengkap {nama+nama_belakang} umur {umur}")

# in not in

# text = "Maman Suprman"
# print("Maman" in text)
# print("Maman" not in text)

# Conditional
# x = 5
# y = 7
# z = 8
# print(x < y or y > z)
# print(x < y and y > z)

# if x > 3:
#     print("Hallo people")
# elif x == 5:
#     print("hallo baraya")
# else:
#     print("Hallo Indonesia")

# Loop
# start = 0
# stop = 5
# step = 2
# for i in range(start, stop, step):
#     print(i)

# default parameter start = 0 stop = 5 step = 1
# for i in range(5):
#     if i == 3:
#         # break
#         continue

#     print(i)

# nilai = 30

# while (nilai < 70):
#     print(f"Nilai Sekarang: " + str(nilai))
#     nilai += 5

# Data Collection
# List: sebuah koleksi urut dan dapat diganti dan bisa menampung elemen yang duplikat

# List = [1, "dadan", 5, "ujang"]
# List2 = List.copy()
# List2[1] = "Maman"
# print(List)
# print(List2)

# Tuple : sama dengan list, tapi elemen tidak bisa diubah dan simbolnya ()
# Dictionary : menyimpan data dalam bentuk key value

# costumer = {
#     # key:value
#     "id": 100,
#     "nama": "Budi",
#     "Umur": 30
# }

# Set : kumpulan elemen unik yang tidak memiliki urutan

# numbers1 = {1, 3, 5, 4, 10}
# numbers2 = {3, 4, 10, 7, 8}

# numbers_union = numbers1.union(numbers2)   #{1, 3, 4, 5, 7, 8, 10}
# print(numbers_union)
# numbers_difference = numbers1.difference(numbers2)
# print(numbers_difference)
# symmetric_difference = numbers1.symmetric_difference(numbers2)
# print(symmetric_difference)
# intersection = numbers1.intersection(numbers2)
# print(intersection)

# Function

# def masak(name, amount):
#     print("nama Masakan :"+name)
#     print("Jumlah :" + str(amount))


# masak("ayam bakar", 3)
# masak(amount=9, name="Daging Kambing")

# lambda


# def tambah(x):
#     return x+5

# print(tambah(3))

# tambah = lambda x: x+5
# print(tambah(5))

# OOP

# class Person:
#     nama = "Budi"


# object = Person()

# print(object.nama)


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year


# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Honda", "Civic", 2022)

# # print(car1.brand)
# print(car1.__dict__)

# Inheritance


# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year


# class Car(Vehicle):
#     def __init__(self, brand, model, year):
#         super().__init__(brand, year)
#         self.model = model


# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Honda", "Civic", 2022)

# print(car1.brand)  # Output: Toyota
# print(car2.model)  # Output: Civic
