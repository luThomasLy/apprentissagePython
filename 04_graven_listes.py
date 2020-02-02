online_players = ["thomas","lune","lumiere", "toto"]
print(online_players)
print(online_players[0])
print(online_players[len(online_players) - 1])

#modifier thomas en thomaslune
online_players[0] = "thomaslune"
online_players[2:4] = ["Paul","Jacques"]

#ajout à la fin de la liste
online_players.append("gamers123")
online_players.extend(["Gom","gim"])

print(online_players)