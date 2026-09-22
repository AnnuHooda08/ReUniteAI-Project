# ReUniteAI

### AI-Assisted Missing-Person Identity Matcher After Disasters

ReUniteAI is an AI-powered system designed to assist in identifying and reconnecting missing persons with unidentified survivors after disasters. It analyzes multiple sources of information and ranks potential matches for authorized human verification.

## ✨ Features

* 🖼️ **Image Analysis** — Extracts visual and facial features from available photographs.
* 📝 **Text Analysis** — Processes descriptions and notes related to missing persons and survivors.
* 👕 **Clothing & Appearance Matching** — Compares clothing and physical descriptions.
* 📍 **Location Analysis** — Considers geographical compatibility between last-seen and found locations.
* 🕐 **Temporal Analysis** — Evaluates whether timestamps are compatible.
* 👤 **Metadata Matching** — Uses information such as age and gender.
* 🔎 **Candidate Retrieval** — Filters and retrieves the most relevant potential matches.
* 🧠 **Multimodal Matching** — Combines visual, textual, spatial, temporal, and contextual evidence.
* 📊 **Candidate Ranking** — Provides a ranked list of potential matches.
* 💡 **Explainable Results** — Shows supporting, conflicting, and missing evidence for candidates.
* 🤖 **Continuous Rematching** — Allows new or updated records to trigger matching again.
* 👨‍💼 **Human Verification** — AI results are intended to assist authorized responders; final identity confirmation remains with humans.
* 🔐 **Responsible AI & Privacy** — Designed with access control, data minimization, auditability, uncertainty handling, and bias evaluation in mind.

## 🛠️ Technologies

* **Python**
* **PyTorch**
* **OpenCV**
* **Transformers / Sentence Transformers**
* **FastAPI**
* **React**
* **PostgreSQL**
* **FAISS / Vector Search**

## 🏗️ System Pipeline

```text
Missing Person / Survivor Records
              ↓
        Data Preprocessing
              ↓
     Feature Extraction
       ↙      ↓       ↘
   Image     Text    Metadata
              ↓
     Constraint Filtering
              ↓
     Heuristic Retrieval
              ↓
    Multimodal Matching
              ↓
      Evidence Fusion
              ↓
      Candidate Ranking
              ↓
   Explanation & Top-K Results
              ↓
      Human Verification
```

## 🎯 Goal

To provide an AI-assisted, multimodal approach for efficiently identifying plausible missing-person and survivor matches while keeping authorized human responders in control of the final identification decision.
