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
        while Validate.user_counter <= 3 and Validate.comp_counter <= 3:
            if User.u_choice == 'Rock' and Comp.c_choice == 'Scissor':
                print("User got 1 point")
                Validate.user_counter += 1
                print(Validate.user_counter)
                if Validate.user_counter == 3:
                    print("User Won game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()

            elif User.u_choice == 'Rock' and Comp.c_choice == 'Paper':
                print("Comp got 1 point")
                Validate.comp_counter += 1
                print(Validate.comp_counter)
                if Validate.comp_counter == 3:
                    print("Comp Won Game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()
            elif User.u_choice == 'Paper' and Comp.c_choice == 'Rock':
                print("User got 1 point")
                Validate.user_counter += 1
                print(Validate.user_counter)
                if Validate.user_counter == 3:
                    print("User Won Game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()
            elif User.u_choice == 'Paper' and Comp.c_choice == 'Scissor':
                print("Comp got 1 point")
                Validate.comp_counter += 1
                print(Validate.comp_counter)
                if Validate.comp_counter == 3:
                    print("Comp Won Game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()
            elif User.u_choice == 'Scissor' and Comp.c_choice == 'Rock':
                print("Comp got 1 point")
                Validate.comp_counter += 1
                print(Validate.comp_counter)
                if Validate.comp_counter == 3:
                    print("Comp Won Game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()
            elif User.u_choice == 'Scissor' and Comp.c_choice == 'Paper':
                print("User got 1 point")
                Validate.user_counter += 1
                print(Validate.user_counter)
                if Validate.user_counter == 3:
                    print("User Won Game")
                else:
                    user.user_choice()
                    comp.comp_choice()
                    validate.score()
            else:
                print("Draw")
                user.user_choice()
                comp.comp_choice()
                validate.score()


user = User()
user.user_choice()
comp = Comp()
comp.comp_choice()
validate = Validate()
validate.score()

