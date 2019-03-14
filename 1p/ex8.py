# Exercice 8

v1 = [0,0]; v2 = [1,0] ; v3 = [0,2];

vertices = [v1, v2, v3]

def area(triangle) :
    triangle1 = 1/2*(v2[0]*v3[1] - v3[0]*v2[1] - v1[0]*v3[1] + v3[0]*v1[1] + v1[0]*v2[1] - v2[0]*v1[1])
    print("Area of triangle is " + str(triangle1))

area(vertices)
    


