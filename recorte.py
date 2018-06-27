from ponto import *
from bresenham import *

def sign(n):
    if n>=0:
        return '0'
    return '1'

def mkcode(p,xmin,xmax,ymin,ymax):
    code = ''
    code += sign(ymax - p.y)
    code += sign(p.y - ymin)
    code += sign(xmax - p.x)
    code += sign(p.x - xmin)
    return code

def test(code, code1, type):
    list = ''
    if type == 'or':
        for i in range(len(code)):
            list+= str(int(code[i]) or int(code1[i]))
        return list
    elif type == 'and':
        for i in range(len(code)):
            list+= str(int(code[i]) and int(code1[i]))
        return list

def findDifBit(code):
    j=0
    for i in code:
        j +=1
        if i == '1':
            return j


#def intersect_lines(find_Window_Line(difBit), (p1,p2)):

def find_Window_Line(difBit, p1, p2, xmin,xmax,ymin,ymax):

    if(difBit == 1):
        # ponto está acima do ymax
        x = p1.get_x() + (p2.get_x() - p1.get_x()) * (ymax - p1.get_y()) / (p2.get_y() - p1.get_y())
        y = ymax

    elif(difBit == 2):
        # ponto está acima do ymin
        x = p1.get_x() + (p2.get_x() - p1.get_x()) * (ymin - p1.get_y()) / (p2.get_y() - p1.get_y())
        y = ymin

    elif(difBit == 3):
        # ponto está acima do xmax
        y = p1.get_y() + (p2.get_y() - p1.get_y()) * (xmax - p1.get_x()) / (p2.get_x() - p1.get_x())
        x = xmax

    elif(difBit == 4):
        # ponto está acima do xmin
        y = p1.get_y() + (p2.get_y() - p1.get_y()) * (xmin - p1.get_x()) / (p2.get_x() - p1.get_x())
        x = xmin

    return Point(x,y)

def outside(c, difBit):
    i = difBit-1
    if c[i] == '1':
        return True
    return False


def CS_Clip(p1,p2,xmin,xmax,ymin,ymax):
    c1 = mkcode(p1,xmin,xmax,ymin,ymax) #gera o código binário para o p1
    c2 = mkcode(p2,xmin,xmax,ymin,ymax) #gera o código binário para o p2

    if test(c1,c2,'or')  == '0000':
        drawLine(p1,p2)#totalmente dentro
        return [p1,p2]

    else:

        if test(c1,c2,'and')  != '0000': #totalmente fora
            return []
        else:
            difBit = findDifBit(test(c1,c2,'or'))
            #encontra 1º bit com valor 1
            #calcula a intersecção i entre a reta e a borda do monitor
            #(referente ao bit encontrado anteriormente)

            i = find_Window_Line(difBit, p1,p2, xmin,xmax,ymin,ymax)
            #Usa o ponto que tem 0 nesse bit e a intersecção i recursivamente

            if outside(c1, difBit):
                CS_Clip(i, p2, xmin, xmax, ymin, ymax)
            else:
                CS_Clip(p1, i, xmin, xmax, ymin, ymax)

