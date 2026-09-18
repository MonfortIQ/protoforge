import os

filepath = 'g:/ProtoForge Studio/assets/js/main.js'

with open(filepath, 'a', encoding='utf-8') as f:
    f.write("""

// --- Global FormSubmit AJAX Interceptor ---
// Automatically intercepts any newsletter or generic form pointing to FormSubmit
// and converts it to a seamless background AJAX request with an inline success message.
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form[action^="https://formsubmit.co"]');
    
    forms.forEach(form => {
        // Skip the main contact form if it already has its own specific handler
        if (form.id === 'contactForm') return;
        
        form.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent page redirect
            
            const submitBtn = form.querySelector('button[type="submit"]');
            let originalBtnText = 'Submit';
            if (submitBtn) {
                originalBtnText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
                submitBtn.disabled = true;
            }

            const formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    form.reset();
                    // Create and show success message dynamically
                    let successMsg = form.parentNode.querySelector('.pf-ajax-success');
                    if (!successMsg) {
                        successMsg = document.createElement('div');
                        successMsg.className = 'alert alert-success mt-3 mb-0 p-2 rounded-3 border-0 bg-success bg-opacity-10 text-success pf-ajax-success small text-center';
                        successMsg.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i> Subscribed successfully!';
                        form.parentNode.appendChild(successMsg);
                    }
                    successMsg.classList.remove('d-none');
                    
                    // Hide message after 5 seconds
                    setTimeout(() => {
                        if(successMsg) successMsg.classList.add('d-none');
                    }, 5000);
                } else {
                    alert('Oops! There was a problem submitting your request.');
                }
            })
            .catch(error => {
                alert('Oops! There was a problem submitting your request.');
            })
            .finally(() => {
                if (submitBtn) {
                    submitBtn.innerHTML = originalBtnText;
                    submitBtn.disabled = false;
                }
            });
        });
    });
});
""")

print('SUCCESS')
