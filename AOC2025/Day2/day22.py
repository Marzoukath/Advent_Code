# fonction pour tester si un nombre est invalide
def est_invalide(n):
    s = str(n)
    l = len(s)
    for p in range(1, l // 2 + 1): # retrouver les diviseurs de la longueur
        if l % p != 0:
            continue
        motif = s[:p]
        repeter = motif  * (l // p)     
        if repeter == s:
            return True
    return False

var = "990244-1009337,5518069-5608946,34273134-34397466,3636295061-3636388848,8613701-8663602,573252-688417,472288-533253,960590-988421,7373678538-7373794411,178-266,63577667-63679502,70-132,487-1146,666631751-666711926,5896-10827,30288-52204,21847924-21889141,69684057-69706531,97142181-97271487,538561-555085,286637-467444,93452333-93519874,69247-119122,8955190262-8955353747,883317-948391,8282803943-8282844514,214125-236989,2518-4693,586540593-586645823,137643-211684,33-47,16210-28409,748488-837584,1381-2281,1-19"

tab = []
for pair in var.split(","):
    a, b = map(int, pair.split("-"))
    tab.append((a, b))


resultat = 0
for j in tab:
    x = j[0]
    y = j[1]
    t = []
    for i in range(x, y + 1):
        if est_invalide(i):
            t.append(i)
    resultat += sum(t)
print(resultat)


 
