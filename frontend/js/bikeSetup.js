const setupForm =
    document.getElementById(
        "setupForm"
    );

setupForm.addEventListener(
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

            rider_height:
                parseInt(
                    document.getElementById(
                        "rider_height"
                    ).value
                ),

            rider_weight:
                parseInt(
                    document.getElementById(
                        "rider_weight"
                    ).value
                ),

            terrain:
                document.getElementById(
                    "terrain"
                ).value,

            bike_type:
                document.getElementById(
                    "bike_type"
                ).value,

            brand:
                document.getElementById(
                    "brand"
                ).value,

            model:
                document.getElementById(
                    "model"
                ).value,

            fork:
                document.getElementById(
                    "fork"
                ).value,

            shock:
                document.getElementById(
                    "shock"
                ).value,

            frame_size:
                document.getElementById(
                    "frame_size"
                ).value,

            wheel_size:
                document.getElementById(
                    "wheel_size"
                ).value,

            drivetrain:
                document.getElementById(
                    "drivetrain"
                ).value,

            brakes:
                document.getElementById(
                    "brakes"
                ).value,

            handlebars:
                document.getElementById(
                    "handlebars"
                ).value
        };

        try {

            const response =
                await fetch(
                    "http://127.0.0.1:5000/bike-setups",
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

            const recommendation =
                result.recommendation;

            document.getElementById(
                "setupResult"
            ).innerHTML =

                `<pre>${JSON.stringify(
                    recommendation,
                    null,
                    2
                )}</pre>`;

        }

        catch (error) {

            document.getElementById(
                "setupResult"
            ).innerHTML =

                `<p>${error.message}</p>`;
        }
    }
);