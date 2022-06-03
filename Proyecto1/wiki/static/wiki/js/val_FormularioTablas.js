var nombreEnemigo = document.getElementById("validationCustom01");
var nomdato = document.getElementById("tipodato");
var categoriaa = document.getElementById("categoria")
const form = document.getElementById("form");
var mensaje = document.getElementById("warnings");



form.addEventListener("submit", e => {
    e.preventDefault();
    let mensajesMostrar = "";
    let entrar = false;
    mensaje.innerHTML = "";

    if(categoriaa = 'mal'){
        mensajesMostrar += 'Seleccione una opcion valida <br>';
        entrar = true;
    }

    if (nombreEnemigo.value.length < 4 ) {
        mensajesMostrar += 'El nombre del dato no tiene el largo necesario <br>';
        entrar = true;
    }
    if(!/[A-Z]/.test(nombreEnemigo.value[0])){  
        mensajesMostrar += 'El nombre del Enemigo/Flora/Arma debe tener al menos una mayuscula <br>';
        entrar = true;
    }
    
    if (nomdato.value.length < 4 ) {
        mensajesMostrar += 'El tipo de dato no tiene el largo necesario <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(nomdato.value[0])){  
        mensajesMostrar += 'El tipo de dato debe tener al menos una mayuscula <br>';
        entrar = true;
    }
   

    if (entrar) {
        mensaje.innerHTML = mensajesMostrar;
        e.preventDefault();
    } else {
        mensaje.innerHTML = "Enviado";
    }
});

function esMayuscula(letra) {
    return letra === letra.toUpperCase();
}

