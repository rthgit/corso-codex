<div align="center">
  <br>
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="OpenAI Logo" width="80"/>
  <h1>⬡ OpenAI Codex — La Guida Definitiva</h1>
  <p><strong>Masterclass Avanzata sull'Ecosistema Agentico di Codex (Edizione Aprile 2026)</strong></p>
  <p><em>Da zero all'ingegneria dei workflow automatizzati: CLI, Desktop App, Worktrees, Handoffs e Governance Enterprise.</em></p>
</div>

---

## 📌 Visione e Scopo

Benvenuto nel repository del **Corso Definitivo su OpenAI Codex**. Nel 2026, l'interazione con l'Intelligenza Artificiale nel software engineering è passata dal semplice autocompletamento (tipo Copilot) all'**orchestrazione agentica autonoma**. 

Codex non è più solo una chat in cui incollare codice: è un ambiente operativo composto da più "superfici" che lavorano in parallelo. Questo corso non ti insegna dei semplici "prompt magici", ma l'**Ingegneria dei Workflow**: come costruire un "Command Center" per la tua codebase, come isolare agenti specializzati, come gestire il Context Budget e come implementare protocolli di sicurezza per i team (Sandbox e Audit).

Se vuoi passare dal fare domande a un LLM al **governare un team di sub-agenti** che scrivono, verificano, testano ed eseguono review avversariali in totale autonomia, sei nel posto giusto.

---

## 🏗️ L'Architettura dell'Ecosistema Codex

Il corso esplora profondamente come le tre superfici operative di Codex interagiscono in uno stack di sviluppo moderno:

1. **L'Estensione IDE (Tactical Mode)**: Micro-editing, spiegazioni inline e refactoring localizzato nel file corrente.
2. **La Desktop App (Command Center)**: Il pannello di controllo dove orchestrare *Subagents in parallelo*, gestire Task Panels, monitorare log in tempo reale e usare il **Computer Use** per interagire visivamente con UI e Browser integrati.
3. **La CLI & GitHub Actions (Automation Mode)**: L'esecuzione headless. Lavorare con `codex-1` in background su `worktrees` Git isolati, oppure automatizzare review di Pull Request in CI/CD tramite `codex-action`.

---

## 🧠 I Pilastri del Corso (I 25 Moduli)

Il documento principale (vedi sezione "Come Utilizzare") è strutturato in 25 moduli densi di contenuto tecnico, diagrammi e prompt copy-paste ready.

### 1. Fondamenta e Governance
- **Configurazione e Setup (`.codex/config.toml`)**: Policy di approvazione e livelli di Sandbox.
- **Context Budgeting e Memoria**: `/compact`, `/clear` e inclusione esplicita di contesto.

### 2. Il Framework Operativo (P-S-I-V-R)
- **Workflow Definitivo**: Plan, Scope, Implement, Verify, Review.
- **Battlefield: I 10 Trucchi Reali**: Micro-abitudini operative per la Desktop App (Stop before code, Diff budget, Regression first).

### 3. Desktop App & Super-App Mastery
- **Worktree Orchestration**: Lavorare in isolamento su branch paralleli.
- **GPT Image Access**: Usare screenshot e mockup come input per il coding e il debugging.
- **Artifact Viewer & Task Sidebar**: Gestire documenti, PDF, spreadsheet e deck direttamente in Codex.
- **Windows Power-User**: Setup avanzato con PowerShell, WSL2 e GitHub CLI.

### 4. Multi-Agent & Orchestration
- **Control Room Multi-Agente**: Far collaborare Codex, Claude Code, Cursor e Antigravity nello stesso workspace senza conflitti.
- **Role Cards & Worker Context**: Pattern per dotare gli agenti di ruoli specializzati e memoria locale (`state.json`).
- **Plugin Engineering**: Sviluppare skill e plugin custom utilizzando il repository `openai/plugins`.

### 5. Knowledge Management & Automazione
- **Knowledge Workspace**: Integrazione con Obsidian e NotebookLM per la gestione della conoscenza operativa.
- **Figma & n8n Layer**: Workflow design-to-code e automazione dei task tramite trigger esterni.
- **Chronicle & Handoffs**: Mantenere un diario operativo del progetto per la sincronizzazione tra agenti e umani.

---

## 🛠️ Come Utilizzare Questo Repository

Il "succo" del corso è interamente contenuto in un file HTML ingegnerizzato per garantire la migliore UX visiva (High Contrast, Layout Enterprise, Esportabile in PDF).

1. Clona il repository:
   ```bash
   git clone https://github.com/rthgit/corso-codex.git
   cd corso-codex
   ```
2. Apri il file **`openai_codex_corso_definitivo_con_community.html`** in un qualsiasi browser moderno (Chrome, Edge, Safari).
3. Esplora i moduli, copia i template dei **Prompt Professionali** e applicali direttamente nella tua Codex Desktop App o CLI.

*(Nota: Il file `codex_desktop_app_corso_pratico_tricks (1).html` è una vecchia bozza mantenuta solo per archivio).*

---

## 💡 Snippet Reale: Il Prompt dell'Handoff

Per farti capire il livello di profondità, ecco un esempio di "Trick Operativo" insegnato nel corso per non perdere contesto a fine giornata:

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

Per i tech lead, il corso analizza in profondità la governance. Codex non deve operare come una "scatola nera" pericolosa per il repo:
- Utilizzo obbligatorio del `config.toml` globale distribuito via secret manager.
- Implementazione delle **Rules** (`allowlist` / `denylist`) per impedire nativamente all'agente di eseguire comandi distruttivi o leggere file contenenti token (`.env`).
- Architettura a **Profili Permissivi**: profili sandbox limitati per i Code Reviewer (`workspace-read`), profili avanzati isolati per gli Implementer.

---
> Costruito per gli ingegneri del software che vogliono scalare. Ottimizzato per la qualità assoluta. Architettato per l'Enterprise.
