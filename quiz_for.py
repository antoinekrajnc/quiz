for i in range(0, 3):
  print("il vous reste {} chances".format(3 - i))
  question = input("Combien de fois la France a gagné la coupe du monde ?")
  if question == "2":
    print("Bravo, vous avez trouvé")
    chances_restantes = 3 - i
    break
  else:
    if i == 2:
        print("Ah, vous avez perdu le jeu...")
        chances_restantes = 0
    else:
        print("Dommage, vous n'avez pas la bonne réponse")

if chances_restantes >0:
    for i in range(0,chances_restantes):
      question = input("Quand est ce qu'a été fondé Apple ?")
      if question == "1976":
        print("Bravo, vous avez trouvé")
        chances_restantes = chances_restantes - i
        break
      else:
        if i == 2:
            print("Ah, vous avez perdu le jeu...")
        else:
            print("Dommage, vous n'avez pas la bonne réponse")
            print("il vous reste {} chances".format(chances_restantes - i -1))


if chances_restantes >0:
    for i in range(0,chances_restantes):
      question = input("Combien de vies possède un chat ?")
      if question == "9":
        print("Bravo, vous avez trouvé")
        chances_restantes = chances_restantes - i
        break
      else:
        if i == 2:
            print("Ah, vous avez perdu le jeu...")
        else:
            print("Dommage, vous n'avez pas la bonne réponse")
            print("il vous reste {} chances".format(chances_restantes - i -1))

if chances_restantes > 0:
    print("Bravo ! Vous avez gagné le quiz")
