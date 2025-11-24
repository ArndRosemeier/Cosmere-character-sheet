# Local Server Guide - Keep Files Separate

## The Problem

When opening `cosmere-character-sheet.html` directly from the filesystem (`file://` protocol), browsers block loading external files like `cosmere-rules.json` due to CORS (Cross-Origin Resource Sharing) security restrictions.

## The Solution

Run a simple local web server! This allows the HTML to load the external JSON file properly while keeping files separate.

## Quick Start

### Option 1: Python Server (Recommended)

1. **Run the server:**
   ```bash
   python run_server.py
   ```

2. **Your browser will open automatically** to:
   ```
   http://localhost:8000/cosmere-character-sheet.html
   ```

3. **The character sheet will now load `cosmere-rules.json` from the external file!**

4. **To stop the server:** Press `Ctrl+C` in the terminal

### Option 2: Python Built-in Server

If you prefer the standard Python HTTP server:

```bash
python -m http.server 8000
```

Then manually open: http://localhost:8000/cosmere-character-sheet.html

### Option 3: Node.js (if you have it)

```bash
npx http-server -p 8000 -c-1
```

Then open: http://localhost:8000/cosmere-character-sheet.html

## Benefits of Using the Server

✅ **External Rules File**: The app will load `cosmere-rules.json` from the external file  
✅ **Easy Updates**: Just edit `cosmere-rules.json` and refresh the browser  
✅ **Fallback**: If the server isn't running, the app uses embedded rules automatically  
✅ **No Installation**: Python is already installed on most systems  

## How It Works

The `run_server.py` script:
1. Starts a local web server on port 8000
2. Serves files from the current directory
3. Adds CORS headers to allow cross-origin requests
4. Opens your default browser automatically

## Benefits of External Rules File

When you update `cosmere-rules.json`:
- **Version Control**: Easy to track changes to rules
- **File Size**: HTML file stays smaller
- **Maintainability**: Separate concerns (presentation vs data)
- **Sharing**: Can share just the rules file for updates

## Note: Embedded Rules Still Work

Even without the server, the character sheet will work! It has all 140 talents embedded as a fallback. The external file is just for convenience when editing rules.

## Troubleshooting

### Port Already in Use
If port 8000 is taken, edit `run_server.py` and change:
```python
PORT = 8000  # Change to 8001, 8080, etc.
```

### Browser Doesn't Open
Manually open: http://localhost:8000/cosmere-character-sheet.html

### Server Won't Start
Make sure you're in the correct directory:
```bash
cd "G:\Meine Ablage\Projekte\Cosmere"
python run_server.py
```

## Development Workflow

**For casual use:**
- Just double-click `cosmere-character-sheet.html`
- Uses embedded rules (works offline)

**For editing rules:**
1. Run `python run_server.py`
2. Edit `cosmere-rules.json`
3. Refresh browser to see changes
4. When done, press `Ctrl+C` to stop server

**For deploying updates:**
1. Edit `cosmere-rules.json` with new talents/rules
2. Run `python update_embedded.py` to update the HTML
3. Now both external and embedded rules are in sync

