class calculator:
    """this class is a toolbox of operation for vector"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """this function print the dot product of two vector"""
        dotProd = sum([V1[i] * V2[i] for i in range(len(V1))])
        print(f"Dot product is: {dotProd}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """this function print the sum of two vector"""
        sumVec = [float(V1[i]) + float(V2[i]) for i in range(len(V1))]
        print(f"Add Vector is : {sumVec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """this function print the difference of two vector"""
        diffVec = [float(V1[i]) - float(V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {diffVec}")
