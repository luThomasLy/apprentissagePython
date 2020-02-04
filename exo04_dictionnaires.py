people = {
    "toto": {
        "email": "tly@lap.com",
        "tel": "06.xx.xx.xx.xx",
    },
    "titi": {
        "email": "tly@gmail.com",
        "tel": "07.xx.xx.xx.xx",
    }
}

print((people.get("toto")).get("email"))
print((people.get("titi")).get("tel"))
print(people)