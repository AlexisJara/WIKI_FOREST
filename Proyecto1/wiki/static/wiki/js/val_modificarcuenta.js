var nombre = document.getElementById("nombre");
var clave = document.getElementById("Clave1");
var apellido = document.getElementById("apellido");
const form = document.getElementById("form2");
var mensaje = document.getElementById("warnings");

form.addEventListener("submit", e => {
    
    let mensajesMostrar = "";
    let entrar = false;
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    let rut = /^[0-9]+[-|‐]{1}[0-9kK]{1}$/
    mensaje.innerHTML = "";

    if (nombre.value.length < 4 || nombre.value.length > 12) {
        mensajesMostrar += 'El nombre no tiene el largo necesario <br>';
        entrar = true;
    }
    if(!/[A-Z]/.test(nombre.value[0])){  
        mensajesMostrar += 'El nombre debe tener al menos una mayuscula <br>';
        entrar = true;
    }
    
    if (apellido.value.length < 4 || apellido.value.length > 12) {
        mensajesMostrar += 'El apellido no tiene el largo necesario <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(apellido.value[0])){  
        mensajesMostrar += 'El apellido debe tener al menos una mayuscula <br>';
        entrar = true;
    }
    if (nomusuario.value.length < 4 || nomusuario.value.length > 12) {
            mensajesMostrar += 'El nombre de usuario no tiene el largo necesario <br>';
            entrar = true;
        }


    if (!regexEmail.test(correo.value)) {
        mensajesMostrar += 'El email no es valido <br>'
        entrar = true
    }

    if(!/[A-Z]/.test(clave.value)||!/[0-9]/.test(clave.value)){
        mensajesMostrar+="La clave debe tener una mayuscula y al menos un numero <br>"
        entrar = true;
    }
    
    if (nombre.value == "Hola") {
        mensajesMostrar += 'xxx <br>';
        entrar = true;
    }
    
    if(clave.value.length < 4|| clave.value.length > 20){
        mensajesMostrar += 'La clave no tiene el largo requerido <br>';
        entrar = true;
    }

    if(Clave1.value != Clave2.value){
        mensajesMostrar += 'Las claves no coinciden';
        entrar = true; 

    }

    if (entrar) {
        mensaje.innerHTML = mensajesMostrar;
        e.preventDefault();
    } else {
        mensaje.innerHTML = "";
    }
});

function esMayuscula(letra) {
    return letra === letra.toUpperCase();
}
