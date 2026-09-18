import os

filepath = 'g:/ProtoForge Studio/assets/js/auth.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the dynamicDashboardLink logic
old_logic = """            if (navList) {
                let existingDash = navList.querySelector('#dynamicDashboardLink');
                if (currentUser) {
                    if (!existingDash) {
                        const dashLi = document.createElement('li');
                        dashLi.className = 'nav-item';
                        dashLi.id = 'dynamicDashboardLink';
                        // User previously requested regular users go to index.html and admin to client-dashboard.html
                        const linkUrl = '/dashboard/client-dashboard.html';
                        dashLi.innerHTML = `<a class="nav-link fw-bold text-primary-pf" href="${linkUrl}">Dashboard</a>`;
                        navList.appendChild(dashLi);
                    }
                } else {
                    if (existingDash) existingDash.remove();
                }
            }"""

new_logic = """            if (navList) {
                let existingDash = navList.querySelector('#dynamicDashboardLink');
                // Always show the Dashboard link, even if logged out (it redirects to login automatically)
                if (!existingDash) {
                    const dashLi = document.createElement('li');
                    dashLi.className = 'nav-item';
                    dashLi.id = 'dynamicDashboardLink';
                    const linkUrl = '/dashboard/client-dashboard.html';
                    dashLi.innerHTML = `<a class="nav-link fw-bold text-primary-pf" href="${linkUrl}">Dashboard</a>`;
                    navList.appendChild(dashLi);
                }
            }"""

if old_logic in content:
    content = content.replace(old_logic, new_logic)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS")
else:
    print("Failed to find logic")
