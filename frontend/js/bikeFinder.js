const form =
    document.getElementById(
        "bikeFinderForm"
    );

form.addEventListener(
    "submit",
    async (e) => {

        e.preventDefault();

        const token =
            localStorage.getItem(
                "token"
            );

        if (!token) {

            alert(
                "Please login first."
            );

            window.location.href =
                "login.html";

            return;
        }

        const data = {

            height: parseInt(
                document.getElementById(
                    "height"
                ).value
            ),

            weight: parseInt(
                document.getElementById(
                    "weight"
                ).value
            ),

            terrain:
                document.getElementById(
                    "terrain"
                ).value,

            budget: parseInt(
                document.getElementById(
                    "budget"
                ).value
            ),

            preferences:
                document.getElementById(
                    "preferences"
                ).value
        };

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:5000/bike-searches",
                    {
                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json",

                            "Authorization":
                                `Bearer ${token}`
                        },

                        body:
                            JSON.stringify(
                                data
                            )
                    }
                );

            const result =
                await response.json();

            if (!response.ok) {

                throw new Error(
                    result.error
                );
            }

            document.getElementById(
                "recommendation"
            ).innerHTML =

                `<pre>${JSON.stringify(
                    result.recommendation,
                    null,
                    2
                )}</pre>`;

        }

        catch (error) {

            document.getElementById(
                "recommendation"
            ).innerHTML =

                `<p>${error.message}</p>`;
        }
    }
);