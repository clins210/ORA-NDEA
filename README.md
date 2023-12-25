# ORA-DEA

# Project Title
Evaluating the performance of company efficiency using network data envelopment analysis(NDEA)

## Abstract
Efficiency evaluation in supply chain management is crucial for assessing the company performance. While the importance of evaluating the company efficiency strategies is widely recognized, there is a lack of well-established quantitative methods for assessing the effectiveness of strategies. This paper introduces a novel approach using network data envelopment analysis (NDEA) to evaluate efficiency. The model takes into account the cost of various strategies, their performance outcomes, and the interdependencies among different stages of the supply chain, specifically focusing on the supplier, manufacturing, and customer segments. A comparative efficiency analysis between NDEA and traditional approaches reveals that NDEA provides a more comprehensive and valuable assessment of supply chain risk mitigation performance. In conclusion, in a multi-stage supply chain scenario, NDEA is considered a preferable choice for evaluating supply chain efficiency.

## Background & Motivation

### Background Description
In the realm of supply chain management, the evaluation of efficiency strategies is a critical pursuit to enhance overall performance. 
However, the complexity of interconnected supply chain entities and multi-dimensional aspects challenges traditional efficiency assessment methods to capture intricate relationships and dependencies.
Therefore, in this paper, we propose a method for evaluating company efficiency strategies that simultaneously includes performance outcomes, and interdependencies among the different stages of the supply chain. 

### Research Purpose
Evaluating supply chain efficiency strategies for each company, and consider each of the entities and their interdependencies.

## Problem Definition

### Problem Definition
Evaluating the Performance of Company Efficiency Using NDEA

### Consider Factors
1. Production factors
2. Performance outcomes
3. Interdependencies across different stages of the supply chain

### Decision-Making Units (DMU):
Each company will receive an efficiency performance score ranging from 0 to 1.
An efficiency score of 1 indicates that the company is highly efficient, while a score less than 1 represents relative inefficiency.

![image](picture or gif url)
Our model is from the perspective of the manufacturers, who must manage efficiency internally and externally,  both upstream and downstream.



## Methodology

### Method Justification (Why using NDEA)
Traditional DEA treats DMUs as black boxes, an assumption not applicable for the complexities of supply chain risk management.
Also, NDEA efficiency is relative, allowing diverse efficiency paths, mirroring firms' unique efficiency strategies. 
In addition, NDEA defines supply chains as interconnected activities, akin to industry-specific supply chain structures. 

### Model Formulation

### Desicion Variable[add picture]

Assume there are k  stages and n  companies (DMUs).
Consider the company r , there are 3 stages: S, M, C.

### Linkage Analysis[add picture]

### NDEA Model[add picture]
![image](picture or gif url)

## Performance Evaluation
We modified their NDEA model from VRS-based to CRS-based and are attempting to compare it with classical DEA (VRS and CRS) models to evaluate our modifications. In sum, there are 4 models to compare:

Models:
1. NDEA CRS-based model
2. NDEA VRS-based model
3. DEA CRS model
4. DEA VRS model

### NDEA CRS-based v.s. NDEA VRS-based model[add picture]
![image](picture or gif url)


### Dual DEA: CRS / VRS model[add picture]
![image](picture or gif url)


### Scenario Analysis
There are 3 types of inputs and outputs
1. Same input; Different output
2. Different input; Same output
3. Different input; Different output

We generate the input and output data according to the original paper survey.
There are 3 input
input 1 : Firm Age (years) 				(Median = 66,		range = 1–179)
input 2 : Risk management program (years)  	(Median = 2, 		range = 0–50)
input 3 : Firm Size (employees)  			(Median = 5000–9999, 	range = 6–25000)
1 output: Sales ($) 					(Median = 0.5 bn. to 1 bn.,  range = 0.5 bn to 10 bn.)

In sum, there are 3 scenarios, with each has different input and output data.

### Comparison Among 4 models[add pictures]
We compare the above 4 models with 3 scenarios and have these finding:
1. 3 scenarios have consistency. 
2. VRS tends to have higher efficiency score than CRS due to its scale flexibility
3. DEA tends to have large fluctuation than NDEA.

In 3 scenarios, when the efficiency score is relatively low, the DEA score is lower than the NDEA score, and the one employing VRS tends to achieve a higher efficiency score. Conversely, when the efficiency score is relatively high, the DEA model attains a higher efficiency than the NDEA model, with a score of 1, indicating a larger fluctuation in DEA. Additionally, consistency is evident in the observation that DEA's lower efficiency score becomes even lower than that of NDEA, while the higher score becomes higher than that of NDEA.

![image](picture or gif url)


### Performance Analysis summary [add picture]
There is no discrimitive power in DEA, as almost all DMUs score 1.
On the contrary, the proposed model, NDEA, can compare the value of score, with different value in each company.
Moreover, a DMU that initially achieved a score of 1 in the benchmark model obtains an efficiency score less than 1 in the NDEA model, indicating that the benchmark model may have reached saturation too rapidly. 

![image](picture or gif url)



## Conclusion
We implement 4 models, and compare the result respectively, and we find that:
1. DEA lacks discriminative power, with most DMUs scoring 1.
2. NDEA allows for score comparison, revealing efficiency variations.
3. In a multi-stage scenario, the linkage assumption better fits the reality of the supply chain applications. Therefore, NDEA is considered a preferable choice for evaluating supply chain efficiency.

## References
[Evaluating the performance of supply chain risk mitigation strategies using network data envelopment analysis](https://www.sciencedirect.com/science/article/pii/S0377221722002235) \
[Incorporating causal modeling into data envelopment analysis for performance evaluation](https://link.springer.com/article/10.1007/s10479-023-05486-0) \
[Innovation performance evaluation for high-tech companies using a dynamic network data envelopment analysis approach](https://www.sciencedirect.com/science/article/abs/pii/S0377221720308870)


<!-- 
limitation/future work ?
-> input dimension
how to improve?

insight???
論文與實務之間的關聯（思考問題 > 思考解法）
high level -->

### File structure
```
├── ORA-DEA
│   ├── code
│   │   ├── core
│   │   │   ├── data.py
│   │   │   ├── model.py
│   │   │   └── util.py
│   │   ├── dataset
│   │   │   ├── DD
│   │   │   ├── DS
│   │   │   └── SD
│   │   ├── main.ipynb
│   │   └── requriment.txt
└── README.md
```


