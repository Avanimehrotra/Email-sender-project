// frontend/scripts.js
document.getElementById("smtp-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const provider = document.getElementById("provider").value;
    const senderEmail = document.getElementById("sender_email").value;
    const password = document.getElementById("password").value;
    const recipientEmail = document.getElementById("recipient_email").value;
    const subject = document.getElementById("subject").value;
    const body = document.getElementById("body").value;

    const response = await fetch("/send_email", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            provider,
            sender_email: senderEmail,
            password,
            recipient_email: recipientEmail,
            subject,
            body
        })
    });

    const result = await response.json();
    alert(result.message || result.error);
});
