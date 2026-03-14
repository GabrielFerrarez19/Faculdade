async function connect() {
  if (global.connection && global.connection.state !== "disconnected")
    return global.connection;

  const mysql = require("mysql2/promise");
  const connection = await mysql.createConnection({
    host: "54.91.193.137",
    user: "libertas",
    password: "123456",
    database: "libertas5per",
  });
  console.log("Conectou no MySQL");
  global.connection = connection;
  return connection;
}

exports.getByID = async (req, res, next) => {
  try {
    const conn = await connect();
    const id = req.params.id;
    const [rows] = await conn.query(
      "SELECT idpessoa AS id, nome, telefone, email FROM pessoa WHERE idpessoa = ?",
      [id]
    );
    res.status(200).send(rows);
  } catch (err) {
    console.error("Erro ao buscar pessoa:", err);
    res.status(500).send({ message: "Erro ao buscar pessoa", error: err.message });
  }
};

exports.get = async (req, res, next) => {
  try {
    const conn = await connect();
    const [rows] = await conn.query(
      "SELECT idpessoa AS id, nome, telefone, email FROM pessoa ORDER BY nome"
    );
    res.status(200).send(rows);
  } catch (err) {
    console.error("Erro ao listar pessoas:", err);
    res.status(500).send({ message: "Erro ao listar pessoas", error: err.message });
  }
};

exports.post = async (req, res, next) => {
  try {
    const conn = await connect();
    const { nome, telefone, email } = req.body;
    await conn.query(
      "INSERT INTO pessoa (nome, telefone, email) VALUES (?, ?, ?)",
      [nome || null, telefone || null, email || null]
    );
    res.status(201).send({ message: "Usuário criado com sucesso" });
  } catch (err) {
    console.error("Erro ao criar pessoa:", err);
    res.status(500).send({ message: "Erro ao criar pessoa", error: err.message });
  }
};

exports.put = async (req, res, next) => {
  try {
    const conn = await connect();
    const id = req.params.id;
    const { nome, telefone, email } = req.body;
    await conn.query(
      "UPDATE pessoa SET nome = ?, telefone = ?, email = ? WHERE idpessoa = ?",
      [nome || null, telefone || null, email || null, id]
    );
    res.status(200).send({ message: "Usuário atualizado com sucesso" });
  } catch (err) {
    console.error("Erro ao atualizar pessoa:", err);
    res.status(500).send({ message: "Erro ao atualizar pessoa", error: err.message });
  }
};

exports.delete = async (req, res, next) => {
  try {
    const conn = await connect();
    const id = req.params.id;
    await conn.query("DELETE FROM pessoa WHERE idpessoa = ?", [id]);
    res.status(204).send({ message: "Usuário deletado com sucesso" });
  } catch (err) {
    console.error("Erro ao deletar pessoa:", err);
    res.status(500).send({ message: "Erro ao deletar pessoa", error: err.message });
  }
};
