# ORA-DEA

# Project Title
**Evaluating the performance of company efficiency using network data envelopment analysis (NDEA)**

## Abstract
Efficiency evaluation in supply chain management is crucial for assessing the company performance. While the importance of evaluating the company efficiency strategies is widely recognized, there is a lack of well-established quantitative methods for assessing the effectiveness of strategies. This paper introduces a novel approach using network data envelopment analysis (NDEA) to evaluate efficiency. The model takes into account the cost of various strategies, their performance outcomes, and the interdependencies among different stages of the supply chain, specifically focusing on the supplier, manufacturing, and customer segments. A comparative efficiency analysis between NDEA and traditional approaches reveals that NDEA provides a more comprehensive and valuable assessment of supply chain risk mitigation performance. In conclusion, in a multi-stage supply chain scenario, NDEA is considered a preferable choice for evaluating supply chain efficiency.

## Background & Research Purpose

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

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p7.png?raw=true)

Our model is from the perspective of the manufacturers, who must manage efficiency internally and externally,  both upstream and downstream.



## Methodology

### Method Justification 
**Why using NDEA**

Traditional DEA treats DMUs as black boxes, an assumption not applicable for the complexities of supply chain risk management.  
Also, NDEA efficiency is relative, allowing diverse efficiency paths, mirroring firms' unique efficiency strategies.  
In addition, NDEA defines supply chains as interconnected activities, akin to industry-specific supply chain structures. 

### Model Formulation

### Desicion Variable: $\lambda$

Assume there are $k$ stages and $n$ companies (DMUs).  
Given a $k = 3, n = 1$ scenario, consider a company $r$ , there are 3 stages: Suppliers, Manufacturing, Customers.  
We need to determine the **weight** assigned to each input and output vector (represent as lambda).  
With the input and output parameter $X, Y, Z$.

$X^1$ is the input vector of the suppliers, while $X^2$ and $X^3$ are the input vectors for the manufacturers and customers. 

$Z^1$ and $Z^2$ are the output vectors for both the supplier and the manufacturer, and are also the input vectors for the manufacturers and customers, making them the link variables. The final output vector from customers is represented by $Y^1$.  

Our model is from the perspective of the **manufacturers**, who must manage risk internally and externally, both upstream and downstream. Therefore, we apply the centralized control model.

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p10.png?raw=true)


### Linkage Assumption
Linkage assumption suggests that the output vectors in the previous stage will become the input vectors of the next stage.  
Assume linkage $(k, h)$ denotes as the linkage from stage $k$ to $h$.  
In the model, there are 3 stages and 2 linkages.

Therefore, we could denote the linkage $(k, h)$ as following:  
$(1, 2)$: the linkage between suppliers and manufacturing  
$(2, 3)$: the linkage between manufacturing and customers.

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p11.png?raw=true)

### NDEA Model $\lambda$
Below shows the mathematics expressions of NDEA model,  
where lambda is the only decision variable, representing the weight assigned to each input and output vector.  
$s^k_-$ and $s^k_+$ represent the input and output slack variables, respectively.

Equation (1) shows the objective function, which is composed of all stage efficiencies with $w_k$ , the relative weight of Stage $k$, multiplies by 1-input vector $x$.  
Equation (2) shows the input vectors multiply decision variables lambda and add slack variables.  
Equation (3) shows the output vectors multiply decision variables lambda and add slack variables.  
Equation (4) shows the relative weight, $w$ for each stage. Here, we assume each stage has equal weight, $w = \frac{1}{3}$.  
Equation (5) shows the Linkages Assumptions, there are 2 $(k, h)$ pairs: (1,2) & (2,3).  
Equation (6) shows the decision variable: $\lambda, s_k^+, s_k^-$, weighted value.  

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p12.png?raw=true)

## Performance Evaluation
We modifies their NDEA model from VRS-based to CRS-based and are attempting to compare it with classical DEA (VRS and CRS) models to evaluate our modifications. In sum, there are 4 models to compare:

Models:
1. NDEA CRS-based model
2. NDEA VRS-based model
3. DEA CRS model
4. DEA VRS model

### NDEA CRS-based v.s. NDEA VRS-based model
We construct the NDEA model with CRS-based and VRS-based.  
The equation is exactly the same as the NDEA model part.  
The only difference between CRS ans VRS is that the sum of weights equals to 1.

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p16.png?raw=true)


### Dual DEA: CRS / VRS model
We construct a Dual DEA with CRS-based and VRS-based.  
The only difference between CRS ans VRS is that the sum of weights equals to 1.

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p17.png?raw=true)


### Scenario Analysis
There are 3 types of inputs and outputs
1. Same input; Different output
2. Different input; Same output
3. Different input; Different output

We generate the input and output data according to the original paper survey.

| Input                                   | Median  | Range             |
|-----------------------------------------|---------|-------------------|
| Firm Age (years)                        | 66      | 1–179             |
| Risk Management Program (years)         | 2       | 0–50              |
| Firm Size (employees)                   | 7500    | 6–25000           |
| **Output**                                  | **Median**      |** Range **           |
| Sales ($)                               | 0.75 bn.    | 0.5 bn. to 10 bn.|


In sum, there are 3 scenarios, with each has different input and output data.

### Comparison Among 4 models
We compare the above 4 models with 3 scenarios and have these finding:
1. 3 scenarios have consistency. 
2. VRS tends to have higher efficiency score than CRS due to its scale flexibility
3. DEA tends to have large fluctuation than NDEA.

In 3 scenarios, when the efficiency score is relatively low, the DEA score is lower than the NDEA score, and the one employing VRS tends to achieve a higher efficiency score. Conversely, when the efficiency score is relatively high, the DEA model attains a higher efficiency than the NDEA model, with a score of 1, indicating a larger fluctuation in DEA. Additionally, consistency is evident in the observation that DEA's lower efficiency score becomes even lower than that of NDEA, while the higher score becomes higher than that of NDEA.

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p19.png?raw=true)


### Performance Analysis summary
There is no discrimitive power in DEA, as almost all DMUs score 1.  
On the contrary, the proposed model, NDEA, can compare the value of score, with different value in each company.  
Moreover, a DMU that initially achieved a score of 1 in the benchmark model obtains an efficiency score less than 1 in the NDEA model, indicating that the benchmark model may have reached saturation too rapidly. 

![image](https://github.com/clins210/ORA-NDEA/blob/main/figures/ORA_p20.png?raw=true)



## Conclusion
We implement 4 models, and compare the result respectively, and we find that:
1. DEA lacks discriminative power, with most DMUs scoring 1.
2. NDEA allows for score comparison, revealing efficiency variations.
3. In a multi-stage scenario, the linkage assumption better fits the reality of the supply chain applications. Therefore, NDEA is considered a preferable choice for evaluating supply chain efficiency.

## Contribution
### Academic Contributions:

1. **Novel Evaluation Capability with NDEA:**  
The introduction of the NDEA model provides a novel and enhanced evaluation capability compared to traditional DEA. This innovation allows for the differentiation of efficiency scores, offering a more nuanced perspective on the performance of Decision Making Units (DMUs).
2. **Quantitative Discrimination in Efficiency Scores:**  
NDEA's ability to compare efficiency scores quantitatively introduces a valuable metric for academics. This capability provides a more sophisticated analysis of the efficiency landscape, moving beyond the limited discrimination power observed in traditional DEA.
3. **Revealing Benchmark Model Saturation:**  
The observation that a DMU initially scoring 1 in the benchmark DEA model obtains an efficiency score less than 1 in the NDEA model contributes to the understanding of benchmark model limitations. This insight highlights the potential for benchmark models to reach saturation prematurely and underscores the importance of adopting more advanced models.
4. **Linkage Assumption in Multi-Stage Scenarios:**  
The acknowledgment that the linkage assumption in multi-stage scenarios better aligns with the reality of supply chain applications contributes to refining modeling assumptions. This insight provides a basis for future research to explore and validate the applicability of linkage assumptions in various supply chain contexts.


### Practical Contributions:

1. **Enhanced Decision-Making Support:**  
The practical contribution of the NDEA model lies in its ability to offer more granular insights into the efficiency of different companies. This enhanced decision-making support empowers practitioners to identify specific areas for improvement and optimization within their operations.
2. **Efficiency Enhancement Strategy:**  
The NDEA model contributes practically by informing the development of more targeted strategies to enhance overall efficiency. With a nuanced understanding of efficiency variations, organizations can proactively identify areas for improvement in their operations and implement specific measures to optimize processes, ultimately enhancing overall efficiency.
3. **Strategic Adoption of NDEA in Supply Chain Management:**  
The endorsement of NDEA as a preferable choice in multi-stage supply chain scenarios provides practical guidance for supply chain managers. This strategic adoption contributes to more accurate efficiency assessments in the dynamic and interconnected nature of modern supply chains.




## Limitation & Future Works

### Limitation
Our model utilizes the NDEA model and demonstrates superior performance compared to traditional DEA models; however, there is room for improvement.  
Firstly, we currently only incorporate one-dimensional data for each input and output value. Considering multi-dimensional inputs and outputs would better reflect reality. Additionally, we solely rely on data generated from the survey in the original thesis. Conducting our own survey will ensure the accuracy of the data. Lastly, the efficiency scores from the NDEA and DEA models only indicate relative efficiency among different companies. To address this limitation, we may consider constructing different efficiency evaluation metrics to compare various circumstances. 

### Future Works 
1. Integrate multi-dimensional inputs and outputs data into the NDEA model.
2. Conduct our own survey to obtain first-hand data.
3. Develop diverse efficiency evaluation metrics to compare various circumstances

## References
- [Evaluating the performance of supply chain risk mitigation strategies using network data envelopment analysis](https://www.sciencedirect.com/science/article/pii/S0377221722002235) \
- [Incorporating causal modeling into data envelopment analysis for performance evaluation](https://link.springer.com/article/10.1007/s10479-023-05486-0) \
- [Innovation performance evaluation for high-tech companies using a dynamic network data envelopment analysis approach](https://www.sciencedirect.com/science/article/abs/pii/S0377221720308870)



