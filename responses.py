lines = str.split(open('Alexa_Responses.txt').read(), '\n')

for line in lines:
    if line != '':
        tup = line.split(': ')
        print 'responses[' + tup[0] + '] = ' + tup[1]

'''
responses = {}
responses[KXOU] = It's the glass room in front of you to the left!
responses[Crossroads] = Go down the hall to your left. It will be on your right after the ramp.
'''
