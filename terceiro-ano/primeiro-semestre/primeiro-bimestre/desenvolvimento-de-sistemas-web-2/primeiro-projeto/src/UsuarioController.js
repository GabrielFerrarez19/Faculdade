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
  const conn = await connect();
  let id = req.params.id;
  let sql = `SELECT * FROM pessoa WHERE id = ${id}`;
  const [rows] = await conn.query(sql);
  res.status(200).send(rows);
};

exports.get = async (req, res, next) => {
  // res.status(200).send("Rota GET!");
  const conn = await connect();
  const [rows] = await conn.query("SELECT * FROM pessoa ORDER BY nome");
  res.status(200).send(rows);
};

exports.post = async (req, res, next) => {
  const conn = await connect();
  let { nome, telefone } = req.body;
  let sql = `INSERT INTO pessoa (nome, telefone) VALUE ('${nome}', '${telefone}')`;
  await conn.query(sql);
  res.status(201).send({ message: "Usuário criado com sucesso" });
};

exports.put = async (req, res, next) => {
  const conn = await connect();
  let id = req.params.id;
  let { nome, telefone } = req.body;
  let sql = `UPDATE pessoa SET nome = '${nome}', telefone = '${telefone}' WHERE id = ${id}`;
  await conn.query(sql);
  res.status(200).send({ message: "Usuário atualizado com sucesso" });
};

exports.delete = async (req, res, next) => {
  const conn = await connect();
  let id = req.params.id;
  let sql = `DELETE FROM pessoa WHERE id = ${id}`;
  await conn.query(sql);
  res.status(204).send({ message: "Usuário deletado com sucesso" });
};
