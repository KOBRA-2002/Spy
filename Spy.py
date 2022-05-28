# -*- coding: cp1251 -*-
import random

colors = ['�������','������','�������','������','�����','�������','���������']

number_of_spy = 0

class Person:
    def __init__(self, weight, height, gender, age, color_eyes, color_hair):
        self.weight = weight
        self.height = height
        self.gender = gender
        self.age = age
        self.color_eyes = color_eyes
        self.color_hair = color_hair

def compare(person1, person2):
    i = 0
    if person1.weight == person2.weight:
        i += 1
    if person1.height == person2.height:
        i += 1
    if person1.gender == person2.gender:
        i += 1
    if person1.age == person2.age:
        i += 1
    if person1.color_eyes == person2.color_eyes:
        i += 1
    if person1.color_hair == person2.color_hair:
        i += 1

    if i > 2:
        print("OK")
        return True
    else:
        return False

def create_random_person(number_person):
    for i in range(number_person):
        weight = random.randint(0, 100)
        height = random.randint(0, 100)
        gender = ('F','M')[random.randint(0,1)]
        age = random.randint(0, 80)
        color_eyes = colors[random.randint(0, len(colors)-1)]
        color_hair = colors[random.randint(0, len(colors)-1)]
        print("i= " + str(i))
        print("���: " + str(weight))
        print("����: " + str(height))
        print("���: " + str(gender))
        print("�������: " + str(age))
        print("���� ����: " + color_eyes)
        print("���� �����: " + color_hair)
        yield Person(weight, height, gender, age, color_eyes, color_hair)

def main():
    global number_of_spy
    print("����� ����������!")
    N = int(input("������ ������ ���������: "))
    print("##########")
    w = int(input("���: "))
    print("##########")
    h = int(input("����: "))
    print("##########")
    print("1-�������")
    print("2-�������")
    g = ('F','M')[int(input("���: "))-1]
    print("##########")
    a = int(input("�������: "))
    print("##########")
    for i in range(len(colors)):
        print(str(i+1) + ' - ' + colors[i])
    color_eyes = colors[int(input("���� ����: "))-1]
    print("##########")
    for i in range(len(colors)):
        print(str(i+1) + ' - ' + colors[i])
    color_hair = colors[int(input("���� �����: "))-1]
    print("##########")
    spy = Person(w,h,g, a,color_eyes, color_hair)
    generator = create_random_person(N)
    for person in generator:
        res = compare(spy, person)
        if res:
            number_of_spy += 1
            print("�������� �������")
        else:
            print("������� �� ��������")
    print("���������� ��������� �������: " + str(number_of_spy))

if __name__ == '__main__':
    main()