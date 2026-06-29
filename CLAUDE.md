# Triumph Builds — Agent Guide

## Purpose
Reusable AI agent to assist an expert Storyline developer at Triumph Motorcycles with e-learning production. Focus areas: asset creation, slide layouts, instructional design, and Triumph branding.

## Hard Constants (every project)
| Variable | Value |
|----------|-------|
| Authoring tool | Articulate Storyline 3 |
| Canvas size | 16:9 (1920 × 1080) |
| Brand | Triumph Motorcycles |
| Brand font | Triumph Brokman (10 weights, in `/TriumphBrokman/`) |

## What this agent helps with
- **Assets** — graphics, icons, illustrations, image direction, alt text
- **Layouts** — slide structure, visual hierarchy, content zones for 16:9
- **Instructional Design** — learning objectives, scenario design, assessment strategy, content chunking
- **Branding** — colour palette, typography, tone of voice, brand-compliant design decisions

## What this agent does NOT do
- Explain Storyline features or mechanics (user is an expert)
- Provide step-by-step Storyline how-to guides
- **Write, rewrite, paraphrase, condense, summarise, or remove SME source content**

---

## 🔴 CRITICAL — Content vs Layout (read every time)

**The user's job is content. My job is layout, structure, organisation and design.**

When designing a slide from `source-content-keyless.md` or any other SME source:

1. **Use SME source content verbatim.** Every sentence, every phrase, every qualifier (e.g. "before the key authentication result is available", "as short as practicable") stays. Word-for-word.
2. **Restructure, don't rewrite.** Splitting a paragraph into bullets, putting sentences into cards/containers, ordering content into visual zones, adding headings/labels for scaffolding — all fine.
3. **Never silently drop or condense content.** Don't skip a sentence because it "feels redundant" or "doesn't fit the layout". If it's in the source, it must appear on the slide.
4. **If something is genuinely redundant, contradictory, or wrong — FLAG IT separately.** Do not silently fix or omit. Output: "Source contains X — I have not included/changed it because Y. Confirm OK to keep/change/drop."
5. **Don't invent labels, consequences, purposes, technical claims, primary/backup designations, etc.** If source says "UHF or LF (as a backup method)" — don't add "Primary" to UHF. The SME chose their words.
6. **After generating every slide, output a "Content audit" listing every change vs source:**
   - Sentences moved / regrouped (acceptable — list anyway)
   - Sentences shortened, paraphrased, omitted (FLAG explicitly)
   - Labels / headings / scaffolding text added by me (FLAG)
   - Anything I'm unsure about (FLAG)
7. **Layout scaffolding I CAN add freely:** section titles like "Communication Methods" / "Authentication" / "Timing", numbered step labels, button microcopy, page indicators, decorative chrome — anything not in the body content stream.

**Why this exists:** User has to present designs to the SME. Missing or rewritten content = SME questions = lost trust + rebuild work. Pattern was established across slides 13, 16, 18 where I removed/invented content and the user had to catch each one. Cost: their time + a near-miss on shipping a half-content module.

---

## Current project — Key & Keyless Ignition Systems

**Status:** Active design. Fresh build from new SME source. Tight deadline — minimise over-engineering.

**Source:** [KEYLESS INST DES.pptx](KEYLESS%20INST%20DES.pptx) — 60 slides. This is the current working source. (The old `Keyless New Proposal 080526.pptx` is archived in repo for reference only — do not use for content.)

**Source-slide rendered previews:** in `source-slides-preview/` (PNGs of all 60 slides from new source).

**Source content text extraction:** `source-content-keyless.md` — verbatim text from new PPT, with SME notes and placeholders flagged.

---

## SME-defined sections (from PPTX section breaks)

These are the exact section headings the SME defined — use these verbatim on the menu slide.

| # | SME section heading | Source slides | Menu item? |
|---|---|---|---|
| 1 | Introduction + Nav | 1–3 | No (pre-menu) |
| 2 | Keyed Vs Keyless Comparrison ⚠ typo | 4–11 | Yes |
| 3 | Key Type Systems | 12–13 | Yes |
| 4 | Keyless Systems - Key Communication | 14–23 | Yes |
| 5 | Key Pairing | 24–32 | Yes |
| 6 | Immobiliser and Key Diagnostics | 33–39 | Yes |
| 7 | TPMS | 40–45 | Yes |
| 8 | Case Study | 46–51 | Yes |
| 9 | PDF Reference Questions | 52–60 | Yes |

⚠ "Comparrison" is a typo in the source — confirm with user whether to correct on menu.
⚠ "PDF Reference Questions" may need a more learner-friendly label on the menu — TBC.

**Known issues in source to resolve before designing:**
- Slide 6: "Comment…?" — incomplete, needs SME input on 4 types of immobiliser content
- Slide 15: Draft artefact — discard, design from slides 16 + 17 instead
- Slide 60: Exact duplicate of slide 59 — drop one
- Slides 9, 39, 42, 49, 50, 51: Image/diagram-only — visual reference in `source-slides-preview/`

---

## Designed slides — carry-over from old source

Old designs that map cleanly to new source (direct reuse or light content update):

| Old design file | New source slide(s) | Reuse verdict |
|---|---|---|
| 09-tpms-overview | 41 | Direct reuse |
| 10-tpms-pairing-flow | 42 | Direct reuse |
| 11-tpms-data-screen | 43 | Direct reuse |
| 19-ignition-on-process | 21 | Direct reuse |
| 26-tdt-menu-summary | 33 | Direct reuse |
| 27-configure-read-dtcs | 34 | Direct reuse |
| 27b-configure-active | 35 | Direct reuse |
| 28-key-signal-function-test | 33–35 | Direct reuse |
| 14-keyless-facts | 14 | Template — content updated |
| 18a-comms-methods | 15–17 | Template — needs rationalisation first |
| 18b-sequence-frequencies | 15–17 | Template — needs rationalisation first |
| 22-summary-keys | 26–27 | Template — content expanded |

**Slides 1–8 (intro, menu, overview, ECM types, key system):** User-built in SL3 — assess against new source before rebuilding.

**New slides to build (no old equivalent):**
- Similarities of Key and Keyless (source 5)
- 4 Types of Immobiliser (source 6 — pending SME clarification)
- Drag-drop assessments (sources 10, 11)
- MCQ slides (sources 18–20, 28–32, 53–60)
- 90-second timeout note (source 23)
- Case study (sources 46–51)
- Keyless Facts section intro (source 52)

---

## Pending questions for SME / user before designing

1. **Source slide 6** — "There are 4 types of immobiliser system used across the model range / Comment…?" Content is incomplete. What goes here?
2. **Sources 15–17** — three slides with overlapping LF/UHF text. Confirm the rationalised version before I design it.
3. **Source slide 8** — diagram only. Check `source-slides-preview/slide-08.png` — is this a component diagram we need to recreate?

---

## Workspace files (current)
- `KEYLESS INST DES.pptx` — **current working source** (do not edit)
- `Keyless New Proposal 080526.pptx` — old source, archived for reference only
- `source-content-keyless.md` — verbatim text extraction from new PPT
- `source-slides-preview/` — per-slide PNG renders (60 slides, from new PPT)
- `Reference-Designs/` — user's earlier design exploration screenshots (vibe reference, not layout reference)
- `TriumphBrokman/` — 10-weight brand font
- `designs/slides/` — per-slide HTML/CSS (source for rendering)
- `designs/assets/` — drop-in screenshots (TDT screens, etc.)
- `designs/build/` — rendered PNG output
- `designs/render.py` — playwright renderer
- `CLAUDE.md` — this file
- `.claude/settings.local.json` — bypass permissions for this workspace

---

## Workflow rules in force (memory)
- `feedback-png-only-deliverable` — PNG only. No editable PPTX. User extracts text from PNG and rebuilds in SL3.
- `feedback-use-real-ui-screenshots` — for TDT / instrument cluster slides, use the actual screenshot, never a stylised recreation.
- `feedback-content-lock-before-design` — content lock with SME before design (mostly moot now, SME gave green light).
- `feedback-preserve-wording` — **VERBATIM ONLY** — restructure/chunk but never rewrite/condense/drop SME content. Flag deviations explicitly. See critical rule above.
- `feedback-iterate-dont-overplan` — match scope to stated goal. Deadline mode = no over-engineering.
- `feedback-no-pptx-import-to-storyline` — known SL3 import bugs documented (phantom dashed lines, font sub).

---

## Design language summary (reference)
- **Background:** dark cinematic (#050508–#0A0A12), subtle red top-left glow, faint diagonal motion lines
- **Title pattern:** white line + red line ("KEY vs KEYLESS / IGNITION SYSTEMS")
- **Eyebrow:** red `/////` slashes
- **Chrome:** TRIUMPH wordmark + triangle top-left · `XX — 14` page top-right · green next circle bottom-right · crop marks at corners · "TRIUMPH · TECHNICIAN TRAINING" foot bottom-left
- **Typography:** Triumph Brokman across the board. Heavy weights (800–900) for titles, 22px+ minimum body
- **Accent uses:**
  - Red for headers / key emphasis / warnings of failure
  - Amber for safety warnings (TPMS warning, info callouts)
  - Green for "success" states, next button
- **Real UI screenshots:** framed in dark surface with hairline border + "● Triumph Diagnostic Tool" green-dot label
