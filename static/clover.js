function createNode(type, child) {
    let node = document.createElement(type)

    if(typeof child === 'string') {
        let text = document.createTextNode(child)
        node.appendChild(text)
    } else {
        node.appendChild(child)
    }

    return node;
}

let titulo = createNode('h2', 'Clover Project Charter')
// let contenido1 = createNode('p', 'Justificacion')
document.getElementById('charter').appendChild(titulo)
// document.getElementById('charter').appendChild(contenido1)

//Creando boton1
let boton1 = createNode('button','¿Cómo consultar mis tareas?')
document.getElementById('charter').appendChild(boton1)
boton1.setAttribute('class', 'desplegable')
boton1.setAttribute('id','b1')
//creando contenido del boton
let cb1 = createNode('div', createNode('p', 'text text text'))
document.getElementById('charter').appendChild(cb1)
cb1.setAttribute('class','content')


//Creando boton2
let boton2 = createNode('button','¿Cómo subir mi tarea?')
document.getElementById('charter').appendChild(boton2)
boton2.setAttribute('class', 'desplegable')
boton2.setAttribute('id','b2')
//creando contenido del boton 2
let cb2 = createNode('div', createNode('p', 'text text text'))
document.getElementById('charter').appendChild(cb2)
cb2.setAttribute('class','content')


//Creando boton3
let boton3 = createNode('button','Datos de contacto del maestro')
document.getElementById('charter').appendChild(boton3)
boton3.setAttribute('class', 'desplegable')
boton3.setAttribute('id','b3')
//creando contenido del boton 3
let cb3 = createNode('div', createNode('p', 'text text text'))
document.getElementById('charter').appendChild(cb3)
cb3.setAttribute('class','content')

//Listener
let borde1 = document.getElementById('b1')
let borde2 = document.getElementById('b2')
let borde3 = document.getElementById('b3')

borde1.addEventListener('click', () => borde1.style = 'border-radius: 10px 10px 0 0')
// borde1.removeEventListener('click', () => borde1.style = '')
borde2.addEventListener('click', () => borde2.style = 'border-radius: 10px 10px 0 0')
borde3.addEventListener('click', () => borde3.style = 'border-radius: 10px 10px 0 0')




//Collapsible

var coll = document.getElementsByClassName("desplegable");
var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight){
            content.style.maxHeight = null;
            } else {
            content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }

//Background event
window.addEventListener('mousemove',(event) => {
    document.body.style.background = 'linear-gradient(to bottom left,#2B463C, #607213)'
})

