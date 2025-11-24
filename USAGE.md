# Usage Guide - Single Source of Truth

## Quick Start

**Just double-click `cosmere-character-sheet.html` - it works immediately!**

No installation, no server, no setup required. Everything is embedded in the HTML file.

## How It Works

**Single Source of Truth:** All rules are embedded directly in the HTML file.

**Separate Files for Editing:** The `cosmere-rules.json` file exists ONLY for convenient editing and version control. It's not loaded by the HTML - it's a source file that gets compiled into the HTML.

## Updating Rules

Think of it like compiling source code:

```
cosmere-rules.json  →  [sync_rules.py]  →  cosmere-character-sheet.html
   (source file)         (compiler)           (compiled app)
```

### Step 1: Edit the Source
Edit `cosmere-rules.json` with any text editor:
- Add new talents
- Modify existing ones
- Update level progression
- Change game rules

### Step 2: Compile/Sync
Run the sync script:
```bash
python sync_rules.py
```

This embeds your changes into the HTML file.

### Step 3: Use the App
Double-click `cosmere-character-sheet.html` - your changes are now live!

## Why This Approach?

### ✅ Advantages
- **No server required** - Just double-click the HTML
- **Works offline** - No internet connection needed
- **Portable** - Share a single HTML file
- **Separate files** - Edit rules in clean JSON format
- **Version control** - Track changes to rules separately
- **Fast** - No server startup time

### 📁 File Organization

```
Cosmere/
├── cosmere-character-sheet.html  ← Use this (double-click)
├── cosmere-rules.json            ← Edit this
└── sync_rules.py                 ← Run this to sync
```

## Workflow Examples

### Example 1: Daily Use
```bash
# Just use it!
double-click cosmere-character-sheet.html
```

### Example 2: Adding New Talents
```bash
# 1. Edit the rules file
notepad cosmere-rules.json

# 2. Sync the changes
python sync_rules.py

# 3. Use the character sheet
double-click cosmere-character-sheet.html
```

### Example 3: Sharing With Friends
```bash
# Just send them the HTML file!
# Everything is embedded - they can use it immediately
```

## Advanced: Local Server (Optional)

If you're doing heavy development and want to avoid the sync step:

```bash
python run_server.py
```

This lets you edit `cosmere-rules.json` and see changes immediately by refreshing the browser.

**But for normal use, you don't need this!**

## Character Data Storage

Your characters are saved in your browser's local storage:
- Automatic saving after each change
- Persists between sessions
- Can export/import as files

## Features

- ✅ **140 Complete Talents**
- ✅ **6 Heroic Paths** with 18 specialties
- ✅ **Level 1-10 Progression**
- ✅ **Integrated Dice Roller**
- ✅ **Auto-calculating Stats**
- ✅ **Character Validation**
- ✅ **Beginner-Friendly UI**
- ✅ **Multi-pathing Support** (one level warrior, next level windrunner)
- ✅ **Talent Prerequisites** (automatic checking)

## Troubleshooting

### Q: Why do I see "Failed to load resource" errors?
**A:** Ignore them! Those are old messages from when the app tried to load external files. The app now only uses embedded rules - it works perfectly.

### Q: Do I need Python installed?
**A:** Only if you want to edit rules. For just using the character sheet, no Python needed!

### Q: Does the HTML load cosmere-rules.json?
**A:** No! The HTML only uses embedded rules. The `cosmere-rules.json` file is just for YOU to edit, then you compile/sync it into the HTML.

### Q: Can I use this on a tablet/phone?
**A:** Yes! Just open the HTML file in any modern browser.

### Q: Where are my characters saved?
**A:** In your browser's local storage. Use the Export button to save them as files for backup.

### Q: Can I share my custom rules?
**A:** Yes! Share your `cosmere-rules.json` file. Others can run `sync_rules.py` to compile it into their HTML.

### Q: What if I mess up the rules file?
**A:** Just restore from your last working version, or start fresh from the HTML's embedded rules.

## Summary

**For 99% of use cases:**
1. Double-click `cosmere-character-sheet.html`
2. Create and manage your characters
3. That's it!

**When updating rules:**
1. Edit `cosmere-rules.json`
2. Run `python sync_rules.py`
3. Double-click HTML file to use updated rules

**No server needed. No complex setup. Just works.**

