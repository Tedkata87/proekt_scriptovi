const token =
    localStorage.getItem(
        "token"
    );

if (!token) {

    window.location.href =
        "login.html";
}


document
    .getElementById(
        "logoutBtn"
    )
    .addEventListener(
        "click",
        () => {

            localStorage.removeItem(
                "token"
            );

            window.location.href =
                "index.html";
        }
    );


loadSearches();

loadSetups();


async function loadSearches() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/bike-searches",
                {
                    headers: {
                        Authorization:
                            `Bearer ${token}`
                    }
                }
            );

        const data =
            await response.json();

        let html = "";

        data.forEach(search => {

            html += `
            <div class="history-item">

                <p>
                    Terrain:
                    ${search.terrain}
                </p>

                <p>
                    Budget:
                    ${search.budget}€
                </p>

            </div>
            `;
        });

        document.getElementById(
            "searchesList"
        ).innerHTML = html;
    }

    catch {

        document.getElementById(
            "searchesList"
        ).innerHTML =
            "Error loading searches";
    }
}


async function loadSetups() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:5000/bike-setups",
                {
                    headers: {
                        Authorization:
                            `Bearer ${token}`
                    }
                }
            );

        const data =
            await response.json();

        let html = "";

        data.forEach(setup => {

            html += `
            <div class="history-item">

                <p>
                    ${setup.brand}
                </p>

                <p>
                    ${setup.model}
                </p>

            </div>
            `;
        });

        document.getElementById(
            "setupsList"
        ).innerHTML = html;
    }

    catch {

        document.getElementById(
            "setupsList"
        ).innerHTML =
            "Error loading setups";
    }
}