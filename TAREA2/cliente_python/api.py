from py_mini_racer import py_mini_racer

codigo_js0 = """

const http = require('http');
const port = 3000;

// Crear un servidor HTTP
const server = http.createServer((req, res) => {
    // Manejar las solicitudes POST y GET
    if (req.method === 'POST' && req.url === '/registro') {
        let data = '';
        req.on('data', chunk => {
            // Recibir los datos del cuerpo de la solicitud
            data += chunk.toString();
        });
        req.on('end', () => {
            // Procesar los datos recibidos
            const { nombre, rut } = JSON.parse(data);
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(`${nombre}_${rut} ha sido registrado`);
        });
    } else if (req.method === 'GET' && req.url === '/muestra') {
        // Generar un número aleatorio entre 0 y 9
        const numeroAleatorio = Math.floor(Math.random() * 10);
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`Todo bien. Número aleatorio: ${numeroAleatorio}`);
    } else {
        // Manejar otras solicitudes
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

// Iniciar el servidor
server.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});


"""

codigo_js = """

const express = require('express');
const app = express();
const port = 3000;

// Endpoint de registro
app.post('/registro', (req, res) => {
    // Suponiendo que recibimos datos en formato JSON
    // Reemplaza este código con la lógica real de registro
    const { nombre, rut } = req.body;
    console.log(nombre, rut);
    res.send(`${nombre}_${rut} ha sido registrado`);
});

// Endpoint de muestra
app.get('/muestra', (req, res) => {
    // Generar un número aleatorio entre 0 y 9
    const numeroAleatorio = Math.floor(Math.random() * 10);
    res.send(`Todo bien. Número aleatorio: ${numeroAleatorio}`);
});

app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});


"""

motor_js = py_mini_racer.MiniRacer()
resultado = motor_js.execute(codigo_js)
print(resultado)
