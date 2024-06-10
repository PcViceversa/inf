// Registrar un usuario
fetch("http://localhost:5000/api/registrar", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        nombre: "Daniel",
        correo: "daniel.duenas@usm.cl",
        clave: "clavecita123",
        descripcion: "Una descripcion que puede escribir el usuario"
    })
})
.then(response => response.json())
.then(data => console.log(`Respuesta al registrar usuario: ${data.estado} - ${data.mensaje}`))
.catch(error => console.error("Error al registrar usuario:", error));

// Bloquear un usuario
fetch("http://localhost:5000/api/bloquear", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        correo: "daniel.duenas@usm.cl",
        clave: "clavecita123",
        correo_bloquear: "fernando.banz@sansano.usm.cl"
    })
})
.then(response => response.json())
.then(data => console.log(`Respuesta al bloquear usuario: ${data.estado} - ${data.mensaje}`))
.catch(error => console.error("Error al bloquear usuario:", error));

// Obtener información pública de un usuario
fetch("http://localhost:5000/api/informacion/sebastian.torrealba@usm.cl")
.then(response => {
    if (response.status === 200) {
        return response.json();
    } else {
        throw new Error(`Error al obtener información del usuario: ${response.status} - ${response.statusText}`);
    }
})
.then(data => {
    console.log(`Información del usuario ${data.correo}:`);
    console.log(`Nombre: ${data.nombre}`);
    console.log(`Descripción: ${data.descripcion}`);
})
.catch(error => console.error(error));
