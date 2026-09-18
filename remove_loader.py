import os
import glob

workspace = "g:/ProtoForge Studio"
html_files = glob.glob(os.path.join(workspace, "**/*.html"), recursive=True)

removed_count = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    skip_mode = False
    div_depth = 0
    
    for line in lines:
        if '<!-- Loading Screen -->' in line:
            skip_mode = True
            div_depth = 0
            
        if skip_mode:
            # Count opening and closing divs to find the end of the loading screen block
            # This is a simple heuristic, but it works well since the block starts with <div id="loading-screen">
            if '<div' in line:
                div_depth += line.count('<div')
            if '</div' in line:
                div_depth -= line.count('</div')
                
            # If we've closed all the divs we opened inside the block, stop skipping
            # Wait, the first line is <!-- Loading Screen -->. The NEXT line is <div...
            # So div_depth is 0 on the first line. We need to wait until it goes > 0 and then back to 0.
            if div_depth == 0 and '<div' not in line and '</div' in line:
                # This logic is a bit flawed. Let's just use string matching for the exact start/end
                pass
                
    # Better approach: read full text, use regex
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    import re
    # Find <!-- Loading Screen --> and everything until the end of that block
    # We know the block has exactly:
    # <div id="loading-screen" class="loading-screen">
    # ...
    # </div> (the matching one)
    # Since it's identical or nearly identical in all files, let's use a regex that grabs it.
    
    pattern = re.compile(r'\s*<!-- Loading Screen -->[\s\S]*?<div id="loading-screen" class="loading-screen">[\s\S]*?<div class="progress-bar-loading"></div>\s*</div>\s*</div>\s*</div>\s*', re.IGNORECASE)
    
    if pattern.search(content):
        new_content = pattern.sub('\n', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        removed_count += 1

print(f"Removed loading screen from {removed_count} files.")
