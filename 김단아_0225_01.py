#문제 1.
gugudan = int(input("단을 입력하시오. => "))

print(f"**{gugudan}단**")
for i in range(1, 10):
    print(gugudan,'*', i,'=', (gugudan * i))


#문제 2.

fir_num = int(input("첫 번째 숫자를 입력하시오. => "))
sec_num = int(input("두 번째 숫자를 입력하시오. => "))

if fir_num > sec_num:
    fir_num, sec_num = sec_num, fir_num

for i in range(fir_num, sec_num + 1):
    print(f"\n**{i}단**")
    for fir in range(1, 10):
        print(i ,'*', fir, '=', i * fir )


#문제 3.
fir_num = int(input("첫 번째 숫자를 입력하시오. => "))
sec_num = int(input("두 번째 숫자를 입력하시오. => "))

if fir_num > sec_num:
    fir_num, sec_num = sec_num, fir_num

for dan in range(fir_num, sec_num + 1):
    print(f"**{dan}단**", end =  "   ")
print()
for i in range(1, 10):
        for dan in range(fir_num, sec_num + 1):
            print(f" {dan}*{ i }= { dan * i}", end= "  ")
        print()