# Changelog

## Version 1.4 - Inline Dice Rolling

### Added
- **🎲 Inline Dice Buttons**: Dice icons next to every rollable value
  - Skills: Click 🎲 next to any skill to roll that test
  - Attributes: Roll attribute tests directly from character sheet
  - Defenses: Quick rolls for defense checks
  - Recovery Die: Dedicated "Roll" button for recovery
  - Toast Notifications: Results pop up briefly in corner, don't interrupt workflow
  
### Improved
- **Integrated Rolling**: No need to open full dice roller for quick rolls
- **Context-Aware**: Each dice button knows exactly what to roll
- **Non-Intrusive**: Toast notifications auto-dismiss after 3 seconds
- **History Tracking**: Inline rolls still save to history
- **Tooltips**: Hover over dice buttons to see what they'll roll

### User Experience
- Roll directly from character sheet
- Results appear as toast notifications (top-right)
- Can still use full dice roller (🎲 FAB button) for complex rolls
- Inline buttons are subtle but discoverable
- Mobile-optimized button sizes

---

## Version 1.3 - Dice Roller & Attribute Fix

### Fixed
- **Starting Attributes**: Corrected from 10 to 12 points (all attributes start at 2, which equals 12 total)
- **Validation Messages**: Now correctly show 12 as the starting total

### Added
- **🎲 Integrated Dice Roller**: Full-featured dice rolling system
  - Floating dice button (bottom-right corner)
  - Quick roll buttons: d4, d6, d8, d10, d12, d20
  - Plot Die mechanic with advantage/disadvantage
  - Custom dice notation (e.g., 2d6+5, 3d8-2)
  - Quick skill rolls with automatic modifiers
  - Roll history (last 20 rolls)
  - Keyboard shortcut: Press 'D' to open roller
  
### Dice Roller Features
- **Quick Rolls**: One-click rolling for common dice
- **Plot Die**: Roll d20 with Plot Die (shows Opportunity/Complication)
- **Custom Notation**: Supports XdY+Z format (e.g., 2d6+3, 1d20-1)
- **Skill Integration**: Automatically shows your character's skills with modifiers
- **Result Display**: Large, clear result with breakdown
- **History Tracking**: Keeps last 20 rolls with timestamps
- **Responsive**: Works on mobile and desktop

---

## Version 1.2 - Beginner-Friendly Validation

### Added
- **Real-time Validation**: Character sheet now validates all inputs and shows clear error/warning messages
- **Attribute Point Tracker**: Shows used/total/remaining attribute points with visual progress bar
- **Skill Rank Tracker**: Shows used/total/remaining skill ranks with visual progress bar
- **Character Complete Badge**: Visual indicator showing if character is complete or has issues
- **Validation Summary**: Clear messages showing exactly what needs to be fixed
- **Automatic Calculations**: All derived values (defenses, resources, etc.) update instantly when attributes change
- **Helpful Tooltips**: Skill descriptions appear on hover, modifiers show calculation breakdown
- **Point Enforcement**: System prevents allocating too many points or exceeding maximums
- **Beginner Guide**: Comprehensive guide explaining validation and character creation

### Improved
- **Input Responsiveness**: Changed from `onchange` to `oninput` for instant updates
- **Visual Feedback**: Color-coded progress bars (red=over, green=complete, gray=incomplete)
- **Error Messages**: Specific, actionable error messages instead of silent failures
- **Skill Display**: Added tooltips showing attribute + rank calculation for each skill

### Fixed
- **Attribute Changes**: Now properly trigger recalculation of all derived values
- **Defense Updates**: Physical/Cognitive/Spiritual defenses update immediately
- **Resource Scaling**: Health, Focus, Investiture properly scale with level changes
- **Skill Modifiers**: Update immediately when attributes or ranks change

### New Validation Checks
- ✅ Character name not empty or "New Character"
- ✅ Attribute points exactly match available (no over/under spending)
- ✅ No attribute exceeds maximum (5)
- ✅ Skill ranks exactly match available (based on level)
- ✅ No skill exceeds maximum (5 ranks)
- ✅ Heroic Path selected (required)
- ⚠️ Purpose recommended (optional)
- ⚠️ Obstacle recommended (optional)

### User Experience
- Point trackers show at-a-glance completion status
- Progress bars provide visual feedback
- Validation messages update in real-time
- Clear distinction between errors (must fix) and recommendations (optional)
- Help text added to major sections explaining requirements

---

## Version 1.1 - Fixed File Loading

### Fixed
- **Browser Security Issue**: Embedded rules directly into the HTML file to fix the "Error loading rules file" issue
- The application now works immediately when opening the HTML file from the filesystem
- No longer requires cosmere-rules.json to function (but still supports it for updates)

### How It Works Now
1. **Embedded Rules**: All rules are now built into the HTML file
2. **External File Support**: Still tries to load `cosmere-rules.json` if available
3. **Automatic Fallback**: Uses embedded rules if external file can't be loaded

### Benefits
- ✅ **True Standalone**: Single HTML file works anywhere
- ✅ **No Setup Required**: Just open the file and start creating characters
- ✅ **Still Updatable**: Place `cosmere-rules.json` in the same folder to override rules
- ✅ **Browser Compatible**: Works with file:// protocol (no server needed)

### Technical Details
The issue was caused by browser CORS (Cross-Origin Resource Sharing) restrictions. When opening HTML files directly from the filesystem (file:// protocol), browsers block fetch() requests to other local files for security reasons.

**Solution**: Embedded the entire rules database as a JavaScript constant in the HTML file, with fallback logic that:
1. Attempts to load external file (works when using a web server)
2. Falls back to embedded data (works when opening directly)

This maintains the modular design while ensuring the application always works.

---

## Version 1.0 - Initial Release

### Features
- Complete character sheet for Cosmere RPG (Stormlight Archive)
- All 6 attributes, 18 skills, 3 defenses
- 6 Heroic Paths and 10 Radiant Orders
- Automatic calculation of all derived stats
- Level progression (1-10) with automatic resource scaling
- Multiple character management
- localStorage auto-save
- Export/Import characters as JSON files
- Responsive design for desktop and mobile
- Print-friendly layout

### Architecture
- Modular rules system (JSON-based)
- Separation of concerns (rules/logic/presentation)
- Type-safe data structures
- No external dependencies
- Pure vanilla JavaScript

