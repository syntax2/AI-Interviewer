const backendUrl = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    if (!userInput) return;

    // Display user message
    const messagesDiv = document.getElementById("messages");
    messagesDiv.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

    // Clear input
    document.getElementById("userInput").value = "";

    // Send message to backend
    const response = await fetch(`${backendUrl}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    messagesDiv.innerHTML += `<div><strong>AI Interviewer:</strong> ${data.response}</div>`;
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
}