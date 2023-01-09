list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for x in range(len(list)):
    list.append(list[x])

message = input("Tapez votre message : ")
clef = int(input("Tapez votre clef : "))

def lettre_codée(lettre, list, clef):
    for i in range(len(list)):
        if lettre == " ":
            return " "
        elif list[i]==lettre:
            return str(list[i+clef])
    return "?"

message_chiffré = str()

for lettre in message:
    message_chiffré += lettre_codée(lettre, list, clef)

print(message_chiffré)