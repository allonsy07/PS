from cv2 import sort
from numpy import arange


'''
N = int(input)

array = []
for i in range(N):
    input_data = input.split()
    array.append((input_data[0],input_data[1],input_data[2],input_data[3]))
'''

array = [("Junkyu", 50, 60, 100), ("Sangkeun",80,60,50), ("Sunyoung",80,70,100),("Soong",50,60,90)
,("Haebin", 50,60,100), ("Kangsoo", 60, 80, 100), ("Donghyuk",80,60,100),("Sei", 70, 70, 70),("Wonseob", 70,70,90), ("Sanghyun",70,70,80)
,("nsj",80,80,80), ("Taewhan",50,60,90)]
array = sorted(array, key=lambda student: (-student[1], student[2], -student[3], student[0]))

for student in array:
    print(student[0], end=' ')