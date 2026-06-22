const loginForm =
    document.getElementById(
        "login-form"
    );

loginForm.addEventListener(
    "submit",
    async (e) => {

        e.preventDefault();

        const email =
            document.getElementById(
                "email"
            ).value;

        const password =
            document.getElementById(
                "password"
            ).value;

        const message =
            document.getElementById(
                "message"
            );

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:5000/sign-in",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            email,
                            password
                        })
                    }
                );

            const data =
                await response.json();

            if (response.ok) {

                localStorage.setItem(
                    "token",
                    data.token
                );

                message.innerText =
                    "Login successful";

                message.style.color = "#00ff00";

                setTimeout(() => {

                    window.location.href =
                        "dashboard.html";

                }, 1000);

            } else {

                message.innerText =
                    data.error || "Login failed";

                message.style.color = "#ff6b6b";
            }

        } catch (error) {

            message.innerText =
                "Network error: " + error.message;

            message.style.color = "#ff6b6b";

            console.error("Fetch error:", error);
        }
    }
);