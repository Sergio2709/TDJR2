package misionTic.cicloCuatro.securityBe.Controladores;


import misionTic.cicloCuatro.securityBe.Modelos.Permiso;
import misionTic.cicloCuatro.securityBe.Repositorios.PermisoRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class PermisoControlador {
    @Autowired
    private PermisoRepositorio permiso_repositorio;

    @GetMapping("")
    public List <Permiso> index(){
        return this.permiso_repositorio.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Permiso created(@RequestBody Permiso info_permiso){
        return this.permiso_repositorio.save(info_permiso);
    }

    @GetMapping("{id}")
    public Permiso show(@PathVariable String id){
        Permiso permiso_1 = this.permiso_repositorio.findById(id).orElse(null);
        return permiso_1;
    }

    @PutMapping("{id}")
    public Permiso update (@PathVariable String id, @RequestBody Permiso info_permiso) {
        Permiso permiso_1 = this.permiso_repositorio.findById(id).orElse(null);
        if (permiso_1 != null){
            permiso_1.setMetodo(info_permiso.getMetodo());
            permiso_1.setUrl(info_permiso.getUrl());
            return this.permiso_repositorio.save(permiso_1);
        }else {
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete (@PathVariable String id) {
        Permiso permiso_1 = this.permiso_repositorio.findById(id).orElse(null);
        if (permiso_1 != null) {
            this.permiso_repositorio.delete(permiso_1);
        }
    }



}
