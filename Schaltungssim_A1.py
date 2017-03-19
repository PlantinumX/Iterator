from  math import exp,pow



def main():
    I_s = 14.11 * pow(10,-9)
    U_d = 0.85
    U_t = 0.026 * 1.984
    I_1 = 10 * pow(10,-3)
    i = 0
    while (i < 20):
        print("Iteration ","  " + str(i+1))
        I_d = I_D(I_s, U_d, U_t)
        print("Current I_d "+str(I_d))
        Geq = GEQ(I_s, U_t, U_d)
        print("Resistance Geq " + str(Geq))
        I_eq = IEQ(I_d, Geq, U_d)
        print("Current I_eq " + str(I_eq))
        R = Resistance(Geq)
        U_dold = U_d
        U_d = (I_1 - I_eq) / Geq
        print("New U_d " + str(U_d))
        if(U_dold - U_d <= 0):
            print(str(U_d),str(U_dold))
        i = i + 1

def IEQ(I_d,Geq,U_d):
    return I_d-Geq*U_d
def Resistance(GEQ):
    return 1/GEQ

def GEQ(I_s,U_t,U_d):
    return (I_s/U_t) * exp(U_d/U_t)



def I_D(I_s,U_d,U_t):
    I_d = I_s * (exp(U_d/U_t)-1)
    return I_d

main()