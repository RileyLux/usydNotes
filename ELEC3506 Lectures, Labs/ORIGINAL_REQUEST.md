# Original User Request

## Initial Request — 2026-09-21T13:28:53Z

Use a multi-agent team where each agent works independently on each lecture.

Extract, synthesize, and write comprehensive, structured summary notes from three independent lecture slide decks (`Lecture1.pdf`, `Lecture2.pdf`, and `Lecture3.pdf` located in `c:\Users\R4iley\Downloads`) into their corresponding markdown files in `c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs\`. Each week's lecture is self-contained and should be processed independently.

Working directory: `c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs`
Integrity mode: development

## Requirements

### R1. Independent Lecture-to-File Processing
Process each lecture deck independently into its target file:
- `Lecture1.pdf` (in `c:\Users\R4iley\Downloads`) → `1. Internet Background.md` (in `c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs`)
- `Lecture2.pdf` (in `c:\Users\R4iley\Downloads`) → `2. Physical Layer.md` (in `c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs`)
- `Lecture3.pdf` (in `c:\Users\R4iley\Downloads`) → `3. Data Link Layer.md` (in `c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs`)
Agents should focus directly on their designated lecture without needing to cross-reference other weeks.

### R2. Hierarchical Obsidian Note Structure & Math
Format all output using Obsidian-compatible markdown:
- Clean hierarchical outline using bullet points (`- `, `\t- `) and clear headings (`#`, `##`, `###`).
- Bold key terms and definitions.
- All mathematical formulas, network parameters, and equations (e.g., Nyquist, Shannon capacity, attenuation, framing/CRC) must be rendered in standard LaTeX math notation (`$...$` for inline, `$$...$$` for block).
- Represent architecture diagrams, protocol stacks, and flowcharts using clear text descriptions, ASCII/Unicode tables, or markdown tables.

### R3. Frontmatter Preservation & Integration
- Preserve existing YAML frontmatter at the top of each file intact (e.g. `Week:`, `Date:`, `tags:`, `Slides Link:`).
- For `1. Internet Background.md`: preserve existing bullet points and diagrams below the frontmatter, seamlessly expanding and completing all missing topics from `Lecture1.pdf`.
- For `2. Physical Layer.md` and `3. Data Link Layer.md`: populate the blank body below the frontmatter with full, comprehensive lecture notes.

## Acceptance Criteria

### Content Completeness
- [ ] `1. Internet Background.md` contains the full breadth of topics from `Lecture1.pdf`, retaining all existing notes and frontmatter while adding missing sections.
- [ ] `2. Physical Layer.md` contains complete, detailed summary notes covering all topics from `Lecture2.pdf`.
- [ ] `3. Data Link Layer.md` contains complete, detailed summary notes covering all topics from `Lecture3.pdf`.

### Formatting & Syntax Verification
- [ ] All three files preserve their initial YAML frontmatter between `---` fences.
- [ ] Formulas and mathematical derivations use valid LaTeX syntax with balanced `$` or `$$` delimiters.
- [ ] Notes adhere consistently to the hierarchical bulleted outline style with bold key terms.
