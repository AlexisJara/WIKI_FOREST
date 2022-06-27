var nomtema = document.getElementById("tema");
var comen = document.getElementById("Comentario");
const form = document.getElementById("form");
var mensaje = document.getElementById("warnings");



form.addEventListener("submit", e => {


    let mensajesMostrar = "";
    let entrar = false;
    mensaje.innerHTML = "";

    
    if (nomtema.value.length < 5 ||  nomtema.value.length > 50) {
        mensajesMostrar += 'El nombre del tema no tiene el largo necesario/limite. <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(nomtema.value[0])){  
        mensajesMostrar += 'El nombre del tema debe tener una mayuscula al inicio. <br>';
        entrar = true;
    }

    if (comen.value.length < 10 ||  comen.value.length > 250) {
        mensajesMostrar += 'El comentario no tiene el largo necesario/limite. <br>';
        entrar = true;
    }

    if(!/[A-Z]/.test(comen.value[0])){  
        mensajesMostrar += 'El comentario debe tener una mayuscula al inicio. <br>';
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
