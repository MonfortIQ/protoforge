import os
import re

def fix_feedback(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add has-validation to input-group classes
    # Wait, in this codebase, input-group contains an eye icon which is absolute positioned anyway?
    # No, the eye icon is positioned absolutely: <span class="input-group-text ... position-absolute end-0 top-0 bottom-0 z-3">
    # If the eye icon is absolute, then the input-group isn't really acting like a flex container for the eye icon.
    # The input-group is just a container.
    # Let's change `<div class="input-group">` to `<div class="input-group has-validation">` for the passwords.
    
    # We can just remove the style="position: absolute; top: 100%;" from invalid-feedback elements.
    content = content.replace('style="position: absolute; top: 100%;"', '')
    
    # Also we should add `has-validation` to `<div class="input-group">` containing password inputs.
    content = content.replace('<div class="input-group position-relative">', '<div class="input-group has-validation position-relative">')
    content = content.replace('<div class="input-group">', '<div class="input-group has-validation">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


fix_feedback('g:/ProtoForge Studio/register.html')
fix_feedback('g:/ProtoForge Studio/login.html')

print('SUCCESS')
