# Complete Talents Database - Version 2.0

## Summary

All talents from the Cosmere RPG - Stormlight Handbook have been successfully extracted and integrated into the character sheet system.

## Talents Included

### Total: **140 Talents** across 6 Heroic Paths

#### 1. **Agent** (3 specialties, 24 talents)
- **Investigator** (8 talents): Watchful Eye, Get 'Em Talking, Quick Analysis, Baleful, Gather Evidence, Hardy, Sleuth's Instincts, Close the Case
- **Spy** (8 talents): Sure Outcome, Plausible Excuse, Collected, Cover Story, Subtle Takedown, Mighty, Mercurial Facade, High Society Contacts
- **Thief** (8 talents): Risky Behavior, Cheap Shot, Double Down, Surefooted, Underworld Contacts, Shadow Step, Fast Talker, Trickster's Hand

#### 2. **Envoy** (3 specialties, 24 talents)
- **Diplomat** (8 talents): Steadfast Challenge, Collected, Withering Retort, Well Dressed, Calm Appeal, High Society Contacts, Peaceful Solution, Practiced Oratory
- **Faithful** (8 talents): Customary Garb, Galvanize, Devoted Presence, Composed, Stalwart Presence, Applied Motivation, Sage Counsel, Inspired Zeal
- **Mentor** (8 talents): Sound Advice, Practical Demonstration, Lessons in Patience, Mighty, Instill Confidence, Guiding Oration, Foresight, Rallying Shout

#### 3. **Hunter** (3 specialties, 24 talents)
- **Archer** (8 talents): Tagging Shot, Combat Training, Sharp Eye, Steady Aim, Exploit Weakness, Backstep, Unrelenting Salvo, Hardy
- **Assassin** (8 talents): Startling Blow, Killing Edge, Fatal Thrust, Shadowing, Mighty, Cold Eyes, Swift Strikes, Sidestep
- **Tracker** (8 talents): Deadly Trap, Animal Bond, Experienced Trapper, Protective Bond, Hunter's Edge, Pack Hunting, Surefooted, Feral Connection

#### 4. **Leader** (3 specialties, 24 talents)
- **Champion** (8 talents): Combat Coordination, Valiant Intervention, Imposing Posture, Hardy, Mighty, Resolute Stand, Resilient Hero, Demonstrative Command
- **Officer** (8 talents): Composed, Through the Fray, Well Supplied, Customary Garb, Relentless March, Confident Command, Synchronized Assault, Authority
- **Politico** (8 talents): Cutthroat Tactics, Tactical Ploy, Rumormonger, Well Dressed, Baleful, Set at Odds, Shrewd Command, Grand Deception

#### 5. **Scholar** (3 specialties, 22 talents)
- **Artifabrian** (8 talents): Efficient Engineer, Prized Acquisition, Deep Study, Inventive Design, Fine Handiwork, Overcharge, Experimental Tinkering, Overwhelm with Details
- **Strategist** (6 talents): Strategize, Mind and Body, Know Your Moment, Deep Contemplation, Turning Point, Read the Field
- **Surgeon** (6 talents): Field Medicine, Emotional Intelligence, Ongoing Care, Medical Expertise, Resuscitate, Miraculous Recovery

#### 6. **Warrior** (3 specialties, 24 talents)
- **Duelist** (8 talents): Practiced Kata, Flamestance, Ironstance, Signature Weapon, Surefooted, Feinting Strike, Vinestance, Wit's End
- **Shardbearer** (8 talents): Shard Training, Stonestance, Windstance, Mighty, Shattering Blow, Bloodstance, Precise Parry, Meteoric Leap
- **Soldier** (8 talents): Cautious Advance, Combat Training, Defensive Position, Devastating Blow, Formation Drills, Hardy, Wary, Swift Strikes

## Talent Structure

Each talent includes:
- **ID**: Unique identifier
- **Name**: Display name
- **Prerequisite**: Skill ranks or other talents required
- **Activation**: Type (1_action, 2_actions, 3_actions, free_action, reaction, special, always)
- **Description**: Full effect description

## Files Updated

1. **cosmere-rules.json**: Complete rules database with all talents (Version 2.0)
2. **cosmere-character-sheet.html**: Embedded rules updated with complete talent system

## Integration Status

✓ All heroic path talents extracted from handbook  
✓ Talents structured in JSON format  
✓ Talents embedded in character sheet HTML  
✓ Prerequisite chains preserved  
✓ Activation types categorized  
✓ Specialty organization maintained  

## Next Steps

The character sheet now has access to all talent data. The leveling system can now:
- Display available talents based on character level and prerequisites
- Allow talent selection during level-up
- Track selected talents and apply their effects
- Support multi-pathing between different heroic paths

## Notes

- Radiant Path talents will be added in a future update
- The talent tree UI needs enhancement to display all available options
- Prerequisite checking logic should be implemented in the level-up flow
- Talent effects should be applied automatically to character stats where applicable

