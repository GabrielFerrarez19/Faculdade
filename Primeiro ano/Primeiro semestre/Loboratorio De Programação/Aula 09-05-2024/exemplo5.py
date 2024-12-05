#fazer um tabale de um campeonato, tendo os times
times={"SPFC","vASCO","atletico","paraisense"}
#SPFCXVASCO
#SPFCXATLETICO
#SPFCXPARAISENSE
#VASCOXSPFC
#VASCOXATLETICO
#VASCOXPARAISENSE
#ATLETICOXSPFC
#ATLETICOVASCO
#ATLETICOXPARAISENSE
#PARAISENSEXSPFC
#PARAISENSEXVASCO
#PARAISENSEXATLETICO
for timeA in times:
    for timeB in times:
        if timeA != timeB:
            print(f"{timeA} x {timeB}")
