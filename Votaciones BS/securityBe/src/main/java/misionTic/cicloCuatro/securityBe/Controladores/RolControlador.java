package misionTic.cicloCuatro.securityBe.Controladores;

import misionTic.cicloCuatro.securityBe.Modelos.Rol;
import misionTic.cicloCuatro.securityBe.Repositorios.RolRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/roles")
@RestController
@CrossOrigin
public class RolControlador {
    @Autowired
    private RolRepositorio rol_repositorio;

    @GetMapping("")
    public List <Rol> index(){
        return this.rol_repositorio.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Rol create(@RequestBody Rol info_rol){
        return this.rol_repositorio.save(info_rol);
    }

    @GetMapping("{id}")
    public Rol show(@PathVariable String id){
        Rol rol_1 = this.rol_repositorio.findById(id).orElse(null);
        return rol_1;
    }

    @PutMapping("{id}")
    public Rol update(@PathVariable String id, @RequestBody Rol info_rol){
        Rol rol_1 = this.rol_repositorio.findById(id).orElse(null);
        if (rol_1 != null) {
            rol_1.setNombre(info_rol.getNombre());
            return this.rol_repositorio.save(rol_1);
        } else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete (@PathVariable String id) {
        Rol rol_1 = this.rol_repositorio.findById(id).orElse(null);
        if (rol_1 != null){
            this.rol_repositorio.delete(rol_1);
        }
    }
}
