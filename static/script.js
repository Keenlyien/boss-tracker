async function loadBosses() {
    try {
        const response = await fetch("/api/bosses");
        const bosses = await response.json();

        const table = document.getElementById("boss-table");
        table.innerHTML = "";

        bosses.forEach(boss => {
            const row = document.createElement("tr");

            const name = document.createElement("td");
            name.textContent = boss.name;

            const status = document.createElement("td");
            status.textContent = boss.alive ? "AVAILABLE" : "DEAD";
            status.classList.add("status", boss.alive ? "available" : "dead");

            const respawn = document.createElement("td");
            respawn.textContent = boss.respawn;

            row.appendChild(name);
            row.appendChild(status);
            row.appendChild(respawn);

            table.appendChild(row);
        });

    } catch (error) {
        console.error("Failed to load bosses:", error);
    }
}

async function refreshBosses() {
    try {
        await fetch("/api/update");
        await loadBosses();
        alert("Boss timers updated!");
    } catch (error) {
        console.error("Update failed:", error);
    }
}

document.addEventListener("DOMContentLoaded", loadBosses);
