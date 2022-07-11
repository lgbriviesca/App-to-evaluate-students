from winners import winners, most_accurate

class Showresults():
    """Arroja los resultados: los dos estudiantes más altos y los estudiantes cuyo porcentaje
    de aciertos fue igual o mayor a 70%. Este código no es dinámico; los valores de porcentaje 
    y el número de estudiantes ganadores puede cambiarse (es dinámico) en el módulo winners.py"""

    def  __init__(self, winners: list = winners, most_accurate: list = most_accurate) -> None:
        """Inicia la clase FindWinners. 
            
        Attributes:
        winners : una lista por defecto que contiene cada estudiante con su puntaje total
        most_accurate : una lista por defecto que contiene cada estudiante con su porcentaje de aciertos total
        """

    def get_final_results(self) -> list:
        """Implementa una función que arroja, de manera redactada, los dos estudiantes con mayor puntaje 
        y porcentaje de aciertos.

        Attributes:
        ninguno

        Un bucle separa la tupla y la une en forma de cadena de texto, en una lista vacía.
        Retorna una cadena de texto con los datos finales solicitados.
        """
        fin_list = []
        for num in most_accurate:
            fin_list.append(f"{num[0]}, con {num[1]}%")
        print("Los dos estudiantes con mayor puntaje fueron: "
        f"{winners[0][0]}, con {winners[0][1]} puntos y {winners[1][0]}, con {winners[1][1]} "
        f"y aquellos con más del 70% de éxito fueron: {fin_list}")
        
winners = Showresults().get_final_results()
#print(winners)