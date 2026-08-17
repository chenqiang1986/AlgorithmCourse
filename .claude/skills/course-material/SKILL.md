---
name: course-material
description: Use whenever the user wants to create, add, or restructure course slides, lessons, a module, or teaching material for this algorithm course — e.g. "make a lesson on X", "create slides for Y", "add a new module about Z", "write course material for...", "start a new topic folder". Also use when expanding an existing lesson file that has grown too long. Encodes this repo's lesson format: concept-first structure, worked examples, judge-style practice problems, and strict per-file length control via splitting into multiple numbered files.
---

# Course Material Skill

This repo's "slides" are not `.pptx`/reveal.js decks — they are short, focused Markdown
lesson files, one sub-topic per file, indexed by a module `README.md`. Follow this format
unless the user explicitly asks for a different presentation medium.

## Step 0: Orient before writing anything

1. Look at 2-3 sibling files in the target (or a similar) module to confirm language and
   tone. Most modules (`000-Basic`, `001-Tree`, `002-DFS`, `003-BFS`, `004-Math`) use C++.
   The `D0N-*` modules use Python/pandas/sklearn instead. Match whichever family the new
   content belongs to — don't default to C++ blindly.
2. Decide: is this a **new module** (new top-level folder) or **new/expanded lesson(s)**
   inside an existing module?
   - New algorithm module → folder name `NNN-TopicName`, where `NNN` is the next unused
     zero-padded 3-digit number after the highest existing one (check top-level dirs).
   - New data/ML module → folder name `D0N-TopicName`, following the same numbering idea
     within the `D` series.
   - If genuinely ambiguous which module a lesson belongs in, ask the user rather than
     guessing.

## Step 1: Module-level README.md

Every module folder has a `README.md` that acts as the index/syllabus. Structure:

```markdown
# NNN - Topic Name

This folder contains the <topic> section of the algorithm course.

## Course Goals

In this module, we will learn:

1. <most basic concept first>
2. <builds on #1>
3. ...

## Lessons

1. [01-slug.md](./01-slug.md)
   <one-line summary of what this lesson covers>
2. [02-slug.md](./02-slug.md)
   <one-line summary>

More lessons can be added later as the course grows.
```

Keep `Course Goals` ordered from foundational concept to advanced application — it mirrors
the lesson order. When you add or reorder lessons, update this file's list in the same edit.

## Step 2: Lesson file structure

Filename: `NN-kebab-case-slug.md` (zero-padded two digits, lowercase, hyphenated).

Every lesson **must start with the basic concept**, not with a problem or code. The
observed shape, in order:

1. `# Lesson N: Title` + a 1-2 sentence intro of what the lesson covers.
2. **Concept introduction** — define the term, give the mental model, use a small
   diagram/example in a ```text block if helpful. No code yet.
3. **Core template** — the minimal, canonical code pattern for the technique, in a fenced
   code block, introduced only after the concept is understood.
4. One or more **"Reading Example"** sections — a complete, runnable-looking worked
   example with an explanation of the non-obvious details/gotchas immediately after the
   code (why a line is ordered the way it is, what invariant it protects).
5. One or more **"Class Practice N: Title"** sections — this is where example/practice
   problems go. Use judge-style problem format so it doubles as reference and drill:
   ```markdown
   ### Input Format
   ### Output Format
   ### Sample Input
   ### Sample Output
   ### Explanation
   ```
6. Optional **"Common Mistakes"** section for lessons with subtle pitfalls (numbered
   sub-sections like `### N.1 Mistake name`).
7. **"Key Takeaways"** — a short bullet list, near the end.
8. A closing sentence that previews the next lesson (skip only for a module's last lesson).

A dedicated "problem list" file (e.g. `05-usaco-bfs-problems.md`) is a valid, shorter
lesson type: title, a short intro line, a flat list of linked problems grouped by
difficulty, and a one-line "How to Use This List" section. No solution analysis in these.

## Step 3: Length control — split, don't cram

This is the most important rule the user asked for. Observed lesson files run roughly
**150–500 lines**; reference/problem-list files run **20–50 lines**. Before writing:

- **One sub-concept per file.** If you're about to introduce a second genuinely distinct
  idea (e.g. "multi-source BFS" after "single-source BFS", or "grid BFS" after "graph
  BFS"), stop and start a new numbered file instead of adding a new top-level section.
- **Practice-problem lists are their own file**, not appended to a concept lesson, once
  there are more than a couple of external reference problems to list.
- If a file you're editing is approaching ~500 lines, or already covers more than 2-3
  distinct `##` concepts, split the trailing content into `NN+1-*.md` rather than
  continuing to grow it. Renumber only the new file — don't renumber existing files just
  to make room; append at the end of the sequence instead, unless the user asks for a
  reorder.
- Never produce a single giant file that tries to cover a whole module. The module is the
  README plus its many small lesson files, not one big document.

## Step 4: Style details to match

- C++ modules: `snake_case` identifiers, `using namespace std;`, prefer `map`/`set`/
  `vector` over raw arrays for teaching clarity, ```cpp fences.
- Headings use sentence case with numbered prefixes (`## 1. What Is BFS?`).
- Keep prose terse and declarative — short paragraphs and bullet lists, not long
  paragraphs of exposition.
- Cross-link: when a lesson depends on something taught earlier, name the earlier lesson
  file rather than re-explaining it.
- **Math formulas must use LaTeX, not backticks or plain text/```text blocks.**
  - Inline math (variables, short expressions used in a sentence): `$n$`, `$k - 1$`,
    `$x_i \ge 1$`.
  - Display math (standalone formulas/derivations, previously a ```text block): `$$...$$`.
    For multi-line derivations, wrap in `\begin{aligned}...\end{aligned}` inside the `$$`
    and align steps with `&`.
  - Use proper LaTeX operators/spacing instead of ASCII: `\ge`/`\le`/`\ne` not `>=`/`<=`/
    `!=`, `\times` or `\cdot` not `*`, `\cdots`/`\ldots` not `...`, subscripts as `x_1, x_i`
    not `x1, xi`, and `C_n^k` / `\binom{n}{k}` for combinations (match whichever a
    module already uses).
  - This applies to every module (C++ and `D0N-*` alike) — any time a variable, equation,
    or formula appears, even inline in a sentence, use `$...$`/`$$...$$` instead of
    backticks or a plain code fence.

## Step 5: After writing

- Update the module `README.md`'s `Lessons` list (and `Course Goals` if the new lesson
  introduces a new learning objective).
- Re-check the new/edited file's line count; if it drifted past the target range, split
  it before finishing.
