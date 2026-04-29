<div align="center">
  <br>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="OpenAI Logo" width="80"/>
  <h1>⬡ OpenAI Codex — La Guida Definitiva</h1>
  <p><strong>Masterclass Avanzata sull'Ecosistema Agentico di Codex (Edizione Aprile 2026)</strong></p>
  <p><em>Desktop App-first, con CLI, IDE, CI/CD e strumenti esterni come superfici complementari.</em></p>
</div>

---

## 📌 Visione e Scopo

Benvenuto nel repository ufficiale del **Corso Definitivo su OpenAI Codex**. Questa è una masterclass operativa avanzata per progettare, governare e verificare workflow agentici con Codex.

Nel 2026, l'interazione con l'Intelligenza Artificiale nel software engineering è passata dal semplice autocompletamento (tipo Copilot) all'**orchestrazione agentica autonoma**. 

Codex non è più solo una chat in cui incollare codice: è un ambiente operativo dove la **Desktop App funge da Command Center**. Questo corso insegna l'**Ingegneria dei Workflow**: come isolare agenti specializzati, come gestire il Context Budget e come implementare protocolli di sicurezza per i team (Sandbox e Audit).

Se vuoi passare dal fare domande a un LLM al **governare un team di sub-agenti** che scrivono, verificano, testano ed eseguono review avversariali in totale autonomia, sei nel posto giusto.

---

## 🏗️ L'Architettura dell'Ecosistema Codex

Il corso esplora profondamente come le superfici operative di Codex interagiscono in uno stack di sviluppo moderno:

1. **Desktop App (Command Center)**: Il pannello di controllo dove orchestrare *Subagents in parallelo*, gestire Task Panels, monitorare log in tempo reale e usare il **Computer Use** per interagire visivamente con UI e Browser integrati.
2. **L'Estensione IDE (Tactical Mode)**: Micro-editing, spiegazioni inline e refactoring localizzato nel file corrente.
3. **La CLI & GitHub Actions (Automation Mode)**: L'esecuzione headless. Lavorare con Codex in background su `worktrees` Git isolati, oppure automatizzare review di Pull Request in CI/CD tramite `codex-action`.

---

## 🧠 I Pilastri del Corso

Il corso è organizzato in 27 moduli principali più laboratori avanzati e playbook operativi.

### 1. Desktop App come Command Center
- Task Panel
- Worktrees
- Diff review
- Browser e Computer Use
- Artifact viewer
- Automations
- Windows/WSL2 setup

### 2. Workflow Operativo P-S-I-V-R
- **Plan**: Esplorazione read-only e generazione di un piano tecnico con evidenza dei rischi.
- **Scope**: Riduzione del perimetro di modifica.
- **Implement**: Scrittura incrementale del codice.
- **Verify**: Esecuzione dei test prima della conferma.
- **Review (Adversarial)**: Loop di review avversariale per trovare bug e falle.
- **Handoff**: Sincronizzazione chirurgica del contesto tra agenti.

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

## 🛠️ Come Utilizzare Questo Repository

Il corso principale è contenuto nel file HTML:

- `openai_codex_corso_definitivo_it.html` — versione italiana
- `openai_codex_corso_definitivo_en.html` — versione inglese

Aprilo in un browser moderno:

```bash
git clone https://github.com/rthgit/corso-codex.git
cd corso-codex
open openai_codex_corso_definitivo_it.html
```

Su Windows:

```powershell
start openai_codex_corso_definitivo_it.html
```

Il file è progettato come corso visuale standalone: non richiede build, server locale o dipendenze.

---

## 💡 Snippet Reale: Il Prompt dell'Handoff

```markdown
Prima di chiudere questa sessione, scrivi un file HANDOFF.md con:
1. Cosa stavamo costruendo (obiettivo preciso)
2. Cosa hai già implementato (con path esatti ai file)
3. Cosa ha funzionato e cosa no (tentativi falliti, in modo da non ripeterli)
4. Lo stato attuale dei test (passano? falliscono? quali?)
5. I prossimi 3 step ESATTI da eseguire nella prossima sessione
6. Eventuali "gotchas" scoperti

Il prossimo agente leggerà SOLO questo file per continuare. Sii chirurgico e preciso.
```

## 🔒 Focus: Enterprise & Security

Per i tech lead, il corso analizza in profondità la governance:
- Utilizzo obbligatorio del `config.toml` globale distribuito via secret manager.
- Implementazione delle **Rules** (`allowlist` / `denylist`) per impedire all'agente di eseguire comandi distruttivi.
- Architettura a **Profili Permissivi**: sandbox limitate per i Code Reviewer (`workspace-read`), profili avanzati isolati per gli Implementer.

---

> Costruito per gli ingegneri del software che vogliono scalare. Ottimizzato per la qualità assoluta. Architettato per l'Enterprise.
