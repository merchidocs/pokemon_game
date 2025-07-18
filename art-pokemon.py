import random
print('''    ,                           .::.
 PokeMon Logo Converted       .;:**'            AMC
                              `                  0
  .:XHHHHk.              db.   .;;.     dH  MX   0
oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN
QMMMMMb  "MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM
  `MMMM.  )M> :X!Hk. MMMM   XMM.o"  .  MMMMMMM X?XMMM MMM>!MMP
   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `" MX MMXXMM
    ~MMMMM~ XMM. .XM XM`"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP
     ?MMM>  YMMMMMM! MM   `?MMRb.    `"""   !L"MMMMM XM IMMM
      MMMX   "MMMM"  MM       ~%:           !Mh.""" dMI IMMP
      'MMM.                                             IMX
       ~M!M                                             IMP
''')
# Game intro
print("Welcome to the Pokemon Battle Arena!\n")

# Pokemon data
player_pokemon = {
    "name": "Pikachu",
    "hp": 100,
    "attack": [10, 20],  # random damage between 10–20
}

enemy_pokemon = {
    "name": "Charmander",
    "hp": 100,
    "attack": [8, 18],   # random damage between 8–18
}

print("🔥 A wild Charmander appeared!")
print(f"⚡ You send out {player_pokemon['name']}!")

# Game loop
while player_pokemon["hp"] > 0 and enemy_pokemon["hp"] > 0:
    input("\nPress Enter to attack...")

    # Player attacks enemy
    player_damage = random.randint(player_pokemon["attack"][0], player_pokemon["attack"][1
    ])
    enemy_pokemon["hp"] -= player_damage
    print(f"{player_pokemon['name']} attacks for {player_damage} damage!")

    # Check if enemy fainted
    if enemy_pokemon["hp"] <= 0:
        print(f"\n{enemy_pokemon['name']} fainted! 🎉 You win!")
        break

    # Enemy attacks player
    enemy_damage = random.randint(*enemy_pokemon["attack"])
    player_pokemon["hp"] -= enemy_damage
    print(f"{enemy_pokemon['name']} attacks for {enemy_damage} damage!")

    # Display HP
    print(f"\n{player_pokemon['name']} HP: {player_pokemon['hp']}")
    print(f"{enemy_pokemon['name']} HP: {enemy_pokemon['hp']}")

    # Check if player fainted
    if player_pokemon["hp"] <= 0:
        print(f"\n{player_pokemon['name']} fainted! 😵 You lose!")

print("\nGame over.")
