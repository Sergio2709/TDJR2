from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("*** Creando Controlador para el Candidato ***")
        self.repositorioCandidato=RepositorioCandidato()

    # Listado
    def index(self):
        print("La lista de candidatos se completo con éxito")
        return  self.repositorioCandidato.findAll()

    # Creacion de candidato
    def create(self, infoCandidato):
        print("Candidato creado con éxito!")
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)


    # Borrar un candidato
    def delete(self, id):
        print("Borrando el candidato con id:  ", id)
        return self.repositorioCandidato.delete(id)

    # actualizacion
    def update(self, id, infoCandidato):
        print("El candidato con id: ", id ," fue actualizado con éxito")
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula=infoCandidato["cedula"]
        candidatoActual.numero = infoCandidato["numero"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    # consulta
    def show(self, id):
        print("Consultando... Candidato: ", id)
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
