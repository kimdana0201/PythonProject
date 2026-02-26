lis = []

while True:

    a = []
    a.append(input("학번을 입력하세요.: "))
    if a[0].lower() == "exit":
        break
    a.append(input("이름을 입력하세요.: "))
    a.append(int(input("국어 점수를 입력하세요.: ")))
    a.append(int(input("영어 점수를 입력하세요.: ")))
    a.append(int(input("수학 점수를 입력하세요.: ")))
    a.append(a[2] + a[3] + a[4]) #총점
    a.append(a[5] / 3) #평균

    lis.append(a)
    print() #줄바꿈

    total = 0
    for a in lis:
        total += 1 # +1로 인원수

    total_2 = 0
    for a in lis:
        total_2 += a[6]


print()
print("\t\t\t\t\t\t***성적표***")
print("==========================================================")
print("   학번      이름     국어    영어    수학    총점    평균 ")
print("==========================================================")
for a in lis: #a 는 가독성이 떨어지니 student로 바꿔서 아래 print도 student[]로 바꾸는 것이 좋을 듯.
    print("%4s   %3s   %4d   %4d   %4d    %4d    %4.2f" %
          (a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
print("==========================================================")
print(f"\t\t\t학생수: {total}", "\t\t\t전체 평균: %4.2f" % (total_2 / total))