import math

ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)

theta = math.acos(bc/ac)

print( int( math.degrees(theta) ), '°', sep='' )
