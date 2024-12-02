# Replication package of the work: Deep Assessment of Code Review Generation Approaches: Beyond Lexical Similarity

In this paper, we explore how semantic similarity between generated and reference reviews can enhance the automated assessment of code reviews. We first present a benchmark called GradedReviews, which is constructed by collecting real-world code reviews from open-source projects, generating reviews using state-of-the-art approaches, and manually assessing their quality. We then evaluate existing metrics for code review assessment using this benchmark, revealing their limitations.

# Directory Structure
There are two folders within the replication package:

./Code: The source code of deep assessment of code review generation approach, includes implementation for BLEU, Embedding-based Score, ChatGPT-based Score, **ROUGE**, **METEOR**, and **DeepSeek-Coder-based Score** 

./DataSet: Data to replicate the evaluation in the paper

# DataSet:
The methodology used for constructing the benchmark
![Methodology for Benchmark Construction](./dataset.png "Methodology for Benchmark Construction")

# Code: 
Step-by-step running deep assessment of code review generation approaches:

  1. BLEU Score:

    python BLEU.py

  2. Embedding-based Score:
   
    python embeddingScore.py

  3. LLM-based Score (ChatGPT-4o):
   
    python LLMScore.py

  4. Decision Tree:
   
    DecisionTree.py

  5. Spearman Rank Correlation Coefficient:

    python spearman.py

  6. Kolmogorov-Smirnov Statistic:

    python ks.py

**7. <font color=red>METEOR Score:</font>** 

    python METEOR.py

**8. ROUGE Score:**
   
     python ROUGE.py
    
**9. LLM-based Score (DeepSeek-Coder):**
   
     python ScoreByDeepSeek.py
