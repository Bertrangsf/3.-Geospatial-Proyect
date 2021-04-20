def city_selection():
    roles = ['designer', 'developer', 'engineer', 'account manager', 'maintenance', 'executive']
    cities = ['madrid', 'miami', 'cape town']
    role = (input("What is your role 'Designer', 'Developer', 'Engineer', 'Account Manager', 'Maintenance', 'Executive'?: ")).lower()
    while role not in roles:
        role = (input("Remember a valid role 😆:  ")).lower()
    if role in roles:
        role
        
    city = (input("What would be your favourite city (Madrid, Miami or Cape Town?: ")).lower()
    while city not in cities:
        city = (input("Remember a valid city 😆:  ")).lower()
    if city in cities:
        city
    
    if role == "designer" or role == "developer" or role == "account manager" or role == "maintenance":
        if city == "madrid":
            election = 1
        elif city == "miami":
            election = 2
        else:
            election = 3
        
    elif role == "engineer" or role == "executive":
        if city == "madrid":
            election = 4
        elif city == "miami":
            election = 5
        else:
            election = 6
        
    return election

def The_Final_City():
    madrid = 0
    miami = 0
    cape = 0
    total = 61   # Total number of votes (13 employees are double weighted)

    while (madrid+miami+cape < total):
        question = city_selection()
        if question == 1: 
            madrid += 1
        elif question == 2:
            miami +=1
        elif question == 3:
            cape += 1   
        elif question == 4:
            madrid += 2
        elif question == 5:
            miami += 2
        else:
            cape += 2                
            
    if madrid > miami and madrid > cape :
        winner = "We are moving to Madrid🚀"
        
    if miami > madrid and miami > cape :
        winner = "We are moving to Miami🚀"        
        
    if cape > madrid and cape > miami :
        winner = "We are moving to Cape Town🚀"      
        
    return winner
            