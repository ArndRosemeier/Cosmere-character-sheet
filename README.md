# Cosmere RPG Character Sheet

An intelligent, standalone character sheet application for the Cosmere RPG (Stormlight Archive) that works entirely in your browser.

**Current Version: 1.4** - Now with inline dice rolling! 🎲

**Latest Updates:**
- ✅ **NEW: Inline dice buttons** - Click 🎲 next to any skill, attribute, or defense to roll instantly!
- ✅ **Toast notifications** - Results pop up briefly, don't interrupt your workflow
- ✅ Fixed starting attributes (now correctly 12 points)
- ✅ Full-featured dice roller with Plot Die mechanic
- ✅ Real-time validation and beginner-friendly guidance
- ✅ Automatic calculations for all derived stats

## Features

### ✨ Core Functionality
- **Complete Character Management**: Create, edit, and delete multiple characters
- **Real-Time Validation**: Instant feedback showing exactly what's incomplete or incorrect
- **Automatic Calculations**: All derived stats (defenses, resources, modifiers) update instantly as you type
- **Point Tracking**: Visual trackers for attribute points and skill ranks with progress bars
- **Beginner-Friendly**: Clear error messages and recommendations guide you through character creation
- **Level Progression**: Built-in leveling system with automatic resource scaling
- **Persistent Storage**: Characters are automatically saved to browser localStorage
- **Import/Export**: Save character files to your filesystem and share them

### 🎲 Character Features
- **Attributes**: Six attributes (Strength, Speed, Intellect, Willpower, Awareness, Presence) - Start with 12 points
- **Skills**: All 18 core skills with automatic modifier calculation
- **Defenses**: Physical, Cognitive, and Spiritual defenses auto-calculated
- **Resources**: Health, Focus, Investiture (for Radiants), Deflect
- **Paths**: Choose from 6 Heroic Paths and 10 Radiant Orders
- **Expertises**: Track your character's specialized knowledge
- **Goals**: Purpose, Obstacle, and custom notes
- **Integrated Dice Roller**: Full-featured rolling system with Plot Die, skill rolls, and history

### 🔧 Technical Features
- **Modular Rules System**: All game rules are in a separate JSON file for easy updates
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Type Safety**: Strict data validation throughout
- **No Server Required**: Runs entirely in your browser
- **Print Ready**: Optimized layout for printing character sheets

## Getting Started

### Requirements
- A modern web browser (Chrome, Firefox, Edge, Safari)
- Just the file: `cosmere-character-sheet.html`
- Optional: `cosmere-rules.json` (for easy rule updates)

### Quick Start

1. **Open the Character Sheet**
   - Double-click `cosmere-character-sheet.html`
   - Or right-click and select "Open with" your preferred browser
   - That's it! The rules are embedded in the HTML file

2. **Create Your First Character**
   - Click "✨ New Character"
   - Enter your character's name
   - Set attributes (you start with 10 points distributed)
   - Choose your ancestry and culture
   - Select a Heroic Path
   - Optionally select a Radiant Order if you're playing a Knight Radiant

3. **Save Your Work**
   - Characters are auto-saved to localStorage
   - Use "📥 Export" to save a character file to disk
   - Use "📤 Import" to load a character file

## Using the Character Sheet

### Basic Information
- **Character Name**: Your character's name
- **Player Name**: Your name
- **Level**: Current character level (1-10)
- **Ancestry**: Human, Singer, Horneater, Herdazian
- **Culture**: Alethi, Veden, Thaylen, Azish, Shin, etc.

### Attributes
Set your six core attributes (0-5). These affect:
- **Strength**: Physical power, Athletics skill
- **Speed**: Quickness, Agility skill, Movement
- **Intellect**: Intelligence, number of Expertises
- **Willpower**: Mental fortitude, Discipline
- **Awareness**: Perception, Senses range
- **Presence**: Charisma, Leadership

### Skills
Each skill has:
- **Rank**: 0-5, representing your training
- **Modifier**: Automatically calculated (Attribute + Rank)

Skills are organized into three categories matching the three Realms:
- **Physical**: Agility, Athletics, Heavy Weapons, Light Weapons, Stealth, Thievery
- **Cognitive**: Crafting, Deduction, Discipline, Intimidation, Lore, Medicine
- **Spiritual**: Deception, Insight, Leadership, Perception, Persuasion, Survival

### Resources
Automatically calculated based on level:
- **Health**: 10 + (Level × 6)
- **Focus**: 5 + (Level × 3)
- **Investiture**: 3 + (Level × 1) - Only for Radiants
- **Deflect**: Set manually (from armor/abilities)
- **Recovery Die**: Improves at levels 3, 5, and 7
- **Movement**: 30 + (Speed × 5) feet
- **Senses Range**: 60 + (Awareness × 10) feet
- **Lifting Capacity**: 100 + (Strength × 50) lbs

### Leveling Up
1. Click "⬆️ Level Up" when you're ready to advance
2. The system shows you what you gain:
   - Talent Points
   - Skill Rank Increases
   - Attribute Increases (at levels 3, 5, 7, 9)
3. Update your attributes and skills accordingly

### Heroic Paths
Choose one of six paths that defines your character's role:
- **Agent**: Stealthy infiltrator
- **Envoy**: Diplomatic specialist
- **Hunter**: Tracker and wilderness expert
- **Leader**: Inspiring commander
- **Scholar**: Knowledgeable expert
- **Warrior**: Combat specialist

### Radiant Orders
If you're bonded to a spren, select your Order:
- **Windrunner**: Adhesion + Gravitation
- **Skybreaker**: Gravitation + Division
- **Dustbringer**: Division + Abrasion
- **Edgedancer**: Abrasion + Progression
- **Truthwatcher**: Progression + Illumination
- **Lightweaver**: Illumination + Transformation
- **Elsecaller**: Transformation + Transportation
- **Willshaper**: Transportation + Cohesion
- **Stoneward**: Cohesion + Tension
- **Bondsmith**: Tension + Adhesion

### Expertises
Add areas of specialized knowledge:
- Click "+ Add Expertise"
- Enter the expertise name (e.g., "Alethi Military History", "Fabrial Engineering")
- Click the × to remove an expertise

## Updating Rules

### How Rules Loading Works

The application has **embedded rules** built into the HTML file, so it works immediately without any external files. However, it also supports loading rules from an external `cosmere-rules.json` file for easy updates.

**Loading Priority:**
1. First tries to load `cosmere-rules.json` (if available)
2. Falls back to embedded rules (if external file not found)

This means:
- ✅ Works standalone - just open the HTML file
- ✅ Easy to update - create/edit `cosmere-rules.json` when needed
- ✅ No server required - works from file:// protocol

### Updating When New Rules Release

**Option 1: Keep Using Embedded Rules** (Easiest)
- Download the updated HTML file when new versions are released
- Your characters are stored separately in localStorage

**Option 2: Use External Rules File** (Most Flexible)
1. Create or edit `cosmere-rules.json` in the same folder
2. Update the relevant sections (skills, paths, surges, etc.)
3. Click "🔄 Reload Rules" in the application
4. All characters will use the updated rules

**Note:** If you're using a web server (not just opening the file), the external JSON file will always be used if present.

### Rules File Structure
The JSON file contains:
- `attributes`: List of all attributes
- `skills`: List of all skills with their attributes
- `defenses`: Defense calculation rules
- `resources`: Health, Focus, Investiture formulas
- `heroicPaths`: All Heroic Paths
- `radiantOrders`: All Radiant Orders with Surges
- `surges`: Surge descriptions
- `advancement`: Level progression table
- `conditions`: Status conditions
- `difficultyClasses`: Standard DCs

## Storage

### Local Storage
- Characters are automatically saved to your browser's localStorage
- Survives browser restarts
- Tied to the specific browser on the specific computer
- No account required

### File Export/Import
- Export individual characters to JSON files
- Files are human-readable and can be edited
- Share character files with other players
- Import creates a copy (doesn't overwrite)

## Browser Compatibility

Tested and working on:
- ✅ Google Chrome 90+
- ✅ Mozilla Firefox 88+
- ✅ Microsoft Edge 90+
- ✅ Safari 14+

## Tips & Tricks

### Quick Character Creation
1. Use default attributes (all 2s) to start quickly
2. Adjust as you learn your character concept
3. Remember: most NPCs have attributes of 2

### Tracking Combat
- Use Current Health/Focus/Investiture fields during play
- Update after rests to restore resources
- Deflect reduces incoming damage

### Multiple Characters
- Create separate characters for different campaigns
- Click any character in the list to switch
- Each character is completely independent

### Backup Your Characters
- Periodically export important characters
- Store the JSON files somewhere safe
- Consider version control if making major changes

### Printing
- Use your browser's Print function (Ctrl+P or Cmd+P)
- The sheet is optimized for printing
- Print preview shows what will be included

### Using the Dice Roller

The sheet includes **TWO** integrated dice rolling systems:

#### 1. Inline Dice Rolling (Fastest!)
**New in v1.4:** Click 🎲 icons directly on your character sheet!

- **Skills**: Every skill has a dice button → Rolls 1d20 + modifier
- **Attributes**: Click 🎲 next to any attribute → Rolls attribute test
- **Defenses**: Quick rolls for defense checks
- **Recovery Die**: Dedicated "Roll" button → Rolls your recovery die

**Toast Notifications:**
- Results pop up in top-right corner
- Auto-dismiss after 3 seconds
- Doesn't interrupt your workflow
- Still saves to roll history

**Perfect for quick skill checks during play!**

#### 2. Full Dice Roller
**Access:**
- Click the floating 🎲 button (bottom-right)
- Press **D** key (keyboard shortcut)

**Features:**
- Quick roll buttons (d4, d6, d8, d10, d12, d20)
- **Plot Die mechanic** - Roll with advantage/disadvantage
- **Skill quick rolls** - One-click rolls with your character's modifiers
- **Custom notation** - Enter any dice formula (2d6+5, 3d8-2, etc.)
- **Roll history** - Last 20 rolls saved with timestamps
- **Result breakdown** - See exactly what you rolled

**Plot Die:**
- Roll 1d6 alongside your d20
- **6** = Opportunity (advantage - keep higher of 2d20)
- **1** = Complication (disadvantage - keep lower of 2d20)
- **2-5** = Normal roll

**Use for complex rolls, Plot Die, and custom formulas!**

## Troubleshooting

### Characters Not Saving
- Check if your browser allows localStorage
- Try in a different browser
- Export characters as backup

### Rules Not Loading
- **Don't worry!** The rules are embedded in the HTML file
- The app will work even without `cosmere-rules.json`
- External file is only needed if you want to customize rules
- Check browser console (F12) to see which rules source is being used

### Import Not Working
- Ensure the file is valid JSON
- Check that it's a character export (not rules)
- Try exporting a test character first

## Future Enhancements

Potential additions based on new content:
- Talent tree tracking
- Equipment inventory management
- Spell/Surge power tracking
- Combat tracker
- Party management
- Dice roller integration

## Contributing

To add new content:
1. Edit `cosmere-rules.json` for new rules
2. Edit the HTML file for new UI features
3. Maintain the separation of rules and presentation

## License & Credits

This is a fan-made tool for the Cosmere RPG.
- Cosmere RPG © Brotherwise Games & Dragonsteel Entertainment
- The Stormlight Archive® by Brandon Sanderson
- This character sheet tool is provided for personal use

## Version

Version 1.0 - Compatible with Stormlight Handbook v1.01

---

**Life before death. Strength before weakness. Journey before destination.**

