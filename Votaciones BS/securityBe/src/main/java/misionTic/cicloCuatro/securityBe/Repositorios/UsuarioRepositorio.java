package misionTic.cicloCuatro.securityBe.Repositorios;

import misionTic.cicloCuatro.securityBe.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface UsuarioRepositorio  extends MongoRepository <Usuario,String> {

    @Query("{'correo':'?0}")
    public Usuario getUsuarioPorCorreo(String correo);
}
