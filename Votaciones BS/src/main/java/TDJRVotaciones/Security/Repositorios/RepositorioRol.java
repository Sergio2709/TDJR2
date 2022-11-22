package TDJRVotaciones.Security.Repositorios;

import TDJRVotaciones.Security.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}
