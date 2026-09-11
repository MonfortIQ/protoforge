import os
from bs4 import BeautifulSoup

base_dir = 'g:/ProtoForge Studio'

def fix_blog_cards(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the wrapping div for the author/date
    old_class = "d-flex justify-content-between align-items-center mb-3"
    new_class = "d-flex flex-column flex-sm-row justify-content-between align-items-start align-items-sm-center gap-1 mb-3"
    
    content = content.replace(f'class="{old_class}"', f'class="{new_class}"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {os.path.basename(filepath)}")

fix_blog_cards(os.path.join(base_dir, 'blog.html'))
fix_blog_cards(os.path.join(base_dir, 'blog2.html'))

os.remove(__file__)
print("SUCCESS")
