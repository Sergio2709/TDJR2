from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido
class ControladorPartido():

    def __init__(self):
        print("*** Creando Controlador para el partido politico ***")
        self.repositorioPartido = RepositorioPartido()

        # Listado partidos politicos
    def index(self):
        print("La lista de los partidos politicos se completo con éxito")
        return self.repositorioPartido.findAll()

        # Creacion de un partido politico
    def create(self, infoPartido):
        print("El partido politico fue creado con éxito!")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

        # Borrar un partido politico
    def delete(self, id):
        print("Borrando el partido politico con id:  ", id)
        return self.repositorioPartido.delete(id)

        # actualizacion de un partido politico
    def update(self, id, infoPartido):
        print("El partido con id: ", id, " fue actualizado con éxito")
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

        # consulta de un aprtido politico 
    def show(self, id):
        print("Consultando... Partido politico: ", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__