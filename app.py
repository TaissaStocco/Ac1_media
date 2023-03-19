from flask import Flask

app = Flask(__name__)
@app.route('/media/<float:nota1>/<float:nota2>')
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return f'A média das notas é {media:.1f}'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/media/<float:nota1>/<float:nota2>')
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return f'A média das notas é {media:.1f}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
