import random

def cointoss():
  headcount = 0
  tailcount = 0

  print "program is starting..."

  for toss in range(1, 5001):

    head = round(random.random()) == 1

    if (head):
      cointype = "head"
      headcount += 1
    else:
      cointype = "tails"
      tailcount += 1

    print "Attempt # " + str(toss) +  " throwing a coin... it's a " + str(cointype) + "! got " +  str(headcount)+ " heads so far and " + str(tailcount) + " tails..."

cointoss()
