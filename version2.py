import random


class User:
    u_choice = ''

    def user_choice(self):
        User.u_choice = input("Rock...Paper...Scissor... : ")
        print(User.u_choice)
        #return User.u_choice


class Comp(User):
    rps = ['Rock', 'Paper', 'Scissor']
    c_choice = ''

    def comp_choice(self):
        Comp.c_choice = random.choice(Comp.rps)
        print(Comp.c_choice)
        #return Comp.c_choice


class Validate(Comp):
    user_counter = 0
    comp_counter = 0

    def score(self):
        #while Validate.user_counter != 3 or Validate.comp_counter != 3:
        if User.u_choice == 'Rock' and Comp.c_choice == 'Scissor':
            print("User got 1 point")
            if Validate.user_counter == 2:
                print("User Won Game")
                exit()
            else:
                Validate.user_counter += 1
            print(Validate.user_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()

        elif User.u_choice == 'Rock' and Comp.c_choice == 'Paper':
            print("Comp got 1 point")
            if Validate.comp_counter == 2:
                print("Comp Won Game")
                exit()
            else:
                Validate.comp_counter += 1
            print(Validate.comp_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()
        elif User.u_choice == 'Paper' and Comp.c_choice == 'Rock':
            print("User got 1 point")
            if Validate.user_counter == 2:
                print("User Won Game")
                exit()
            else:
                Validate.user_counter += 1
            print(Validate.user_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()

        elif User.u_choice == 'Paper' and Comp.c_choice == 'Scissor':
            print("Comp got 1 point")
            if Validate.comp_counter == 2:
                print("Comp Won Game")
                exit()
            else:
                Validate.comp_counter += 1
            print(Validate.comp_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()

        elif User.u_choice == 'Scissor' and Comp.c_choice == 'Rock':
            print("Comp got 1 point")
            if Validate.comp_counter == 2:
                print("Comp Won Game")
                exit()
            else:
                Validate.comp_counter += 1
            print(Validate.comp_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()

        elif User.u_choice == 'Scissor' and Comp.c_choice == 'Paper':
            print("User got 1 point")
            if Validate.user_counter == 2:
                print("User Won Game")
                exit()
            else:
                Validate.user_counter += 1
            print(Validate.user_counter)
            user.user_choice()
            comp.comp_choice()
            validate.score()

        elif User.u_choice == Comp.c_choice:
            print("Draw")
            user.user_choice()
            comp.comp_choice()
            validate.score()


            """else:
                if Validate.user_counter == 3:
                    print("USER WON GAME......")
                else:
                    print("COMP WON GAME......")"""


user = User()
user.user_choice()
comp = Comp()
comp.comp_choice()
validate = Validate()
validate.score()

