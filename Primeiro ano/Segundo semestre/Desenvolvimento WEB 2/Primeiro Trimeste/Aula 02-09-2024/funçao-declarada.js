var cor_default = '#444';
var cor_um = "orange";
var cor_dois = "moccasin";
var btnPadrao = document.querySelectorAll(".cor") [0];
var btnUm = document.querySelectorAll(".cor") [1];
var btnDois = document.querySelectorAll(".cor")[2];

btnPadrao.addEventListener('click', corPadrao);
btnUm.addEventListener('click', corUm);
btnDois.addEventListener('click', corDois);

function corPadrao(){
    document.body.style.backgroundColor = cor_default
}

function corUm(){
    document.body.style.backgroundColor = cor_um
}

function corDois(){
    document.body.style.backgroundColor = cor_dois
}