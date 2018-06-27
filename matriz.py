class matriz:
    def __init__(self, m ):
        self.m = m

    def list(self):
        return list(self.m)

    def __add__(self, m2):
        aux = [[0 for i in range(len(m2.m[0]))] for i in range(len(self.m))]
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                aux[i][j] = self.m[i][j] + m2.m[i][j]

        return aux

    def transposeMatrix(self):
        matriz = self.list()
        aux = []
        for j in range(len(matriz[0])):
            linha = []
            for i in range(len(matriz)):
                linha.append(matriz[i][j])
            aux.append(linha)
        return aux

    def __mul__(self, m2):
        matrizA = self.list()
        matrizB = m2.list()
        """Multiplica duas matrizes."""
        sizeLA = len(matrizA)
        sizeCA = len(matrizA[0])  # deve ser igual a sizeLB para ser possível multiplicar as matrizes
        sizeCB = len(matrizB[0])
        matrizR = []
        # Multiplica
        for i in range(sizeLA):
            matrizR.append([])
            for j in range(sizeCB):
                val = 0
                for k in range(sizeCA):
                    val += matrizA[i][k] * matrizB[k][j]
                matrizR[i].append(val)
        return matrizR



    def __str__(self):
        return str(self.m)

