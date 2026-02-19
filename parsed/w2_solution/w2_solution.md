# SC3021 Excercise: What is Data Science?

## Sample Solution Week 2 Tutorial

Here are three short examples of real-world questions that can be addressed by data science.

1. How does socioeconomic status impact access to education?
2. How can we predict the failure of our machines?
3. What products should we recommend to customers of our e-commerce platform?

However, due to their brevity, some details of the underlying data science problem remain unclear. This exercise focuses on elaborating and completing essential details that characterize a data science problem, as defined in class. The definition of Data Science is repeated here for convenience. Highlighted terms are the focus of this exercise.

> **Definition of Data Science [Öszu23]:** “Data science is a **data-based** approach to problem solving by analyzing and exploring possibly **multi-modal** and **heterogeneous** data, extracting **knowledge and insight** from it, and using information for better **decision-making**. It involves the process of collecting, preparing, managing, analyzing, explaining, and disseminating the data and analysis results.”

**TASK:** For one of the above sample questions, create and complete a table following the template below.

---

<table>
    <tr>
        <th>Problem</th>
        <th>[point out / discuss at least two details that would need to be clarified before developing a solution. Rewrite a possible refined question that takes your previous points into account.]</th>
    </tr>
    <tr>
        <td></td>
        <td>1. Specific type of education? Which factors of socioeconomic status? Refined to: How does family income affect access to secondary education?</td>
    </tr>
    <tr>
        <td></td>
        <td>2. What constitutes a failure? What kind of machine? In advance? Refined to: How can we predict hydraulic failure of a drilling machine within one month?</td>
    </tr>
    <tr>
        <td></td>
        <td>3. Specific types of products? What kind of customer, e.g., B2B, B2C, key accounts? Refined to: What end consumer electronics should we recommend to customers of our B2C e-commerce platform?</td>
    </tr>
    <tr>
        <td>Data</td>
        <td>[List in bullet points the data needed to answer the question. Specify if it is multi-modal or heterogeneous (as below)]</td>
    </tr>
    <tr>
        <td></td>
        <td>1. (1) data about household income (gross, net, per household member), likely tabular data. (2) data about access to secondary education per family income category, e.g., which secondary schools are attended, how many members of the household attend(ed) secondary school, etc. Multi-modal: NO, Heterogeneous: YES if collected from different agencies.</td>
    </tr>
    <tr>
        <td></td>
        <td>2. (1) Sensor measurements about hydraulic pressure (time series); (2) machine specifications about normal range of operation, (3) historical data about normal and abnormal conditions leading to failure. Multi-modal: yes - time-series, semi-structured data, Heterogeneous: yes.</td>
    </tr>
    <tr>
        <td></td>
        <td>3. (1) product data, (2) shopping history of customers. Multi-modal: NO, assuming both are available as structured / tabular datasets, Heterogeneous: YES, the column headers are different for the different files.</td>
    </tr>
    <tr>
        <td></td>
        <td>multi-modal: YES □ NO □ Heterogeneous YES □ NO □</td>
    </tr>
    <tr>
        <td>Acquired knowledge / insight</td>
        <td>[What knowledge or insight the analysis necessary to answer the question could bring.]</td>
    </tr>
    <tr>
        <td></td>
        <td>1. Correlation of household income and access to education, allowing for a better understanding of whether one is potentially related to the other.</td>
    </tr>
    <tr>
        <td></td>
        <td>2. Analysis allows to potentially recognize when a machine will fail.</td>
    </tr>
    <tr>
        <td></td>
        <td>3. Allows to gain insights on what products customers may like.</td>
    </tr>
    <tr>
        <td>Decision-making</td>
        <td>What decisions could the acquired knowledge / insight support?</td>
    </tr>
    <tr>
        <td></td>
        <td>1. Influence policies to improve access to education</td>
    </tr>
    <tr>
        <td></td>
        <td>2. Schedule maintenance of machine to avoid failure</td>
    </tr>
    <tr>
        <td></td>
        <td>3. Optimization of stocks in warehouses / procurement.</td>
    </tr>
</table>2