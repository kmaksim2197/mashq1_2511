# 1-misol
docs = input("Hujjat topshirilganmi? (ha/yo'q): ").strip().lower()
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ").strip().lower()
test = input("Testdan o'tdingizmi? (ha/yo'q): ").strip().lower()

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif docs == "ha" and interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif docs == "ha" and interview == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")

# 2-misol
s = input()
words = s.split()
code = ""
for w in words:
    code += w[0]
print(code)

# 3-misol
words = eval(input())

max1 = ""
max2 = ""

for w in words:
    if len(w) > len(max1):
        max2 = max1
        max1 = w
    elif len(w) > len(max2) and w != max1:
        max2 = w

print("1-chi eng uzun so'z:", max1)
print("2-chi eng uzun so'z:", max2)
