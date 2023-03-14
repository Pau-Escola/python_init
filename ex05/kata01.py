kata = {
        'Python' : 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
x = kata.keys()
print (x[0] + " was created by " + kata.get(x[0]))
print (x[1] + " was created by " + kata.get(x[1]))
print (x[2] + " was created by " + kata.get(x[2]))
