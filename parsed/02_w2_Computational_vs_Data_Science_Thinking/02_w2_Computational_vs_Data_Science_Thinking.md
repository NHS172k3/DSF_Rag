# Data Science Fundamentals
[SC3021/SC5003]

## Chapter 2: Data Science Thinking vs Computational Thinking

Assoc. Prof. Melanie Herschel | CCDS

---

# Course content

- Data science overview
  - What is Data Science?
  - **Data Science Thinking vs. Computational Thinking**
    - •Computational Thinking
    - •Data Science Thinking
    - •Comparison
  - Data Science Ecosystem
- Data preparation and data management
  - Data profiling
  - Structuring
  - Enriching
  - Data cleaning
  - Data management platforms
  - Schema design
  - Querying data
- Data analytics and understanding
  - Descriptive analytics
  - Diagnostic Analytics
  - Prescriptive analytics
  - Predictive analytics
  - Data visualization
- Design considerations
  - Privacy
  - Security
  - Ethics
  - Psychology
  - Policies



<table>
  <caption>Course content</caption>
  <thead>
    <tr>
      <th>Data science overview</th>
      <th>Data preparation and data management</th>
      <th>Data analytics and understanding</th>
      <th>Design considerations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>What is Data Science?</li>
          <li>Data Science Thinking vs. Computational Thinking
            <ul>
              <li>Computational Thinking</li>
              <li>Data Science Thinking</li>
              <li>Comparison</li>
            </ul>
          </li>
          <li>Data Science Ecosystem</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Data profiling</li>
          <li>Structuring</li>
          <li>Enriching</li>
          <li>Data cleaning</li>
          <li>Data management platforms</li>
          <li>Schema design</li>
          <li>Querying data</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Descriptive analytics</li>
          <li>Diagnostic Analytics</li>
          <li>Prescriptive analytics</li>
          <li>Predictive analytics</li>
          <li>Data visualization</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Privacy</li>
          <li>Security</li>
          <li>Ethics</li>
          <li>Psychology</li>
          <li>Policies</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>




<table>
  <caption>Data analytics and understanding (Icon Representation)</caption>
  <thead>
    <tr>
      <th>Analytics Category</th>
      <th>Relative Value (Estimated)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Descriptive analytics</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Diagnostic Analytics</td>
      <td>10</td>
    </tr>
    <tr>
      <td>Prescriptive analytics</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Predictive analytics</td>
      <td>3</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
2

---

# The content of this lecture is designed to enable you to...

- ...describe and compare the main characteristics of Computational Thinking and Data Science Thinking.
- ... explain how cross-functional thinking skills complement each other to solve a data science problem.
- ... argue why and how a problem should be addressed through Data Science Thinking (or not).
- ... conceive a rough agenda to solve a new problem by following the Data Science Thinking process.

> <img src="image.png" alt="Image of a target with arrows hitting the center, symbolizing precision and focus." width="500"/>

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 3

---

# COMPUTATIONAL THINKING

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
4

---

# Computational Thinking introduction

- Computational Thinking is a process for solving complex problems.
- Thought process involved in formulating a problem and expressing its solution such that a computer, human, or machine can effectively carry it out.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 5

---

# Overview of key components

- Decomposition
- Pattern recognition
- Abstraction
- Algorithm design

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
6

---

# Running (toy) example

## Problem:
Preparing a kaya toast

> Nanyang Technological University. All rights reserved.

---

# Decomposition

- Break down a complex problem into subproblems.
  - Subproblems are smaller, more manageable
  - Subproblems are easier to solve
- Combining the solutions to all subproblems solves the overall problem.

> Get bread

> Get kaya

> Get butter

> Toast bread

> Spread kaya on one slice

> Spread butter on the other slice

> Put slices together

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved. 8

---

# Pattern recognition

- Identify patterns or trends
  within a problem.
  - Steps following the same
    pattern may reuse same
    solution.
  - Patterns and trends allow to
    simplify the solution.

Get bread
Get kaya
Get butter
Toast bread
Spread kaya on
one slice
Spread butter on
the other slice
Put slices together

- Repeating pattern of spreading a
  filling (butter or kaya) on a slice.
- The pattern is repeated twice.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 9

---

# Abstraction

- Identify similarities and differences among similar problems to work toward a generic solution.
- Focuses on essential properties of a problem (invariant for similar problems)
- Ignores details of different problem instances.
- Simplifies problem solving by focusing on the fundamental characteristics of the type of problem to solve.

## Similar problems 1:
making different kinds of kaya toast
- Ignore specific brand of kaya, toast, butter, etc.
- Ignore specific type of toast
- Ignore specific type of toasting

## Similar problems 2:
making different types of simple sandwiches
- Ignore specific type of bread, spread
- All require three ingredients
- All follow the same pattern of spreading a topping on a base and stacking these.
- Ignore (outsource) uncommon steps like toasting the bread before use.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
10

---

# Algorithm design

- Algorithm: a step-by-step plan to solve a problem.
- Can be used to solve similar problems as well.
- Previous Computational Thinking steps allow to define an algorithm at an appropriate generalization and abstraction level.

```python
MakeSandwich(slice1, slice2, spread1, spread2) {
    half1 := Apply spread1 to one side of slice1;
    half2 := Apply spread2 to one side of slice2;
    Stack half1 and half2 s.t. sides with spread face each other;
}
```

```python
MakeKayaToast() {
    initialize toast1, toast2, kaya, butter;
    slice1 := toast(toast1);
    slice2 := toast(toast2);
    makeSandwich(slice1, slice2, kaya, butter);
}
```

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 11

---

# Computational Thinking (CT) and Computer Science (CS)

- CT is applied within CS to create efficient algorithms and solutions to complex problems
- CT during programming, data structures, algorithms, computer architecture, software engineering, etc.
- Modular programming (decomposition), data mining (pattern recognition), modeling (abstraction), algorithm analysis (algorithm design)
- CS contributes tools and techniques to implement the CT process

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
12

---

# CS example 1: Merge Sort

**Problem**: sort array [6,0,8,3,9,2] in ascending order

- **Decomposition**: The problem of sorting large array breaks down into smaller problems (i.e., sorting smaller arrays). The smallest problem size is one, leading to trivially sorted arrays.
- **Pattern Recognition**: Sorted subarrays can be merged efficiently to create larger sorted arrays.
- **Abstraction**: Specific values in the array are not relevant.
- **Algorithm Design**: Recursive design, dividing into a split phase (decomposition) and merge phase (based on recognized pattern).

> Split

> Merge

```text
algorithm MergeSort (F) → Fₛ
Input: an array to be sorted F
Output: a sorted array Fₛ

if F contains one element
then return F
else
    Divide F into F₁ and F₂;
    F₁ := MergeSort (F₁);
    F₂ := MergeSort (F₂);
    return Merge (F₁, F₂);
```

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 13

---

# CS example 2: Database management systems

> 

<table>
  <caption>CS example 2: Database management systems Architecture</caption>
  <thead>
    <tr>
      <th colspan="5">User Interfaces (Web form, SQL Interface, Dashboard)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"></td>
      <td>Executor</td>
      <td>Parser</td>
      <td rowspan="2"></td>
      <td rowspan="2"></td>
    </tr>
    <tr>
      <td>Operator evaluator</td>
      <td>Optimizer</td>
    </tr>
    <tr>
      <td rowspan="2">Transaction manager</td>
      <td colspan="3">File and access methods</td>
      <td rowspan="3">Recovery manager</td>
    </tr>
    <tr>
      <td colspan="3">Buffer manager</td>
    </tr>
    <tr>
      <td>Lock manager</td>
      <td colspan="3">Disk space manager</td>
    </tr>
    <tr>
      <td colspan="5">Database with files, index structures, ...</td>
    </tr>
  </tbody>
</table>



**Problem**: Support use of large amounts of data

- **Decomposition**: Break down the task into subtasks like data storage, retrieval, query processing, ...
- **Pattern recognition**: Patterns in data access are used to optimize query performance. Patterns in typical information need guide query language design...
- **Abstraction**: Table-based data model hides physical implementation details. Declarative query language focuses on what data is requested, not how to get it.
- **Algorithm design**: Numerous algorithms for efficient data storage, retrieval, query processing, ...

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 14

---

# CS example 3: Autonomous vehicles

**Problem**: Build software for self-driving cars

1.  **Decomposition**: Problem divides into subproblems such as perception, prediction, planning, control.
2.  **Pattern recognition**: Use of machine learning algorithms to recognize patterns in sensor data to identify important features (e.g., traffic lights, pedestrians, other vehicles)
3.  **Abstraction**: Focus is on essential features of the driving environment, Details irrelevant to autonomous driving are ignored (e.g., color of other cars).
4.  **Algorithm design**: Development and use of various algorithms for different subtasks (e.g., search algorithms, control algorithms, machine learning algorithms)

> Nanyang Technological University. All rights reserved.

---

# Summary of Computational Thinking

- Computational Thinking is a thought process for solving complex problems.
- Allows to express a problem solution such that a computer, human, or machine can effectively carry it out.
- Process divides into four main parts, namely decomposition, pattern recognition, abstraction, and algorithm design.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 16

---

# DATA SCIENCE THINKING

> Nanyang Technological University. All rights reserved.

---

# Data Science Thinking introduction

- Data Science Thinking is a process for solving data science problems.
  - Data science problems qualify as complex problems to be solved (cf. Computational Thinking)
  - The multi-disciplinary nature of data science problems (cf. definition of data science) requires methods of thinking beyond Computational Thinking.
- The notion of Data Science Thinking is quite new, with many variations of its definition.
- Goal of this lecture is to highlight core aspects that are reflected in most definitions.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 18

---

# Core concepts

- Data Science Thinking combines and adapts existing ways of thinking to answer data science questions.
- The process underlying Data Science Thinking is composed of abstract steps to solve a problem of interest to some stakeholder.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 19

---

# Core concepts

- Data Science Thinking combines and adapts existing ways of thinking to answer data science questions.

> The process underlying Data Science Thinking is composed of abstract steps to solve a problem of interest to some stakeholder.

---

# The different hats of data scientists

- Think like an engineer
- Think like a stakeholder (impact)
- Think like a scientist

> Note that there is no direct connection between ways of thinking and data science pillars, as the correspondence is not one-to-one.

---

# Think like an engineer

- Why?
  - Need for code
  - Complex systems
  - Deploy models
  - Create systems to solve problems
- How?
  - Clean software engineering
  - Design for scalability, robustness, extensibility
  - Automatic processing
- Computational Thinking

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 22

---

# Think like a scientist

## Why?
- Need for advanced analytics
- Investigation of motivations
- Looking for patterns
- Aim to understand the why

## How?
- Follow the scientific method
- Research to understand the problem
- Hypothesize and come up with possible solutions
- Hypothesis testing
- Evaluation, measure results
- Critical Thinking

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
23

---

# Think like a stakeholder

- Why
  - Keep business / scientific goal in mind
  - Measure performance
  - Present insights
  - Consider ethical or societal aspects
- How
  - Develop, quantify, measure, and track key performance indicators (KPIs) wrt goals
  - Presentation, communication, visualization, storytelling
  - Compliance and accountability

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 24

---

# Summary of cross-functional thinking skills

<ins>Software engineering</ins>
<ins>Data Science</ins>
<ins>Math and Statistics</ins>
<ins>Domain expertise</ins>

Data Science Thinking combines ways of thinking stemming from the different disciplines it is based on.

> Critical Thinking

> Computational Thinking

> Impact orientation

---

# Core concepts

> Data Science Thinking combines and adapts existing ways of thinking to answer data science questions.

> The process underlying Data Science Thinking is composed of abstract steps to solve a problem of interest to some stakeholder.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 26

---

# Running example

> How can my athletes get better?

> I may be able to help you based on data. Let’s see ...

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 27

---

# Data Science Thinking Process

The image displays a circular diagram illustrating the "Data Science Thinking Process," which consists of six interconnected steps arranged in a cycle. The steps are:

- **Ask**
- **Prepare**
- **Process**
- **Analyze**
- **Share**
- **Act**

Each step is represented by a blue rectangular box with white text, connected by light gray arrows that indicate the flow of the process in a clockwise direction.

> The diagram is a visual representation of a cyclical workflow in data science, emphasizing the iterative nature of the process.

<table>
  <thead>
    <tr>
        <th>Step</th>
        <th>Process</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Ask</td>
        <td>Ask</td>
    </tr>
    <tr>
        <td>Prepare</td>
        <td>Prepare</td>
    </tr>
    <tr>
        <td>Process</td>
        <td>Process</td>
    </tr>
    <tr>
        <td>Analyze</td>
        <td>Analyze</td>
    </tr>
    <tr>
        <td>Share</td>
        <td>Share</td>
    </tr>
    <tr>
        <td>Act</td>
        <td>Act</td>
    </tr>
  </tbody>
</table>

The diagram is presented on a white background with a red circular icon in the top right corner, which appears to be a logo or symbol related to the content. The bottom of the page includes a footer with the text "Nanyang Technological University. All rights reserved." and the page number "28" in the bottom right corner.

---

# Data Science Thinking Process

> The image shows a circular diagram with six steps in the data science thinking process. The steps are arranged in a circle and connected by arrows indicating a cyclical process. The steps are:
> - Ask (highlighted in blue)
> - Prepare
> - Process
> - Analyze
> - Share
> - Act
> 
> The word "Ask" is at the top of the circle, and the other steps are arranged clockwise around it. The arrows indicate a flow from "Ask" to "Prepare," then to "Process," then to "Analyze," then to "Share," then to "Act," and finally back to "Ask."

---

# Ask

- Define the problem
  - Clearly articulate the business question or problem to be solved with data.
  - Identify the kind of problem.
  - Understand stakeholder expectations.
- Identify the goal
  - Determine what should be achieved by the analysis.
  - Understand why it is relevant to the stakeholder(s).

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
30

---

# Ask (Example)

- How can my athletes get better?
- Let’s start with my sprint athletes. I want them to run faster.
- You are right. Let’s focus on the 100m sprint.
- My athletes are world class, I expect them to run < 10s.

> I may be able to help you based on data. Let’s see ...

- Can you be more specific? What kind of athletes? Better than what? In doing what? ...
- The solutions probably depend on the distance to run. Which one do you have in mind?
- Faster is always better of course. But what level are we talking about? What performance would you expect?

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 31

---

# Ask (Example)

> Yes. The women’s team is doing great already.

> My athletes all have their individual needs and styles. So I’d prefer understanding key factors to optimize their individual plan myself.

> OK, I see. Given these numbers, I suppose your athletes are male, right?

> Are you more interested in understanding factors playing a part in such high sprint performance or do you want recommendations for specific measures?

> OK, great. I should be able to support this based on data.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 32

---

# Ask (Example)

- Define the problem
  - Problem to be solved: Identify key factors that play a role in male sprinters to run 100m in less than 10s.
  - Underlying kind of problem: Prediction of athlete performance depending on a variety of factors.
  - Stakeholder expectations: Actionable insights to get male team to world class level.
- Identify the goal
  - Goal of the analysis: Identified key factors may guide the definition of measures implemented to improve athlete performance.
  - Relevance to stakeholders: They want to make well-informed adaptations to the training plans to become internationally competitive.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 33

---

# Data Science Thinking Process

<table>
  <thead>
    <tr>
        <th>Step</th>
        <th>Description</th>
    </tr>
    <tr>
        <th>Ask</th>
        <th>Define the problem and ask the right questions.</th>
    </tr>
    <tr>
        <th>Prepare</th>
        <th>Gather and prepare the data for analysis.</th>
    </tr>
    <tr>
        <th>Process</th>
        <th>Clean, transform, and process the data.</th>
    </tr>
    <tr>
        <th>Analyze</th>
        <th>Analyze the data to extract insights.</th>
    </tr>
    <tr>
        <th>Share</th>
        <th>Communicate the findings and insights.</th>
    </tr>
    <tr>
        <th>Act</th>
        <th>Take action based on the insights.</th>
    </tr>
  </thead>
</table>

> The process is cyclical, with each step feeding into the next, and the final step often leading back to the initial "Ask" step to refine the problem or explore new questions.

---

# Prepare

- Data collection: Gather relevant data from various sources, such as databases, spreadsheets, or APIs.
- Data understanding: understand the data and the metrics you will need for analysis to assess the usefulness of the data.
- Data access: Evaluate and handle different data locations (internal or external), copyright, privacy, and security.
- Data modeling: organize and transform the data into a format that is suitable for further processing.
- Data integration: Combine data from different sources into a unified dataset.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 35

---

# Prepare (example)

## Observation: Abundance of available data and factors to consider

- Performance may be influenced by diet, spikes, weather, speed, ...
- Many sources with data on many factors (historical records, measurements, logs, videos, ...)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 36

---

# Prepare (example)

**Preparation:** Collect and understand data to gather data that is relevant to gain insights that are actionable to adapt training plans.

- We cannot change the weather, but it is likely a relevant factor to be considered when predicting performance → Integrate wind data, temperature
- Average speed over 100m may be a too coarse granularity.
  → Focus on sources with speed measured at different times of the race
- Is it ok to consider race a factor?
  - Not actionable for the specific goal of our example → ignore
  - May be actionable for related questions, e.g., team selection. But is it ethical?

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
37

---

# Prepare (example)

**Observation**: differences in data and governing policies

- Structured records (historical records), time series (measurements), recordings of races (videos), ...
- Different copyrights (open historical data, proprietary videos), privacy of personal data (blood pressure measurements, medical data), ...

> Nanyang Technological University. All rights reserved.

---

# Prepare (example)

**Preparation**: Access, model, and integrate relevant data to ultimately obtain data that are both relevant and usable to reach the analytical goal.

- **Access**
  - Download CSV and Excel files (free)
  - Query time series data via APIs (restricted number of accesses)
  - Stream high quality video footage (pay per query)
  - Gather health data from athletes via various apps and wearables (secure access and storage)
- **Model**
  - Store all data in tables
  - Avoid redundancy by uniquely representing each athlete and race
- **Integrate**
  - Correctly align race data from CSV records with health data of individual athletes
  - Connect time series details with correct races
  - Link videos to events and extract relevant data from videos (to be put in tables)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 39

---

# Prepare (example)

<table>
    <tr>
        <th>ID</th>
        <th>Athlete</th>
        <th>dateTime</th>
        <th>result</th>
        <th>wind</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Tom</td>
        <td>01:01:19:10:00</td>
        <td>9.98</td>
        <td>+1.2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Lin</td>
        <td>12:03:14:16:00</td>
        <td>10.21</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Paulo</td>
        <td>14/03/14 15:00</td>
        <td>10.1</td>
        <td>-0.04</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Karl</td>
        <td>17/05/12 08:30</td>
        <td>10.4</td>
        <td>+0.25</td>
    </tr>
</table>From downloaded CSV
From downloaded Excel

> Correct alginment

<table>
    <tr>
        <th>SplitID</th>
        <th>RID</th>
        <th>Time</th>
        <th>Distance</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>2.04</td>
        <td>10</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>3.14</td>
        <td>20</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>3.95</td>
        <td>30</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>4.78</td>
        <td>40</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>5.69</td>
        <td>50</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
</table>> Extracted from video

<table>
    <tr>
        <th>SplitID</th>
        <th>RID</th>
        <th>Time</th>
        <th>Distance</th>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>10.21</td>
        <td>100</td>
    </tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>2801</td>
        <td>10</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>4120</td>
        <td>20</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
</table>> Retrieved via API

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 40

---

# Data Science Thinking Process

The image displays a circular diagram illustrating the "Data Science Thinking Process" with six stages arranged in a cycle. The stages are:

- Ask
- Prepare
- Process
- Analyze
- Share
- Act

The "Process" stage is highlighted in a darker blue box, while the other stages are in lighter blue boxes. Arrows indicate the flow from one stage to the next, forming a continuous loop.

> The diagram is a visual representation of a cyclical process in data science, emphasizing the iterative nature of the work.

Nanyang Technological University. All rights reserved.

---

# Process

- Data transformation: Convert data into a suitable format for analysis, such as numerical or categorical.
- Data cleaning: Cleanse the data by removing errors, inconsistencies, and missing values. Necessary to avoid garbage-in-garbage-out problem.
- Feature engineering: Create new features or variables from existing data for analysis.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
42

---

# Process (example)

<table>
    <tr>
        <th>ID</th>
        <th>Athlete</th>
        <th>dateTime</th>
        <th>result</th>
        <th>wind</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Tom</td>
        <td>01:01:19:10:00</td>
        <td>9.98</td>
        <td>+1.2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Lin</td>
        <td>12:03:14:16:00</td>
        <td>10.21</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Paulo</td>
        <td>14/03/14 15:00</td>
        <td>10.1</td>
        <td>-0.04</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Karl</td>
        <td>17/05/12 08:30</td>
        <td>10.4</td>
        <td>+0.25</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>SplitID</td>
        <td>RID</td>
        <td>Time</td>
        <td>Distance</td>
    <td></td></tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>2.04</td>
        <td>10</td>
    <td></td></tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>3.14</td>
        <td>20</td>
    <td></td></tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>3.80</td>
        <td>30</td>
    <td></td></tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>4.20</td>
        <td>40</td>
    <td></td></tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>5.18</td>
        <td>50</td>
    <td></td></tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    <td></td></tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>10.21</td>
        <td>100</td>
    <td></td></tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>2801</td>
        <td>10</td>
    <td></td></tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>4120</td>
        <td>20</td>
    <td></td></tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    <td></td></tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 43

---

# Process (example)

<table>
    <tr>
        <th>ID</th>
        <th>Athlete</th>
        <th>dateTime</th>
        <th>result</th>
        <th>wind</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Tom</td>
        <td>01:01:19:10:00</td>
        <td>9.98</td>
        <td>+1.2</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Lin</td>
        <td>12:03:14:16:00</td>
        <td>10.21</td>
        <td>0.00</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Paulo</td>
        <td>14:03:14:15:00</td>
        <td>10.13</td>
        <td>-0.04</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Karl</td>
        <td>17:05:12:08:30</td>
        <td>10.42</td>
        <td>+0.25</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>SplitID</td>
        <td>RID</td>
        <td>Time</td>
        <td>Distance</td>
        <td>Velocity</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>2.04</td>
        <td>10</td>
        <td>4.90</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>3.14</td>
        <td>20</td>
        <td>9.09</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>3.95</td>
        <td>30</td>
        <td>12.35</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>4.78</td>
        <td>40</td>
        <td>12.04</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>5.69</td>
        <td>50</td>
        <td>10.98</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    <tr>
        <td>1</td>
        <td>2</td>
        <td>10.21</td>
        <td>100</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>2.80</td>
        <td>10</td>
        <td>3.57</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
        <td>4.12</td>
        <td>20</td>
        <td>7.58</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 44

---

# Data Science Thinking Process

The image displays a circular diagram illustrating the "Data Science Thinking Process," which consists of six interconnected steps arranged in a cycle. The steps are:

- **Ask**
- **Prepare**
- **Process**
- **Analyze**
- **Share**
- **Act**

The "Analyze" step is highlighted in a darker blue box, indicating it is the current focus or a key step in the process. The other steps are in lighter blue boxes. Arrows connect the boxes in a clockwise direction, showing the flow of the process.

> The diagram is a visual representation of a cyclical process, emphasizing that data science thinking is an iterative and continuous activity.

Nanyang Technological University. All rights reserved. 45

---

# Analyze

- Exploratory data analysis: Explore the data to understand its characteristics and identify patterns.
- Statistical analysis: Apply statistical techniques to test hypotheses and draw inferences.
- Machine learning: Utilize machine learning algorithms to uncover hidden insights and make predictions.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
46

---

# Analyze (example)



<table>
  <caption>Velocity over Time during a Sprint (Acceleration, Peak, and Deceleration Phases)</caption>
  <thead>
    <tr>
      <th>time (s)</th>
      <th>velocity (m/s)</th>
      <th>Phase Marker</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0</td>
      <td>0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>1.0</td>
      <td>6.0</td>
      <td></td>
    </tr>
    <tr>
      <td>2.0</td>
      <td>9.0</td>
      <td></td>
    </tr>
    <tr>
      <td>3.0</td>
      <td>10.2</td>
      <td></td>
    </tr>
    <tr>
      <td>4.0</td>
      <td>10.8</td>
      <td></td>
    </tr>
    <tr>
      <td>4.3</td>
      <td>11.0</td>
      <td>Phase Transition (Acceleration to Peak)</td>
    </tr>
    <tr>
      <td>5.0</td>
      <td>11.1</td>
      <td></td>
    </tr>
    <tr>
      <td>6.0</td>
      <td>11.2</td>
      <td></td>
    </tr>
    <tr>
      <td>6.9</td>
      <td>11.2</td>
      <td>Phase Transition (Peak to Deceleration)</td>
    </tr>
    <tr>
      <td>8.0</td>
      <td>11.1</td>
      <td></td>
    </tr>
    <tr>
      <td>9.0</td>
      <td>11.1</td>
      <td></td>
    </tr>
    <tr>
      <td>10.0</td>
      <td>11.1</td>
      <td></td>
    </tr>
    <tr>
      <td>10.4</td>
      <td>11.1</td>
      <td></td>
    </tr>
  </tbody>
</table>



Through exploratory analysis, recognize the pattern that sprints typically divided into three phases (acceleration, peak, deceleration)

Study correlations of factors or metrics using statistical tests to determine that length of maximum velocity is not strongly correlated with final time.

Train a predictive model using machine learning to predict realistic performance under various conditions.

Images from [https://doi.org/10.1371/journal.pone.0303366](https://doi.org/10.1371/journal.pone.0303366)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 47

---

# Data Science Thinking Process

- Ask
- Prepare
- Process
- Analyze
- Share
- Act

> Nanyang Technological University. All rights reserved.

48

---

# Share

- Data visualization: Create visualizations (charts, graphs, dashboards) to communicate findings effectively.
- Storytelling: Present the findings in a clear and concise manner, tailored to the audience's needs.
- Reporting: Generate reports summarizing the key findings and recommendations.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
49

---

# Share (Example)

Our model can accurately predict
velocity over 10s splits (see bottom
graph), as tested on a large variety of
races in terms of final time (see
histogram). You can use this to see at
which phase your athletes have the
most room for improvement.

Peak velocity shows by far the
strongest negative correlation with
final time. This may help prioritize
training increasing peak velocity.

Histogram of final time


<table>
  <caption>Histogram of final time and Velocity over 10s splits</caption>
  <thead>
    <tr>
      <th colspan="2">Histogram of final time</th>
      <th colspan="2">Velocity over 10s splits</th>
    </tr>
    <tr>
      <th>Final Time Interval (s)</th>
      <th>Frequency</th>
      <th>Time (s)</th>
      <th>Actual Mean Velocity (m/s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[9.58, 9.73]</td>
      <td>5</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>(9.73, 9.88]</td>
      <td>19</td>
      <td>2</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>(9.88, 10.03]</td>
      <td>66</td>
      <td>3</td>
      <td>9.4</td>
    </tr>
    <tr>
      <td>(10.03, 10.18]</td>
      <td>122</td>
      <td>4</td>
      <td>10.5</td>
    </tr>
    <tr>
      <td>(10.18, 10.33]</td>
      <td>139</td>
      <td>5</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td>(10.33, 10.48]</td>
      <td>97</td>
      <td>6</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.48, 10.63]</td>
      <td>36</td>
      <td>7</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td>(10.63, 10.78]</td>
      <td>37</td>
      <td>8</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.78, 10.93]</td>
      <td>18</td>
      <td>9</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>(10.93, 11.08]</td>
      <td>9</td>
      <td>10</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td>&gt; 11.08</td>
      <td>32</td>
      <td>10.5</td>
      <td>10.6</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 50


<table>
  <caption>Athletic Performance Analysis: Final Time Distribution and Velocity Prediction</caption>
  <thead>
    <tr>
      <th colspan="2">Histogram of final time</th>
      <th colspan="2">Velocity over 10s splits</th>
    </tr>
    <tr>
      <th>Final Time Interval (s)</th>
      <th>Frequency (Count)</th>
      <th>Time (s)</th>
      <th>Actual Mean Velocity (m/s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[9.58, 9.73]</td>
      <td>5</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>(9.73, 9.88]</td>
      <td>19</td>
      <td>1.0</td>
      <td>2.5</td>
    </tr>
    <tr>
      <td>(9.88, 10.03]</td>
      <td>66</td>
      <td>2.0</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>(10.03, 10.18]</td>
      <td>122</td>
      <td>3.0</td>
      <td>9.4</td>
    </tr>
    <tr>
      <td>(10.18, 10.33]</td>
      <td>139</td>
      <td>4.0</td>
      <td>10.5</td>
    </tr>
    <tr>
      <td>(10.33, 10.48]</td>
      <td>97</td>
      <td>5.0</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td>(10.48, 10.63]</td>
      <td>36</td>
      <td>6.0</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.63, 10.78]</td>
      <td>37</td>
      <td>7.0</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td>(10.78, 10.93]</td>
      <td>18</td>
      <td>8.0</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.93, 11.08]</td>
      <td>9</td>
      <td>9.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>&gt; 11.08</td>
      <td>32</td>
      <td>10.0</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>10.5</td>
      <td>10.6</td>
    </tr>
  </tbody>
</table>



<table>
  <caption>Data from "Histogram of final time" and "Velocity vs. Time" charts</caption>
  <thead>
    <tr>
      <th colspan="2">Histogram of final time</th>
      <th colspan="2">Velocity over 10s splits</th>
    </tr>
    <tr>
      <th>Final Time Interval (s)</th>
      <th>Frequency</th>
      <th>Time (s)</th>
      <th>Actual Mean Velocity (m/s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[9.58, 9.73]</td>
      <td>5</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>(9.73, 9.88]</td>
      <td>19</td>
      <td>1</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>(9.88, 10.03]</td>
      <td>66</td>
      <td>2</td>
      <td>9.4</td>
    </tr>
    <tr>
      <td>(10.03, 10.18]</td>
      <td>122</td>
      <td>3</td>
      <td>10.5</td>
    </tr>
    <tr>
      <td>(10.18, 10.33]</td>
      <td>139</td>
      <td>4</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td>(10.33, 10.48]</td>
      <td>97</td>
      <td>5</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.48, 10.63]</td>
      <td>36</td>
      <td>6</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td>(10.63, 10.78]</td>
      <td>37</td>
      <td>7</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>(10.78, 10.93]</td>
      <td>18</td>
      <td>8</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>(10.93, 11.08]</td>
      <td>9</td>
      <td>9</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td>&gt; 11.08</td>
      <td>32</td>
      <td>10</td>
      <td>10.6</td>
    </tr>
  </tbody>
</table>

---

# Share (example)

> [Facebook20]

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved. 51

---

# Data Science Thinking Process

- Ask
- Prepare
- Process
- Analyze
- Share
- Act

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 52

---

# Act

- Decision-making: Use the insights gained from the analysis to make informed decisions.
- Implementation: Put the decisions into action to achieve the desired outcomes.
- Tracking: Define and implement measures and metrics to monitor impact of the implementation.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 53

---

# Act (Example)

Tom is doing exceptionally well in the first half of the race, but performance deteriorates in second half. Let’s work on reducing deceleration.

Let’s implement the following measures to that end: 🏋️‍♂️⚡🏃‍♂️



<table>
  <caption>Velocity vs. Time for Athlete Performance Analysis</caption>
  <thead>
    <tr>
      <th>time (s)</th>
      <th>actual mean data (velocity m/s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>2.0</td>
      <td>5.2</td>
    </tr>
    <tr>
      <td>3.0</td>
      <td>9.4</td>
    </tr>
    <tr>
      <td>4.0</td>
      <td>10.5</td>
    </tr>
    <tr>
      <td>5.0</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td>6.0</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>7.0</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td>8.0</td>
      <td>11.1</td>
    </tr>
    <tr>
      <td>9.0</td>
      <td>11.0</td>
    </tr>
    <tr>
      <td>10.0</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td>10.5</td>
      <td>10.6</td>
    </tr>
  </tbody>
</table>



<table>
    <tr>
        <th>ID</th>
        <th>Athlete</th>
        <th>dateTime</th>
        <th>result</th>
        <th>wind</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Tom</td>
        <td>01:01:19:10:00</td>
        <td>9.98</td>
        <td>+1.2</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>SplitID</td>
        <td>RID</td>
        <td>Time</td>
        <td>Distance</td>
        <td>Velocity</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>2.04</td>
        <td>10</td>
        <td>4.90</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>3.14</td>
        <td>20</td>
        <td>9.09</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>3.95</td>
        <td>30</td>
        <td>12.35</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>4.78</td>
        <td>40</td>
        <td>12.04</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>5.69</td>
        <td>50</td>
        <td>10.98</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 54

---

# Data Science Thinking Process

- Ask
  - (again)
- Prepare
- Process
- Analyze
- Share
- Act

> The diagram shows a circular process with six steps: Ask (again), Prepare, Process, Analyze, Share, and Act. Arrows indicate a cyclical flow from one step to the next, starting from "Ask (again)" and ending at "Act," which then loops back to "Ask (again)."

Nanyang Technological University. All rights reserved. 55

---

# Ask (iterative)

- Reflect on results: Evaluate the effectiveness of the analysis and the actions taken.
- Identify new questions: Based on the insights gained, formulate new questions for further exploration.
- Start the process again: Begin a new cycle of data analysis to address the new questions.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 56

---

# Act (Example)

... as time has passed...

> Wow, Tom made great progress! Most of my other athletes, too.

> Can we find out which measures I tried were most effective to optimize future training plans?

> I may be able to help you based on data. Let’s see ...

<table>
    <tr>
        <th>ID</th>
        <th>Athlete</th>
        <th>dateTime</th>
        <th>result</th>
        <th>wind</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Tom</td>
        <td>01:01:24:10:00</td>
        <td>9.79</td>
        <td>+0.9</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>SplitID</td>
        <td>RID</td>
        <td>Time</td>
        <td>Distance</td>
        <td>Velocity</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>2.02</td>
        <td>10</td>
        <td>4.93</td>
    </tr>
    <tr>
        <td>2</td>
        <td>1</td>
        <td>3.12</td>
        <td>20</td>
        <td>9.12</td>
    </tr>
    <tr>
        <td>3</td>
        <td>1</td>
        <td>3.94</td>
        <td>30</td>
        <td>12.25</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>4.76</td>
        <td>40</td>
        <td>12.23</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1</td>
        <td>5.66</td>
        <td>50</td>
        <td>11.99</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 57

---

# Summary

- Define the problem
- Identify the goals



<table>
  <caption>Summary: Data Analysis Lifecycle</caption>
  <thead>
    <tr>
      <th>Stage</th>
      <th>Activities / Goals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ask</td>
      <td>
        <ul>
          <li>Define the problem</li>
          <li>Identify the goals</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Prepare</td>
      <td>
        <ul>
          <li>Collect data</li>
          <li>Understand data</li>
          <li>Access data</li>
          <li>Model data</li>
          <li>Integrate data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Process</td>
      <td>
        <ul>
          <li>Transform data</li>
          <li>Clean data</li>
          <li>Enrich data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Analyze</td>
      <td>
        <ul>
          <li>Use exploratory analysis</li>
          <li>Apply statistical methods</li>
          <li>Leverage machine learning</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Share</td>
      <td>
        <ul>
          <li>Visualize</li>
          <li>Report</li>
          <li>Captivate stakeholders</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Act</td>
      <td>
        <ul>
          <li>Make decisions</li>
          <li>Implement actions</li>
          <li>Monitor KPIs</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>



- Collect data
- Understand data
- Access data
- Model data
- Integrate data

- Transform data
- Clean data
- Enrich data

- Use exploratory analysis
- Apply statistical methods
- Leverage machine learning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 58


<table>
  <caption>Summary: Data Analysis Lifecycle</caption>
  <thead>
    <tr>
      <th>Stage</th>
      <th>Actions / Objectives</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ask</td>
      <td>
        <ul>
          <li>Define the problem</li>
          <li>Identify the goals</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Prepare</td>
      <td>
        <ul>
          <li>Collect data</li>
          <li>Understand data</li>
          <li>Access data</li>
          <li>Model data</li>
          <li>Integrate data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Process</td>
      <td>
        <ul>
          <li>Transform data</li>
          <li>Clean data</li>
          <li>Enrich data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Analyze</td>
      <td>
        <ul>
          <li>Use exploratory analysis</li>
          <li>Apply statistical methods</li>
          <li>Leverage machine learning</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Share</td>
      <td>
        <ul>
          <li>Visualize</li>
          <li>Report</li>
          <li>Captivate stakeholders</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Act</td>
      <td>
        <ul>
          <li>Make decisions</li>
          <li>Implement actions</li>
          <li>Monitor KPIs</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

---

# Computational Thinking and Data Science Thinking

## COMPARISON

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
59

---

# Similarities

Both Computational Thinking and Data Science Thinking ...

- ... define thought processes that help solve complex problems.
- ... involve problem solving and analytical skills.
- ... leverage computational tools.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 60

---

# Differences

<table>
    <tr>
        <th></th>
        <th>Computational Thinking</th>
        <th>Data Science Thinking</th>
    </tr>
    <tr>
        <td>**Focus**</td>
        <td>Broad, general problem-solving</td>
        <td>Focus on gaining data-based insights</td>
    </tr>
    <tr>
        <td>**Domain-knowledge**</td>
        <td>Not strictly required</td>
        <td>Required</td>
    </tr>
    <tr>
        <td>**Tools and techniques**</td>
        <td>Wide range of computational tools and techniques</td>
        <td>Focus on data-oriented tools and techniques, scientific methodology</td>
    </tr>
    <tr>
        <td>**Outcome**</td>
        <td>Efficient and systematic solutions</td>
        <td>Data-based insights</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
61

---

# Computational Thinking and Data Science Thinking

## SUMMARY

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 62

---

# Summary
(data science perspective)

Computational Thinking is part of Data Science Thinking follows Process for data-based insights

- Decomposition
- Pattern recognition
- Abstraction
- Algorithm design

<table>
  <thead>
    <tr>
        <th>Computational Thinking</th>
        <th>Data Science</th>
        <th>Critical Thinking</th>
    </tr>
    <tr>
        <th>Impact orientation</th>
        <th colspan="2"></th>
    </tr>
  </thead>
</table>

> Process for data-based insights

> <img src="https://i.imgur.com/1234567.png" alt="Circular diagram showing the process for data-based insights with six steps: Ask, Prepare, Process, Analyze, Share, Act." />

- Ask
- Prepare
- Process
- Analyze
- Share
- Act

Nanyang Technological University. All rights reserved. 63

---

# You are now equipped to ...

- ...describe and compare the main characteristics of Computational Thinking and Data Science Thinking.
- ... explain how cross-functional thinking skills complement each other to solve a data science problem.
- ... argue why and how a problem should be addressed through Data Science Thinking (or not).
- ... conceive a rough agenda to solve a new problem by following the Data Science Thinking process.

> Nanyang Technological University. All rights reserved.

---

# Questions?

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.

---

# References / Additional reading

- [Facebook20] [https://www.facebook.com/EMsportscience/videos/from-1896-to-our-days-the-evolution-of-100m-sprint/866569130746512/](https://www.facebook.com/EMsportscience/videos/from-1896-to-our-days-the-evolution-of-100m-sprint/866569130746512/)
- [EMC14] EMC Education Services, ed. *Data science and big data analytics: discovering, analyzing, visualizing and presenting data*. John Wiley & Sons, 2014.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
66