// assets/js/theme-rtl.js

function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("protoforge_theme", theme);
    updateThemeIcon(theme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    setTheme(newTheme);
}

function updateThemeIcon(theme) {
    const themeToggles = document.querySelectorAll('#themeToggle, #themeToggleDash');
    themeToggles.forEach(toggle => {
        if (theme === 'dark') {
            toggle.innerHTML = '<i class="bi bi-moon-fill theme-icon" style="transform: rotate(180deg); transition: 0.4s ease;"></i>';
        } else {
            toggle.innerHTML = '<i class="bi bi-sun-fill theme-icon" style="transform: rotate(0deg); transition: 0.4s ease;"></i>';
        }
    });
}

function setDirection(direction) {
    document.documentElement.setAttribute("dir", direction);
    localStorage.setItem("protoforge_direction", direction);
    updateDirectionIcon(direction);
    updateCharts(direction);
}

function toggleDirection() {
    const currentDirection = document.documentElement.getAttribute("dir");
    const newDirection = currentDirection === "rtl" ? "ltr" : "rtl";
    setDirection(newDirection);
}

function updateDirectionIcon(direction) {
    const rtlToggle = document.getElementById('rtlToggle');
    if (rtlToggle) {
        if (direction === 'rtl') {
            rtlToggle.innerHTML = '<span class="rtl-text fw-bold">LTR</span>';
        } else {
            rtlToggle.innerHTML = '<span class="ltr-text fw-bold">RTL</span>';
        }
    }
}

function updateCharts(direction) {
    if (typeof Chart !== 'undefined') {
        Chart.instances.forEach(chart => {
            chart.options.rtl = direction === 'rtl';
            chart.update();
        });
    }
}

// Initialize on load to ensure buttons match the pre-applied theme/dir from the <head> script
document.addEventListener('DOMContentLoaded', () => {
    const theme = document.documentElement.getAttribute("data-theme") || "light";
    const dir = document.documentElement.getAttribute("dir") || "ltr";
    
    updateThemeIcon(theme);
    updateDirectionIcon(dir);

    // Bind theme toggles
    const themeBtns = document.querySelectorAll('#themeToggle, #themeToggleDash');
    themeBtns.forEach(btn => {
        // Remove old listeners by replacing the element if necessary, 
        // but since we only add it here now, it's fine.
        const newBtn = btn.cloneNode(true);
        btn.parentNode.replaceChild(newBtn, btn);
        newBtn.addEventListener('click', toggleTheme);
    });

    // Bind RTL toggles
    const rtlBtn = document.getElementById('rtlToggle');
    if (rtlBtn) {
        const newRtlBtn = rtlBtn.cloneNode(true);
        rtlBtn.parentNode.replaceChild(newRtlBtn, rtlBtn);
        newRtlBtn.addEventListener('click', toggleDirection);
    }
});
