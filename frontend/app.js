const API_URL = "http://127.0.0.1:5000/autos/";

async function cargarAutos() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Error al obtener autos");
        }

        const autos = await response.json();

        renderizarAutos(autos);

    } catch (error) {
        console.error("Error:", error);
        alert("No se pudieron cargar los autos");
    }
}

function renderizarAutos(autos) {
    const tabla = document.getElementById("tabla-autos");

    tabla.innerHTML = ""; // limpia antes de renderizar

    autos.forEach(auto => {
        const fila = `
            <tr>
                <td>${auto.id}</td>
                <td>${auto.marca}</td>
                <td>${auto.modelo}</td>
                <td>${auto.year}</td>
                <td>$${auto.precio}</td>
            </tr>
        `;

        tabla.innerHTML += fila;
    });
}
