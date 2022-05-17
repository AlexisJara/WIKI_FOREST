var url = "https://apis.digital.gob.cl/dpa/comunas";
fetch(url).then(function(result){
  if(result.ok){
    return result.json();
  }

}).then(function(data){
  data.forEach(function(element){
    let regiones = document.getElementById("countries");
    let opt = document.createElement("option");
    opt.appendChild(document.createTextNode(element.nombre));
    opt.value=element.codigo;

    regiones.appendChild(opt);

  })
})