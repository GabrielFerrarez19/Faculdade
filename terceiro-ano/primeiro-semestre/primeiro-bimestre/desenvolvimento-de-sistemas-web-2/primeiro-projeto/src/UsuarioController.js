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

exports.getByID = (req, res, next) => {
  let id = req.params.id;
  res.status(200).send(`Rota GET! ${id}`);
};

exports.get = async (req, res, next) => {
  // res.status(200).send("Rota GET!");
  const conn = await connect();
  const [rows] = await conn.query("SELECT * FROM pessoa");
  res.status(200).send(rows);
};

exports.post = (req, res, next) => {
  res.status(201).send("Rota POST");
};

exports.put = (req, res, next) => {
  let id = req.params.id;
  res.status(200).send(`Rota PUT! ${id}`);
};

exports.delete = (req, res, next) => {
  let id = req.params.id;
  res.status(204).send(`Rota DELETE! ${id}`);
};
