import operator
from extra_points import scores
from processing import accuracy_rates

class FindWinners(): 
    """Representa los estudiantes con mayores puntajes."""

    def  __init__(self, scores: dict) -> None:
        """Inicia la clase FindWinners. 
            
        Attributes:
        scores : un diccionario que contiene cada estudiante con su puntaje total
        """
        self.scores = scores

    def get_winners(self, numberOfWinners: int) -> list:
        """Implementa una función que arroja el número de estudiantes con mayor puntaje.

        Attributes:
        numberOfWinners : un entero que indique la cantidad que se quiere saber de personas con mayores puntajes

        Crea el diccionario winners_are, que ordena, por valor, los items del diccionario self.scores,
        de forma descendente. 
        Crea la lista de tuplas required_winners con el número de estudiantes recibido como atributo
        """

        winners_are = dict( sorted(self.scores.items(), key=operator.itemgetter(1),reverse=True))
        required_winners = list(winners_are.items())[:numberOfWinners]
        return(required_winners)

class FindStudentsByAccuracyRate(): 
    """Representa los estudiantes con mayores porcentajes de acierto.
    
    Attributes:
        accuracy_rates : un diccionario que contiene cada estudiante con su porcentaje de aciertos
    """

    def  __init__(self, accuracy_rates: dict) -> None:
        """Inicia la clase FindStudentsByAccuracyRate. 
            
        Attributes:
        accuracy_rates : un diccionario que contiene cada estudiante con su porcentaje de aciertos
        """
        self.accuracy_rates = accuracy_rates

    def get_most_accurate(self, accuracy: int) -> list:
        """Implementa una función que arroja el grupo de estudiantes cuyo porcentaje de éxitos es igual
        o mayor al especificado como atributo.

        Attributes:
        accuracy: un entero que indique el porcentaje que deben cumplir los estudiantes a mostrar
        """
        most_accurate_are = []
        for key, value in self.accuracy_rates.items():
            if value / 4 >= accuracy:
                most_accurate_are.append((key, int(value/4)))
        return most_accurate_are

winners = FindWinners(scores).get_winners(2)
#print(winners)
most_accurate = FindStudentsByAccuracyRate(accuracy_rates).get_most_accurate(70)
#print(most_accurate)

