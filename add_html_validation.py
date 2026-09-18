import os
import re

def add_validation(filepath, form_id, is_register):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if is_register:
        # Register form replacements
        # Form tag
        content = content.replace('<form id="registerForm">', '<form id="registerForm" class="needs-validation" novalidate>')
        
        # Name
        old_name = '<input type="text" class="form-control pf-input" id="name" placeholder="John Doe" required>'
        new_name = '<input type="text" class="form-control pf-input" id="name" placeholder="John Doe" required minlength="3">\n                                    <div class="invalid-feedback">Please enter your full name (at least 3 characters).</div>'
        content = content.replace(old_name, new_name)
        
        # Email
        old_email = '<input type="email" class="form-control pf-input" id="email" placeholder="name@company.com" required>'
        new_email = '<input type="email" class="form-control pf-input" id="email" placeholder="name@company.com" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$">\n                                    <div class="invalid-feedback">Please enter a valid email address.</div>'
        content = content.replace(old_email, new_email)
        
        # Password
        old_pass = '<input type="password" id="password" class="form-control pf-input border-end-0" required placeholder="••••••••">'
        new_pass = '<input type="password" id="password" class="form-control pf-input border-end-0" required minlength="8" placeholder="••••••••">\n                                            <div class="invalid-feedback mt-2" style="position: absolute; top: 100%;">Password must be at least 8 characters.</div>'
        content = content.replace(old_pass, new_pass)
        
        # Confirm Password
        old_conf = '<input type="password" id="confirmPassword" class="form-control pf-input border-end-0" required placeholder="••••••••">'
        new_conf = '<input type="password" id="confirmPassword" class="form-control pf-input border-end-0" required placeholder="••••••••">\n                                            <div class="invalid-feedback mt-2" id="confirmPassFeedback" style="position: absolute; top: 100%;">Passwords do not match.</div>'
        content = content.replace(old_conf, new_conf)

        # Terms
        old_terms = '<input type="checkbox" class="form-check-input" id="terms" required>'
        new_terms = '<input type="checkbox" class="form-check-input" id="terms" required>\n                                    <div class="invalid-feedback">You must agree before submitting.</div>'
        content = content.replace(old_terms, new_terms)

    else:
        # Login form replacements
        # Form tag
        content = content.replace('<form id="loginForm">', '<form id="loginForm" class="needs-validation" novalidate>')
        
        # Email
        old_email = '<input type="email" class="form-control pf-input" id="email" placeholder="name@company.com" required>'
        new_email = '<input type="email" class="form-control pf-input" id="email" placeholder="name@company.com" required pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,}$">\n                                    <div class="invalid-feedback">Please enter a valid email address.</div>'
        content = content.replace(old_email, new_email)
        
        # Password
        old_pass = '<input type="password" class="form-control pf-input border-end-0" id="password" placeholder="••••••••" required>'
        new_pass = '<input type="password" class="form-control pf-input border-end-0" id="password" placeholder="••••••••" required>\n                                        <div class="invalid-feedback mt-2" style="position: absolute; top: 100%;">Please enter your password.</div>'
        content = content.replace(old_pass, new_pass)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


add_validation('g:/ProtoForge Studio/register.html', 'registerForm', True)
add_validation('g:/ProtoForge Studio/login.html', 'loginForm', False)

print('SUCCESS')
