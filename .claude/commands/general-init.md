# Initialize General Purpose Session Overview

You are the session overview creator for general purpose sessions. When the user runs this command, guide them through creating a flexible SESSION.md document that adapts to any type of work.

## Command Usage

```
/general-init
```

**No parameters required.** This command is interactive.

**Prerequisites:**
- Must have an active session of type "general"
- Should be run after `/session-init` (user selected "general" type)

---

## Your Tasks

### 1. Check Session Type

First, verify this is a general purpose session:

Read `.aiwork/session.yaml`:
- If `type: "general"` → Continue
- If other type → Show error

**Error if not general session:**
```
❌ This command is for general purpose sessions only

Your session type: {type}

For general sessions:
1. Initialize session: /session-init
2. Select type: 7 (general)
3. Then run: /general-init

For other session types, use the appropriate command:
- software → /project-init
- data-analysis → /analysis-init
- content → /content-init
- decision → /decision-init
- learning → /learning-init
- research → /research-init
```

### 2. Check if SESSION.md Already Exists

Check if `.aiwork/SESSION.md` exists:

**If exists:**
```
⚠️ SESSION.md already exists

Found existing session overview at .aiwork/SESSION.md

Options:
1. View existing SESSION.md (cancel this command)
2. Update existing SESSION.md (edit manually or recreate)
3. Recreate from scratch (⚠️  will overwrite)

Choose option: (1/2/3)
```

Only proceed with recreation if user explicitly chooses option 3.

### 3. Interactive Session Overview Creation

Guide the user through 6 flexible questions.

**Tone:** Very flexible and adaptive. Emphasize that this is customizable for any type of work.

---

#### Question 1: Work Description

```
Let's create your General Purpose Session Overview!

This flexible format works for ANY type of structured work:
- Project planning
- Brainstorming sessions
- Event planning
- Personal organization
- Business process design
- ... anything you need!

---

Q1: What type of work are you doing in this session? (Describe in 1-2 sentences)

Example 1: "Planning and executing a company offsite retreat for 50 people"
Example 2: "Organizing and decluttering my home office over the next month"
Example 3: "Brainstorming and prototyping new product ideas"
Example 4: "Managing a complex multi-stakeholder project with dependencies"

→ {user input}
```

---

#### Question 2: Goals and Objectives

```
Q2: What are your main goals or objectives? (List 3-5 key goals)

These can be outcomes you want to achieve, problems you want to solve, or deliverables you want to produce.

Example for event planning:
1. Define event theme, agenda, and budget
2. Book venue and arrange logistics
3. Organize activities and speakers
4. Manage registrations and communications
5. Execute smooth event and gather feedback

Example for personal organization:
1. Sort and categorize all items in office
2. Create filing system for documents
3. Set up digital organization system
4. Design productive workspace layout
5. Establish maintenance routines

→ {user input}
```

---

#### Question 3: Key Stakeholders or Participants

```
Q3: Who is involved or affected by this work?

List people, teams, or groups who are:
- Working with you on this
- Affected by the outcomes
- Need to be kept informed
- Will use the results

Example for company offsite:
- Executive team (decision makers)
- All staff (50 participants)
- Venue coordinator
- Activity facilitators
- Catering service

Example for personal project:
- Just me (primary)
- Family members (may be affected by changes)
- Optional: Accountability partner or coach

Or simply: "Solo project - just me"

→ {user input}
```

---

#### Question 4: Resources and Inputs

```
Q4: What resources, information, or inputs do you have or need?

This could include:
- Documents, data, or materials
- Budget or financial resources
- Tools or equipment
- Information you need to gather
- External dependencies

Example for product brainstorming:
- Market research reports
- Customer feedback data
- Competitor analysis
- Budget: $50K for prototyping
- Team: 3 designers, 2 engineers

Example for home organization:
- Storage containers and labels (need to buy)
- Photos of organized spaces for inspiration
- Time: 4 weekends
- Tools: Label maker, shelving units

→ {user input}
```

---

#### Question 5: Expected Outcomes and Deliverables

```
Q5: What are the expected outcomes or deliverables?

What will exist at the end that doesn't exist now? What will be different?

Example for event planning:
- Confirmed venue booking
- Complete event agenda with timings
- Registered participant list
- All logistics arranged (catering, AV, materials)
- Post-event: Feedback survey results and lessons learned doc

Example for workspace organization:
- Organized and labeled filing system
- Clear desk with only essential items
- Digital folder structure mirroring physical
- Maintenance checklist for keeping organized
- Before/after photos

→ {user input}
```

---

#### Question 6: Timeline and Milestones

```
Q6: What's your timeline? Any key dates or milestones?

Include:
- Overall timeline or deadline
- Key milestones or checkpoints
- Dependencies or date constraints

Example: "Event is Sept 15. Must book venue by July 1, finalize agenda by Aug 1, send invites by Aug 15"

Or: "Flexible 4-week timeline, aiming to complete one room per weekend"

Or: "No fixed deadline, working on this iteratively over the next few months"

→ {user input}
```

---

### 4. Generate SESSION.md

Create `.aiwork/SESSION.md` using all the answers:

```markdown
# Session: {session-name converted to title case}

**Session ID**: {session-id from session.yaml}
**Type**: General Purpose
**Created**: {timestamp}
**Status**: Active

---

## Work Overview

{Answer from Q1}

**Type of Work**: {Infer category from Q1, e.g., "Event Planning", "Personal Organization", "Project Planning", etc.}

---

## Goals & Objectives

{Parse Q2 answer - convert to checklist with emoji status indicators}
1. ⚪ {Goal 1}
2. ⚪ {Goal 2}
3. ⚪ {Goal 3}
4. ⚪ {Goal 4}
5. ⚪ {Goal 5}

**Status Key**: ⚪ = Pending, 🔄 = In Progress, ✅ = Completed

---

## Stakeholders & Participants

{Parse Q3 answer - format as list}

**Key People:**
{If multiple people/groups:}
- {Person/Group 1} - {role or relevance}
- {Person/Group 2} - {role or relevance}

{If solo:}
- {User name or "Solo project"}

---

## Resources & Inputs

{Parse Q4 answer - organize into categories if possible}

### Available Resources
{List what they have}

### Resources Needed
{List what they need to acquire}

### Key Information
{List information or data they have/need}

### Constraints
{List any budget, time, or other constraints}

---

## Expected Outcomes & Deliverables

{Parse Q5 answer - convert to checklist}

### Tangible Outputs
- [ ] {Deliverable 1}
- [ ] {Deliverable 2}
- [ ] {Deliverable 3}

### Outcomes & Changes
- [ ] {Outcome 1}
- [ ] {Outcome 2}

---

## Timeline & Milestones

{Parse Q6 answer}

**Overall Timeline**: {timeline or "Flexible"}
**Key Deadline**: {deadline or "No fixed deadline"}

{If milestones mentioned:}
### Key Milestones
| Date | Milestone | Status |
|------|-----------|--------|
| {date-1} | {milestone-1} | ⚪ |
| {date-2} | {milestone-2} | ⚪ |

---

## Workflows

*Workflows will be added as you create them with `/workflow-new`*

| ID | Name | Status | Steps | Completed |
|----|------|--------|-------|-----------|
| - | - | - | - | - |

---

## Progress Summary

**Session Status**: 🟢 Active

**Progress:**
- Workflows created: 0
- Workflows completed: 0
- Total steps: 0
- Completed steps: 0
- Completion: 0%

---

## Notes & Observations

*Add notes, ideas, and observations as you work*

{Empty initially}

---

## Lessons Learned

*Document what works, what doesn't, and insights gained*

{Empty - to be filled as you work}

---

## Next Actions

*Track immediate next steps and action items*

### Immediate Next Steps
- [ ] {Action 1}
- [ ] {Action 2}

### Blocked / Waiting On
{Empty initially}

---

## Appendix

### Related Resources
*Links, documents, references*

### Contacts
*Important contacts for this work*

### Change Log
| Date | Change | Notes |
|------|--------|-------|
| {timestamp} | Session overview created | Initial setup |

---

**Session Created**: {timestamp}
**Last Updated**: {timestamp}

---

## About This Session

This is a **general purpose** session, which means it's flexible and can adapt to any type of work.

**How to use this session:**
1. Create workflows for different phases or areas of your work
2. Break workflows into manageable steps
3. Use context packages to work with different AI tools
4. Track progress and update this overview as you go

**Tips:**
- Update Goals status (⚪ → 🔄 → ✅) as you make progress
- Use Notes section liberally - capture ideas and insights
- Add Next Actions as you identify them
- Use workflows to organize different aspects of the work
```

### 5. Update Session Tracking

Update `.aiwork/session.yaml`:

```yaml
session_id: "{session-id}"
type: "general"
# ... existing fields ...
session_overview_created: "{timestamp}"
session_overview_version: "1.0"
```

### 6. Output Summary

```
✅ General Purpose Session Overview Created!

Location: .aiwork/SESSION.md
Type: General Purpose (Flexible)
Created: {timestamp}

📋 Session Overview:
- Work type: {inferred from Q1}
- {N} goals defined
- {N} stakeholders/participants
- {N} expected deliverables
- Timeline: {timeline from Q6}

🎯 Your Goals:
{List goals from Q2, numbered}

⏰ Timeline:
{Timeline from Q6}

📋 Next Steps:

1. **Review your session overview**:
   → Open .aiwork/SESSION.md
   → Make any edits or additions

2. **Create your first workflow**:
   → /workflow-new <workflow-name>
   → Tip: You can use any template or create custom workflow
   → Workflows help you break down work into manageable steps

3. **Start working**:
   → /workflow-plan (generates steps)
   → /step-prepare 1 (creates context package)
   → Execute step and mark complete

💡 Tips for General Purpose Sessions:

- **Flexible structure**: Adapt workflows and steps to your needs
- **Custom workflows**: Create workflows that make sense for your work
- **Use templates if helpful**: Software, data-analysis, etc. templates can work for various purposes
- **Iterative approach**: Start with one workflow, add more as needed
- **Track everything**: Use SESSION.md to capture notes, ideas, lessons learned

Examples of workflows you might create:
{Suggest 2-3 workflow examples based on their Q1 answer}

Example: /workflow-new planning-phase
Example: /workflow-new execution
Example: /workflow-new review-and-improve
```

---

## Important Notes

- **Most flexible session type** - Can be used for literally anything
- **No rigid structure** - User defines their own workflow patterns
- **SESSION.md is adaptable** - Can be customized as work evolves
- **Good for unique work** - Work that doesn't fit other categories
- **Can use any template** - Existing templates can be adapted
- **Experimental work** - Try new AI collaboration patterns

---

## Error Handling

### If no session found:
```
❌ No session found

Initialize a general purpose session first:
→ /session-init
→ Select: 7 (general)

Then run: /general-init
```

### If wrong session type:
```
❌ Wrong session type

Your session type: {type}

This command is for general purpose sessions only.

For {type} sessions, use:
- software → /project-init
- data-analysis → /analysis-init
- content → /content-init
- decision → /decision-init
- learning → /learning-init
- research → /research-init
```

---

## Example Use Cases for General Sessions

### Project Management
```
Q1: Managing a cross-functional product launch
Q2: Define scope, coordinate teams, track deliverables, launch successfully
Q3: Product team, engineering, marketing, sales
Q4: Project plan, budget, team schedules
Q5: Launch checklist, go-to-market plan, post-launch report
Q6: Launch date: March 1, milestones: design freeze Jan 15, beta Feb 1
```

### Event Planning
```
Q1: Planning company annual retreat for 50 people
Q2: Define theme, book venue, plan activities, manage logistics
Q3: All staff (participants), exec team (sponsors), vendors
Q4: Budget $15K, venue options research, activity ideas
Q5: Confirmed bookings, agenda, post-event feedback
Q6: Event Sept 15, venue by July 1, invites by Aug 15
```

### Personal Organization
```
Q1: Declutter and organize home office
Q2: Sort items, create filing system, design workspace, establish routines
Q3: Solo project (me), family affected
Q4: Storage containers, label maker, 4 weekends time
Q5: Organized space, filing system, before/after photos, maintenance plan
Q6: 4 weekends starting next month, one room per weekend
```

### Creative Project
```
Q1: Write and illustrate a children's book
Q2: Develop concept, write story, create illustrations, self-publish
Q3: Solo (author/illustrator), beta readers, editor, designer
Q4: Story ideas, art supplies, publishing budget $2K
Q5: Finished manuscript, illustrations, published book
Q6: 6 months, draft by month 2, illustrations by month 4, publish month 6
```

---

**Remember**: General purpose sessions are the most flexible. There's no "wrong" way to use them. Adapt the structure to fit your work!
