async function getDados() {
    // faz a chamada ao endpoint Flask
    const response = await fetch('http://127.0.0.1:5000/soma')

    // verificar se a resposta foi bem sucedida
    if (!response.ok){
        const dados = await response.text()
        console.log(dados)
        document.getElementById('saida').textContent = dados
    }
}

async function buscaCliente() {
    const doc_cpf = document.getElementById("cpf").value;
    if (!doc_cpf){
        alert("Porfavor, insira um CPF");
        return;
    }
    // devemos tratar erros
    const response = await fetch(`http://127.0.0.1:5000/consulta?doc=${doc_cpf}`)

    const dados = await response.json();
    console.log(dados)
    document.getElementById("nome").textContent = dados.nome;
    document.getElementById("nasc").textContent = dados.data_nascimento;
    document.getElementById("email").textContent = dados.email;
}


async function cadastrarClientes() {
    // pegar os valores inseridos 
    const cpf = document.getElementById("cadcpf").value;
    const nome = document.getElementById("cadnome").value;
    const data_nascimento = document.getElementById("cadnascimento").value;
    const email = document.getElementById("cademail").value;

    //criar estrutura que definimos pro json
    const payload = {
        cpf,
        dados:{
            nome,
            data_nascimento,
            email
        }
    };

    //fazer requisição do back end
    const response = await fetch(`http://127.0.0.1:5000/cadastro`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
        const errorMessage = await response.text();
        console.error(`Erro: ${errorMessage}`);
        alert("Ocorreu um erro ao cadastrar o cliente.");
        return;
    }
    
    alert("Cliente cadastrado com sucesso!");
}