#!/usr/local/bin/python2.7
    
TypeStrings = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electr', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']

Matrix = [[1.0 for x in xrange(18)] for x in xrange(18)]

#Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electr, Psychic, Ice, Dragon, Dark, Fairy

#Normal
Matrix[0][5] = 0.5
Matrix[0][7] = 0.0
Matrix[0][8] = 0.5

#Fighting
Matrix[1][0] = 2.0
Matrix[1][2] = 0.5
Matrix[1][3] = 0.5
Matrix[1][5] = 2.0
Matrix[1][6] = 0.5
Matrix[1][7] = 0.0
Matrix[1][8] = 2.0
Matrix[1][13] = 0.5
Matrix[1][14] = 2.0
Matrix[1][16] = 2.0
Matrix[1][17] = 0.5

#Flying
Matrix[2][1] = 2.0
Matrix[2][5] = 0.5
Matrix[2][6] = 2.0
Matrix[2][8] = 0.5
Matrix[2][11] = 2.0
Matrix[2][12] = 0.5

#Poison
Matrix[3][3] = 0.5
Matrix[3][4] = 0.5
Matrix[3][5] = 0.5
Matrix[3][7] = 0.5
Matrix[3][8] = 0.0
Matrix[3][11] = 2.0
Matrix[3][17] = 2.0

#Ground
Matrix[4][2] = 0.0
Matrix[4][3] = 2.0
Matrix[4][5] = 2.0
Matrix[4][6] = 0.5
Matrix[4][8] = 2.0
Matrix[4][9] = 2.0
Matrix[4][11] = 0.5
Matrix[4][12] = 2.0

#Rock
Matrix[5][1] = 0.5
Matrix[5][2] = 2.0
Matrix[5][4] = 0.5
Matrix[5][6] = 2.0
Matrix[5][8] = 0.5
Matrix[5][9] = 2.0
Matrix[5][14] = 2.0

#Bug
Matrix[6][1] = 0.5
Matrix[6][2] = 0.5
Matrix[6][3] = 0.5
Matrix[6][7] = 0.5
Matrix[6][8] = 0.5
Matrix[6][9] = 0.5
Matrix[6][11] = 2.0
Matrix[6][13] = 2.0
Matrix[6][16] = 2.0
Matrix[6][17] = 0.5

#Ghost
Matrix[7][0] = 0.0
Matrix[7][7] = 2.0
Matrix[7][13] = 2.0
Matrix[7][16] = 0.5

#Steel
Matrix[8][5] = 2.0
Matrix[8][8] = 0.5
Matrix[8][9] = 0.5
Matrix[8][10] = 0.5
Matrix[8][12] = 0.5
Matrix[8][14] = 2.0
Matrix[8][17] = 2.0

#Fire
Matrix[9][5] = 0.5
Matrix[9][6] = 2.0
Matrix[9][8] = 2.0
Matrix[9][9] = 0.5
Matrix[9][10] = 0.5
Matrix[9][11] = 2.0
Matrix[9][14] = 2.0
Matrix[9][15] = 0.5

#Water
Matrix[10][4] = 2.0
Matrix[10][5] = 2.0
Matrix[10][9] = 2.0
Matrix[10][10] = 0.5
Matrix[10][11] = 0.5
Matrix[10][15] = 0.5

#Grass
Matrix[11][2] = 0.5
Matrix[11][3] = 0.5
Matrix[11][4] = 2.0
Matrix[11][5] = 2.0
Matrix[11][6] = 0.5
Matrix[11][8] = 0.5
Matrix[11][9] = 0.5
Matrix[11][10] = 2.0
Matrix[11][11] = 0.5
Matrix[11][15] = 0.5

#Electr
Matrix[12][2] = 2.0
Matrix[12][4] = 0.0
Matrix[12][10] = 2.0
Matrix[12][11] = 0.5
Matrix[12][12] = 0.5
Matrix[12][15] = 0.5

#Psychic
Matrix[13][1] = 2.0
Matrix[13][3] = 2.0
Matrix[13][8] = 0.5
Matrix[13][13] = 0.5
Matrix[13][16] = 0.0

#Ice
Matrix[14][2] = 2.0
Matrix[14][4] = 2.0
Matrix[14][8] = 0.5
Matrix[14][9] = 0.5
Matrix[14][10] = 0.5
Matrix[14][11] = 2.0
Matrix[14][14] = 0.5
Matrix[14][15] = 2.0

#Dragon
Matrix[15][8] = 0.5
Matrix[15][15] = 2.0
Matrix[15][17] = 0.0

#Dark
Matrix[16][1] = 0.5
Matrix[16][7] = 2.0
Matrix[16][13] = 2.0
Matrix[16][16] = 0.5
Matrix[16][17] = 0.5

#Fairy
Matrix[17][1] = 2.0
Matrix[17][3] = 0.5
Matrix[17][8] = 0.5
Matrix[17][9] = 0.5
Matrix[17][15] = 2.0
Matrix[17][16] = 2.0

def getTypes(n):
  #Return a boolean[] with the types of combination n
  print('Getting types for ' + repr(n))
  k = 32768
  idx = 0
  types = [False] * 17
  while(k > 0):
    #print('k = ' + repr(k))
    if(k <= n):
      #print(n)
      types[idx] = True
      n -= k
      #print(n)
    k /= 2
    idx += 1
  return types
  

def dispEffect(types, effects):
  dispStr = "Type: "
  for i in range(0, 17):
    if(types[i]):
      dispStr += TypeStrings[i] + " "
  
  print(dispStr)  
  for i in range(0, 17):
    effectStr = "Effectiveness " + repr(effects[i]) + " against " + TypeStrings[i]
    print(effectStr)
  
  print('')


'''
for attacker in range(0,17):
  for defender in range(0,17):
    if(Matrix[attacker][defender] != 1.0):
      testStr = TypeStrings[attacker] + ' has effectiveness ' + repr(Matrix[attacker][defender]) + ' against ' + TypeStrings[defender]
      print testStr
'''


#The i th bit tells us if the current type combination has type i
for i in range(0, 32767):
  types = getTypes(i)
  effects = [1.0] * 17
  for j in range(0,17):
    if (types[j]):
      for k in range(0, 17):
        effects[k] *= Matrix[j][k]
    
  dispEffect(types, effects)
