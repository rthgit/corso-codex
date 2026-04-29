<div align="center">
  <br>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="OpenAI Logo" width="80"/>
  <h1>⬡ OpenAI Codex — The Definitive Guide</h1>
  <p><strong>Advanced Masterclass on the Codex Agentic Ecosystem (April 2026 Edition)</strong></p>
  <p><em>From zero to automated workflow engineering: CLI, Desktop App, Worktrees, Handoffs, and Enterprise Governance.</em></p>
</div>

---

## 📌 Vision and Scope

Welcome to the repository of the **Definitive Course on OpenAI Codex**. In 2026, interacting with Artificial Intelligence in software engineering has evolved from simple autocompletion (like Copilot) to **autonomous agentic orchestration**.

Codex is no longer just a chat to paste code into: it's an operational environment made of multiple "surfaces" working in parallel. This course doesn't teach simple "magic prompts," but **Workflow Engineering**: how to build a "Command Center" for your codebase, isolate specialized agents, manage Context Budgets, and implement security protocols for teams (Sandbox and Auditing).

If you want to move from asking an LLM questions to **governing a team of sub-agents** that write, verify, test, and execute adversarial reviews completely autonomously, you're in the right place.

---

## 🏗️ The Codex Ecosystem Architecture

The course deeply explores how Codex's three operational surfaces interact in a modern development stack:

1. **The IDE Extension (Tactical Mode)**: Micro-editing, inline explanations, and localized refactoring in the current file.
2. **The Desktop App (Command Center)**: The control panel where you orchestrate *Subagents in parallel*, manage Task Panels, monitor real-time logs, and use **Computer Use** to visually interact with UIs and integrated browsers.
3. **The CLI & GitHub Actions (Automation Mode)**: Headless execution. Work with `codex-1` in the background on isolated Git `worktrees`, or automate Pull Request reviews in CI/CD via `codex-action`.

---

## 🧠 The Course Pillars (The 25 Modules)

The main document (see the "How to Use" section) is structured into 25 content-dense technical modules, diagrams, and copy-paste ready prompts.

### 1. Foundations and Governance
- **Configuration and Setup (`.codex/config.toml`)**: Approval policies and Sandbox levels.
- **Context Budgeting and Memory**: `/compact`, `/clear` and explicit context inclusion.

### 2. The Operational Framework (P-S-I-V-R)
- **Definitive Workflow**: Plan, Scope, Implement, Verify, Review.
- **Battlefield: The 10 Real Tricks**: Operational micro-habits for the Desktop App (Stop before code, Diff budget, Regression first).

### 3. Desktop App & Super-App Mastery
- **Worktree Orchestration**: Working in isolation on parallel branches.
- **GPT Image Access**: Using screenshots and mockups as input for coding and debugging.
- **Artifact Viewer & Task Sidebar**: Manage documents, PDFs, spreadsheets, and decks directly in Codex.
- **Windows Power-User**: Advanced setup with PowerShell, WSL2, and GitHub CLI.

### 4. Multi-Agent & Orchestration
- **Multi-Agent Control Room**: Orchestrate Codex, Claude Code, Cursor, and Antigravity in the same workspace without conflicts.
- **Role Cards & Worker Context**: Patterns for equipping agents with specialized roles and local memory (`state.json`).
- **Plugin Engineering**: Develop custom skills and plugins using the `openai/plugins` repository.

### 5. Knowledge Management & Automation
- **Knowledge Workspace**: Integration with Obsidian and NotebookLM for operational knowledge management.
- **Figma & n8n Layer**: Design-to-code workflows and task automation via external triggers.
- **Chronicle & Handoffs**: Maintain a project operational diary for agent-to-human synchronization.

---

## 🛠️ How to Use This Repository

The "core" of the course is entirely contained in an HTML file engineered to guarantee the best visual UX (High Contrast, Enterprise Layout, PDF Exportable).

1. Clone the repository:
   ```bash
   git clone https://github.com/rthgit/corso-codex.git
   cd corso-codex
   ```
2. Open the file **`openai_codex_corso_definitivo_con_community_en.html`** in any modern browser (Chrome, Edge, Safari).
3. Explore the modules, copy the **Professional Prompt** templates, and apply them directly in your Codex Desktop App or CLI.

*(Note: The `codex_desktop_app_corso_pratico_tricks (1).html` file is an old draft kept for archival purposes only).*

---

## 💡 Real Snippet: The Handoff Prompt

To help you understand the level of depth, here is an example of an "Operational Trick" taught in the course so you don't lose context at the end of the day:

```markdown
Before closing this session, write a HANDOFF.md file with:
1. What we were building (precise goal)
2. What you have already implemented (with exact file paths)
3. What worked and what didn't (failed attempts, so as not to repeat them)
4. The current state of tests (passing? failing? which ones?)
5. The EXACT next 3 steps to execute in the next session
6. Any discovered "gotchas"

The next agent will read ONLY this file to continue. Be surgical and precise.
```

## 🔒 Focus: Enterprise & Security

For tech leads, the course analyzes governance in depth. Codex must not operate as a dangerous "black box" for the repo:
- Mandatory use of global `config.toml` distributed via secret manager.
- Implementation of **Rules** (`allowlist` / `denylist`) to natively prevent the agent from executing destructive commands or reading files containing tokens (`.env`).
- **Permissive Profiles** Architecture: limited sandbox profiles for Code Reviewers (`workspace-read`), isolated advanced profiles for Implementers.

---
> Built for software engineers who want to scale. Optimized for absolute quality. Architected for the Enterprise.
