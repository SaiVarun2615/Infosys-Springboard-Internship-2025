# **Day 4 — Literature Retrieval & ML Pipeline (Detailed Explanation)**

## **1. Understanding the ML Pipeline (Step-by-Step)**

A Machine Learning / AI project follows a clear structured pipeline.  
Today’s task focused on understanding this flow and implementing automated research paper retrieval.

---

### **1) Problem Definition**
Every ML project begins by defining what problem is being solved.

For this internship project, the goal is:

**“Build an AI system to automatically retrieve, analyze, and summarize scientific research papers.”**

Problem definition includes:
- What input the system receives  
- What output should be generated  
- Evaluation expectations  
- Real-world usefulness  

---

### **2) Data Collection**
After the problem is defined, the next step is collecting raw data.

For this project, data comes from:
- **OpenAlex API (used today – no key needed)**
- **Semantic Scholar API (will be used once the API key arrives)**
- Other public research sources

Data includes:
- Title  
- Abstract  
- Authors  
- Venue  
- DOI  
- Citation count  
- Publication year  

---

### **3) Data Preprocessing / Cleaning**
Raw data usually contains noise and missing elements.

Preprocessing includes:
- Removing unwanted symbols  
- Fixing incomplete fields  
- Normalizing text  
- Structuring data into JSON  
- Cleaning long abstracts  
- Handling missing metadata  

This helps the ML models understand the data properly.

---

### **4) Feature Extraction**
Features are meaningful parts extracted from raw data.

In research papers, useful features include:
- Title  
- Abstract text  
- Keywords  
- Research field  
- Publication year  
- Citations count  
- Authors  

These features help in summarization, clustering, ranking, and embeddings.

---

### **5) Data Splitting (Fragmentation)**
To properly train and validate models, datasets must be split into:

- **Training Set (80%)** → model learns  
- **Validation Set (10%)** → tuning hyperparameters  
- **Testing Set (10%)** → evaluating final performance  

This ensures good generalization.

---

### **6) Model / Algorithm Selection**
Based on project requirements, different models can be used:
- Classical ML models  
- Transformers  
- Deep learning architectures  
- LLM-based summarizers  
- Retrieval-Augmented Generation (RAG) models  

Our project will later use NLP transformer-based pipelines.

---

### **7) Training & Testing**
This step teaches the model to identify patterns in the data.

Includes:
- Fine-tuning  
- Hyperparameter selection  
- Calculating losses  
- Monitoring validation accuracy  
- Avoiding overfitting  
- Running tests on unseen data  

---

### **8) Evaluation**
To measure performance, evaluation metrics include:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROUGE & BLEU (for summarization tasks)  

Evaluation ensures the system is reliable and ready for real use.

---

### **9) Real-World Testing**
After training and evaluation, the model should be tested on **completely new research papers**.

This checks:
- Generalization ability  
- Consistency  
- Robustness  
- Performance on unseen data  

---

# **2. Day 4 Practical Task — Automated Literature Retrieval**

Today, the goal was to:
- Create a query file  
- Build a Python script to search for research papers  
- Retrieve paper metadata using the **OpenAlex API**  
- Save the results into a structured JSON file  

This completes the data collection phase for the literature review module.

---

## **Files Created Today**

### **1. `research/queries.txt`**
Contains search queries relevant to the project:
- AI research paper summarization
- machine learning literature review automation
- deep learning scientific paper analysis
- natural language processing long document summarization
- RAG research papers retrieval

---

### **2. `scripts/list.py`**
This Python script:
- Reads queries from `queries.txt`  
- Sends them to the OpenAlex API  
- Retrieves 20 papers per query  
- Extracts title, authors, year, venue, DOI, abstract  
- Appends everything to a combined list  
- Saves all results into `papers.json`

This script is the automated literature retrieval system.

---

### **3. `research/papers.json`**
The output JSON file created after running the script.

It contains:
- ~100 research papers  
- Clean metadata  
- All papers fetched from queries  

This JSON will be used later for:
- Ranking papers  
- Summarization  
- Semantic search  
- Embedding generation  

---

# **3. Summary of Today’s Progress**
- Understood the full ML project pipeline  
- Implemented automated research retrieval  
- Successfully generated structured JSON data  
- Prepared the foundation for literature review AI  
- Ready for integration with Semantic Scholar (after API approval)

This completes Day 4 successfully.

---

# **End of Day 4 — Task Completed ✔️**
