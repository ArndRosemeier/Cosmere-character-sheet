# How It Works - Single Source of Truth

## The Design

**One source of truth:** Rules are embedded in the HTML file.

**Separate files for editing:** The JSON file is just for convenient editing.

## Visual Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  YOU EDIT THIS                                              │
│  ═══════════════                                            │
│                                                             │
│  cosmere-rules.json  ← Edit this file with any text editor │
│  ═══════════════════                                        │
│  - Clean JSON format                                        │
│  - Easy to read and modify                                  │
│  - Version control friendly                                 │
│  - NOT loaded by the HTML!                                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ python sync_rules.py
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  SINGLE COMPILED FILE                                       │
│  ═════════════════════                                      │
│                                                             │
│  cosmere-character-sheet.html ← Double-click to use!       │
│  ═════════════════════════════                              │
│  - All rules embedded inside                                │
│  - Standalone, no dependencies                              │
│  - Share this single file with others                       │
│  - Works offline, no server needed                          │
└─────────────────────────────────────────────────────────────┘
```

## Think of It Like...

### Programming Analogy
```
source.cpp    →   compile   →   program.exe
cosmere-rules.json → sync_rules.py → cosmere-character-sheet.html
```

### Document Analogy
```
master.docx   →   "Save As PDF"   →   document.pdf
cosmere-rules.json → sync_rules.py → cosmere-character-sheet.html
```

## Why This Design?

### ✅ Advantages

1. **No confusion** - HTML only loads from one place (itself)
2. **No CORS errors** - Nothing tries to load external files
3. **Portable** - Share one HTML file, it just works
4. **Editable** - Keep rules in clean JSON for editing
5. **Version control** - Track changes to JSON separately
6. **Offline** - Works anywhere, no server needed

### ❌ What We Avoided

- Two sources of truth (confusing!)
- Fallback logic (complex!)
- CORS errors (annoying!)
- External dependencies (brittle!)
- Need for a server (inconvenient!)

## File Roles

| File | Role | Who Uses It |
|------|------|-------------|
| `cosmere-rules.json` | Source file for editing | YOU (human editor) |
| `sync_rules.py` | Compiler/sync script | YOU (when updating) |
| `cosmere-character-sheet.html` | Compiled application | EVERYONE (end users) |

## Daily Workflow

### 99% of the time:
```
Double-click cosmere-character-sheet.html
→ Play!
```

### When updating rules:
```
1. Edit cosmere-rules.json
2. Run: python sync_rules.py
3. Double-click cosmere-character-sheet.html
→ Play with updated rules!
```

## What You'll See (Normal Behavior)

When you double-click the HTML:
```
✅ Rules loaded: Object
✅ Loaded from localStorage
✅ Character sheet renders
```

You will NOT see:
- ❌ "Failed to load resource" (removed that code!)
- ❌ "CORS policy" errors (removed that code!)
- ❌ "External rules file" messages (removed that code!)

## Clean and Simple

- **One source of truth:** Embedded rules in HTML
- **One editing workflow:** JSON → sync → HTML
- **No external file loading:** Everything is self-contained
- **No confusion:** Clear separation of concerns

