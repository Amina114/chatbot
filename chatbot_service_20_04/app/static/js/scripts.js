document.getElementById("chatbot-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const userInput = document.getElementById("user_input").value;

    const response = await fetch("/api/chatbot/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: userInput })
    });

    const result = await response.json();
    const responseArea = document.getElementById("response-area");

    if (result.status === "success") {
        responseArea.innerHTML = `
            <h3>Résultats de l'analyse :</h3>
            <p><strong>Client :</strong> ${result.data.client}</p>
            <p><strong>Label :</strong> ${result.data.label}</p>
            <p><strong>Gravité :</strong> ${result.data.severity}</p>
        `;
    } else {
        responseArea.innerHTML = `<p>Erreur : ${result.detail}</p>`;
    }
});document.getElementById("chatbot-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const userInput = document.getElementById("user_input").value;

    const response = await fetch("/api/chatbot/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: userInput })
    });

    const result = await response.json();
    const responseArea = document.getElementById("response-area");

    if (result.status === "success") {
        responseArea.innerHTML = `
            <h3>Résultats de l'analyse :</h3>
            <p><strong>Client :</strong> ${result.data.client}</p>
            <p><strong>Label :</strong> ${result.data.label}</p>
            <p><strong>Gravité :</strong> ${result.data.severity}</p>
        `;
    } else {
        responseArea.innerHTML = `<p>Erreur : ${result.detail}</p>`;
    }
});