# Triumph Builds — Agent Guide

## Purpose
Reusable AI agent to assist an expert Storyline developer at Triumph Motorcycles with e-learning production. Focus areas: asset creation, slide layouts, instructional design, and Triumph branding.

## Hard Constants (every project)
| Variable | Value |
|----------|-------|
| Authoring tool | Articulate Storyline |
| Canvas size | 16:9 |
| Brand | Triumph Motorcycles |

## What this agent helps with
- **Assets** — graphics, icons, illustrations, image direction, alt text
- **Layouts** — slide structure, visual hierarchy, content zones for 16:9
- **Instructional Design** — learning objectives, scenario design, assessment strategy, content chunking
- **Branding** — colour palette, typography, tone of voice, brand-compliant design decisions

## What this agent does NOT do
- Explain Storyline features or mechanics (user is an expert)
- Provide step-by-step Storyline how-to guides

---

## Current project — Key & Keyless Ignition Systems

**Status:** Source extracted, initial structure proposed. **Design phase PARKED until SME content lock.**

**Workflow lesson learned:** Tried a speculative design head-start before the SME meeting; pulled back because the audit trail from source → designs was opaque. Workflow rule going forward: **content + mapping lock with SME first, design after.** Captured in memory as `feedback-content-lock-before-design`.

**Source:** [Keyless New Proposal 080526.pptx](Keyless%20New%20Proposal%20080526.pptx) — 68 slides, drafter has pre-flagged e-learning/PDF split (e-learning = 1–39, PDF reference = 40–68).

**Proposed module structure (to validate with SME, not locked):** 7 sections, ~37–40 screens.
1. Welcome & Big Picture
2. The Key System (incl. TPMS + safety)
3. The Keyless System
4. Communications & Wake-up
5. TDT Diagnostics
6. Case Study (capstone)
7. Wrap + PDF signpost

**SME meeting agenda items (see §7 and §8 of [breakdown-and-id-keyless.md](breakdown-and-id-keyless.md)):**
1. Duplicate slides 22/24 and 23/25 — intentional or copy-paste?
2. Add/Re-Register decision — keep in both Key and Keyless sections, or factor out?
3. Case study placement — capstone or embedded?
4. Knowledge checks — per section, or just mid + final?
5. Module duration target?
6. Case study Word file availability (needed for Section 6).
7. The "ideas?" notes in slides 41–55 — user to answer, or back to SME?

**Next step (in order):**
1. SME meeting — walk through proposed structure + agenda above, capture decisions
2. If SME has sent a revised pptx, re-extract content and refresh the breakdown
3. Produce a **source-slide → designed-screen mapping document** (one page). SME signs off the mapping before any design work begins.
4. Only after mapping sign-off — restart design phase. Claude Design becomes a polishing step on locked content, not a content restructurer.

---

## Workspace files
- `Keyless New Proposal 080526.pptx` — original source document (do not edit)
- `source-content-keyless.md` — verbatim text extraction of every slide + notes (reference)
- `breakdown-and-id-keyless.md` — content map, issues spotted, proposed module structure, open questions
- `CLAUDE.md` — this file
- `.claude/settings.local.json` — permission settings (gitignored)

---

## Proven workflow (validated this session)
1. **Source → extract** — pull verbatim text from .pptx via Python in this Codespace.
2. **Breakdown → ID brief** — produce content map, structure, per-screen brief in this chat. **Preserve SME wording verbatim** ([feedback-preserve-wording](memory)).
3. **Per-screen design handoffs** — write paste-ready prompts for [claude.ai/design](https://claude.ai/design).
4. **Claude Design → export** — generate as a multi-screen set in one go, export as PNG (preferred) or PPTX.
5. **Storyline import** — if PPTX, expect [known import bugs](memory) with documented workarounds (transparent-line trick for phantom dashed outlines; embed fonts before export to avoid substitution).
6. **Interactivity layered natively in Storyline** on top.

---

## Knowledge libraries (populate over time)
- **Triumph Brand Reference** — colour palette, typography, logo usage, tone of voice. *To be populated.*
- **Instructional Design Patterns** — preferred frameworks, scenario templates, assessment approaches. *To be populated.*
- **Layout Library** — named layout patterns (e.g. "hero intro", "split comparison", "stepped flow diagram"). *Three proven so far in workflow test — to be documented.*
- **Asset Guidelines** — image style, icon style, illustration direction, photography tone. *To be populated.*
