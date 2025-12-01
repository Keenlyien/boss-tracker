async function loadBosses() {
    const res = await fetch("/api/bosses");
    const data = await res.json();
    const bosses = data.bosses;

    const tableBody = document.getElementById("boss-table-body");
    tableBody.innerHTML = ""; // clear previous rows

    bosses.forEach(boss => {
        const row = document.createElement("tr");

        const status = boss.last_killed
            ? "Dead (killed at " + new Date(boss.last_killed).toLocaleString() + ")"
            : "Alive";

        row.innerHTML = `
            <td>${boss.name}</td>
            <td>${boss.level}</td>
            <td>${boss.location}</td>
            <td>${boss.respawn}</td>
            <td class="${boss.last_killed ? 'status dead' : 'status available'}">${status}</td>
            <td><button onclick="markDead('${boss.name}')">Mark Dead</button></td>
        `;

        tableBody.appendChild(row);
    });
}

async function markDead(name) {
    await fetch(`/api/update?boss=${encodeURIComponent(name)}`);
    alert(name + " marked dead!");
    loadBosses(); // refresh table without reloading page
}

// Load bosses on page load
loadBosses();
