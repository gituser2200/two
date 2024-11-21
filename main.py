import random,time


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0

    def create_hero(name, race):
        name = name
        hp = 0
        damage = 0
        if race == race_list[0]:
            hp += 50
            damage += 50
        elif race == race_list[1]:
            hp += 65
            damage += 60
        elif race == race_list[2]:
            hp += 45
            damage += 50
        elif race == race_list[3]:
            hp += 80
            damage += 50
        elif race == race_list[4]:
            hp += 70
            damage += 65
        else:
            print("Tu CDeLaL OIIIu6Ky")
            quit()
        return Player(name, hp, damage)

    def attack(self, victim):
        max_exp = 25*self.lvl
        rnd_attk = random.randint(1,5)
        if rnd_attk == 1:
            print("Ты ультанул!!!!!!")
            victim.hp -= self.damage*2
        elif rnd_attk == 2:
            print("Ну, ты промазал....")
        else:
            victim.hp -= self.damage
        if victim.hp <= 0:
            rnd_exp = random.randint(10,25)
            self.exp+=rnd_exp
            print(f"TbI no6eDuJI U BbIirpaJI KaPaC9I, и получил {rnd_exp} опыта")
            if self.exp>=max_exp:
                self.level_up(max_exp)
            if self.lvl%3==0:
                weapon=self.create_weapon
                print(f"Вам выпало {weapon[1]} оружие:{weapon[0]}")
            return False
        else:
            print(f"Y {victim.name} OcTaJIoC {victim.hp} 3DoPoBuya")
            return True

    def level_up(self,max_exp):
        self.exp-=max_exp
        self.lvl+=1
        self.damage+=2
        self.hp+=1
        print(f"твой уровень повысился!у тебя {self.hp} эйчпи и {self.damage} дэмэджа.level:{self.lvl}.{self.exp}")


    def create_weapon(self):
        rnd_type=weapon_types [random.randint(0,3)]
        rnd_rare=random.choice(list(weapon_rarity.keys()))
        if rnd_type == weapon_types[0]:
            self.damage+=2*rnd_rare
        elif rnd_type == weapon_types[1]:
            self.damage+=3*rnd_rare
        elif rnd_type == weapon_types[2]:
            self.damage+=5*rnd_rare
        elif rnd_type == weapon_types[3]:
            self.damage+=8*rnd_rare
        return rnd_type,weapon_rarity[rnd_rare]






class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def create_enemy():
        r_name = random.choice(spesok_vragov)
        r_hp = random.randint(40, 60)
        r_damage = random.randint(40,45)
        return Enemy(r_name, r_hp, r_damage)

    def attack(self, victim):
        rnd_attk = random.randint(1, 5)
        if rnd_attk == 1:
            print("Враг кританул!!!!!!")
            victim.hp -= self.damage * 2
        elif rnd_attk == 2:
            print("Ура враг промазал!!!!")
        else:
            victim.hp -= self.damage
        if victim.hp <= 0:
            print("TbI npoUrpAJI")
            quit()
        else:
            print(f"Y {victim.name} OcTaJIoC {victim.hp} 3DoPoBuya")


def fight_choice():
    vopros = input('Xo4eIII Boo6IIIe Cpa)I(aTca? "Da" "Hexo4y"')
    if vopros == "Da":
        atk = player.attack(enemy)
        if atk:
            enemy.attack(player)
            fight_choice()
    elif vopros == "Hexo4y":
        escape = random.randint(1,100)
        if escape<=25:
            print("блина тебя догнали")
            enemy.attack(player)
            fight_choice()
        else:
            print("ну как хочишь блин")
    else:
        print("таково вареанта нета")
        fight_choice()

race_list = ["KaPJIUK", "rHoMUK", "JIuJIunuTuK", "PuCCKUY", "AMERICANEC"]
spesok_vragov = ["Pudge", "nepBoKJIaccHuK", "El_PriMo", "KPUnEP", "TAPAKAH"]
weapon_rarity = {1:"Обычное", 2:"Редкое", 3:"Эпическое", 4:"Легендарное"}
weapon_types = ["Мечь", "Лук", "Клинок", "Посох"]
my_name = input("nPuBeT_UrPoK,KaK Te69I 3oByT?")
race = input(f"BubePy CBoю Race(ZheLateLno PuCCKUY){race_list}:")
player = Player.create_hero(my_name, race)
print(f"Tu Bu6PaJI HuKHaMe {player.name},Y TeBya {player.hp} hp,{player.damage} damage,")
while True:
    time.sleep(2)
    rand_num = random.randint(1, 3)
    if rand_num == 1:
        print("Не встретил никого")
    elif rand_num == 2:
        print("Встретил монстра")
        enemy = Enemy.create_enemy()
        print(f"Имя врага {enemy.name}, у него {enemy.hp} эйчпи, и у него {enemy.damage} дэмэдж")
        time.sleep(2)
        print(f"у тебя {player.hp} эйчпи,{player.damage} дэмэджа,твой лвл:{player.lvl},опыт:{player.exp} ")
        fight_choice()
    elif rand_num == 3:
        print("Нашел помидор")
        player.hp += 10
        print(f"Теперь у тебя {player.hp} хп")


