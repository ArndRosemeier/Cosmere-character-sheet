"""
Sync Rules - Updates embedded rules in HTML from external JSON file

This allows you to:
1. Edit cosmere-rules.json (keep files separate for version control)
2. Run this script to sync changes into the HTML
3. Use the HTML normally (no server needed!)

Usage: python sync_rules.py
"""

import json
import os

def sync_rules():
    # Check if files exist
    if not os.path.exists('cosmere-rules.json'):
        print("[ERROR] cosmere-rules.json not found")
        return False
    
    if not os.path.exists('cosmere-character-sheet.html'):
        print("[ERROR] cosmere-character-sheet.html not found")
        return False
    
    # Read the rules
    print("[INFO] Reading cosmere-rules.json...")
    with open('cosmere-rules.json', 'r', encoding='utf-8') as f:
        rules = json.load(f)
    
    # Validate rules
    if 'version' not in rules:
        print("[ERROR] Invalid rules file (missing version)")
        return False
    
    # Minify the JSON
    print("[INFO] Minifying JSON...")
    minified_rules = json.dumps(rules, separators=(',', ':'))
    
    # Read the HTML file
    print("[INFO] Reading HTML file...")
    with open('cosmere-character-sheet.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Find and replace the embedded rules
    lines = html_content.split('\n')
    updated = False
    
    for i, line in enumerate(lines):
        if 'const COSMERE_RULES = ' in line and not line.strip().startswith('//'):
            old_line = line
            lines[i] = f'        const COSMERE_RULES = {minified_rules};'
            updated = True
            print(f"[INFO] Updated line {i+1}")
            break
    
    if not updated:
        print("[ERROR] Could not find COSMERE_RULES in HTML")
        return False
    
    # Write the updated HTML
    print("[INFO] Writing updated HTML...")
    with open('cosmere-character-sheet.html', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    # Summary
    print("")
    print("[SUCCESS] Rules synced successfully!")
    print(f"  Version: {rules['version']}")
    print(f"  Heroic Paths: {len(rules['heroicPaths'])}")
    print(f"  Total Talents: {sum(len(spec['talents']) for path in rules['heroicPaths'] for spec in path['specialties'])}")
    if 'advancement' in rules:
        print(f"  Levels: {len(rules['advancement']['levelProgression'])}")
    print("")
    print("[INFO] You can now use cosmere-character-sheet.html")
    print("[INFO] No server needed - just double-click the HTML file!")
    
    return True

if __name__ == "__main__":
    print("")
    print("="*60)
    print(" COSMERE RPG - SYNC RULES TO HTML")
    print("="*60)
    print("")
    
    success = sync_rules()
    
    if not success:
        print("")
        print("[ERROR] Sync failed!")
        exit(1)

