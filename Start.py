#!/usr/local/bin/python2.7
    
print "Hello World!\n";


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
