const UsuarioController = require("./UsuarioController");

module.exports = (app) => {
  app.get("/pessoa", UsuarioController.get);
  app.get("/pessoa/:id", UsuarioController.getByID);
  app.post("/pessoa", UsuarioController.post);
  app.put("/pessoa/:id", UsuarioController.put);
  app.delete("/pessoa/:id", UsuarioController.delete);
};
