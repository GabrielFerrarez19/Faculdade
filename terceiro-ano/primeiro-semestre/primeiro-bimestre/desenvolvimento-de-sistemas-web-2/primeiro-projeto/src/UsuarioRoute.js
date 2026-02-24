const UsuarioController = require("./UsuarioController");

module.exports = (app) => {
  app.get("/usuario", UsuarioController.get);
  app.post("/usuario", UsuarioController.post);
  app.put("/usuario", UsuarioController.put);
  app.delete("/usuario", UsuarioController.delete);
};
