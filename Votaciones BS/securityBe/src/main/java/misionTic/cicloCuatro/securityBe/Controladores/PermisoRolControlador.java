package misionTic.cicloCuatro.securityBe.Controladores;

import misionTic.cicloCuatro.securityBe.Modelos.Permiso;
import misionTic.cicloCuatro.securityBe.Modelos.PermisoRol;
import misionTic.cicloCuatro.securityBe.Modelos.Rol;
import misionTic.cicloCuatro.securityBe.Repositorios.PermisoRepositorio;
import misionTic.cicloCuatro.securityBe.Repositorios.PermisoRolRepositorio;
import misionTic.cicloCuatro.securityBe.Repositorios.RolRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisoRol")
public class PermisoRolControlador {
    @Autowired
    private PermisoRolRepositorio repositorioPermisoRol;
    @Autowired
    private PermisoRepositorio repositorioPermiso;
    @Autowired
    private RolRepositorio repositorioRol;


    @GetMapping("")
    public List<PermisoRol>index(){
        return this.repositorioPermisoRol.findAll();
    }

    @GetMapping("{id}")
    public PermisoRol show(@PathVariable String id ) {
        PermisoRol PRActual = this.repositorioPermisoRol.findById(id).orElse(null);
        return PRActual;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisoRol PRActual = this.repositorioPermisoRol.findById(id).orElse(null);
        if(PRActual != null){
            this.repositorioPermisoRol.delete(PRActual);
        }
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisoRol create(@PathVariable String id_rol, @PathVariable String id_permiso) {
        PermisoRol pr = new PermisoRol();
        Permiso p = this.repositorioPermiso.findById(id_permiso).get();
        Rol r = this.repositorioRol.findById(id_rol).get();
        if(p != null && r != null) {
            pr.setPermiso(p);
            pr.setRol(r);
            return this.repositorioPermisoRol.save(pr);
        } else {
            return null;
        }
    }

    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisoRol update(@PathVariable String id,
                             @PathVariable String id_rol,
                             @PathVariable String id_permiso) {
        Rol r = this.repositorioRol.findById(id_rol).get();
        Permiso p = this.repositorioPermiso.findById(id_permiso).get();
        PermisoRol pr = this.repositorioPermisoRol.findById(id).orElse(null);
        if(r != null && p != null && pr != null) {
            pr.setRol(r);
            pr.setPermiso(p);
            return this.repositorioPermisoRol.save(pr);
        }else {
            return null;
        }
    }

    @GetMapping("/valida-permiso/rol/{id_rol}")
    public PermisoRol getPermiso(@PathVariable String id_rol,
                                 @RequestBody Permiso dataPermiso){
        Rol r = this.repositorioRol.findById(id_rol);
        Permiso p = this.PermisoRepositorio.getPermiso(dataPermiso.getUrl(),dataPermiso.getMetodo());
        if (r != null && p != null) {
            return this.PermisoRolRepositorio.getPermisoRol(r.getId(), p.getId());
        } else {
            return null;
        }
    }
}
