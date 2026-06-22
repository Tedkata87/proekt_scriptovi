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
                "Трябва първо да се впишеш."
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
                ).value || null,

            shock:
                document.getElementById(
                    "shock"
                ).value || null,

            frame_size:
                document.getElementById(
                    "frame_size"
                ).value || null,

            wheel_size:
                document.getElementById(
                    "wheel_size"
                ).value || null,

            drivetrain:
                document.getElementById(
                    "drivetrain"
                ).value || null,

            brakes:
                document.getElementById(
                    "brakes"
                ).value || null,

            handlebars:
                document.getElementById(
                    "handlebars"
                ).value || null
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

            const setupData = result;

            let html = `<div class="result-item">
                <h3>Конфигурация на настройката</h3>
                <h4>${setupData.brand} ${setupData.model}</h4>
                <hr>
                <p><strong>Височина на наездача:</strong> ${setupData.rider_height} см</p>
                <p><strong>Тегло на наездача:</strong> ${setupData.rider_weight} кг</p>
                <p><strong>Терен:</strong> ${setupData.terrain}</p>
                <p><strong>Тип велосипед:</strong> ${setupData.bike_type}</p>`;

            if (setupData.suspension_setup) {
                html += `<h4>Настройка на суспензията</h4>
                <p><strong>Натиск на вилка:</strong> ${setupData.suspension_setup.fork_pressure}</p>
                <p><strong>Натиск на амортисьор:</strong> ${setupData.suspension_setup.shock_pressure}</p>
                <p><strong>Sag вилка:</strong> ${setupData.suspension_setup.sag_fork}</p>
                <p><strong>Sag амортисьор:</strong> ${setupData.suspension_setup.sag_shock}</p>
                <p><strong>Rebound:</strong> ${setupData.suspension_setup.rebound}</p>`;
            }

            if (setupData.tire_pressure) {
                html += `<h4>Натиск на гуми</h4>
                <p><strong>Предни гуми:</strong> ${setupData.tire_pressure.front_tire}</p>
                <p><strong>Задни гуми:</strong> ${setupData.tire_pressure.rear_tire}</p>
                <p><em>${setupData.tire_pressure.advice}</em></p>`;
            }

            if (setupData.components && Object.keys(setupData.components).length > 0) {
                html += `<h4>Компоненти</h4>`;
                Object.entries(setupData.components).forEach(([key, value]) => {
                    if (value) {
                        html += `<p><strong>${key}:</strong> ${value}</p>`;
                    }
                });
            }

            html += `</div>`;

            document.getElementById(
                "setupResult"
            ).innerHTML = html;

        }

        catch (error) {

            document.getElementById(
                "setupResult"
            ).innerHTML =

                `<p class="error">Грешка: ${error.message}</p>`;
        }
    }
);