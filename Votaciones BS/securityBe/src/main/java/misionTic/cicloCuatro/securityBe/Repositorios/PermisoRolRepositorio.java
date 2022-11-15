package misionTic.cicloCuatro.securityBe.Repositorios;

import misionTic.cicloCuatro.securityBe.Modelos.PermisoRol;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface PermisoRolRepositorio extends MongoRepository <PermisoRol,String> {
    @Query("{'rol.$id': ObjectId(?0), 'permiso.$id_permiso': ObjectId(?1) }")
    public PermisoRol getPermisoRol(String id_rol, String id_permiso);
}
