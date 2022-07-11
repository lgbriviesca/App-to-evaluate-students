from processing import scores

class ExtraPoints(): 
    """Representa los estudiantes con puntaje extra."""

    def  __init__(self, scores: dict) -> None:
        """Inicia la clase ExtraPoints. 
        
        Attributes:
        scores: un diccionario en que se actualizarán los puntos extras
        """
        self.scores = scores

    def find_students_and_summ_points(self, name: str, last_name: str, extra_score: int,):
        """Implementa una búsqueda de las personas con puntaje extra y actualiza el puntaje con el nuevo puntaje.

        Attributes:
        name : un string con el primer nombre
        last_name : un string con el apellido
        extra_score : un entero con el puntaje extra

        Busca las coincidencias en las keys del diccionario, del nombre recibido.
        Obtiene el puntaje del estudiante encontrado.
        Actualiza el valor (score) del estudiante sumando los puntos extras más el puntaje anterior. 
        """
        name = f"{name} {last_name}"
        student = [k for k in self.scores if name in k]
        student_score= self.scores.get(student[0])
        updated_scores = self.scores.update({student[0]: student_score + extra_score})
        return self.scores

first_student_with_extra_points = ExtraPoints(scores).find_students_and_summ_points("kevin", "salvador", 8000)
second_student_with_extra_points = ExtraPoints(scores).find_students_and_summ_points("diego", "angeles", 2000)

#print(scores)