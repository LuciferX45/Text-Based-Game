for i in range (1000):
    x=int(input("""enter the OPTION you want to use/play (if you want to exit then press 0) :
                                1.GUESSING NUMBER
                                2.MAGIC 8 BALL
                                3.LENGTH CONVERTER(STANDARD TO IMPERIAL)/(IMPERIAL TO STANDARD)
                                4.PASSWORD GENERATOR
                                5.MOON SURIVAL GAME
                                """))

    if x==1:
        print("YOU HAVE 5 GUESSES TO GUESS THE NUMBER")
        import random
        number = random.randint(1, 99)
        guesses = 0
        while guesses < 5:
            guess = int(input("Enter an integer from 1 to 99: "))
            guesses +=1
            print ("this is your guess ",guesses)
            if guess < number:
                print ("guess is low")
            elif guess > number:
                print ("guess is high")
            elif guess == number:
                print("you guessed it right")
                break
        if guess == number:
            guesses = str(guesses)
            print ("You guess it in : ", guesses + " guesses")
        if guess != number:
            number = str(number)
            print ("The secret number was",  number)

    elif x==2:
        import random
        ans = True

        while ans:
            question = input("Ask the magic 8 ball a question: (press enter to quit) ")
            answers = ["It is certain", \
            "It is decidedly so", \
            "Without a doubt", \
            "Yes definitely", \
            "You may rely on it", \
            "As I see it yes", \
            "Most likely", \
            "Outlook good", \
            "Yes", \
            "Signs point to yes", \
            "Reply hazy try again", \
            "Ask again later", \
            "Better not tell you now", \
            "Cannot predict now", \
            "Concentrate and ask again", \
            "Don't count on it", \
            "My reply is no", \
            "My sources say no", \
            "Outlook not so good", \
            "Very doubtful"]
    
            if question == "":
                print("blank question not answerable")
                exit
            else:
                print(answers[random.randint(0, len(answers))-1])

    elif x==3:
        i=True
        while i :
            u=int(input("""enter the conversion of length on the list (press 0 for exit ):
                                                1.km to miles
                                                2.m to ft
                                                3.cm to in
                                                4.miles to km
                                                5.m to ft
                                                6.cm to in
                                                """))
            if u==0:
                exit
            else:
                v=int(input("enter the value"))
                if u ==1:
                    print(v/1.6," miles")
                elif u==2:
                    print(v*3.26," ft")
                elif u==3:
                    print(v*2.54," in")
                elif u==4:
                    print(v*1.6," km")
                elif u==5:
                    print(v/3.26," m")
                elif u==6:
                    print(v/2.54," cm")

    elif x==4:
        import random
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"
        number =int(input('number of passwords?'))
        length = int(input('password length?'))
        print('\nhere are your passwords:')
        for pwd in range(0,number):
             password = ""
             for c in range(0,length):
                 password += random.choice(chars)
                 if len(password)==length:
                     print(password)
                 else:
                    continue

    elif x==5:
         items = [
        "A: 3 litres of water",
        "B: Shampoo",
        "C: An extra Spacesuit",
        "D: A shovel",
        "E: A 10 day oxygen supply",
        "F: Solar panels",
        "G: The seeds for your mission",
        "H: The soil for your mission",
        "I: A 3 day food supply"
        ]
         print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
         print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
         print("You can get to the base in 3 days on your lunar rover")
         print("The lunar rover can only fit you in your spacesuit and 4 other items")
         print("Out of the items below, which do you bring? \n")
         for o in items :
             print(o)

         print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces \n Ex: A,B,C,D")
         user_choice = input(">>> ")

         user_list =  list(user_choice.split(','))
         if "A" not in user_list:
           print("Without a liter of water a day you will dehydrate")
         if "E" not in user_list:
           print("Without oxygen you will not have any air to breathe!")
         if "F" not in user_list:
           print("Without solar panels your lunar rover will not have enough power to make it to the base")
         if "I" not in user_list:
           print("Although you might be able to survive without food for 3 days you will need your energy to drive the rover. You will not make it without food.")
         if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
           print("Hooray! You picked the correct 4 items. You will make it to the moonbase safely")
         else:
           print("You did not pick the correct 4 items for survival. You will not make it safely to the moon base.")


    elif x==0:
        break
        exit

    
    
   
