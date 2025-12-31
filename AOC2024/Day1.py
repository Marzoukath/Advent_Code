import sys
sys.stdin = open("data.in", "r")
liste1=[]
liste2=[]
distance = 0
for line in sys.stdin:
    a,b = map (int, line.split())
    liste1.append(a)
    liste2.append(b)
    
liste1.sort()
liste2.sort()

for i in range (len(liste1)):
    distance += abs(liste1[i]-liste2[i])
print(distance) 
