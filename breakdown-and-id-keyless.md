# Triumph Keyless Project — Content Breakdown & ID Overview

> Source: `Keyless New Proposal 080526.pptx` (68 slides, 14 with notes)
> Reference: full verbatim extraction saved to `source-content-keyless.md`

---

## 1. At a glance

| | |
|---|---|
| Total slides in source | 68 |
| Drafter's intent | E-learning + supporting PDF reference (split flagged in source) |
| **E-learning candidate slides** | **1–39** (with cuts) |
| **PDF reference slides** | **40–68** (explicitly marked "Remove" by drafter) |
| Audience | Trained Triumph technicians |

---

## 2. E-learning content map (slides 1–39)

Grouped by what the content actually does, not slide order:

| Theme | Source slides | What it covers |
|---|---|---|
| **A · Setup** | 1, 2 | Drafter's proposal note + course purpose |
| **B · Big picture** | 3, 4 | KEY vs KEYLESS overview, comparison table |
| **C · The Key system** | 5, 6, 7, 8, 9, 10, 11 | Key facts, TDT Add/Re-Register, TPMS (sits under Key), TPMS data screen, frequencies |
| **D · The Keyless system** | 12, 13, 14, 15, 16 | Steering lock, Time of Flight, keyless facts, TDT Add/Re-Register, CR2032 battery |
| **E · Communications & Wake-up** | 18, 19, 20, 21 | UHF vs LF, 8-stage wake-up sequence, 90-second passive-key rule |
| **F · Summary / Knowledge** | 17, 22, 23, 24, 25 | TPMS Qs, "In Summary", 5-question general info |
| **G · TDT Diagnostics** | 26, 27, 28, 29, 30, 31, 32, 33, 34 | Immobiliser menus, Configure/Pair, Key Signal Function Test (UHF / LF / Antenna), US isolator, 30-sec TDT window, Diagnostic Q&A |
| **H · Case study** | 35, 36, 37, 38, 39 | Bike-won't-power-on scenario, flash sequences, DTC lookup, bonus question |

---

## 3. PDF reference content map (slides 40–68)

All marked "Remove" by the drafter — these go to the printable reference:

| Theme | Source slides | What it is |
|---|---|---|
| Component locations | 40, 41, 42, 43, 44 | Keyless component locations (drag-n-drop idea), ECM locations, electrical architecture overviews |
| Wake-up sequence (detail) | 45 | Refined 8-stage write-up |
| TDT menus | 46, 61, 62 | Menu overviews per model type (Key / All Keyless / 400cc only) |
| TPMS technical detail | 47, 48, 49, 50, 51 | Repeat of TPMS warning + frequencies, pairing flow, data screen, key/TPMS frequencies |
| Communications examples | 52, 53, 54 | Two worked KCU search-order tables, antenna proximity |
| Diagnostic process | 55, 56, 57, 63, 64, 65, 66 | General information points (the long-form rules), 6-step diagnostic process, diagnostic reminders |
| Download flow charts | 58, 59, 60 | Rocket 3 GT calibration + failed-download recovery |
| Pairing failure causes | 67 | Persistence / electrical noise / antenna position notes |
| Flash sequences | 68 | Instrument panel flash code table |

---

## 4. Issues spotted — flag before signoff

| # | Issue | Where | Action |
|---|---|---|---|
| 1 | **Exact duplicate slides** | Slide 22 = Slide 24 ("In Summary") | Keep one, drop the other |
| 2 | **Exact duplicate slides** | Slide 23 = Slide 25 (5-question general info) | Keep one, drop the other |
| 3 | All-caps body copy | Slide 12 (keyless features) | Accessibility / readability — suggest sentence case |
| 4 | Typos | "TLyre" (slide 8, 47), "obly" (slide 62) | Fix |
| 5 | Number consistency check | Slide 5: "Max 4 keys" (Key system) vs Slide 14: "Max 3 keys" (Keyless) vs Slide 22/24: "up to three keys" | Not a contradiction (different systems) but worth labelling clearly in copy |
| 6 | "efi" lowercased inline | Slide 3, 5 etc | Confirm Triumph house style — usually "EFI" |
| 7 | Drafter's open questions | Many "ideas?" notes in slides 41–55 | These are the drafter asking the team for input — we need answers before building those reference pages |
| 8 | Case study refers to separate file | Slide 39 ("see separate word file") | Need that file to complete the case study |

---

## 5. What's strong in the source

- **The case study (slides 35–37)** — proper realistic technician scenario, decision-tree shaped. Real ID gold.
- **The 8-stage wake-up sequence (slides 19–20)** — natural animation/interaction territory.
- **UHF vs LF explanation (slide 18)** — well-pitched technical depth for the audience.
- **The Add New Key vs Re-Register All Keys decision (slides 5/6 & 14/15)** — clear, testable, procedural. Heart of the module.
- **Drafter has already done the cognitive-load split work** — saves us a lot of judgement calls.

---

## 6. Proposed e-learning module structure

7 sections, rough screen counts. **Not a final spec — this is the structural skeleton to agree on before drilling into per-screen design.**

| # | Section | Source slides used | Est. screens | Notes |
|---|---|---|---|---|
| **1** | Welcome & Big Picture | 2, 3, 4 | ~5 | Purpose + KEY vs KEYLESS + comparison |
| **2** | The Key System | 5, 6, 7, 8, 9, 10, 11 | ~7–8 | Includes TPMS (sits under Key) + safety screen + Add/Re-Register scenario |
| **3** | The Keyless System | 12, 13, 14, 15, 16 | ~6 | Features + Time of Flight + battery + Add/Re-Register scenario |
| **4** | Communications & Wake-up | 18, 19, 20, 21 | ~5 | UHF/LF + 8-stage animation + 90-sec rule |
| **5** | TDT Diagnostics | 26, 27, 28, 29, 30, 31, 32, 33, 34 | ~7–8 | Menus + Key Signal Function Test + diagnostic facts |
| **6** | Case Study | 35, 36, 37, 38, 39 | ~5–6 | Branching scenario through the customer problem |
| **7** | Wrap & PDF signpost | — | ~2 | Recap + safety reminder + link to PDF reference |
| | **TOTAL** | | **~37–40 screens** | |

Plus a parallel deliverable: the **PDF reference document** from slides 40–68 (separate workstream).

---

## 7. Big strategic decisions to lock before per-screen ID

1. **Section 2 (Key) and Section 3 (Keyless) repeat the Add/Re-Register decision.** Do we:
   - (a) keep both for completeness (technicians learn each system's specifics), or
   - (b) factor out a single "TDT Add/Re-Register" decision screen that applies to both?
   I'd lean (a) — the rules are subtly different (max keys, attack delays) and technicians work on one system at a time.

2. **Where does the case study sit?** Two options:
   - (a) at the end of the module, as a capstone assessment (current proposal)
   - (b) embedded within the diagnostics section, with section 6 becoming "Reflection & wrap" only
   I'd lean (a) — case study is too rich to bury inside another section.

3. **Knowledge checks — per section or only at the end?** Current proposal is per-section. Alternative: just two checks (mid-module + final) to reduce screen count.

4. **The CR2032 battery screen (slide 16)** — is this content current? The drafter's notes mention "Annual Service Item to replace a battery!" — feels like more of a service-bulletin item than core ignition training. Confirm in or out.

---

## 8. Open questions for you / SME

1. Are duplicate slides 22/24 and 23/25 intentional (different intended placement) or copy-paste errors?
2. Is the **case study word file** (referenced on slide 39) available? Need it to build Section 6 properly.
3. Are the **"ideas?" notes** in slides 41–55 yours to answer, or do they need to go back to a SME?
4. Should **TPMS** sit under Section 2 (Key), get its own section, or only live in the PDF reference?
5. **Module duration target** — any constraint I should structure to (e.g. 30 min, 45 min)?

---

*End of overview. Once decisions 1–4 in §7 and questions in §8 are answered, next step is the per-screen ID brief for Section 1.*
