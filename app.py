from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Productos disponibles con más información
productos = [
    {
        'id': 1,
        'nombre': '𝕆𝕡𝕥𝕚𝕞𝕚𝕫𝕒𝕔𝕚ó𝕟 𝔹á𝕤𝕚𝕔𝕒',
        'descripcion': 'Mejora el rendimiento básico de tu PC, incluye limpieza de archivos basura y optimización de inicio.',
        'precio': 20,
        'imagen': 'producto1.jpg',
        'detalles': 'Este servicio optimiza los componentes básicos de tu PC para mejorar el rendimiento en juegos y aplicaciones cotidianas.',
        'tiempo': '1-2 horas',
        'nivel': 'Básico',
        'enlace': 'https://www.tienda.com/optimiza-basis'
    },
    {
        'id': 2,
        'nombre': '𝕆𝕡𝕥𝕚𝕞𝕚𝕫𝕒𝕔𝕚ó𝕟 𝔸𝕧𝕒𝕟𝕫𝕒𝕕𝕒',
        'descripcion': 'Optimización avanzada para un rendimiento máximo. Incluye actualizaciones y ajustes en la BIOS.',
        'precio': 50,
        'imagen': 'producto2.jpg',
        'detalles': 'Este servicio optimiza el sistema operativo, mejora el rendimiento de la CPU y gestiona los recursos para maximizar tu PC.',
        'tiempo': '2-4 horas',
        'nivel': 'Avanzado',
        'enlace': 'https://www.tienda.com/optimiza-avanzado'
    },
    {
        'id': 3,
        'nombre': '𝕄𝕒𝕟𝕥𝕖𝕟𝕚𝕞𝕚𝕖𝕟𝕥𝕠 ℂ𝕠𝕞𝕡𝕝𝕖𝕥𝕠',
        'descripcion': 'Mantenimiento completo que incluye limpieza de hardware y software, así como ajustes en el sistema.',
        'precio': 70,
        'imagen': 'producto3.jpg',
        'detalles': 'Servicio integral de optimización, limpieza interna, mejora de rendimiento, y software para aumentar la vida útil de tu PC.',
        'tiempo': '4-6 horas',
        'nivel': 'Completo',
        'enlace': 'https://www.tienda.com/mantenimiento-completo'
    }
]

# Página principal (gamer.html)
@app.route('/')
def gamer():
    return render_template('gamer.html')

# Página de inicio (index.html)
@app.route('/inicio')
def home():
    return render_template('index.html')


@app.route('/productos')
def ver_productos():
    return render_template('productos.html', productos=productos)

@app.route('/pedido/<int:producto_id>', methods=['GET', 'POST'])
def pedido(producto_id):
    producto = next(p for p in productos if p['id'] == producto_id)
    if request.method == 'POST':
        return redirect(url_for('gracias', producto_nombre=producto['nombre']))
    return render_template('pedido.html', producto=producto)

@app.route('/gracias')
def gracias():
    return "¡Gracias por tu compra! Te hemos enviado un correo con los detalles."


if __name__ == '__main__':
    app.run(debug=True)
