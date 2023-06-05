let pathArray = window.location.pathname.split('/');
let secondLevelLocation = pathArray[1];
if(secondLevelLocation == ""){
    secondLevelLocation = "dashboard"
}

let linkActivo = document.getElementById(secondLevelLocation)
linkActivo.classList.add('seleccionado')
