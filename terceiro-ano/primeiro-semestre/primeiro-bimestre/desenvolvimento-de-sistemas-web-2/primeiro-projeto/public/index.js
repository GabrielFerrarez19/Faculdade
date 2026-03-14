document.addEventListener("DOMContentLoaded", () => {
  listar();
  document.getElementById("btnNovo").addEventListener("click", novo);
  document.getElementById("btnSalvar").addEventListener("click", salvar);
  document.getElementById("btnCancelar").addEventListener("click", cancelar);
});

function novo() {
  document.getElementById("formulario").style.display = "block";
  document.getElementById("conteudo").closest(".card").style.display = "none";
  document.getElementById("formTitulo").textContent = "Nova pessoa";
  document.getElementById("id").value = "";
  document.getElementById("nome").value = "";
  document.getElementById("telefone").value = "";
  document.getElementById("email").value = "";
}

function cancelar() {
  document.getElementById("formulario").style.display = "none";
  document.getElementById("conteudo").closest(".card").style.display = "block";
  listar();
}

async function salvar() {
  const id = document.getElementById("id").value;
  const payload = {
    nome: document.getElementById("nome").value.trim(),
    telefone: document.getElementById("telefone").value.trim(),
    email: document.getElementById("email").value.trim(),
  };

  const url = id ? `/pessoa/${id}` : "/pessoa";
  const method = id ? "PUT" : "POST";

  try {
    const resp = await fetch(url, {
      method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const retorno = await resp.json().catch(() => ({}));
    if (!resp.ok) {
      alert(retorno.message || "Erro ao salvar. Tente novamente.");
      return;
    }
    document.getElementById("formulario").style.display = "none";
    document.getElementById("conteudo").closest(".card").style.display = "block";
    listar();
  } catch (err) {
    alert("Erro de conexão. Tente novamente.");
  }
}

async function editar(id) {
  try {
    const resp = await fetch(`/pessoa/${id}`, { method: "GET" });
    const dados = await resp.json();
    if (!resp.ok || !dados || dados.length === 0) {
      alert("Pessoa não encontrada.");
      return;
    }
    const p = Array.isArray(dados) ? dados[0] : dados;
    document.getElementById("id").value = p.id;
    document.getElementById("nome").value = p.nome || "";
    document.getElementById("telefone").value = p.telefone || "";
    document.getElementById("email").value = p.email || "";
    document.getElementById("formTitulo").textContent = "Alterar pessoa";
    document.getElementById("formulario").style.display = "block";
    document.getElementById("conteudo").closest(".card").style.display = "none";
  } catch (err) {
    alert("Erro ao carregar dados. Tente novamente.");
  }
}

async function excluir(id, nome) {
  if (!confirm(`Deseja realmente excluir "${nome || "esta pessoa"}"?`)) return;
  try {
    const resp = await fetch(`/pessoa/${id}`, { method: "DELETE" });
    if (!resp.ok) {
      const err = await resp.json().catch(() => ({}));
      alert(err.message || "Erro ao excluir.");
      return;
    }
    listar();
  } catch (err) {
    alert("Erro de conexão. Tente novamente.");
  }
}

async function listar() {
  const conteudo = document.getElementById("conteudo");
  conteudo.innerHTML = '<p class="text-muted text-center py-4">Carregando...</p>';

  try {
    const resp = await fetch("/pessoa", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });
    const dados = await resp.json();

    if (!dados || dados.length === 0) {
      conteudo.innerHTML =
        '<p class="text-muted text-center py-4">Nenhuma pessoa cadastrada.</p>';
      return;
    }

    let tabela = `
      <div class="table-responsive">
        <table class="table table-hover table-striped align-middle">
          <thead class="table-primary">
            <tr>
              <th>Nome</th>
              <th>Telefone</th>
              <th>E-mail</th>
              <th class="text-end" style="width: 180px">Ações</th>
            </tr>
          </thead>
          <tbody>
    `;
    for (let i = 0; i < dados.length; i++) {
      const d = dados[i];
      tabela += `
        <tr>
          <td>${escapeHtml(d.nome || "-")}</td>
          <td>${escapeHtml(d.telefone || "-")}</td>
          <td>${escapeHtml(d.email || "-")}</td>
          <td class="text-end">
            <button type="button" class="btn btn-sm btn-outline-primary me-1" onclick="editar(${d.id})">Editar</button>
            <button type="button" class="btn btn-sm btn-outline-danger" onclick="excluir(${d.id}, '${escapeHtmlAttr(d.nome || "")}')">Excluir</button>
          </td>
        </tr>
      `;
    }
    tabela += "</tbody></table></div>";
    conteudo.innerHTML = tabela;
  } catch (err) {
    conteudo.innerHTML =
      '<p class="text-danger text-center py-4">Erro ao carregar a lista.</p>';
  }
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function escapeHtmlAttr(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
