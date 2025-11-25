hujjat = input("Hujjat topshirdingizmi? (ha/yo'q): ").lower()
if hujjat != "ha":
    print("Avvalo hujjatlaringizni topshiring.")
else:
    suhbat = input("Suhbatdan o'tdingizmi? (ha/yo'q): ").lower()
    if suhbat != "ha":
        print("Suhbatdan o'tmagansiz.")
    else:
        test = input("Testdan o'tdingizmi? (ha/yo'q): ").lower()
        if test != "ha":
            print("Test natijalari yetarli emas.")
        else:
            print("Jarayon davom etmoqda – degan xabar chiqsin.")
            print("Tabriklaymiz! Siz ishga qabul qilindingiz!")

print("Salom bu mening yangi loyiham")
print("Salom!")
print("Bugun havo juda chiroyli")

royxat = [4, 7, 2, 5, 1, 10]
ma_lumot = [x for x in royxat if x % 2 == 0]
print(ma_lumot)
