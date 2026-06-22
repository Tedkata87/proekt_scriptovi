const signupForm =
    document.getElementById(
        "signup-form"
    );

signupForm.addEventListener(
    "submit",
    async (e) => {

        e.preventDefault();

        const username =
            document.getElementById(
                "username"
            ).value;

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
                    "http://127.0.0.1:5000/sign-up",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            username,
                            email,
                            password
                        })
                    }
                );

            const data =
                await response.json();

            if (response.ok) {

                message.innerText =
                    "Registration successful!";

                message.style.color = "#00ff00";

                setTimeout(() => {

                    window.location.href =
                        "login.html";

                }, 1500);

            } else {

                message.innerText =
                    data.error || "Registration failed";

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