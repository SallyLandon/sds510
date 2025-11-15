# Module 06 — Connected Data Analysis  
### Network Analysis of the *Cocaine Dealing (Natarajan)* Dataset

This folder contains my work for Module 06 of the Connected Data assignment.  
The goal of this assignment was to analyze a covert social network dataset, identify the most influential or structurally critical member, and evaluate the effect of removing that node on the structure of the network.

---

## 📄 Contents

**module-06.ipynb**  
My full analysis notebook, including:
- Data import and cleaning steps  
- Construction of the network graph  
- Computation of degree centrality and betweenness centrality  
- Simulation of removing the most central node (*Kay*)  
- Effects on graph connectivity and component fragmentation  
- Write-up and interpretation of results  

**cocaine-network-gephi.png**  
High-resolution visualization of the network created in Gephi Lite, showing:
- Node size proportional to degree centrality  
- Node color mapped to betweenness centrality  
- Kay highlighted as the dominant broker whose removal fragments the network into smaller clusters  

---

## 📊 Summary of Findings

The network consists of **28 nodes** and **40 edges**.  
Centrality metrics and visualization reveal that:

- **Kay** is the dominant broker, with the highest degree and betweenness centrality.  
- Removing Kay causes the network to fragment from **1 connected component → 12 components**.  
- The largest connected component drops from **28 nodes → 16 nodes**.  
- This demonstrates Kay’s critical structural role and suggests that targeting her would be the most effective intervention to disrupt information or resource flow in this covert network.

Details and supporting metrics are in the notebook.

---

## 🙋 Academic Integrity & Assistance Acknowledgment

I completed this assignment myself.  

I used ChatGPT as a support tool for:
- Clarifying instructions  
- Explaining Python and NetworkX functions  
- Assisting with Gephi Lite interface issues  
- Drafting text that I later edited for clarity and accuracy  

I used Google Gemini to help identify and correct minor coding issues.  

I independently verified my understanding of all code, analysis steps, and interpretations, including checking reasoning with ChatGPT where needed.  

This README was drafted with assistance from ChatGPT and then revised by me.

---

## 📁 Viewing the Notebook on GitHub

GitHub natively renders:
- Jupyter notebooks  
- Embedded images  
- Markdown explanations  

The visualization image (`cocaine-network-gephi.png`) is stored in the same directory as `module-06.ipynb`, so it should appear correctly inside the notebook.

---

## ✔️ How to Run the Notebook (Optional)

To rerun this notebook locally or in Colab:

1. Download `module-06.ipynb` and (optionally) `cocaine-network-gephi.png`.  
2. Open the notebook in Jupyter or Google Colab.  
3. Install required packages (for example: `networkx`, `pandas`, `numpy`, `matplotlib`).  
4. Execute the cells in order.

