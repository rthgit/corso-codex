# ⬡ OpenAI Codex — Corso Definitivo (Edizione Aprile 2026)

Benvenuto nel repository ufficiale del **Corso Definitivo su OpenAI Codex**. Questa guida rappresenta il riferimento più avanzato e completo oggi disponibile per padroneggiare l'ecosistema agentico di Codex (Desktop App, CLI, Integrazioni CI/CD) in ambienti di produzione e contesti Enterprise.

## 📌 Cos'è questo corso?

A differenza delle guide di base sul prompt engineering, questo corso si focalizza sull'**Ingegneria dei Workflow Agentici**. Ti insegnerà come trasformare la Codex Desktop App e la CLI in un vero e proprio "Command Center" per la gestione parallela di agenti specializzati, integrando le migliori pratiche architetturali del 2026.

## 🚀 Cosa imparerai

Il corso è diviso in **14 Moduli** progressivi che coprono:

- **Basi Avanzate & CLI:** Utilizzo dei modelli (`codex-1`, `codex-mini-latest`, `gpt-5.5`), gestione dei context budget e Slash Commands.
- **Workflow Architetturale:** Il pattern P-S-I-V-R (Plan, Scope, Implement, Verify, Review) e la tecnica dell'Adversarial Review.
- **Desktop App Mastery:** Utilizzo dei **Task Panels**, **Worktrees** paralleli per l'isolamento degli esperimenti, e l'integrazione del **Computer Use** per l'interazione visiva e il debugging di UI.
- **Agent Workforce Management:** Creazione di *Role Cards* per specializzare i worker (es. test-quality, backend-api) isolando il loro ambito di azione (`state.json`, `owned_paths`).
- **Orchestration & Vector DB:** Creazione di una memoria a lungo termine per progetti multi-agente, dove un orchestratore valida ed estrae fatti durevoli da passare al Vector Database locale.
- **Enterprise Security & Governance:** Isolamento a livello OS (Seatbelt/Landlock), livelli di Sandbox, `.codex/config.toml` e Continuous Integration via GitHub Actions.

## 📂 Struttura del Repository

- `openai_codex_corso_definitivo_con_community.html`
  **[Source of Truth]** Il documento del corso vero e proprio. È un file HTML autoconclusivo, responsive, ad alto contrasto e pronto sia per la lettura offline che per la stampa/esportazione in PDF. Contiene tutto il materiale, i template YAML e i prompt operativi (copy-paste ready).
  
- `codex_desktop_app_corso_pratico_tricks (1).html`
  Il draft originale che conteneva trick community-sourced, successivamente ri-strutturato, ripulito e fuso nel file definitivo. (Mantenuto per storico).

## 🛠️ Come usare questa guida

1. **Clona o scarica** questo repository.
2. Fai doppio clic sul file `openai_codex_corso_definitivo_con_community.html` per aprirlo nel tuo browser.
3. Affianca la guida al tuo IDE e alla Desktop App di Codex.
4. Usa i prompt evidenziati nei box `PROMPT` per avviare le tue sessioni.

## 🎯 A chi è rivolto

- **Software Engineers** che vogliono raddoppiare la loro velocità di iterazione mantenendo il controllo assoluto su codice e test.
- **AI Engineers & Tech Leads** che devono definire la governance, i security audit e i workflow per interi team di sviluppo.
- Chiunque voglia andare oltre l'uso "chat" dell'AI per abbracciare l'automazione algoritmica strutturata.

---

*Costruito per l'ecosistema Codex — Ottimizzato per la qualità del codice — Progettato per l'Enterprise.*
