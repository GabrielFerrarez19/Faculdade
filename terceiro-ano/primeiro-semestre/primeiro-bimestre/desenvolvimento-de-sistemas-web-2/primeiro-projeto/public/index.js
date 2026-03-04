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
async function consultar() {
  document.getElementById("conteudo").innerHTML = "aguarde...";

  const resp = await fetch("/pessoa/222", {
    method: "GET",
    headers: {
      "Content-type": "apllication/json",
    },
  });

  if (!resp.ok) {
    console.log("erro " + resp.status);
  }

  //se fosse json, converte a resposta para json
  //const dados = await resp.json();
  const retorno = await resp.text();

  document.getElementById("conteudo").innerHTML = retorno;
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
