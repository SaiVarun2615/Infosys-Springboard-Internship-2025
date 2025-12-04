# 📘 Day 3 — Environment Ready, Tools Installed, and Retrieval Kickoff

---

## 1) Today’s Objectives
- Finish all installs (software, tools, libraries)  
- Be comfortable with Git & GitHub  
- Understand the workflow overview  
- Prepare environment for the upcoming retrieval module

---

## 2) Software & Tools (must be installed today)
- Python 3.10+  
- Git & GitHub  
- VS Code  
- Conda / virtualenv  
- (Optional) PostgreSQL client tools  

### Create & activate environment
```bash
conda create -n aisrsp python=3.11 -y
conda activate aisrsp
```

**OR**
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

---

## 3) Python Libraries to Install (Day 3)
```bash
pip install \
  requests tqdm tenacity pyyaml rich python-dotenv \
  gradio grandalf huggingface_hub \
  langchain langgraph langsmith \
  openai pydantic psycopg tiktoken \
  PyMuPDF4LLM pdfplumber \
  pytest
```

**Notes**  
- PyMuPDF4LLM / pdfplumber → PDF extraction  
- LangChain / LangGraph → pipeline orchestration  
- Gradio → UI  
- OpenAI / tiktoken → drafting + token mgmt  
- Grandalf → graph modelling  

**Environment variables (`.env`)**
```
OPENAI_API_KEY=
HUGGINGFACE_TOKEN=
SEMANTIC_SCHOLAR_API_KEY=
```

---

## 4) Git & GitHub — what you must know today
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

```bash
git clone <repo>
cd <repo>
git checkout -b feat/retrieval-day3
```

```bash
git add .
git commit -m "Day 3 setup completed"
git push -u origin feat/retrieval-day3
```

---

## 5) Input / Output & Methodology 

### **How Input Reaches Output? (Flow)**

#### **1. Input PDF**
The user uploads a research paper (PDF format).

#### **2. PDF Handling**
- Use **pdfplumber** or **PyMuPDF4LLM** to extract text.  
- If the PDF is scanned → use **PyTesseract/OCR** (if required).

#### **3. Cleaning + Processing**
- Clean extracted text  
- Remove junk characters  
- Apply regex rules  
- Split into logical sections (Abstract, Introduction, Methods, Results, Conclusion)

#### **4. AI Processing**
Powered by OpenAI / LangChain:
- Summarization  
- Extracting important points  
- Generating structured review  
- Creating highlights  

#### **5. Output**
- Clean summary  
- Structured review (bullet points)  
- Highlights  
- JSON or plain text output

---

### **Methodology**

#### **1. Research Phase**
- Topic scoping  
- Semantic Scholar search  
- Select top papers (configurable)  
- Download PDFs  

#### **2. Analysis Phase**
- Extract full text from PDFs  
- Break into sections  
- Identify key findings  
- Compare papers  

#### **3. Writing Phase**
- Generate summary sections  
- Produce Abstract (~100 words)  
- Write Methods & Results  
- Format APA references  

#### **4. Review Phase**
- LLM-powered critique  
- Quality improvement  
- Final draft preparation  

---

## 6) Where Each Library Will Be Used
- **requests, tenacity, tqdm** → API calls, retries, progress  
- **huggingface_hub, openai, tiktoken** → LLM access & token mgmt  
- **langchain, langgraph, langsmith, grandalf** → pipeline & graph  
- **PyMuPDF4LLM, pdfplumber** → PDF extraction  
- **gradio** → front-end UI  
- **pydantic** → data validation models  

---

## 7) What Must Be Ready Tomorrow (Carry-over)

### **Day 1**
- Repo scaffold created  
- Working Python environment  
- `requirements.txt` updated  

### **Day 2**
- All required libraries installed  
- CLI bootstrap done  
- README updated with setup steps  

### **Day 3 (Tomorrow’s Discussion)**
Sir will explain:  
**“What exactly are we going to do in the first step of the project?”**

This will officially begin the first working component of the system.

---

## ✅ End of Day 3 Summary
- Environment setup completed  
- All tools and Python libraries installed  
- Git & GitHub workflow is understood  
- Input → Output flow understood  
- Project methodology understood from the document  
- Ready for tomorrow’s session where the mentor explains the **first step of the project**
