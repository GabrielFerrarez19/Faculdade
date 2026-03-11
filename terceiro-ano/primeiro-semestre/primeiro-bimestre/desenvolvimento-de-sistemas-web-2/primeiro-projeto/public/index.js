listar();

async function novo() {
  document.getElementById("formulario").style.display = "block";
  document.getElementById("conteudo").style.display = "none";
  document.getElementById("nome").value = "";
  document.getElementById("telefone").value = "";
}
async function salvar() {
  document.getElementById("conteudo").innerHTML = "aguarde...";
  const request = {
    nome: document.getElementById("nome").value,
    telefone: document.getElementById("telefone").value,
  };
  const resp = await fetch("/pessoa", {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify(request),
  });
  if (!resp.ok) {
    console.log("erro " + resp.status);
  }
  const retorno = await resp.text();
  document.getElementById("conteudo").innerHTML = retorno;
  document.getElementById("formulario").style.display = "none";
  document.getElementById("conteudo").style.display = "block";
  listar();
}

async function listar() {
  const conteudo = document.getElementById("conteudo");
  conteudo.innerHTML = "aguarde...";

  const resp = await fetch("/pessoa", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  });

  const dados = await resp.json();

  let tabela = `<table> 
                <th>nome</th>
                <th>Telefone</th>
     `;
  for (let i = 0; i < dados.length; i++) {
    tabela += `<tr>
        <td>${dados[i].nome}</td>
        <td>${dados[i].telefone}</td>
    </tr>`;
  }

  tabela += "</table>";

  document.getElementById("conteudo").innerHTML = tabela;
}
async function inserir() {
  document.getElementById("conteudo").innerHTML = "aguarde...";

  const novo = {
    nome: "Bill gates",
    email: "bill@microsoft.com",
  };

  const resp = await fetch("/pessoa", {
    method: "POST",
    headers: {
      "Content-type": "apllication/json",
    },
    body: JSON.stringify(novo),
  });

  if (!resp.ok) {
    console.log("erro " + resp.status);
  }

  //se fosse json, converte a resposta para json
  //const dados = await resp.json();
  const retorno = await resp.text();

  document.getElementById("conteudo").innerHTML = retorno;
}
async function alterar() {
  document.getElementById("conteudo").innerHTML = "aguarde...";

  const novo = {
    nome: "Bill gates",
    email: "bill@microsoft.com",
  };

  const resp = await fetch("/pessoa/123", {
    method: "PUT",
    headers: {
      "Content-type": "apllication/json",
    },
    body: JSON.stringify(novo),
  });

  if (!resp.ok) {
    console.log("erro " + resp.status);
  }

  //se fosse json, converte a resposta para json
  //const dados = await resp.json();

  const retorno = await resp.text();

  document.getElementById("conteudo").innerHTML = retorno;
}
async function excluir() {
  document.getElementById("conteudo").innerHTML = "aguarde...";

  const novo = {
    nome: "Bill gates",
    email: "bill@microsoft.com",
  };

  const resp = await fetch("/pessoa/222", {
    method: "DELETE",
    headers: {
      "Content-type": "apllication/json",
    },
    body: JSON.stringify(novo),
  });

  if (!resp.ok) {
    console.log("erro " + resp.status);
  }

  //se fosse json, converte a resposta para json
  //const dados = await resp.json();
  const dados = await resp.text();

  document.getElementById("conteudo").innerHTML = dados;
}
