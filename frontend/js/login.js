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

        const message =
            document.getElementById(
                "message"
            );

        if (response.ok) {

            localStorage.setItem(
                "token",
                data.token
            );

            message.innerText =
                "Login successful";

            setTimeout(() => {

                window.location.href =
                    "dashboard.html";

            }, 1000);

        } else {

            message.innerText =
                data.error;
        }
    }
);