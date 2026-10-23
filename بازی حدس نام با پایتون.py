from random import choice

list_g= input(" لبستت رو بهم بده ففط حواست باشه با , اسامی رو از هم جدا کنی:")
karbar = list_g.split(",")
print(karbar,
      "لیست نهایی شما")
karbar_cp = karbar.copy()

while True:
    if len(karbar_cp) == 0:
        print("همه رو کفتم که ! کیرمون کردی داش")
        break

    cmp_choice = choice(karbar_cp)
    ans = input(f"حدس شما این بود؟ {cmp_choice} بله/خیر : ")

    if "بله" in ans:
        print("افرین به خودم.")
        break
    elif "خیر" in ans:
       print("بزار یه حدس دیگه بزنم .")

    else:
       print("خشگل از اسامی که دادی تو لیست بگو")


    karbar_cp.remove(cmp_choice)
