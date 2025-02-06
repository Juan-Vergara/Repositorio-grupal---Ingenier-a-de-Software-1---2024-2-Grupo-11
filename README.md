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
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2E7D32;
        }
        ul {
            list-style-type: square;
        }
        code {
            background: #f4f4f4;
            padding: 3px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>EcoScan</h1>
    <p><strong>Repositorio grupal - Ingeniería de Software 1 - 2024-2 Grupo 11</strong></p>
    <p><strong>Integrantes:</strong> Alejandro Arguello Muñoz, Juan Luis Vergara Novoa, Steven David Alfonso Galindo, Daniel Santiago Delgado Pinilla</p>
    
    <h2>Objetivo Principal</h2>
    <p>Crear una aplicación funcional y bien documentada que facilite el reciclaje mediante el reconocimiento de imágenes y brinde contenido educativo sobre manejo de residuos.</p>
    
    <h2>Descripción</h2>
    <p><strong>EcoScan</strong> es una aplicación móvil gratuita diseñada para asistir a los usuarios en la clasificación adecuada de sus residuos. Utiliza tecnología de reconocimiento de imágenes para identificar objetos y sugerir el contenedor correspondiente para su disposición (reciclaje, orgánico, basura general, etc.), fomentando prácticas de reciclaje y un impacto positivo en el medio ambiente.</p>
    
    <h2>Estructura del Equipo y Roles</h2>
    <ul>
        <li><strong>Backend (Django):</strong> Desarrollo del servidor, APIs, gestión de la base de datos y lógica de negocio.</li>
        <li><strong>Frontend (Flutter):</strong> Desarrollo de la interfaz de usuario, navegación y consumo de las APIs del backend.</li>
    </ul>
    
    <h2>Tecnologías Utilizadas</h2>
    <h3>Backend</h3>
    <ul>
        <li><strong>Lenguaje y Frameworks:</strong> Python con TensorFlow y OpenCV para el procesamiento de imágenes y reconocimiento de materiales.</li>
        <li><strong>APIs y Servicios:</strong> Integración con Firebase Cloud Messaging para notificaciones y Firebase Auth para la autenticación.</li>
    </ul>
    
    <h3>Frontend</h3>
    <ul>
        <li><strong>Framework:</strong> Flutter para el desarrollo de una aplicación móvil multiplataforma (Android y opcionalmente iOS).</li>
        <li><strong>UI/UX:</strong> Diseño responsivo e intuitivo, basado en las últimas tendencias de diseño para aplicaciones móviles.</li>
    </ul>
    
    <h3>Base de Datos y Servicios en la Nube</h3>
    <ul>
        <li><strong>Firebase:</strong> Para autenticación, almacenamiento de datos (historial de escaneos, perfiles de usuario) y mensajería.</li>
        <li><strong>Infraestructura:</strong> Servidores en la nube (por ejemplo, Google Cloud Platform o AWS) para asegurar alta disponibilidad y escalabilidad.</li>
    </ul>
</body>
</html>
