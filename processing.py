from imports import files

class ProcessData:
    """Representa el puntaje y porcentaje totales del grupo."""

    def  __init__(self, files:list, ) -> list:
        """Inicia la clase ProcessData. 
        
        Attributes:
        files : Una tupla de listas
        """
        self.files = files

    def process_score_dicts(self) -> dict:
        """Procesa la tupla y retorna un diccionario cuyo key es el nombre y el valor, puntaje.

        Creará la variable total_scores, que será un diccionario vacío.
        Iterará la tupla y para cada lista que itere, buscará cada elemento por el key "Name" y lo almacenará
        en la variable old_score, si no existe, tomará su valor como default.
        La variable total_scores recibirá los valores de la variable old_score más los que haya en la key "Score"
        de cada una de las listas (los quizes).
        A partir de ello, creará el diccionario en la variable total_scores.
        """
        total_scores = {}
        quiz_dicts = self.files
        for quiz_dict in quiz_dicts:
            for quiz in quiz_dict:
                old_score = total_scores.get(quiz["Name"].strip(), 0)
                total_scores[quiz["Name"].strip()] = old_score + quiz["Score"]
        total_scores = dict(total_scores)
        return total_scores

    def process_percentage_dicts(self) -> dict:
        """Procesa la tupla y retorna un diccionario cuyo key es el nombre y el valor, porcentaje de acierto.

        Creará la variable total_percentage, que será un diccionario vacío.
        Iterará la tupla y para cada lista que itere, buscará cada elemento por el key "Name" y lo almacenará
        en la variable old_porcentage, si no existe, tomará su valor como default.
        La variable total_percentage recibirá los valores de la variable old_porcentage más los que haya en la key "Accuracy"
        de cada una de las listas (los quizes).
        A partir de ello, creará el diccionario en la variable total_percentage.
        """
        total_percentage = {}
        quiz_dicts = self.files
        for quiz_dict in quiz_dicts:
            for quiz in quiz_dict:
                old_porcentage = total_percentage.get(quiz["Name"].strip(), 0)
                total_percentage[quiz["Name"].strip()] = old_porcentage + quiz["Accuracy"]
        total_percentage = dict(total_percentage)
        return total_percentage

scores = ProcessData(files).process_score_dicts()
accuracy_rates = ProcessData(files).process_percentage_dicts()

#print(scores)
#print(accuracy_rates)