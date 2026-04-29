<div align="center">
  <br>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="OpenAI Logo" width="80"/>
  <h1>⬡ OpenAI Codex — The Definitive Guide</h1>
  <p><strong>Advanced Masterclass on the Codex Agentic Ecosystem (April 2026 Edition)</strong></p>
  <p><em>Desktop App-first, with CLI, IDE, CI/CD, and external tools as complementary surfaces.</em></p>
</div>

---

## 📌 Vision and Scope

Welcome to the official repository of the **Definitive Course on OpenAI Codex**. This is an advanced operational masterclass for designing, governing, and verifying agentic workflows with Codex.

In 2026, interacting with Artificial Intelligence in software engineering has evolved from simple autocompletion (like Copilot) to **autonomous agentic orchestration**.

Codex is no longer just a chat to paste code into: it's an operational environment where the **Desktop App serves as the Command Center**. This course teaches **Workflow Engineering**: how to isolate specialized agents, manage Context Budgets, and implement security protocols for teams (Sandbox and Auditing).

If you want to move from asking an LLM questions to **governing a team of sub-agents** that write, verify, test, and execute adversarial reviews completely autonomously, you're in the right place.

---

## 🏗️ The Codex Ecosystem Architecture

The course deeply explores how Codex's operational surfaces interact in a modern development stack:

1. **Desktop App (Command Center)**: The control panel where you orchestrate *Subagents in parallel*, manage Task Panels, monitor real-time logs, and use **Computer Use** to visually interact with UIs and integrated browsers.
2. **The IDE Extension (Tactical Mode)**: Micro-editing, inline explanations, and localized refactoring in the current file.
3. **The CLI & GitHub Actions (Automation Mode)**: Headless execution. Working with Codex in the background on isolated Git `worktrees`, or automating Pull Request reviews in CI/CD via `codex-action`.

---

## 🧠 The Course Pillars

The course is organized into 25 main modules plus advanced labs and operational playbooks.

### 1. Desktop App as Command Center
- Task Panel
- Worktrees
- Diff review
- Browser and Computer Use
- Artifact viewer
- Automations
- Windows/WSL2 setup

### 2. Operational Workflow P-S-I-V-R
- **Plan**: Read-only exploration and generation of a technical plan highlighting risks.
- **Scope**: Reducing the modification perimeter.
- **Implement**: Incremental code writing.
- **Verify**: Running tests before confirmation.
- **Review (Adversarial)**: Adversarial review loop to find bugs and flaws.
- **Handoff**: Surgical context synchronization between agents.

### 3. Multi-Agent Engineering
- Role cards
- Worker context
- Agent state
- Orchestrator
- Vector DB
- Chronicle

### 4. Plugin & Skill Engineering
- `openai/plugins`
- `.codex-plugin/plugin.json`
- Skills
- MCP
- Commands
- Hooks
- Marketplace

### 5. Knowledge & Automation Layer
- Obsidian
- NotebookLM
- LLM Wiki
- Figma
- n8n
- Cursor
- Antigravity
- Claude Code

---

## 🛠️ How to Use This Repository

The main course is contained in the HTML file:

- `openai_codex_corso_definitivo_it.html` — Italian version
- `openai_codex_corso_definitivo_en.html` — English version

Open it in a modern browser:

```bash
git clone https://github.com/rthgit/corso-codex.git
cd corso-codex
open openai_codex_corso_definitivo_en.html
```

On Windows:

```powershell
start openai_codex_corso_definitivo_en.html
```

The file is designed as a standalone visual course: it requires no build, local server, or dependencies.

---

## 💡 Real Snippet: The Handoff Prompt

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

For tech leads, the course analyzes governance in depth:
- Mandatory use of global `config.toml` distributed via secret manager.
- Implementation of **Rules** (`allowlist` / `denylist`) to natively prevent the agent from executing destructive commands.
- **Permissive Profiles** Architecture: limited sandbox profiles for Code Reviewers (`workspace-read`), isolated advanced profiles for Implementers.

---
> Built for software engineers who want to scale. Optimized for absolute quality. Architected for the Enterprise.
