lines = str.split(open('Alexa_Responses.txt').read(), '\n')

for line in lines:
    if line != '':
        tup = line.split(': ')
        print 'responses[\'' + tup[0] + '\'] = \'' + tup[1] + '\''
