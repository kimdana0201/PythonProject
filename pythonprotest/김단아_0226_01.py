lis = []

while True:

    dct = {}
    dct['num'] = input("학번을 입력하세요.: ")
    if dct['num'].lower() == "exit":
        break
    dct['name'] = input("이름을 입력하세요.: ")
    dct['kor'] = int(input("국어 점수를 입력하세요.: "))
    dct['eng'] = int(input("영어 점수를 입력하세요.: "))
    dct['mat'] = int(input("수학 점수를 입력하세요.: "))
    dct['hap'] = dct['kor'] + dct['eng'] + dct['mat']
    dct['a'] = dct['hap'] / 3
    lis.append(dct)

    total = 0
    for dct in lis:
        total += 1
    total_2 = 0
    for dct in lis:
        total_2 += dct['a']

print()
print("\t\t\t\t\t\t***성적표***")
print("==========================================================")
print("   학번      이름     국어    영어    수학    총점    평균 ")
print("==========================================================")
for dct in lis:
    print("%4s   %3s   %4d   %4d   %4d    %4d    %4.2f" %
          (dct['num'], dct['name'], dct['kor'], dct['eng'], dct['mat'], dct['hap'], dct['a']))
print("==========================================================")
print(f"\t\t\t학생수: {total}", "\t\t\t전체 평균: %4.2f" % (total_2 / total))