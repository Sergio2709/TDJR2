package misionTic.cicloCuatro.securityBe.Repositorios;

import misionTic.cicloCuatro.securityBe.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RolRepositorio extends MongoRepository<Rol,String> {
}
