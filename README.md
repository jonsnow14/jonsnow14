<div align="center">

# Vishal Kumar

**AI Engineer** · RAG, agents, applied ML · Remote

[![Email](https://img.shields.io/badge/email-vishalvoid4%40gmail.com-1B365D?style=flat-square&logo=gmail&logoColor=white)](mailto:vishalvoid4@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vishal--kumar-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishal-kumar-77950554/)
[![Manaswi](https://img.shields.io/badge/Manaswi-manaswi.fly.dev-1B365D?style=flat-square)](https://manaswi.fly.dev/)
[![Notes](https://img.shields.io/badge/notes-jonsnow14.github.io-181717?style=flat-square&logo=github)](https://jonsnow14.github.io/)

</div>

Five years building applied ML and LLM systems across manufacturing, supply chain, healthcare, and education. I ship RAG and agent products — hybrid retrieval, fail-closed ACLs, citation grounding, eval harnesses . Production computer-vision and time-series models I built are used by **Mahindra**, **Flexera**, and **Dorman**.

---

<h2>
  <img src="assets/live-dot.gif" width="18" height="18" alt="live" />
  Now
  <img src="assets/live-badge.gif" height="20" alt="LIVE" />
</h2>

<img src="assets/live-dot.gif" width="13" height="13" alt="live" /> **[Manaswi](https://manaswi.fly.dev/)** — AI co-learner and teacher assistant. Mock interviews, Feynman-style concept checks, assignment/test design, classroom translation, and progress tracking. Plagiarism review is a class-local lexical detector, not a web-scale “% copied” score: word 5-grams, containment (not Jaccard), and an adaptive window `W(n) = clamp(floor(n/3), 30, 100)` with a higher match bar on short CBSE answers. Scoring is closed-form (no HTTP in the scorer); Sarvam-105B only narrates spans already found. Evidence for the teacher, not a verdict. [How it works](https://www.linkedin.com/pulse/how-manaswi-detects-plagiarism-part-ii-mathematics-limits-kumar-lipvc/)

<img src="assets/live-dot.gif" width="13" height="13" alt="live" /> **[ClinAssistIndia](https://github.com/jonsnow14/clinassitInda)** — PHC case workspace (POC, rural India). A Hinglish / Hindi / English note becomes an ICMR-grounded clinical card: urgency, ICD-10, PHC-feasible steps, referral. RAG over official ICMR Standard Treatment Workflows (Chroma MiniLM → Sarvam-105B). Human-triggered ops for beds, ambulance, pharmacy, expert, SOS. Silent FHIR R4 bundles on disk. Decision support only — treating judgment stays with the clinician.

<img src="assets/live-dot.gif" width="13" height="13" alt="live" /> **[Enterprise Knowledge Assistant](https://github.com/jonsnow14/rag-based-enterprise-knowledge-assistant)** — Agent-free Azure RAG over HR / Finance / IT / Legal / Sales policy. Hybrid BM25 + vector search, fail-closed ACL filters, evidence gate, citation allowlist. ~40-case golden set on Azure AI Foundry: groundedness **~4.6/5**, relevance **~4.5/5**, `citation_ok` **1.0**. [Live demo](https://northwind-rag-azure.azurewebsites.net). Ingest is structure-first, then length: split on policy headings and Excel sheets, then `C(n) = clamp(floor(n/α), 128, 512)`. On the live Northwind pack (112 chunks / 11 files) the proportional band is empty — what shipped is one heading, one chunk, plus atomic sheets. Length-adaptive windows are implemented for longer sections; they did not produce this index. [Write-up](https://www.linkedin.com/pulse/structure-first-adaptive-chunking-enterprise-rag-part-vishal-kumar-1yljc/)

---

## Impact

Shipped for **Mahindra**, **Flexera**, **Dorman**, and **Corning**. Intern → Associate Data Scientist → Data Scientist. Out-of-cycle promotion for the Mahindra NLP work.

| Client | What shipped | Result |
| --- | --- | --- |
| [Manaswi](https://manaswi.fly.dev/) · plagiarism | Class-local 5-gram detector with length-adaptive windows and τ. Stylometry is a side channel and cannot move the risk band. LLM explains; it does not score. | Labelled synthetic CBSE physics (200 + 500): verbatim **1.00**, near-verbatim **0.99**; paraphrase miss by design; independent overlap **~0.3–0.6**. [Part II](https://www.linkedin.com/pulse/how-manaswi-detects-plagiarism-part-ii-mathematics-limits-kumar-lipvc/) |
| Enterprise Knowledge Assistant · ingest | Structure-first policy chunker: do not merge short headings to fill 512 tokens; keep sheets whole; prefix vectors, leave BM25 unprefixed. `C(n)` is implemented. | **112** chunks from 11 files (98 section / 4 sheet / 10 window). Length-adaptive band unused on this short pack. [Part I](https://www.linkedin.com/pulse/structure-first-adaptive-chunking-enterprise-rag-part-vishal-kumar-1yljc/) |
| Mahindra Research Valley, Chennai | NLP retrieval that extracted root causes from English mechanical-failure writeups | **~60%** average reduction in ORC closing time |
| Mahindra plants | Computer-vision sealant-fault detector on poor-quality line images | VAPT reported **~90%** increase in fault detection without stopping the line. Recognized by the VP, Mahindra Emerging Tech Division, Mumbai |
| Flexera / Dorman | Time-series license-demand and units-sold forecasts (holidays, attrition, sparse history, overlapping seasonality, concept drift) | Production forecasts on non-stationary demand |
| Mahindra shop floor + tenders | Real-time YOLO proximity alerts; Azure Custom Vision ANPR retrained for graffiti, occlusion, and degraded Indian plates; Azure OCR (Read API) + clause-level tender diffs on App Service | Live CV + document-integrity review |
| [justuju.in](https://justuju.in) · EvalAI | Automated evaluation of student submissions (flowcharts → code, code → Mermaid, Math/Physics tests). The same junior team of 7–8 used the tool instead of grading by hand | **~50–60** submissions/day manually → **~1,000**/day with the tool; **~98%** accuracy on handwritten flowchart → Python |

---

## Work experience

| Role | Where | When | One-liner |
| --- | --- | --- | --- |
| <img src="assets/live-dot.gif" width="13" height="13" alt="live" /> AI Engineer and Creator <img src="assets/present-badge.gif" height="16" alt="doing at present" /> | [Manaswi](https://manaswi.fly.dev/) · [ClinAssistIndia](https://github.com/jonsnow14/clinassitInda) | Apr 2026 – Present | Independent product work: Sarvam-105B co-learner and ICMR-grounded PHC workspace |
| AI Engineer | [justuju.in](https://justuju.in) | Jan 2025 – Mar 2026 | AI consultant and SME; EvalAI for ed-tech assessments |
| Career break | — | Oct 2023 – Oct 2024 | Family and travel; ICPC India AI plagiarism-checker POC |
| Data Scientist | Bristlecone | Jan 2020 – Oct 2023 | Intern → Associate DS → DS; NLP, CV, and forecasting for Mahindra, Flexera, Dorman, Corning |

---

## Stack

**Languages & ML** — Python, SQL, PyTorch, scikit-learn, pandas, NumPy, OpenCV, YOLO, NLTK

**LLM systems** — RAG, hybrid BM25 + vector search, agentic workflows, evaluation, guardrails, token/cost telemetry, DSPy, LangChain, CrewAI

**Platform** — FastAPI, PostgreSQL, MongoDB, ChromaDB, Azure (OpenAI, AI Search, Foundry, App Service), AWS

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img alt="Azure" src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" />
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" />
  <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" />
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
  <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
</p>

---

## Notes

Writing down how the pieces actually work:

- [How Manaswi detects plagiarism — Part II](https://www.linkedin.com/pulse/how-manaswi-detects-plagiarism-part-ii-mathematics-limits-kumar-lipvc/) — adaptive windows, containment, measured limits
- [Structure-first adaptive chunking — Part I](https://www.linkedin.com/pulse/structure-first-adaptive-chunking-enterprise-rag-part-vishal-kumar-1yljc/) — what shipped on the 112-chunk Northwind index vs what is still Phase II
- [How RAG Works: Part I](https://jonsnow14.github.io/ai/rag/deep-dive/2026/06/18/how-rag-works-part1.html) — why a plain LLM falls short, and how retrieval before generation fixes it
- [How Agentic RAG Works: Part I](https://jonsnow14.github.io/ai/rag/agents/deep-dive/2026/06/18/agentic-rag-part1.html) — from single-pass retrieval to self-correcting agents
- [How Claude CLI Works: Part I](https://jonsnow14.github.io/ai/cli/deep-dive/2026/06/17/how-claude-cli-works-part1.html) — sessions, context, memory limits, and where a coding agent can be attacked

---

## Education

**B.Tech**, Electrical and Electronics Engineering — Manipal University Jaipur, 2020

---

<div align="center">

Open to remote work on RAG, agents, eval, and production ML.

[vishalvoid4@gmail.com](mailto:vishalvoid4@gmail.com) · [LinkedIn](https://www.linkedin.com/in/vishal-kumar-77950554/) · [Manaswi](https://manaswi.fly.dev/)

</div>
