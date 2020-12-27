import math

def inverse_kinematics(x, y, z):
    # x, y, and z in cm
    a = 10
    l = 15
    h = 20
    d = 3
    x = float(x)
    y = float(y)
    z = float(z)
    E1 = 2*(a-d)*l-2*l*x
    F1 = -2*l*z
    G1 = z**2+y**2+x**2+2*(d-a)*x+l**2+(d**2-2*a*d+a**2-h**2)
    t1_1 = (-F1+math.sqrt(E1**2+F1**2-G1**2))/(G1-E1)
    t1_2 = (-F1-math.sqrt(E1**2+F1**2-G1**2))/(G1-E1)
    th1_1 = (180/math.pi)*2*math.atan(t1_1)
    th1_2 = (180/math.pi)*2*math.atan(t1_2)

    E2 = l*x+2*l*(a-d)-l*y*math.sqrt(3)
    F2 = -2*l*z
    G2 = (d-a)*y*math.sqrt(3)+z**2+y**2+x**2+(a-d)*x+l**2+d**2-2*a*d+a**2-h**2
    t2_1 = (-F2+math.sqrt(E2**2+F2**2-G2**2))/(G2-E2)
    t2_2 = (-F2-math.sqrt(E2**2+F2**2-G2**2))/(G2-E2)
    th2_1 = (180/math.pi)*2*math.atan(t2_1)
    th2_2 = (180/math.pi)*2*math.atan(t2_2)

    E3 = l*y*math.sqrt(3)+l*x+2*(a-d)*l
    F3 = -2*l*z
    G3 = (a-d)*y*math.sqrt(3)+z**2+y**2+x**2+(a-d)*x+l**2+d**2-2*a*d+a**2-h**2
    t3_1 = (-F3+math.sqrt(E3**2+F3**2-G3**2))/(G3-E3)
    t3_2 = (-F3-math.sqrt(E3**2+F3**2-G3**2))/(G3-E3)
    th3_1 = (180/math.pi)*2*math.atan(t3_1)
    th3_2 = (180/math.pi)*2*math.atan(t3_2)

    if th1_1 > -120 and th1_1 < 150 and th2_1 > -120 and th2_1 < 150 and th3_1 > -120 and th3_1 < 150:
        if abs(th1_1)<abs(th1_2) and abs(th2_1)<abs(th2_2) and abs(th3_1)<abs(th3_2):
            th1 = th1_1
            th2 = th2_1
            th3 = th3_1
            return [th1, th2, th3]
        elif abs(th1_1)>abs(th1_2) and abs(th2_1)>abs(th2_2) and abs(th3_1)>abs(th3_2):
            th1 = th1_2
            th2 = th2_2
            th3 = th3_2
            return [th1, th2, th3]
    elif th1_2 > -120 and th1_2 < 150 and th2_2 > -120 and th2_2 < 150 and th3_2 > -120 and th3_2 < 150:
        if abs(th1_1)<abs(th1_2) and abs(th2_1)<abs(th2_2) and abs(th3_1)<abs(th3_2):
            th1 = th1_1
            th2 = th2_1
            th3 = th3_1
            return [th1, th2, th3]
        elif abs(th1_1)>abs(th1_2) and abs(th2_1)>abs(th2_2) and abs(th3_1)>abs(th3_2):
            th1 = th1_2
            th2 = th2_2
            th3 = th3_2
            return [th1, th2, th3]
