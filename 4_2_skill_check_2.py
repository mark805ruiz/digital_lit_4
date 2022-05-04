def getInput(word):
    print('Give me a ' + word)
    userInput = input()
    return userInput

person = 'person.'
verb = 'verb.'
place = 'place.'
item = 'item (plural).'

print('Welcome to MadLibs!')
person = getInput(person)
place = getInput(place)
verb = getInput(verb)
item = getInput(item)

print('The %s went to the %s to %s a box of %s.' % (person, place, verb, item))
