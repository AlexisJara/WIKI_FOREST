var nomdato = document.getElementById("nombreDato");
var tidato = document.getElementById("tipodato");
var descri = document.getElementById("descripcion");
var categoriaa = document.getElementById("categoria")
const form = document.getElementById("form");
var mensaje = document.getElementById("warnings");



form.addEventListener("submit", e => {


    let mensajesMostrar = "";
    let entrar = false;
    mensaje.innerHTML = "";

    if(categoriaa.value == 0){
        mensajesMostrar += 'Seleccione una opcion valida en categoria. <br>';
        entrar = true;
    }

    if (nomdato.value.length < 4 ) {
        mensajesMostrar += 'El nombre del dato no tiene el largo necesario. <br>';
        entrar = true;
    }
    if(!/[A-Z]/.test(nomdato.value[0])){  
        mensajesMostrar += 'El nombre del Enemigo/Flora/Arma/Logros/Animales debe tener una mayuscula al inicio. <br>';
        entrar = true;
    }
    
    if (tidato.value.length < 4 ) {
        mensajesMostrar += 'El tipo de dato no tiene el largo necesario. <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(tidato.value[0])){  
        mensajesMostrar += 'El tipo de dato debe tener una mayuscula al inicio. <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(descri.value[0])){  
        mensajesMostrar += 'La descripcion de tener una mayuscula al inicio. <br>';
        entrar = true;
    }

    if (descri.value.length < 20 ||  descri.value.length > 250) {
        mensajesMostrar += 'La descripcion del dato no tiene el largo necesario/limite. <br>';
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

