document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("cadastro");

    if (form) {
        form.addEventListener("submit", function (event) {
            const userInput = document.getElementById("user").value;
            const passwordInput = document.getElementById("password").value;

            // Credenciais permitidas
            const usuarioCorreto = "Jmello21";
            const senhaCorreta = "Mac2025*@";

            // Validação
            if (userInput !== usuarioCorreto || passwordInput !== senhaCorreta) {
                // Impede o envio do formulário se estiver errado
                event.preventDefault();
                alert("⚠️ Usuário ou senha incorretos! Verifique suas credenciais.");
            } else {
                // Se estiver correto, avisa antes de enviar
                console.log("Login validado com sucesso no frontend!");
            }
        });
    }
});