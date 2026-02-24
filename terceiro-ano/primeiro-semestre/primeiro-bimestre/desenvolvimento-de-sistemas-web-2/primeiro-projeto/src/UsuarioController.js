exports.get = (req, res, next) => {
  res.status(200).send("Rota GET!");
};

exports.post = (req, res, next) => {
  res.status(200).send("Rota POST");
};

exports.put = (req, res, next) => {
  res.status(200).send("Rota PUT");
};

exports.delete = (req, res, next) => {
  res.status(200).send("Rota DELETE");
};
