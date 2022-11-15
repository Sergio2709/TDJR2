from Repositorios.RepositorioResultados import RepositorioResultados
from Modelos.Resultados import Resultados
class ControladorResultados():

    def __init__(self):
        print("*** Creando Controlador para los resultados de las votaciones ***")
        self.repositorioResultados = RepositorioResultados()

        # Listado resultados
    def index(self):
        print("La lista de los resultados de las votaciones se completo con éxito")
        return self.repositorioResultados.findAll()

        # Creacion de un resultado
    def create(self, infoResultados):
        print("Los resultados de las votaciones fueron creados con éxito!")
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

        # Borrar un resultado
    def delete(self, id):
        print("Borrando los resultados con id:  ", id)
        return self.repositorioResultados.delete(id)

        # actualizacion de los resultados
    def update(self, id, infoResultados):
        print("los resultados con id: ", id, " fueron actualizados con éxito")
        ResultadoActual = Resultados(self.repositorioResultados.findById(id))
        ResultadoActual.numero = infoResultados["numero"]
        ResultadoActual.idPartido = infoResultados["idPartido"]
        return self.repositorioResultados.save(ResultadoActual)

        # consulta de resultados
    def show(self, id):
        print("Consultando... Resultados de las votaciones: ", id)
        losResultados = Resultados(self.repositorioResultados.findById(id))
        return losResultados.__dict__