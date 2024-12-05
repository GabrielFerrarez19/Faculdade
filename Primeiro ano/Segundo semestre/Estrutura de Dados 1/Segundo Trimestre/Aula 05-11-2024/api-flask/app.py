from flask import Flask

app = Flask("Minha API")

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/soma")
def soma():
    s = 0
    for i in range(10):
        s += i
    return f"resultado = {s}"


if __name__ == "__main__":
    app.run()