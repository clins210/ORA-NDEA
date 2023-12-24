# ORA-DEA

# Project Title
Evaluating the performance of company efficiency using network data envelopment analysis

## Background and Motivation

### Motivation
The significance of effective vendor selection and order allocation under uncertain on-time-delivery is crucial in optimizing supply chain operations. This project aims to address the challenges associated with demand fulfillment in a dynamic supply chain network.

### Background
In the realm of supply chain management, the evaluation of efficiency strategies is a critical pursuit to enhance overall performance. 
The complexity of interconnected supply chain entities and multi-dimensional aspects challenges traditional efficiency assessment methods to capture intricate relationships and dependencies.
In this paper, we propose a method for evaluating efficiency strategies that simultaneously includes performance outcomes, and interdependencies among the different stages of the supply chain. 

### Problem Definition
This study proposes a stochastic programming model to minimize the total cost of capacity allocation for demand fulfillment in a supply chain network. The model considers uncertainties associated with on-time delivery, aligning with concepts covered in the ORA course.

Problem:
Evaluating the Performance of Company Efficiency Using NDEA
Considered Factors:
Production factors
Performance outcomes
Interdependencies across different stages of the supply chain
Decision-Making Units (DMU):
Each company will receive an efficiency performance score ranging from 0 to 1.
An efficiency score of 1 indicates that the company is highly efficient, while a score less than 1 represents relative inefficiency.


## Methodology

### Assumptions, Limitations, Pros, and Cons
- Assumptions: [List any assumptions made in your model]
- Limitations: [Highlight any limitations of your methodology]
- Pros: [Enumerate the advantages of the chosen method]
- Cons: [Discuss any drawbacks or challenges]

### Method Justification
The chosen stochastic programming approach is justified based on its ability to handle uncertainty in the on-time delivery aspect of supply chain operations. The mathematical rigor of this method aligns with the complexity of the problem at hand.

### Tutorial
For a theoretical and mathematical introduction to the methodology, refer to the [Tutorial](./tutorial.md) file in this repository. It explains the uncertain factors, their impact, and the application of stochastic programming in the analysis.

## Data Collection and Analysis Result

### Data Collection
The dataset used for this project is sourced generated randomly base on their survey. If real data is unavailable, a data generating process (DGP) or simulation is applied to justify the dataset's relevance to the problem.

### Analysis
Detailed analysis using the stochastic programming method outlined in Section 3 is presented in the [Analysis](./analysis.md) file. Tables and figures illustrate the numerical results obtained.

### Results and Managerial Implications
The analysis leads to the identification of optimal solutions or recommendations. The results and their managerial implications are discussed in [Results](./results.md).

## Conclusion
The project concludes by summarizing key findings and insights gained from the application of stochastic programming to vendor selection and order allocation in a supply chain network. 

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


