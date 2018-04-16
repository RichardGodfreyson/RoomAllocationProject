import math

def diversity(numPeopleByGroup):
    '''
    inputs a dict type numPeopleByGroup representing number of people (value) in each group (key)
    outputs the infomation entropy of configuration
    '''

    entropy = 0
    totalPeople = sum(numPeopleByGroup.values())
    #cumulative sum of entropy for each element
    for key in numPeopleByGroup:
        probability = float(numPeopleByGroup[key]) / float(totalPeople)
        entropy += (- probability * math.log2(probability))
    return entropy

def inputNationality():
    '''
    reads nationalities from a list of inputs
    returns them in a list
    '''

    numberOfPeople = int (input ("Please input the number of people involved: "))
    nationalities = []
    for i in range(numberOfPeople):
        nationalities.append(input())
    return nationalities

def diversityEvaluation(allocation):
    '''
    inputs allocation of room {str:{}}
    each line contains the members of the room
    returns the diversity of the allocation
    '''
    
    div = 0
    for room in allocation.values():
        nationalities = [people[name] for name in room]
        div += diversity(Counter(nationalities)) #Calculate diversity for each room
    retrun diversity