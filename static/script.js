async function checkAuth() {
    const res = await fetch("/api/check_auth");
    const data = await res.json();
    if (!data.authenticated) {
        // redirect to login page
        window.location.href = "/login.html";
        return false;
    }
    return true;
}

async function loadBosses() {
    const ok = await checkAuth();
    if (!ok) return;
    const res = await fetch("/api/bosses");
    const data = await res.json();
    const bosses = data.bosses || [];

    const tableBody = document.getElementById("boss-table-body");
    tableBody.innerHTML = ""; // clear previous rows

    bosses.forEach(boss => {
        const row = document.createElement("tr");

        const status = boss.last_killed
            ? "Dead (killed at " + new Date(boss.last_killed).toLocaleString() + ")"
            : "Alive";

        row.innerHTML = `
            <td>${boss.name}</td>
            <td>${boss.location || ''}</td>
            <td>${boss.respawn || boss.respawn_minutes || ''}</td>
            <td>${status}</td>
            <td>
                <button onclick="markDead('${boss.name}')">Kill Now</button>
                <button onclick="openTimeModal('${boss.name}')">Set Kill Time</button>
            </td>
        `;

        tableBody.appendChild(row);
    });
}

async function markDead(name) {
    await fetch(`/api/update?boss=${encodeURIComponent(name)}`);
    loadBosses(); // refresh table without reloading page
}

function openTimeModal(name) {
    document.getElementById("modal-boss-name").textContent = name;
    document.getElementById("kill-datetime").value = "";
    document.getElementById("time-modal").style.display = "flex";

    document.getElementById("save-kill-time").onclick = async function() {
        const isoLocal = document.getElementById("kill-datetime").value;
        if (!isoLocal) { alert("Pick a date/time"); return; }
        // convert local datetime-local value to ISO (browser gives local)
        const dt = new Date(isoLocal);
        const iso = dt.toISOString();
        const name = document.getElementById("modal-boss-name").textContent;
        const res = await fetch("/api/set_kill_time", {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({name: name, killed_at: iso})
        });
        if (res.ok) {
            document.getElementById("time-modal").style.display = "none";
            loadBosses();
        } else {
            const text = await res.text();
            alert("Error: " + text);
        }
    };

    document.getElementById("cancel-kill-time").onclick = function() {
        document.getElementById("time-modal").style.display = "none";
    };
}

// Logout link
document.addEventListener("DOMContentLoaded", function() {
    const logout = document.getElementById("logout-link");
    if (logout) {
        logout.addEventListener("click", async function(e) {
            e.preventDefault();
            await fetch("/api/logout");
            window.location.href = "/login.html";
        });
    }
    loadBosses();
});
