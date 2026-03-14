const express = require("express");

const cors = require("cors");

const app = express();

app.use(cors());

app.use(express.json());

// Evita 404 no favicon (navegador pede automaticamente)
app.get("/favicon.ico", (req, res) => res.status(204).end());

require("./src/index")(app);
app.use(express.static("public"));
app.listen(3333);
