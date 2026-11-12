
import random
import time

player = input("Qahramon ismini kiriting: ")

jon = 100
pul = 100
level = 1
kuch = 20
tajriba = 0

print("\n⚔️ RPG O'YINIGA XUSH KELIBSIZ!")
print("Qahramon:", player)

while True:
    print("\n========== MENU ==========")
    print("1. Jang qilish")
    print("2. Do'kon")
    print("3. Holat")
    print("4. Dam olish")
    print("5. O'yindan chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        maxluq = random.randint(20, 80)
        print("\n👹 Dushman paydo bo'ldi!")
        print("Dushman kuchi:", maxluq)

        while maxluq > 0 and jon > 0:
            print("\n1. Hujum")
            print("2. Qochish")

            amal = input("Amal: ")

            if amal == "1":
                zarar = random.randint(10, kuch)
                maxluq -= zarar
                print("⚔️ Siz", zarar, "zarar berdingiz!")

                if maxluq > 0:
                    dushman_zarari = random.randint(5, 20)
                    jon -= dushman_zarari
                    print("👹 Dushman sizga", dushman_zarari, "zarar berdi!")

            elif amal == "2":
                print("🏃 Siz qochdingiz!")
                break

            else:
                print("Noto'g'ri tanlov!")

        if maxluq <= 0:
            print("\n🏆 G'ALABA!")
            pul += 50
            tajriba += 30
            print("+50 oltin, +30 XP")

        if jon <= 0:
            print("O'yin tugadi!")
            break

        if tajriba >= level * 50:
            level += 1
            kuch += 10
            jon = 100
            print("🔥 LEVEL OSHDI!")
            print("Yangi level:", level)

    elif tanlov == "2":
        print("\n====== DO'KON ======")
        print("1. Kuchni oshirish - 50 oltin")
        print("2. Jonni tiklash - 30 oltin")
        print("3. Chiqish")

        buyum = input("Tanlang: ")

        if buyum == "1" and pul >= 50:
            pul -= 50
            kuch += 10
            print("⚔️ Kuch oshdi!")

        elif buyum == "2" and pul >= 30:
            pul -= 30
            jon = 100
            print("❤️ Jon tiklandi!")

        elif buyum == "3":
            continue

        else:
            print("Pul yetarli emas!")

    elif tanlov == "3":
        print("\n====== Qahramon ======")
        print("Ism:", player)
        print("Level:", level)
        print("Jon:", jon)
        print("Kuch:", kuch)
        print("Oltin:", pul)
        print("XP:", tajriba)

    elif tanlov == "4":
        jon = min(100, jon + 30)
        print("❤️ 30 jon tiklandi!")

    elif tanlov == "5":
        print("O'yin tugadi. Xayr,", player)
        break

    else:
        print("Bunday tanlov yo'q!")