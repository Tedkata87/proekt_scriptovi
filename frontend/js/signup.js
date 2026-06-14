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

        const message =
            document.getElementById(
                "message"
            );

        if (response.ok) {

            message.innerText =
                "Registration successful!";

            setTimeout(() => {

                window.location.href =
                    "login.html";

            }, 1500);

        } else {

            message.innerText =
                data.error;
        }
    }
);