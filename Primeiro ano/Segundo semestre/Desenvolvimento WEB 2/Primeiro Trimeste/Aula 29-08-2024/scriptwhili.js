let contador = 1;
while (contador <= 5) {
    console.log("Numero" + contador);
    contador++;
    
}

let resposta = "sim";
while (resposta == "sim"){
    console.log("Ola! Quer ser cumprimentado novamente?");
    resposta = prompt("Digite a resposta: ");
}

let base = 2;
expoente = 0;
while (expoente = 0){
    console.log(` ${base} elevado a ${expoente} é:` , Math.pow(base, expoente));
    expoente++
     
}

let frutas = ["maça", "banana", "manga"];
let indice = 0;
while (indice < frutas.length){
    console.log("Eu gosto de " + frutas[indice])
    indice++
}

let msg = " ";
let j = 0;
do {
    msg += j + "\n";
    j++
}while(j <=10);
console.log(msg);

const Carro = {
    marca: "Renault",
    modelo: "logan",
    comprimento: "4.250mm",
    largura: "1.735mm",
    altura: "1.525mm"
};

let msg2 = " ", k;
for (k in Carro){
    msg2 += k + ": " + Carro[k] + "\n";
}
console.log(msg2);