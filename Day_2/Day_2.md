# 📘 Day 2 – Daily Progress
## **AI System to Automatically Review and Summarize Research Papers**

---

## 🔹 **What was taught, explained, or discussed in today’s session?**
- Explain clearly what our project title is.
- What exactly we are going to build?
- What is the problem statement?
- What is the expected output?
- What is the project about in simple terms?
- What are the requirements of the project?
- What do *you* know about the project so far?
- How do we reach from **input → processing → output**?
- Why are we developing this type of project?
- What software, libraries, tools will be used?
- Tasks to prepare for tomorrow.

---

## 🏷 **Project Title**
**AI System to Automatically Review and Summarize Research Papers**

---

## 🧠 **What exactly we are going to do?**
We are going to build an AI-powered system that:
- Takes a research paper (PDF) as input.
- Extracts text automatically.
- Analyses the content using AI models.
- Generates a clear, structured summary.
- Generates review points such as: objectives, methods, results, conclusion.

---

## ❗ **Problem Statement**
Reading and understanding long research papers manually is **time-consuming**, **boring**, and **difficult** for many students and researchers. There is no simple automated tool that can extract, analyze, and generate meaningful summaries or reviews without human effort.

---

## 🎯 **Expected Outcome**
- A system that can **extract text** from any research paper (PDF).
- Summarize the paper in simple words.
- Identify key sections like **Abstract, Problem Statement, Methodology, Results, Conclusion**.
- Provide review comments or explanation using AI.
- Provide structured output in JSON/text.

---

## 📘 **What the Project is About (Simple Explanation)**
It is an AI tool that reads a research paper on behalf of the user and gives:
- Summary
- Key points
- Main idea
- Important highlights
- Paper review

Basically: **You upload → AI reads → AI explains → You understand easily**.

---

## ⚙️ **Requirements of the Project**
- Automatically extract text from PDF.
- Clean & preprocess the text.
- Use an AI model (like OpenAI / LangChain) for summarization.
- Classify the extracted text into sections.
- Build simple CLI / Jupyter Notebook based flow.
- Maintain logs.
- Write unit tests.
- Use proper version control with Git/GitHub/GitLab.

---

## 🤔 **What I know about the project (My Understanding)**
- We need Python knowledge.
- We will process PDF files.
- AI/LangChain/OpenAI APIs will help in generating summaries.
- The system must be modular: extraction → processing → summarization.
- We will use Jupyter Notebook for execution (cell-wise running).
- Git/GitHub will be used for code backup.

---

## 🔄 **How Input Reaches Output? (Flow)**

### **1. Input PDF**
Research paper uploaded.

### **2. PDF Handling**
Using **pdfplumber** or **PyTesseract** (for scanned PDFs) to extract text.

### **3. Cleaning + Processing**
- Use regex  
- Remove junk characters  
- Split into sections  

### **4. AI Processing**
Use **OpenAI API** or **LangChain** to:
- Summarize  
- Extract important sections  
- Generate review  

### **5. Output**
- Clean summary  
- Structured review (points)  
- Highlights  
- JSON or text output displayed  

---

## 🔍 **Why are we doing this project?**
- To reduce time spent reading long papers.
- To help students understand research easily.
- To automate repetitive tasks.
- To solve a real-world academic problem.
- To learn AI, NLP, LangChain, APIs, PDF processing.

---

## 🛠 **Software & Tools Needed**

### **Primary**
- **Python 3.10+**
- **Jupyter Notebook** (for executing cell-wise)
- **Git / GitHub / GitLab**

### **Important Python Libraries**

#### 📄 **PDF Handling**
- `pdfplumber`
- `PyTesseract`

#### 🌐 **API / Web Tools**
- `beautifulsoup4`
- `requests`
- `openai`
- `langchain`

#### 🧹 **Text Processing**
- `re` (regex)
- `nltk` / `spacy` (optional)

#### 📊 **Data Handling**
- `pandas`
- `numpy`

#### 📉 **Visualization**
- `matplotlib`
- `seaborn`

#### 📝 **Logging**
- `logging`

#### 🧪 **Testing**
- `pytest`
- `pytest-mock`

---

## 📚 **Tasks to Know for Tomorrow**

### ✔ 1. Have a basic understanding of the software, tools, and libraries used in the project
- Know what each tool/library is for  
- Understand why they are required in the workflow  

### ✔ 2. Learn basics of Python again
- How to run cell-wise in Jupyter Notebook  
- Basic syntax, functions, loops, imports  

### ✔ 3. Learn basics of Git, GitHub, GitLab
- Push, pull, commit, clone, branch  
- How to upload daily files  

### ✔ 4. Read the PDF shared by mentor  
You must come with:  
- **Problem Statement**  
- **Expected Output**  

---

## ✅ **End of Day 2 Summary**
Day 2 focused on understanding the whole project clearly, required tools, libraries, flow, and preparation tasks for the next session.

---
