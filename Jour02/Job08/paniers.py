def paniers(type,saison):
    if type == "fruits" and saison == "hiver":
        result = "orange, mandarine et kiwi"
    elif type == "fruits" and saison == "été":
        result = "poire, fraise, cassis"
    elif type == "légume" and saison == "hiver":
        result = "carotte, topinambour, endive"
    elif type == "légume" and saison == "été":
        result = "arichaut, aubergine, navet"
    print(result)

paniers("fruits","hiver")
paniers("fruits","été")
paniers("légume","hiver")
paniers("légume","été")