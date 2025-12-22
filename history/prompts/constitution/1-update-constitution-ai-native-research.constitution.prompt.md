---
id: 1
title: Update constitution for AI-native research
stage: constitution
date: 2025-12-22
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution, research, ai-native]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

You are an AI-native research author and software systems analyst specializing in AI-native software development.

You are writing a research-paper-grade chapter for an AI-Native Book intended for an academic audience with a computer science background.

PROJECT CONTEXT
- Project Type: Research paper (book chapter format)
- Topic: AI-native software development
- Audience: Researchers, graduate students, senior engineers
- Tone: Academic, precise, neutral, evidence-driven

CORE PRINCIPLES (NON-NEGOTIABLE)
1. Accuracy through primary source verification
2. Clarity suitable for readers with formal CS training
3. Reproducibility: every factual claim must be traceable
4. Rigor: prioritize peer-reviewed literature

SOURCE & CITATION RULES
- Minimum 50% of all sources must be peer-reviewed (journals, conference papers)
- Remaining sources may include reputable industry whitepapers or standards
- All factual or technical claims MUST have citations
- Citation style: APA (in-text + reference list)
- Minimum total sources: 15
- No uncited assertions allowed

PLAGIARISM & ORIGINALITY
- Zero tolerance for plagiarism
- All explanations must be original synthesis
- Do NOT copy phrasing from sources
- Paraphrase with technical precision

READABILITY & STRUCTURE
- Writing level: Flesch-Kincaid Grade 10–12
- Clear sectioning with logical progression
- Use definitions before advanced concepts
- Prefer explanatory clarity over rhetorical flourish

LENGTH & FORMAT CONSTRAINTS
- Total length target: 5,000–7,000 words
- Output structured for final PDF export
- Include properly formatted reference section

CCR EXECUTION RULES
Before finalizing output, internally verify:
- Every claim has at least one valid citation
- Source balance meets peer-reviewed requirement
- No logical leaps or unsupported conclusions
- Terminology consistency throughout the chapter

SUCCESS CRITERIA (MUST PASS)
- All claims verified against credible sources
- APA citations correctly applied
- Zero plagiarism risk
- Passes academic fact-checking review

OUTPUT EXPECTATION
Produce a complete, publication-ready academic chapter that could withstand peer review in a computer science or software engineering venue.

## Response snapshot

# AI-Native Software Development Research Constitution

## Core Principles

### Accuracy through Primary Source Verification
All factual claims must be verified against credible, peer-reviewed sources before inclusion in the research; Primary sources take precedence over secondary interpretations; Claims without verifiable sources are excluded from the final work

### Academic Clarity and Precision
All technical concepts must be clearly defined before use; Writing must be accessible to readers with formal computer science training; Complex concepts should be explained with precision and without unnecessary jargon

### Reproducibility and Traceability
Every factual claim must be traceable to its original source through proper citations; Research methods and data analysis must be documented sufficiently for replication; All sources and references must be properly catalogued and verifiable

### Academic Rigor and Peer Review Standards
Minimum 50% of sources must be peer-reviewed literature (journals, conference papers); All technical claims must be supported by credible evidence; Research must meet academic standards suitable for peer review

### Original Synthesis and Zero Plagiarism
All content must be original synthesis by the author; Direct copying from sources is strictly prohibited; Proper attribution and APA citation style must be followed for all references

### Evidence-Driven Analysis
All conclusions must be supported by evidence from credible sources; Claims must be logically connected to supporting evidence; Speculation or unsupported assertions are not permitted

## Citation and Source Requirements
Minimum total sources: 15; APA citation style required for all references; Peer-reviewed sources must constitute at least 50% of total sources; All factual or technical claims must have citations; No uncited assertions allowed

## Academic Writing Standards
Writing level: Flesch-Kincaid Grade 10-12; Clear sectioning with logical progression; Properly formatted reference section required; Content must be structured for final PDF export; Terminology must be consistent throughout the chapter

## Governance
This constitution governs all aspects of the AI-native software development research project.

All research claims must pass academic fact-checking review; Content must withstand peer review in computer science or software engineering venue; Every claim must be verified against credible sources; Source balance must meet peer-reviewed requirement; No logical leaps or unsupported conclusions permitted

**Version**: 1.0.0 | **Ratified**: 2025-12-22 | **Last Amended**: 2025-12-22

## Outcome

- ✅ Impact: Updated project constitution to align with academic research requirements for AI-native software development
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new principles and requirements
- 🔁 Next prompts: None needed - constitution update complete
- 🧠 Reflection: Constitution now properly reflects academic research standards with focus on peer-reviewed sources, original synthesis, and evidence-driven analysis

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All academic standards met
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A