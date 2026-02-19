# Data Science Fundamentals
## [SC3021]

### Chapter 4: Data Preparation

Assoc. Prof. Melanie Herschel | CCDS

---

# Chapter content

- Data science overview
  - What is Data Science?
  - Data Science Thinking vs. Computational Thinking
  - Data Science Ecosystem
- Data preparation and data management
  - Flow of data
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
  - Explanation
  - Data visualization
- Design considerations
  - Privacy
  - Security
  - Ethics
  - Psychology
  - Policies



<table>
  <caption>Chapter content</caption>
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
      <td>What is Data Science?</td>
      <td>Flow of data</td>
      <td>Descriptive analytics</td>
      <td>Privacy</td>
    </tr>
    <tr>
      <td>Data Science Thinking vs. Computational Thinking</td>
      <td>Data profiling</td>
      <td>Diagnostic Analytics</td>
      <td>Security</td>
    </tr>
    <tr>
      <td>Data Science Ecosystem</td>
      <td>Structuring</td>
      <td>Prescriptive analytics</td>
      <td>Ethics</td>
    </tr>
    <tr>
      <td></td>
      <td>Enriching</td>
      <td>Predictive analytics</td>
      <td>Psychology</td>
    </tr>
    <tr>
      <td></td>
      <td>Data cleaning</td>
      <td>Explanation</td>
      <td>Policies</td>
    </tr>
    <tr>
      <td></td>
      <td>Data management platforms</td>
      <td>Data visualization</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Schema design</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Querying data</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 2

---

# Chapter 4.2: Data profiling (continued)

> NANYANG TECHNOLOGICAL UNIVERSITY SINGAPORE

---

<table>
  <caption>Classification of standard profiling tasks</caption>
  <thead>
    <tr>
      <th>Level 1</th>
      <th>Level 2</th>
      <th>Level 3</th>
      <th>Level 4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="11">Data profiling</td>
      <td rowspan="3">Single column</td>
      <td>Cardinalities</td>
      <td></td>
    </tr>
    <tr>
      <td>Patterns and data types</td>
      <td></td>
    </tr>
    <tr>
      <td>Value distributions</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="8">Multiple columns</td>
      <td rowspan="3">Uniqueness</td>
      <td>Key discovery</td>
    </tr>
    <tr>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
    <tr>
      <td rowspan="3">Inclusion dependencies</td>
      <td>Foreign key discovery</td>
    </tr>
    <tr>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
    <tr>
      <td rowspan="2">Functional dependencies</td>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
  </tbody>
</table>



# Classification of standard profiling tasks

- Applies to structured (tabular) data.
- Distinguishes between profiling of data stored in a single column and data stored across multiple columns.
- For profiling tasks on multiple columns, exact, conditional, and partial tasks exist.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 4

---

# Single-column vs. multi-column

## Single column profiling
- Most basic form of data profiling
- Assumption: All values are of same type
- Assumption: All values have some common properties that are to be discovered
- Often part of the basic statistics gathered by DBMS
- Complexity: Number of values/rows

## Multi-column profiling
- Discover joint properties
- Discover dependencies
- Complexity: Number of columns and number of values

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 5

---

# Single-column vs. multi-column

> Multiple columns

- Uniqueness
- Inclusion Dependencies
- Functional dependencies

> Multi-column profiling

- Discover joint properties
- Discover dependencies
- Complexity: Number of columns and number of values

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 6

---

# Uniqueness and keys

- Unique column: all values are unique
- Unique column combination
  - Considers values from multiple attributes A
  - Only unique value combinations when combining values of A
  - Minimality: No strict subset A' ⊂ A is a unique column (combination)
- Key candidate: Unique values AND no null values
- Key
  - Column / column combination that serves as general unique identifier for entities modeled by a table.
  - Uniqueness and non-null in one instance of a table does not imply key: Only human can specify keys.
- Applications: schema design, data integration, indexing, query optimization.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 7

---

# Uniqueness and keys

- **Name**
  - Text
  - Unique
- **Distinct** 891
- **Distinct (%)** 100.0%
- **Missing** 0
- **Missing (%)** 0.0%
- **Memory size** 73.2 KiB

> Titanic dataset exploration with ydata

Unique column
No missing values
=> Key candidate
=> Not a key, because, in general, it is possible that multiple passengers boarding a ship have the same name.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 8

---

# Uniqueness and Keys

<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>ZIP</th>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>42</td>
        <td>1234</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
        <td>39</td>
        <td>9876</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Smith</td>
        <td>42</td>
        <td>2468</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>22</td>
        <td>1234</td>
    </tr>
</table>> No single column is unique

> Column combination (Firstname, Lastname, Age, ZIP) is unique, BUT not minimal!

Minimal unique column combinations:
- (Lastname, Age)
- (Firstname, Age)
- (Age, ZIP)

> Discovery algorithms find all, relevance assessed by domain expert.

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

> Nanyang Technological University. All rights reserved. 9

---

# Inclusion dependencies and foreign keys

- A ⊆ B: All values in attribute A are also present in attribute B
- A₁,...,Aᵢ ⊆ B₁,...,Bᵢ:
  All value combinations in A₁,...,Aᵢ are also present in B₁,...,Bᵢ
- Prerequisite for foreign key that defines attributes referencing attributes of another table (via value equality)
  - Used across relations
  - Use across databases
  - But again: Discovery on a given instance, only user can specify if it holds in general and should be defined as foreign key at schema level.
- Applications: schema design, data integration, indexing, query optimization.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 10

---

# Inclusion dependencies and foreign keys

## Data from one source S1

<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>ZIP</th>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>42</td>
        <td>1234</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
        <td>39</td>
        <td>9876</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Smith</td>
        <td>42</td>
        <td>2468</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>22</td>
        <td>1234</td>
    </tr>
</table>## Data from another source S2

<table>
    <tr>
        <th>ZIP</th>
        <th>City</th>
    </tr>
    <tr>
        <td>1234</td>
        <td>Blue Mountain</td>
    </tr>
    <tr>
        <td>2345</td>
        <td>Green Forest</td>
    </tr>
    <tr>
        <td>2468</td>
        <td>Big River</td>
    </tr>
    <tr>
        <td>5588</td>
        <td>Gold Hill</td>
    </tr>
    <tr>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
</table>S1.ZIP ⊆ S2.ZIP  
but not vice versa

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 11

---

# Functional dependencies

- Let X be a set of attributes and A be a single attribute.
- A functional dependency exists from X to A if, whenever two records have the same X values, they also have the same A values.
- A functional dependency is written as X → A (pronounced X determines A).
- Applications: schema design, data cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
12

---

# Functional dependencies

<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>ZIP</th>
        <th>City</th>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>42</td>
        <td>1234</td>
        <td>Blue Mountain</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
        <td>39</td>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Smith</td>
        <td>42</td>
        <td>2468</td>
        <td>Big River</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>22</td>
        <td>1234</td>
        <td>Blue Mountain</td>
    </tr>
    <tr>
        <td>Jack</td>
        <td>Smith</td>
        <td>65</td>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
    <tr>
        <td>Jill</td>
        <td>Park</td>
        <td>22</td>
        <td>2469</td>
        <td>Big River</td>
    </tr>
</table>ZIP → City holds

But City does NOT determine ZIP (one city can have several zip codes)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
13

---

# Partial dependencies

- Also known as “approximate dependencies”
- Refers to dependencies that do not perfectly hold.
- Examples: Dependency holds
  - For all but 10 of the tuples
  - Only for 80% of the tuples
  - Only for 1% of the tuples
- Classification of data profiling tasks includes partial dependencies for multi-attribute profiling tasks.
- Generalizes to further profiling tasks, e.g., for patterns, types, etc.
- Applications: data quality assessment, data cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 14

---

# Partial dependencies

<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>ZIP</th>
        <th>City</th>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>42</td>
        <td>1234</td>
        <td>Blue Mountain</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
        <td>39</td>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Smith</td>
        <td>42</td>
        <td>2468</td>
        <td>Big River</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>22</td>
        <td>1234</td>
        <td>BM</td>
    </tr>
    <tr>
        <td>Jack</td>
        <td>Smith</td>
        <td>65</td>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
    <tr>
        <td>Jill</td>
        <td>Park</td>
        <td>22</td>
        <td>2469</td>
        <td>Big River</td>
    </tr>
</table>ZIP → City **almost** holds

> Data quality issue: City name was abbreviated, which is not the standard format.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
15

---

# Conditional dependencies

- Given a partial inclusion dependency or functional dependency, conditional dependencies define for which part of the data they hold.
- Expressed as a condition over the attributes of the relation.
- Problems:
  - Infinite possibilities of conditions
  - Interestingness:
    - Many distinct values: less interesting
    - Few distinct values: surprising condition – high coverage
- Applications: data integration, data cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 16

---

# Conditional dependencies

Data from one source S1 covering several countries

<table>
    <tr>
        <th>Firstname</th>
        <th>Lastname</th>
        <th>Age</th>
        <th>ZIP</th>
        <th>Country</th>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>42</td>
        <td>1234</td>
        <td>E</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>Doe</td>
        <td>39</td>
        <td>9876</td>
        <td>E</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Smith</td>
        <td>42</td>
        <td>2468</td>
        <td>E</td>
    </tr>
    <tr>
        <td>John</td>
        <td>Doe</td>
        <td>22</td>
        <td>1234</td>
        <td>E</td>
    </tr>
    <tr>
        <td>Pierre</td>
        <td>Dupont</td>
        <td>58</td>
        <td>1234</td>
        <td>F</td>
    </tr>
    <tr>
        <td>Jeanne</td>
        <td>Petit</td>
        <td>63</td>
        <td>5712</td>
        <td>F</td>
    </tr>
</table>Data from another source S2 covering country E only

<table>
    <tr>
        <th>ZIP</th>
        <th>City</th>
    </tr>
    <tr>
        <td>1234</td>
        <td>Blue Mountain</td>
    </tr>
    <tr>
        <td>2345</td>
        <td>Green Forest</td>
    </tr>
    <tr>
        <td>2468</td>
        <td>Big River</td>
    </tr>
    <tr>
        <td>5588</td>
        <td>Gold Hill</td>
    </tr>
    <tr>
        <td>9876</td>
        <td>Ice Lake</td>
    </tr>
</table>S1.ZIP ⊆ S2.ZIP only partially holds.

It holds (exactly) for tuples where S1.Country = E

→ This conditional inclusion dependency helps us to correctly integrate data.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 17

---

# Computational complexity

- Identifying multi-column constraints may require to consider all possible column combinations
  → exponential in the number of columns
- Checking if a constraint holds for one specific column combination requires checking the data, e.g., by comparing all rows to each other → quadratic in the number of rows
- Altogether, this is considered practically infeasible for large amounts of data.
- Designing efficient algorithms for multi-column profiling is important.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 18

---

<table>
  <caption>Data profiling classification summary</caption>
  <thead>
    <tr>
      <th>Root Category</th>
      <th>Scope</th>
      <th>Profiling Type</th>
      <th>Specific Tasks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="11">Data profiling</td>
      <td rowspan="3">Single column</td>
      <td>Cardinalities</td>
      <td></td>
    </tr>
    <tr>
      <td>Patterns and data types</td>
      <td></td>
    </tr>
    <tr>
      <td>Value distributions</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="8">Multiple columns</td>
      <td rowspan="3">Uniqueness</td>
      <td>Key discovery</td>
    </tr>
    <tr>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
    <tr>
      <td rowspan="3">Inclusion dependencies</td>
      <td>Foreign key discovery</td>
    </tr>
    <tr>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
    <tr>
      <td rowspan="2">Functional dependencies</td>
      <td>Conditional</td>
    </tr>
    <tr>
      <td>Partial</td>
    </tr>
  </tbody>
</table>



# Data profiling
## classification summary

- Distinguishes between
  profiling of data stored in a
  single column and data
  stored across multiple
  columns.
- For profiling tasks on
  multiple columns, exact,
  conditional, and partial tasks
  exist.
- Applications vary for different
  profiling tasks, but all are
  relevant to data science.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 19

---

# CONCLUSION

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 23

---

# Summary

- Data evolves through stages (from raw over refined to production)
- Data preparation is essential for data actions and analytical actions across all data flow stages.
- Two critical tasks of data preparation are data profiling and data transformation.
- Data profiling is the set of activities and processes to determine relevant metadata about a given dataset.
- Such metadata can relate to single columns or multiple columns.
- Data profiling applies at various stages and for various applications throughout data processing.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 24

---

# You should now be able to...

- ... explain different profiling tasks and how they may apply at different data science stages.
- ... identify profiling tasks suited to gain relevant information on a given dataset for a specific application.
- ... reflect on the computational complexity of profiling tasks when applying them to large data sets.

> Nanyang Technological University. All rights reserved.

25

---

# References and credits

- Joseph M. Hellerstein, Tye Rattenbury, Jeffrey Heer, Sean Kandel, Connor Carreras. Principles of Data Wrangling. O’Reilly Media. 2017 – Chapter 4
- Ziawasch Abedjan, Lukasz Golab, Felix Naumann: Profiling relational data: a survey. VLDB J. 24(4): 557-581 (2015)
- Slides partially based on slides shared by Felix Naumann, Hasso-Plattner-Institut Potsdam, Germany

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
26