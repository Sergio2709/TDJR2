package misionTic.cicloCuatro.securityBe.Controladores;

import misionTic.cicloCuatro.securityBe.Modelos.Permiso;
import misionTic.cicloCuatro.securityBe.Modelos.PermisoRol;
import misionTic.cicloCuatro.securityBe.Modelos.Rol;
import misionTic.cicloCuatro.securityBe.Modelos.Usuario;
import misionTic.cicloCuatro.securityBe.Repositorios.RolRepositorio;
import misionTic.cicloCuatro.securityBe.Repositorios.UsuarioRepositorio;
import misionTic.cicloCuatro.securityBe.Repositorios.PermisoRepositorio;
import misionTic.cicloCuatro.securityBe.Repositorios.PermisoRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;
import java.util.Optional;


@CrossOrigin
@RestController
@RequestMapping("/usuarios")

public class UsuarioControlador {
    @Autowired
    private UsuarioRepositorio repositorio;
    @Autowired
    private RolRepositorio repositorioRol;

    @GetMapping("")
    public List<Usuario> index() {
        return this.repositorio.findAll();
    }

    @PostMapping
    public Usuario create(@RequestBody Usuario dataUsuario) {
        dataUsuario.setClave(convertirSHA256(dataUsuario.getClave()));
        return this.repositorio.save(dataUsuario);
    }

    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario dataUsuario) {
        Usuario usuario = this.repositorio.findById(id).orElse(null);
        if (usuario != null) {
            usuario.setSeudonimo(dataUsuario.getSeudonimo());
            usuario.setCorreo(dataUsuario.getCorreo());
            usuario.setClave(convertirSHA256(dataUsuario.getClave()));
            return this.repositorio.save(usuario);
        } else {
            return null;
        }

    }

    @GetMapping("{id}")
    public Usuario show(@PathVariable String id) {
        Usuario us = this.repositorio.findById(id).orElse(null);
        return us;
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)

    @DeleteMapping("{id}")
    public void delete(@PathVariable String id) {
        Usuario us = this.repositorio.findById(id).orElse(null);
        if (us != null) {
            this.repositorio.delete(us);

        }
    }


    private String convertirSHA256(String clave) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException ex) {
            ex.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(clave.getBytes());
        StringBuffer sb = new StringBuffer();
        for (byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    @PostMapping("/validar")
    public Usuario validar(@RequestBody Usuario usuario, final HttpServletResponse rta) throws IOException {
        System.out.print(usuario);
        Usuario usr = this.repositorio.getUsuarioPorCorreo(usuario.getCorreo());
        System.out.print(usr);
        if (usr != null && usr.getClave().equals(convertirSHA256(usuario.getClave()))) {
            usr.setClave("");
            return usr;
        } else {
            rta.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}

