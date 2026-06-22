const form =
    document.getElementById(
        "bikeFinderForm"
    );

recommendation = db.Column(db.Text)

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
                "Трябва първо да се впишеш."
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

            const searchData = result;

            let html = `<div class="result-item">
                <h3>Препоръчени велосипеди</h3>
                <p><strong>Височина:</strong> ${searchData.height} см</p>
                <p><strong>Тегло:</strong> ${searchData.weight} кг</p>
                <p><strong>Терен:</strong> ${searchData.terrain}</p>
                <p><strong>Бюджет:</strong> €${searchData.budget}</p>
                <hr>`;

            if (searchData.sizing_advice) {
                html += `<h4>Препоръка за размер</h4>
                <p><strong>${searchData.sizing_advice.advice}</strong></p>
                <p>Твоят размер: <strong>${searchData.sizing_advice.frame_size}</strong></p>`;
            }

            if (searchData.bikes && searchData.bikes.length > 0) {
                html += `<h4>Препоръчени велосипеди:</h4>`;
                searchData.bikes.forEach((bike, index) => {
                    html += `<div style="background: #333; padding: 10px; margin: 8px 0; border-radius: 5px;">
                        <p><strong>${index + 1}. ${bike.name}</strong></p>
                        <p>Цена: ${bike.price}</p>
                        <p>Тип: ${bike.type}</p>
                        <p style="color: #ffb703;">${bike.reason}</p>
                    </div>`;
                });
            }

            if (searchData.custom_notes) {
                html += `<p><strong>Твои забележки:</strong> ${searchData.custom_notes}</p>`;
            }

            html += `<p style="margin-top: 15px; color: #888; font-size: 12px;">ID: ${searchData.id} | Дата: ${searchData.created_at}</p></div>`;

            document.getElementById(
                "recommendation"
            ).innerHTML = html;

        }

        catch (error) {

            document.getElementById(
                "recommendation"
            ).innerHTML =

                `<p class="error">Грешка: ${error.message}</p>`;
        }
    }
);