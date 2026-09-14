from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Docker App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 50px; }
            .container { max-width: 600px; margin: 0 auto; }
            h1 { color: #2196F3; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Flask Docker App</h1>
            <p>Aplicacion Flask ejecutandose en Docker</p>
            <p><a href="/api/health">Verificar estado de la API</a></p>
            <p><a href="/api/info">Informacion del contenedor</a></p>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "message": "Flask app funcionando correctamente"
    })

@app.route('/api/info')
def info():
    import os
    import platform
    return jsonify({
        "app": "Flask Docker Demo",
        "version": "1.0.0",
        "python_version": os.sys.version,
        "hostname": platform.node()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
