// auth.js

document.addEventListener('DOMContentLoaded', () => {
    updateAuthUI();

    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match!');
                return;
            }

            const users = JSON.parse(localStorage.getItem('protoforge_users')) || [];
            if (users.find(u => u.email === email)) {
                alert('Email already registered!');
                return;
            }

            const newUser = { name, email, password, id: Date.now() };
            users.push(newUser);
            localStorage.setItem('protoforge_users', JSON.stringify(users));
            localStorage.setItem('protoforge_current_user', JSON.stringify(newUser));
            
            alert('Registration successful! Redirecting to dashboard...');
            window.location.href = '/dashboard/client-dashboard.html';
        });
    }

    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const users = JSON.parse(localStorage.getItem('protoforge_users')) || [];
            const user = users.find(u => u.email === email && u.password === password);

            if (user) {
                localStorage.setItem('protoforge_current_user', JSON.stringify(user));
                window.location.href = '/dashboard/client-dashboard.html';
            } else {
                alert('Invalid email or password.');
            }
        });
    }
});

function logout() {
    localStorage.removeItem('protoforge_current_user');
    window.location.href = '/index.html';
}

function updateAuthUI() {
    const containers = document.querySelectorAll('.auth-buttons-container');
    const currentUser = JSON.parse(localStorage.getItem('protoforge_current_user'));

    containers.forEach(container => {
        let authLinks = '';
        if (currentUser) {
            authLinks = `
                <a href="/dashboard/client-dashboard.html" class="btn pf-btn-secondary text-nowrap flex-shrink-0" style="padding: 0.5rem 1.5rem;">Dashboard</a>
                <button onclick="logout()" class="btn pf-btn-primary text-nowrap flex-shrink-0" style="padding: 0.5rem 1.5rem;">Logout</button>
            `;
        } else {
            authLinks = `
                <a href="/login.html" class="btn pf-btn-secondary text-nowrap flex-shrink-0 me-2 pf-hover-lift" style="padding: 0.5rem 1.5rem;">Login</a>
                <a href="/register.html" class="btn pf-btn-primary text-nowrap flex-shrink-0 pf-hover-lift" style="padding: 0.5rem 1.5rem;">Sign Up</a>
            `;
        }
        
        const toggles = `
            <div class="d-flex align-items-center gap-3 me-3 border-end pe-3 border-secondary-subtle">
                <button id="themeToggle" class="clay-icon-btn pf-hover-lift m-0" aria-label="Toggle Theme">
                    <i class="bi bi-moon-fill"></i>
                </button>
                <button id="rtlToggle" class="clay-pill-btn pf-hover-lift m-0" style="font-size: 0.8rem;" aria-label="Toggle RTL">
                    RTL
                </button>
            </div>
        `;
        
        container.innerHTML = toggles + authLinks;
    });

    // Protect dashboard routes
    if (window.location.pathname.includes('/dashboard/') && !currentUser) {
        window.location.href = '/login.html';
    }
}
