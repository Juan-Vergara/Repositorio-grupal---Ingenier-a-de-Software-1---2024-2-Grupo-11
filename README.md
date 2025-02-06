<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoScan - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background: #eee;
            padding: 5px;
            border-radius: 5px;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>📌 EcoScan</h1>
    <p><strong>EcoScan</strong> es una aplicación móvil gratuita diseñada para ayudar a los usuarios a clasificar adecuadamente sus residuos. Utiliza tecnología de <strong>reconocimiento de imágenes</strong> para identificar objetos y sugerir el contenedor adecuado para su disposición (<em>reciclaje, orgánico, basura general, etc.</em>), fomentando así prácticas de reciclaje y un impacto positivo en el medio ambiente.</p>

    <h2>🎯 Objetivo Principal</h2>
    <p>Crear una aplicación funcional y bien documentada que facilite el reciclaje mediante el <strong>reconocimiento de imágenes</strong> y brinde contenido educativo sobre el manejo de residuos.</p>

    <h2>🏗️ Estructura del Equipo y Roles</h2>
    <ul>
        <li><strong>Backend (Django):</strong> Desarrollo del servidor, APIs, gestión de la base de datos y lógica de negocio.</li>
        <li><strong>Frontend (Flutter):</strong> Desarrollo de la interfaz de usuario, navegación y consumo de las APIs del backend.</li>
    </ul>
    
    <h3>👥 Integrantes del equipo:</h3>
    <ul>
        <li>Alejandro Arguello Muñoz</li>
        <li>Juan Luis Vergara Novoa</li>
        <li>Steven David Alfonso Galindo</li>
        <li>Daniel Santiago Delgado Pinilla</li>
    </ul>

    <h2>🛠️ Tecnologías Utilizadas</h2>
    <h3>Backend</h3>
    <ul>
        <li><strong>Lenguaje y Frameworks:</strong> Python con <strong>Django</strong>, <strong>TensorFlow</strong> y <strong>OpenCV</strong> para el procesamiento de imágenes y reconocimiento de materiales.</li>
        <li><strong>APIs y Servicios:</strong>
            <ul>
                <li>Firebase Cloud Messaging para notificaciones.</li>
                <li>Firebase Auth para la autenticación.</li>
            </ul>
        </li>
    </ul>
    
    <h3>Frontend</h3>
    <ul>
        <li><strong>Framework:</strong> <strong>Flutter</strong> para el desarrollo de una aplicación móvil multiplataforma (<strong>Android y opcionalmente iOS</strong>).</li>
        <li><strong>UI/UX:</strong> Diseño responsivo e intuitivo, basado en tendencias modernas de diseño para aplicaciones móviles.</li>
    </ul>

    <h3>Base de Datos y Servicios en la Nube</h3>
    <ul>
        <li><strong>Firebase:</strong> Autenticación, almacenamiento de datos (historial de escaneos, perfiles de usuario) y mensajería.</li>
        <li><strong>Infraestructura:</strong> Servidores en la nube (<strong>Google Cloud Platform o AWS</strong>) para asegurar alta disponibilidad y escalabilidad.</li>
    </ul>

    <h2>🚀 Instalación y Uso</h2>

    <h3>🔹 Requisitos previos</h3>
    <ul>
        <li>Tener instalado <strong>Python 3.8+</strong> y <strong>Django</strong> para el backend.</li>
        <li>Tener instalado <strong>Flutter</strong> para el frontend.</li>
        <li>Configurar Firebase para la autenticación y el almacenamiento.</li>
    </ul>

    <h3>🔹 Clonar el repositorio</h3>
    <pre><code>git clone https://github.com/tu-usuario/EcoScan.git
cd EcoScan</code></pre>

    <h3>🔹 Configuración del Backend</h3>
    <pre><code>cd backend
pip install -r requirements.txt
python manage.py runserver</code></pre>

    <h3>🔹 Configuración del Frontend</h3>
    <pre><code>cd frontend
flutter pub get
flutter run</code></pre>

</body>
</html>
