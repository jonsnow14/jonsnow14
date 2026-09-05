<div align="center">

# Vishal Kumar

**AI Engineer** · RAG, agents, applied ML · Remote

[![Email](https://img.shields.io/badge/email-vishalvoid4%40gmail.com-1B365D?style=flat-square&logo=gmail&logoColor=white)](mailto:vishalvoid4@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vishal--kumar-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishal-kumar-77950554/)
[![Manaswi](https://img.shields.io/badge/Manaswi-manaswi.fly.dev-1B365D?style=flat-square)](https://manaswi.fly.dev/)
[![Notes](https://img.shields.io/badge/notes-jonsnow14.github.io-181717?style=flat-square&logo=github)](https://jonsnow14.github.io/)

</div>

Five years building applied ML and LLM systems across manufacturing, supply chain, healthcare, and education. I ship RAG and agent products — hybrid retrieval, fail-closed ACLs, citation grounding, eval harnesses — on Azure. Production computer-vision and time-series models I built are used by **Mahindra**, **Flexera**, and **Dorman**.

---

<h2>
  <img src="assets/live-dot.gif" width="18" height="18" alt="live" />
  Now
  <img src="assets/live-badge.gif" height="20" alt="LIVE" />
</h2>

<img src="assets/live-dot.gif" width="13" height="13" alt="live" /> **[Manaswi](https://manaswi.fly.dev/)** — AI co-learner and teacher assistant on Sarvam-105B. Mock interviews, Feynman-style concept checks, plagiarism review, assignment/test design, classroom translation, and progress tracking.

<img src="assets/live-dot.gif" width="13" height="13" alt="live" /> **[ClinAssistIndia](https://github.com/jonsnow14/clinassitInda)** — PHC case workspace (POC, rural India). A Hinglish / Hindi / English note becomes an ICMR-grounded clinical card: urgency, ICD-10, PHC-feasible steps, referral. RAG over official ICMR Standard Treatment Workflows (Chroma MiniLM → Sarvam-105B). Human-triggered ops for beds, ambulance, pharmacy, expert, SOS. Silent FHIR R4 bundles on disk. Decision support only — treating judgment stays with the clinician.

---

## Work experience

**AI Engineer** · [Manaswi](https://manaswi.fly.dev/) · [ClinAssistIndia](https://github.com/jonsnow14/clinassitInda) · Remote · independent product work  
*April 2026 – Present*

- **Manaswi:** AI co-learner and teacher assistant — mock interviews, Feynman-style concept checks, plagiarism review, assignment/test design, classroom translation, and progress tracking. Built on Sarvam-105B.
- **ClinAssistIndia** (POC, rural PHCs): Hinglish / Hindi / English note → ICMR-grounded clinical card (urgency, ICD-10, feasible steps, referral). RAG over ICMR PDFs (Chroma MiniLM → Sarvam-105B). FHIR R4 bundles on disk; ops agents for beds, ambulance, pharmacy, SOS.

**AI Engineer** · [Justuju](https://justuju.in) · AI consultant and SME for a junior team on ed-tech products  
*January 2025 – March 2026*

- **EvalAI:** handwritten flowcharts → executable Python (and code → Mermaid); CrewAI multi-agent RAG engine for high-school Math/Physics assessments. File-level Gemini token telemetry so cost is visible per file, not only as console aggregates.

**Career break**  
*October 2023 – October 2024*

Family responsibilities and travel. Oct–Dec 2024: volunteer with ICPC India on an AI plagiarism-checker POC for code submissions.

**Data Scientist** · Bristlecone · Intern → Associate Data Scientist → Data Scientist  
*January 2020 – October 2023*  
Mahindra, Flexera, Dorman, Corning

- Owned an NLP retrieval system that extracted root causes from English mechanical-failure writeups at Mahindra Research Valley, Chennai. **~60%** average reduction in ORC closing time. Out-of-cycle promotion for this work.
- Computer-vision sealant-fault detector for Mahindra plants (poor-quality images). VAPT reported **~90%** increase in fault detection without stopping the line. Recognized by the VP, Mahindra Emerging Tech Division, Mumbai.
- Time-series license-demand forecast for Flexera (holidays, attrition, sparse history, overlapping seasonality) and units-sold forecast for Dorman with concept drift on non-stationary data.
- Real-time YOLO proximity alerts on Mahindra plant floors. Azure Custom Vision ANPR retrained for graffiti, occlusion, and degraded Indian plates. Tender-document integrity: Azure OCR (Read API) + clause-level diff, reviewed on Azure App Service.

---

## Selected work

| Project | What it is | Links |
| --- | --- | --- |
| **Enterprise Knowledge Assistant** | Agent-free Azure RAG over HR / Finance / IT / Legal / Sales policy. Hybrid BM25 + vector search, fail-closed ACL filters, evidence gate, citation allowlist. ~40-case golden set on Azure AI Foundry: groundedness **~4.6/5**, relevance **~4.5/5**, `citation_ok` **1.0**. | [repo](https://github.com/jonsnow14/rag-based-enterprise-knowledge-assistant) · [live](https://northwind-rag-azure.azurewebsites.net) |
| **ClinAssistIndia** | ICMR-grounded PHC workspace: clinical card + beds / ambulance / pharmacy / SOS agents. Next.js + FastAPI + Sarvam. | [repo](https://github.com/jonsnow14/clinassitInda) |
| **Local private RAG** | Conversational Q&A over your PDFs with Ollama, LangChain, ChromaDB, HuggingFace. No API keys. Nothing leaves the machine. | [repo](https://github.com/jonsnow14/local-private-RAG-pipeline) |
| **EvalAI @ Justuju** | Handwritten flowcharts → executable Python (and code → Mermaid). CrewAI multi-agent RAG that drafts high-school Math/Physics tests. File-level Gemini token and cost telemetry. | [justuju.in](https://justuju.in) |

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
