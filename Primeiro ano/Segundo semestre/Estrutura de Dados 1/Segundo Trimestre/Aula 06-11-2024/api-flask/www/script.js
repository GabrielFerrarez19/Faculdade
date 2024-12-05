async function getDados() {
    // Faz a chamada ao endpoint Flask
    const response = await fetch('http://127.0.0.1:5000/soma');

    // Verificar se a resposta foi bem sucedida
    if (response.ok) {
        const dados = await response.text();
        document.getElementById("saida").textContent = dados;
    }else{
        console.log(response)
    }
}


async function bucaCliente() {
    const doc_cpf = document.getElementById("cpf").value;
    if(!doc_cpf ){
        alert("Por favor insira um CPF");
        return;
    }

    //devemos tratar erros
    const response = await fetch(`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`);

    const dados = await response.json();

    document.getElementById('nome').textContent = dados.nome;
    document.getElementById('nasc').textContent = dados.data_nascimento;
    document.getElementById('email').textContent = dados.email;

    cpf_anterior = doc_cpf
}