from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():

    def __init__(self):
        print("*** Creando Controlador para la mesa ***")
        self.repositorioMesa = RepositorioMesa()

        # Listado
    def index(self):
        print("La lista de las mesas se completo con éxito")
        return self.repositorioMesa.findAll()

        # Creacion de una mesa
    def create(self, infoMesa):
        print("La mesa fue creada con éxito!")
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

        # Borrar una mesa
    def delete(self, id):
        print("Borrando la mesa con id:  ", id)
        return self.repositorioMesa.delete(id)

        # actualizacion de una mesa
    def update(self, id, infoMesa):
        print("La mesa con id: ", id, " fue actualizada con éxito")
        MesaActual = Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero = infoMesa["numero"]
        MesaActual.cantidad = infoMesa["cantidad"]
        return self.repositorioMesa.save(MesaActual)

        # consulta
    def show(self, id):
        print("Consultando... Mesa: ", id)
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__