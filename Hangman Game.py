#Hangman game
#In this game, there are words present, out of which the interpreter will choose 1 random word.
#The user first has to input their names and then, will be asked to guess any alphabet.
#If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet.
#User will be given few turns(can be changed accordingly) to guess the complete word.
#In the hangman game the user has to guess the correct words to save a life

import random

class game(object):
    # Hangman game
    dangle = []
    dangle.append(' *===*')
    dangle.append(' *   *')
    dangle.append('     *')
    dangle.append('     *')
    dangle.append('     *')
    dangle.append('     *')
    dangle.append(' =====')
    lad = {}
    lad[0] = [' @   *']
    lad[1] = [' @   *', ' !   *']
    lad[2] = [' @   *', '/!   *']
    lad[3] = [' @   *', '/!\\  *']
    lad[4] = [' @   *', '/!\\  *', '/    *']
    lad[5] = [' @   *', '/!\\  *', '/ \\  *']
    z = []
    states = ''' gujarat kerala karnataka westbengal maharashtra uttarakhand odisha tamilnadu
                bihar telangana rajasthan chhattisgarh assam jharkhand haryana andhrapradesh 
                punjab madhyapradesh goa newdelhi ladakh jammukashmir arunachalpradesh manipur 
                nagaland mizoram tripura meghalaya sikkim '''.split()

    design = '@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\''

    def __init__(K, *args, **kwargs):
        m, n = 2, 0
        K.z.append(K.dangle[:])
        for k in K.lad.values():
            p, n = K.dangle[:], 0
            for i in k:
                p[m + n] = i
                n += 1
            K.z.append(p)
    def Select_Word(K):
        return K.states[random.randint(0, len(K.states) - 1)]
    def photo(K, x, wordLen):
        for slash in K.z[x]:
            print(slash)
    def game(K, term, value, notpresent):
        q = input()
        if q == None or len(q) != 1 or (q in value) or (q in notpresent):
            return None, False
        m = 0
        p = q in term
        for i in term:
            if i == q:
                value[m] = i
            m += 1
        return q, p
    def data(K, data):
        x = len(K.design)
        print(K.design[:-3])
        print(data)
        print(K.design[3:])
    def process(K):
        name = input("Enter your name: ")
        print("Good Luck ,",name)
        print('*****Hangman game starts*****')
        term = list(K.Select_Word())
        outcome = list('_' * len(term))
        print('The state is: ', outcome)
        y, m, k = False, 0, []
        while m < len(K.z) - 1:
            print('Guess the state name : ', end='')
            x, x1 = K.game(term, outcome, k)
            if x == None:
                print('Repeated character.')
                continue
            print(''.join(outcome))
            if outcome == term:
                K.data('Excellent ! You saved a life :)')
                y = True
                break
            if not x1:
                k.append(x)
                m += 1
            K.photo(m, len(term))
            print('Missed words: ', k)
        if not y:
            K.data('The state was \'' + ''.join(term) + '\' Game over ! Man was hanged')

a = game().process()