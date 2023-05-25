Abbreviation = {
    "idk" : "I dont know",
    "Lmao": "laughing my ass off",
    "ily": "I love you",

}


userimput = input("enter an abbreviation")

print(Abbreviation)

if(userimput in Abbreviation):
    print(Abbreviation.get(userimput))
else:
    print("sorry, that word is not in the abbreviation list")

