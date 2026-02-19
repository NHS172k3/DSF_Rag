# Data Science Fundamentals
[SC3021]

## Chapter 4: Data Preparation

Assoc. Prof. Melanie Herschel | CCDS

---

# Data transformation tasks

- Data Profiling
- Data Structuring
- Data preparation
- Data Enriching
- Data Cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
2

---

# Chapter 4.3: Data Transformation

> NANYANG TECHNOLOGICAL UNIVERSITY SINGAPORE

---

# Overview of structuring transformations

> **Structuring**
> - **Intrarecord**
>   - Reordering attributes
>   - Creating attributes
>   - Combining attributes
> - **Interrecord**
>   - Filtering dataset
>   - Aggregation
>   - Pivot

---

# Interrecord structuring

## Filtering
Removal of columns or rows.

## Aggregation
Attributes are added with values extracted from existing attributes

## Pivot
Attributes are merged into a single attribute

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
5

---

# Filtering

- Removes records or attributes from a dataset.
- Is considered a structuring operation when it is used to alter the granularity of a dataset by changing the types of represented records and attributes.
- Two sub-types:
  - Record-based filtering removes records (rows)
  - Attribute-based filtering removes attributes (columns)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
6

---

# Filtering - Examples

- Record-based filtering:
  “Zoom-in” to only one type of entity that made each donation by limiting dataset to rows with Column7 = “PAC”
- Attribute-based filtering:
  “Zoom-in” by retaining only relevant attributes.
- Both result in a finer-grained granularity than the original dataset.



<table>
    <caption>Filtering Examples: Record-based and Attribute-based</caption>
    <thead>
        <tr>
            <th colspan="4">Record-based Filtering Results</th>
        </tr>
        <tr>
            <th>Column1</th>
            <th>Column2</th>
            <th>Column3</th>
            <th>Column4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>C00495580</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00495580</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00495580</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00495580</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00495580</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00515049</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00563601</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00587030</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00603084</td>
            <td>N</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00578997</td>
            <td>A</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00114439</td>
            <td>A</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00114439</td>
            <td>A</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00536664</td>
            <td>A</td>
            <td>YE</td>
            <td>P</td>
        </tr>
        <tr>
            <td>C00626390</td>
            <td>A</td>
            <td>YE</td>
            <td>P</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th colspan="4">Attribute-based Filtering Results</th>
        </tr>
        <tr>
            <th>Column1</th>
            <th>Column2</th>
            <th>Column3</th>
            <th>Column4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>C00276311</td>
            <td>15</td>
            <td>IND</td>
            <td>NE</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>NY</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>DC</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>DC</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>CA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>NY</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>MA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>FL</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15E</td>
            <td>IND</td>
            <td>VA</td>
        </tr>
        <tr>
            <td>C00495351</td>
            <td>15</td>
            <td>IND</td>
            <td>MA</td>
        </tr>
    </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 7

---

# Aggregation

- Combination of data that obtains new attributes with a **shifted granularity** compared to the original data.
- Each input record maps to exactly one output record.
- Each output record combines one or more input records.
- Values of the new attributes in the output are obtained through aggregation functions (sum, mean, min, list concatenation, etc.) of input record attributes.

Input
Output

---

# Aggregation – Example

- Manipulate the granularity of the dataset so that each row summarizes the campaign contributions made to each campaign committee.
- For each campaign committee, we create three new columns:
  - The average contribution made to it
  - The sum of contributions made to it
  - The number of contributions made to it

```python
# Group by 'Column1' and calculate the average, sum, and count of 'Column15'
grouped = df.groupby('Column1')['Column15'].agg(['mean', 'sum', 'count'])

# Rename the columns for clarity
grouped = grouped.rename(columns={
    'mean': 'Average_Column15',
    'sum': 'Sum_Column15',
    'count': 'Count_Column15'
})

print(grouped)
```

> <img src="https://i.imgur.com/1234567.png" alt="Diagram showing data aggregation process" width="200">

```text
          Average_Column15  Sum_Column15  Count_Column15
Column1
C00001016          101.250000      86670             856
C00001198           896.275862      25992              29
C00001214          1151.478261      26484              23
C00001727           500.000000        500               1
C00002469            92.820724     112870            1216
...
C00629956          2000.000000      2000               1
C00630012          5000.000000      5000               1
C00630103           500.000000        500               1
C00630186           328.000000      1640               5
C90016742            29.500000        59               2
```

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 9

---

# Pivot

- Flips between row values and columns
- Two types of pivot:
  - Row-to-column pivot
  - Column-to-row pivot (aka unpivot)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
10

---

# Row-to-column pivot

- Output records are based on multiple input records
- Values of output record attributes are based on some aggregation of input record attribute values.
- Frequently combined with aggregation, such that input records can contribute to multiple output records.

A
B
A
C

Pivot

> A B C

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 11

---

# Column-to-row pivot (unpivot)

- Each input record maps to multiple output records.
- Each output record is based on exactly one input record.
- Values of separate attributes of the input are unified into a single attribute in the output.

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

---

# Pivot – Example

- Six distinct values of Column7 identify different source types of contributions.
- Contributions made from various US states.
- Aggregation + pivot to count the number of contributions per state (i.e., Column10 remains) and source type (pivots from row values to columns)

```python
#Create data grouped by source type and state
grouped = df.groupby(
['Column7','Column10'])['Column1'].agg(['count'])

#Pivot grouped to get Column7 as columns
pivot_table = grouped.pivot_table(
index='Column10',
columns='Column7',
values='count',
aggfunc='sum',
fill_value=0
)
print(pivot_table)
```


<table>
  <tbody>
    <tr>
      <td><b>Column7</b></td>
      <td><b>CAN</b></td>
      <td><b>CCM</b></td>
      <td><b>COM</b></td>
      <td><b>IND</b></td>
      <td><b>ORG</b></td>
      <td><b>PAC</b></td>
    </tr>
    <tr>
      <td><b>Column10</b></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>AA</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AE</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AK</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>402</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AL</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2242</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AR</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1683</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>AZ</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2278</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>CA</td>
      <td>7</td>
      <td>a</td>
      <td>a</td>
      <td>19391</td>
      <td>17</td>
      <td>a</td>
    </tr>
  </tbody>
</table>

> Nanyang Technological University. All rights reserved. 13

---

# Unpivot – Example

- “Reverse” the previous example.
- Each state will be associated with six values that correspond to the six attributes we will “put back” from the column header to the data records.

```python
# Unpivot the pivot table
unpivoted_df = pd.melt(
    pivot_table.reset_index(),
    id_vars='Column10',
    value_vars=['CAN', 'CCM', 'COM', 'IND', 'ORG', 'PAC'])
print(unpivoted_df.sort_values(by='Column10'))
```

<table>
    <tr><th></th>
        <th>Column10</th>
        <th>Column7</th>
        <th>value</th>
    </tr>
    <tr>
        <td>0</td>
        <td>AA</td>
        <td>CAN</td>
        <td>0</td>
    </tr>
    <tr>
        <td>57</td>
        <td>AA</td>
        <td>CCM</td>
        <td>0</td>
    </tr>
    <tr>
        <td>171</td>
        <td>AA</td>
        <td>IND</td>
        <td>1</td>
    </tr>
    <tr>
        <td>228</td>
        <td>AA</td>
        <td>ORG</td>
        <td>0</td>
    </tr>
    <tr>
        <td>285</td>
        <td>AA</td>
        <td>PAC</td>
        <td>0</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    <tr>
        <td>227</td>
        <td>ZZ</td>
        <td>IND</td>
        <td>28</td>
    </tr>
    <tr>
        <td>113</td>
        <td>ZZ</td>
        <td>CCM</td>
        <td>0</td>
    </tr>
    <tr>
        <td>56</td>
        <td>ZZ</td>
        <td>CAN</td>
        <td>0</td>
    </tr>
    <tr>
        <td>284</td>
        <td>ZZ</td>
        <td>ORG</td>
        <td>0</td>
    </tr>
    <tr>
        <td>341</td>
        <td>ZZ</td>
        <td>PAC</td>
        <td>0</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 14

---

# Summary of structuring transformations

- Structuring as a transformation action involves changing the structure and granularity of a dataset.
- Structuring transformations create new data based on data already present in the dataset.

<table>
  <thead>
    <tr>
        <th>Structuring</th>
        <th>Intrarecord</th>
        <th>Reordering attributes</th>
    </tr>
    <tr>
        <th></th>
        <th></th>
        <th>Creating attributes</th>
    </tr>
    <tr>
        <th></th>
        <th></th>
        <th>Combining attributes</th>
    </tr>
    <tr>
        <th></th>
        <th>Interrecord</th>
        <th>Filtering dataset</th>
    </tr>
    <tr>
        <th></th>
        <th></th>
        <th>Aggregation</th>
    </tr>
    <tr>
        <th></th>
        <th></th>
        <th>Pivot</th>
    </tr>
  </thead>
</table>

> Note: The diagram shows a hierarchical structure where "Structuring" is the main category, branching into "Intrarecord" and "Interrecord". "Intrarecord" further branches into "Reordering attributes", "Creating attributes", and "Combining attributes". "Interrecord" branches into "Filtering dataset", "Aggregation", and "Pivot".

---

# ENRICHING

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved.

16

---

# Overview of enriching

- Results in the net addition of information to a dataset.
  - Inserts additional records or attributes from other related datasets.
  - Use formulas to calculate new fields.
- Three primary types of enriching transformations:
  - Unions
  - Joins
  - Deriving new fields

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 17

---

# Overview of enriching

- Enriching
  - Unions
    - Set and bag union
    - Outer union
  - Joins
    - Inner join
    - Outer joins
  - Derivation of values
    - Generic
    - Proprietary
  - Metadata

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 18

---

# Unions – Set and bag union

- Given relations $R$ and $S$ with compatible schemas, union ($\cup$) creates a relation that includes all tuples from $R$ and all tuples from $S$.
- Compatible schemas have the same number of attributes and each attribute $R.A_i$ has the same data type as $S.A_i$.
- Depending on the semantics, duplicate records are removed (set-semantics) or not (bag-semantics).

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
19

---

# Unions - Outer union

- When combining data from multiple sources, they do not necessarily have compatible schemas.
  - Overlap on some attributes
  - Other attributes are only present in some sources.
- Given two relations $R(A_1 A_2, ..., A_m)$ and $S(B_1 B_2, ..., B_n)$, the outer union ($\uplus$)
  - Creates a relation with schema attributes $\{A_1 A_2, ..., A_m\} \cup \{B_1 B_2, ..., B_n\}$
  - Adds null values ($\bot$) to attributes of $R$ not present in $S$ and vice versa.
  - Unifies the resulting tuples to obtain the final result.

> Nanyang Technological University. All rights reserved. 20

---

# Outer union - example

```python
# Sample data for two tables
data1 = {'ID': [1, 2], 'Value1': ['A', 'B']}
data2 = {'ID': [2, 3], 'Value2': ['B', 'C']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# (Outer) union of the two tables
union_df = pd.concat([df1, df2]).drop_duplicates()
print(df1)
print(df2)
print(union_df)
```

> ID Value1
> 
> 0 1 A
> 
> 1 2 B
> 
> ID Value2
> 
> 0 2 B
> 
> 1 3 C
> 
> ID Value1 Value2
> 
> 0 1 A NaN
> 
> 1 2 B NaN
> 
> 0 2 NaN B
> 
> 1 3 NaN C

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 21

---

# Joins

- Linking records from one dataset $R$ to records from another dataset $S$.
- Linking based on a condition on (join) key attributes, e.g.,
  - Exact match of key values (most common)
  - Approximate match of key values (e.g., to account for data quality issues)

> $Join(A, B)$

> =

---

# Types of joins for enrichment

## Inner join
Only produce a record when there are matching records from each dataset being blended. If there are duplicate join keys, the output records are similarly duplicated.

## Left outer join
Retains all records from the left (or initial) dataset, even if there is no matching record in the right (or incoming) dataset. Missing values from the right are padded with null values.

## Right outer join
Retains all records from the right (or incoming) dataset, even if there is no matching record in the left (or initial) dataset. Missing values from the left are padded with null values.

## Full outer join
Full outer joins retain all records from both datasets, even if they have a corresponding match. Missing values from either side are padded with nulls.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
23

---

# Left outer join - example

```python
# Sample data for two tables
data1 = {'ID': [1, 2], 'Value1': ['A', 'B']}
data2 = {'ID': [1, 3], 'Value2': ['B', 'C']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Left outer join of the two tables
joined_df = pd.merge(df1, df2, on='ID', how='left')
print(df1)
print(df2)
print(joined_df)
```

> ID Value1
> 
> 0 1 A
> 
> 1 2 B
> 
> ID Value2
> 
> 0 1 B
> 
> 1 3 C
> 
> ID Value1 Value2
> 
> 0 1 A B
> 
> 1 2 B NaN

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 24

---

# Generic derivation of values

- Generic derivations apply to many datasets and rely on general rules or formulas.
- May call external services for enrichment.
- Examples:
  - Enrichment to address the time dimension
  - Enrichment to obtain geography or spatial encodings
  - Enrichment based on analyzing data (e.g., text)
  - Values derived from numeric calculations

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 25

---

# Proprietary derivation of values

- Organizations may have custom models that derive information to enrich their data.
- Examples:
  - Custom models for credit scoring
  - Custom model for health status of patients
- In data preparation systems, proprietary functionality is often encoded as user-defined functions (UDFs).

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 26

---

# Metadata

- (Retrieved) Metadata are integrated into the records as additional attributes.
- Common examples:
  - filenames of the source data
  - Byte offsets and/or record numbers
  - current date and/or time
  - creation/update/access timestamps
  - record and/or record attribute provenance

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 27

---

# Summary of enriching

## Results in the addition of information to a dataset.

<table>
  <thead>
    <tr>
        <th>Enriching</th>
        <th>Unions</th>
        <th>Set and bag union</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td></td>
        <td></td>
        <td>Outer union</td>
    </tr>
    <tr>
        <td></td>
        <td>Joins</td>
        <td>Inner join</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>Outer joins</td>
    </tr>
    <tr>
        <td></td>
        <td>Derivation of values</td>
        <td>Generic</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>Proprietary</td>
    </tr>
    <tr>
        <td></td>
        <td>Metadata</td>
        <td></td>
    </tr>
  </tbody>
</table>

> Nanyang Technological University. All rights reserved.

---

# DATA CLEANING

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 29

---

# Data cleaning overview

- Data cleaning is the process of identifying and mitigating **data errors** within a dataset.
- It is an essential step in data science that ensures that the **quality** of data is high to allow effective and reliable analysis and decision-making.
- **Data cleaning transformation actions** fall in two categories:
  - Identification of data quality issues
  - Correction or repair of the data

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 30

---

# Data cleaning overview

- Throughout this sub-chapter, we cover:
  - Data quality: What is it? What dimensions are important?
  - Data errors: What types of errors to look out for?
  - Data cleaning transformation actions: Overview of detection and correction transformation actions.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 31

---

# DATA QUALITY

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 32

---

# What is data quality?

- Fitness for use
    - Accuracy, Objectivity, Believability,
    - Reputation, Accessibility, Security,
    - Relevance, Value-Added, Timeliness,
    - Completeness, Amount of Data,
    - Interpretability, Understandability,
    - Consistency, Concise Representation
- > 150 dimensions

1
15
Too detailed

Many dimensions!
Not all of them
fixable by data
cleaning (or
transformation).

Understanding
important
dimensions still
relevant when
developing data
science systems.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 33

---

# Many classifications of quality dimensions

- SEMANTIC-ORIENTED CLASSIFICATIONS
  - PARTITION QUALITY DIMENSIONS SOLELY
  - BASED ON THEIR MEANING
- PROCESS-ORIENTED CLASSIFICATIONS
  - PARTITION QUALITY DIMENSIONS
  - ACCORDING TO THEIR DEPLOYMENT IN
  - DIFFERENT PHASES OF DATA PROCESSING
- GOAL-ORIENTED CLASSIFICATIONS
  - MATCH GOALS THAT ARE TO BE REACHED
  - WITH THE HELP OF QUALITY REASONING.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
34

---

# Requirement Survey – A comprehensive semantic-oriented classification

- **Content-related criteria**
  - Concern the actual data
  - Criteria:
    - Accuracy
    - Documentation
    - Relevancy
    - Value-added
    - Completeness
    - Interpretability

- **Technical criteria**
  - Concern software and hardware
  - Criteria:
    - Timeliness
    - Reliability
    - Latency
    - Performability
    - Response time
    - Security
    - Accessibility
    - Price
    - Customer support

- **Intellectual criteria**
  - Concern subjective aspects.
  - Criteria:
    - Believability
    - Reputation
    - Objectivity

- **Instantiation-related criteria**
  - Concern the presentation of retrieved data.
  - Criteria:
    - Verifiability
    - Amount of data
    - Understandability
    - Concise representation
    - Consistent representation

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
35

---

# Requirement Survey – Content-based criteria

- Accuracy is the extent to which data is correct, reliable, and certified free of error. [WS96]
- Completeness is the extent to which data is not missing and is of sufficient breadth, depth, and scope for the task at hand. [WS96]
- Customer support is the amount and usefulness of human help via email or telephone.
- Documentation is the amount and usefulness of documents with metadata.
- Interpretability is the extent to which data is in appropriate languages, symbols, and units, and the definitions are clear. [WS96]
- Relevancy (or relevance) is the extent to which data is applicable and helpful for the task at hand. [WS96]
- Reliability is the degree to which the user can trust the information
- Value-Added is the extent to which data is beneficial and provides advantages from its use. [WS96]

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 36

---

# Requirement Survey – Technical criteria

- Accessibility (or availability) of a DBMS
  - is the probability that a feasible query is correctly answered must time range.
  - Is the extent to which data are available or easily and quickly receivable [WS96].
- Latency is the amount of time from issuing the query until the first data item reaches the user
- Price (cost effectiveness)
  - is the amount of money a user must pay for a query.
  - is the extent to which the cost of collecting appropriate data is reasonable [WS96].
- Response time measures the delay in seconds between submission of a query by the user and reception of the complete response from the information system.
- Security is the extent to which access to data is restricted appropriately to maintain its security [WS96].
- Timeliness is the extent to which the age of the data is appropriate for the task at hand [WS96].

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 37

---

# Requirement Survey – Intellectual criteria

- Believability is the extent to which data is regarded as true, real, and credible [WS96].
- Objectivity is the extent to which data is unbiased, unprejudiced, and impartial [WS96].
- Reputation is the extent to which data is trusted or highly regarded in terms of its source or content [WS96].

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 38

---

# Requirement Survey – Instantiation-related criteria

- Amount of data is the extent to which the quantity or volume of available data is appropriate [WS96].
- Representational conciseness is the extent to which data is compactly represented without being overwhelming [WS96].
- Representational consistency is the extent to which data is always represented in the same format and are compatible with previous data [WS96].
- Understandability (ease of understanding) is the extent to which data are clear without ambiguity and easily comprehended [WS96].
- Verifiability (traceability, lineage) Is the extent to which data are well documented, verifiable, and easily attributed to a source [WS96].

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 39

---

# Requirement Survey – Summary

## Content-related criteria
- Concern the actual data
- Criteria:
  - Accuracy
  - Documentation
  - Relevancy
  - Value-added
  - Completeness
  - Interpretability

> Multiple content-related criteria can be improved through proper data preparation, in particular data cleaning.

## Technical criteria
- Concern software and hardware
- Criteria:
  - Timeliness
  - Reliability
  - Latency
  - Performability
  - Response time
  - Security
  - Accessibility
  - Price
  - Customer support

> Technical criteria Influence data management and data science deployment considerations

## Intellectual criteria
- Concern subjective aspects.
- Criteria:
  - Believability
  - Reputation
  - Objectivity

> Intellectual criteria are essential during data selection.

## Instantiation-related criteria
- Concern the presentation of retrieved data.
- Criteria:
  - Verifiability
  - Amount of data
  - Understandability
  - Concise representation
  - Consistent representation

> Multiple problems related to instantiation-related criteria can be mitigated through data preparation.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 40

---

# DATA ERRORS

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 41

---

# Examples of data errors that affect data quality

- representation
- uniqueness
- contradiction
- referential integrity
- dummy value
- incorrect values
- duplicates
- typo

<table>
    <tr>
        <th>CNr</th>
        <th>Name</th>
        <th>Birthday</th>
        <th>Age</th>
        <th>Sex</th>
        <th>Phone</th>
        <th>ZIP</th>
    </tr>
    <tr>
        <td>1234</td>
        <td>Smith, John</td>
        <td>18.2.80</td>
        <td>21</td>
        <td>m</td>
        <td>999-9999</td>
        <td>70567</td>
    </tr>
    <tr>
        <td>1234</td>
        <td>Jane Doe</td>
        <td>32.2.70</td>
        <td>46</td>
        <td>f</td>
        <td>768-4511</td>
        <td>55555</td>
    </tr>
    <tr>
        <td>1235</td>
        <td>John Smith</td>
        <td>18.2.80</td>
        <td>36</td>
        <td>m</td>
        <td>567-3211</td>
        <td>70567</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>ZIP</td>
        <td>Place</td>
    <td></td><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>70567</td>
        <td>Stuttgart</td>
    <td></td><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>70567</td>
        <td>Stutgart</td>
    <td></td><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>70569</td>
        <td>Germany</td>
    <td></td><td></td><td></td><td></td><td></td></tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
42

---

# Classification of errors [DR00]

<table>
    <tr>
        <th></th>
        <th>Single data source</th>
        <th>Integrated (clean) data sources</th>
    </tr>
    <tr>
        <td>**Schema level**</td>
        <td>Lack of integrity constraints, poor schema design</td>
        <td>Heterogeneous data models and schema designs</td>
    </tr>
    <tr>
        <td></td>
        <td>- Invalid value</td>
        <td>- Labeling conflicts</td>
    </tr>
    <tr>
        <td></td>
        <td>- Violation of attribute dependency</td>
        <td>- Modeling conflicts</td>
    </tr>
    <tr>
        <td></td>
        <td>- Uniqueness violation</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>- Violation of referential integrity</td>
        <td></td>
    </tr>
    <tr>
        <td>**Instance level**</td>
        <td>Data entry errors</td>
        <td>Overlapping, contradicting and inconsistent data</td>
    </tr>
    <tr>
        <td></td>
        <td>- Missing value</td>
        <td>- Contradictory values*</td>
    </tr>
    <tr>
        <td></td>
        <td>- Typographical error or wrong value</td>
        <td>- Different representations</td>
    </tr>
    <tr>
        <td></td>
        <td>- Cryptic value</td>
        <td>- Different scales</td>
    </tr>
    <tr>
        <td></td>
        <td>- Embedded value</td>
        <td>- Different precision</td>
    </tr>
    <tr>
        <td></td>
        <td>- Misfielded value</td>
        <td>- Different level of aggregation</td>
    </tr>
    <tr>
        <td></td>
        <td>- Contradictory values</td>
        <td>- Duplicates*</td>
    </tr>
    <tr>
        <td></td>
        <td>- Transposition</td>
        <td>- Data conflicts*</td>
    </tr>
    <tr>
        <td></td>
        <td>- Duplicates</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>- Data conflicts</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>- Wrong references</td>
        <td></td>
    </tr>
</table>* Same error types as in a single data source, but the process of data integration can result in additional instances of these error types (even if individual sources are clean)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 43

---

# Single data source – Schema level

<table>
    <tr><th></th>
        <th>Problem</th>
        <th>Dirty Data</th>
        <th>Reasons/Remarks</th>
    </tr>
    <tr>
        <td>Attribute level</td>
        <td>Illegal values</td>
        <td>bdate=30.13.70</td>
        <td>values outside of domain range</td>
    </tr>
    <tr>
        <td>Intra-record level</td>
        <td>Violated attribute dependencies</td>
        <td>age=22, bdate=12.02.70</td>
        <td>age = (current date – birth date) should hold</td>
    </tr>
    <tr>
        <td>Inter-record level</td>
        <td>Uniqueness violation</td>
        <td>emp1=(name="John Smith", FIN="123456") emp2=(name="Peter Miller", FIN="123456")</td>
        <td>uniqueness of FIN (Foreigner Identification number) is violated</td>
    </tr>
    <tr>
        <td>Inter-table level</td>
        <td>Referential integrity violation</td>
        <td>emp=(name="John Smith", deptno=127)</td>
        <td>referenced department (127) is not defined in department table</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 44

---

# Single data source – Instance level

<table>
    <tr>
        <th></th>
        <th>Problem</th>
        <th>Dirty Data</th>
        <th>Reasons/Remarks</th>
    </tr>
    <tr>
        <td></td>
        <td>Missing values</td>
        <td>phone=9999-999999</td>
        <td>unavailable values during data entry(dummy values or null)</td>
    </tr>
    <tr>
        <td></td>
        <td>Misspellings</td>
        <td>city="Bellin"</td>
        <td>usually typos, phonetic errors</td>
    </tr>
    <tr>
        <td></td>
        <td>Cryptic values, abbreviations</td>
        <td>experience="B"; occupation="DB Prog."</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>Embedded values</td>
        <td>name="J. Smith 12.02.70 New York"</td>
        <td>multiple values entered in one attribute (e.g. in a free-form field)</td>
    </tr>
    <tr>
        <td></td>
        <td>Misfielded values</td>
        <td>city="Germany"</td>
        <td></td>
    </tr>
    <tr>
        <td>Intra-record level</td>
        <td>Violated attribute dependencies</td>
        <td>city="Redmond", zip=77777</td>
        <td>city and zip code should correspond</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
45

---

# Single data source – Instance level
(continued)

<table>
    <tr>
        <th>Problem</th>
        <th>Dirty Data</th>
        <th>Reasons/Remarks</th>
    </tr>
    <tr>
        <td>**Inter-record level**</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Word transpositions</td>
        <td>name1= "J. Smith", name2="Miller P."</td>
        <td>usually in a free-form field</td>
    </tr>
    <tr>
        <td>Duplicated records</td>
        <td>emp1=(name="John Smith",...); emp2=(name="J. Smith",...)</td>
        <td>same employee represented twice due to some data entry errors</td>
    </tr>
    <tr>
        <td>Contradicting records</td>
        <td>emp1=(name="John Smith",bdate=12.02.70); emp2=(name="John Smith", bdate=12.12.70)</td>
        <td>the same real-world entity is described by different values</td>
    </tr>
    <tr>
        <td>**Inter-table level**</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Wrong references</td>
        <td>emp=(name="John Smith", deptno=17)</td>
        <td>referenced department (17) is defined but wrong</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 46

---

# Integrated data sources – Schema level

## Table-table conflicts

- Labeling conflicts
  - Semantically equivalent tables have different names (synonyms)
  - Semantically different tables have equal names (homonym)
- Modeling conflicts
  - Missing attributes
  - Missing but derivable attributes
  - IC conflicts (IC = integrity constraint)

> IC conflict (uniqueness)

<table>
    <tr>
        <th>EID</th>
        <th>Firstname</th>
        <th>lastname</th>
        <th>role</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Peter</td>
        <td>Müller</td>
        <td>Assistant</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Petra</td>
        <td>Schmidt</td>
        <td>Asst.</td>
    </tr>
</table>> Employee

<table>
    <tr>
        <th>EID</th>
        <th>firstname</th>
        <th>lastname</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Stefanie</td>
        <td>Meier</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Petra</td>
        <td>Schmidt</td>
    </tr>
</table>> Homonym

> Employee (Semantic: managing)

> Missing but derivable attribute

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 47

---

# Integrated data sources – Schema level
(continued)

## Attribute-attribute conflicts

- Labeling conflicts
  - Different names for semantically equal attributes (synonyms)
  - Same label for attributes with different semantics (homonyms)
- Modeling conflicts
  - Default value conflicts
  - IC conflicts
    - Data type conflicts
    - Condition conflicts

> IC conflict (age > 18)

```sql
Employee
```

<table>
    <tr>
        <th>p_id</th>
        <th>firstn VARCHAR(35)</th>
        <th>lastname</th>
        <th>age</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Wolfgang</td>
        <td>Meyer</td>
        <td>33</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Klaus</td>
        <td>Schmidt</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
</table>```sql
Employee
```

<table>
    <tr>
        <th>p_id</th>
        <th>firstn VARCHAR(20)</th>
        <th>name</th>
        <th>age</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Peter</td>
        <td>Müller</td>
        <td>0</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Petra</td>
        <td>Weger</td>
        <td>17</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
</table>> Default value

> Data type

> Synonym

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 48

---

# Integrated data sources – Instance level

Errors that arise due to the integration of overlapping, contradicting and inconsistent data across sources.

- Contradictory values
- Different representations
- Different scales
- Different precision
- Duplicates
- Data conflicts
- Different level of aggregation

<table>
    <tr>
        <th>CID</th>
        <th>Name</th>
        <th>Size</th>
        <th>Billing</th>
        <th>Phone</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Smith, John</td>
        <td>8.5</td>
        <td>80 USD</td>
        <td>(123) 4567</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Doe, Jane</td>
        <td>7.0</td>
        <td>70 USD</td>
        <td>(408) 9012</td>
    </tr>
    <tr>
        <td>A</td>
        <td>John Smith</td>
        <td>42</td>
        <td>580 SGD</td>
        <td>4444 8888</td>
    </tr>
    <tr>
        <td>B</td>
        <td>Chris Lim</td>
        <td>42</td>
        <td>420 SGD</td>
        <td>9182 7374</td>
    </tr>
</table>Data from source 1
Data from source 2

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 49

---

# Data errors summary

- Various types of errors need to be considered.
  - This entails a high variety of solutions to detect and correct these errors.
- Errors are either defined at schema or data level.
  - Knowledge of this distinction helps in choosing suited methods for error detection and correction.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 50

---

# CLEANING TRANSFORMATION
ACTIONS

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
51

---

# Cleaning actions overview

- ERROR DETECTION
  - IDENTIFIES ERRONEOUS RECORDS
  - OR ATTRIBUTE VALUES.
- ERROR CORRECTION
  - CHANGES VALUES TO CORRECT
  - ERRORS.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 52

---

# Error detection

- Can be performed by leveraging metadata gathered during data profiling.
  *Examples: approximate functional dependencies, cardinalities*
- Further data mining or data analysis methods can be used.
  *Examples: outlier detection, entity resolution to identify different representations of a same entity*
- Can produce additional metadata pinpointing detected quality issues, subsequently used to fix them manually, semi-automatically, or fully automatically.
  *Example: additional duplicate entityID as a result of entity resolution, Boolean flag indicating an error in a specific field.*

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 53

---

# Error correction

- Distinction between cleaning actions
  addressing missing values and erroneous
  values.
- A simple cleaning action to correct both types
  of errors is to delete (filter) affected records.
- Error correction beyond deletion discussed
  based on the classification on the next slide.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
54

---

# Error correction beyond deletion

> **Error correction**
>
> - **Missing values**
>   - Densification
>   - Imputation
> - **Erroneous values**
>   - Possible worlds
>   - Standardization
>   - Value derivation

---

# Correcting missing values

- Data densification: merge records that complement each other to reduce / eliminate missing or NULL values.
- Data imputation: fills in the missing values through
  - Computation, approximation, or extrapolation
  - Inference based on similar or related records
  - Generation using generative models

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 56

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>NULL</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>NULL</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>14</td>
        <td>Home</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 57

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>NULL</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>NULL</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>14</td>
        <td>Home</td>
    </tr>
</table>> Records complement each other and can be densified into one single tuple with no missing values

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 58

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>NULL</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>14</td>
        <td>Home</td>
    </tr>
</table>> Price is approximated based on the price of similar products (e.g., using the average)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 59

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>14</td>
        <td>NULL</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>14</td>
        <td>Home</td>
    </tr>
</table>> Category can be inferred by the category of similar products.

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>14</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>NULL</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>14</td>
        <td>Home</td>
    </tr>
</table>> Strong order of records allows to extrapolate possible date

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
61

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>14</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>04/01/2024</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>NULL</td>
        <td>19</td>
        <td>Home</td>
    </tr>
</table>> Generative model can generate a likely value

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 62

---

# Correcting missing values

<table>
    <tr>
        <th>Date</th>
        <th>Product</th>
        <th>Price</th>
        <th>Category</th>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Rubik's cube</td>
        <td>10</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>01/01/2024</td>
        <td>Bath towel</td>
        <td>13</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>02/01/2024</td>
        <td>Beach towel</td>
        <td>14</td>
        <td>**HOME**</td>
    </tr>
    <tr>
        <td>03/01/2024</td>
        <td>Large towel</td>
        <td>15</td>
        <td>Home</td>
    </tr>
    <tr>
        <td>04/01/2024</td>
        <td>Jigsaw</td>
        <td>20</td>
        <td>Puzzle</td>
    </tr>
    <tr>
        <td>05/01/2024</td>
        <td>**XL towel**</td>
        <td>19</td>
        <td>Home</td>
    </tr>
</table>> No more missing values

<sub>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE</sub>
<sub>Nanyang Technological University. All rights reserved.</sub>
<sub>63</sub>

---

# Correcting erroneous values

- Possible worlds: Conduct downstream processing (e.g., analysis) both with invalid value and without to assess its impact on possible insights.
- Standardization: Uses dictionaries, external services, rules to correct errors.
- Value derivation: Obtain correct / consistent value for an attribute that overwrites the original (invalid) value through conversion, calculation, statistical modelling, etc.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
64

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestril planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>1.9</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>8700</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Zerez</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Glace</td>
    </tr>
</table>> Standardization based on fixed library of valid names of solar system object. Replaced by most similar one.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 65

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestril planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>1.9</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>8700</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Ceres</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Glace</td>
    </tr>
</table>> Standardization using domain knowledge mapping planet names to their mass.

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestril planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>**189870.00**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>**8700**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Ceres</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Glace</td>
    </tr>
</table>> Derivation of correctly formatted value (all others have two decimals).

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestril planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>189870.00</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>8700.00</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Ceres</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Glace</td>
    </tr>
</table>> Correction of typographical error by replacing this outlier value by more frequent type (assume a larger table with few errors)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 68

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>**189870.00**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>**8700.00**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Ceres</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Glace</td>
    </tr>
</table>Discovered functional dependency  
Type → Surface  
and value distribution  
allow to determine Ice  
as the correct value  
(assume a more complete relation)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 69

---

# Correcting erroneous values

<table>
    <tr>
        <th>Object</th>
        <th>Mass</th>
        <th>Type</th>
        <th>Surface</th>
    </tr>
    <tr>
        <td>Earth</td>
        <td>597.20</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Venus</td>
        <td>486.70</td>
        <td>Terrestrial planet</td>
        <td>Solid</td>
    </tr>
    <tr>
        <td>Jupiter</td>
        <td>**189870.00**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Uranus</td>
        <td>**8700.00**</td>
        <td>Jovian planet</td>
        <td>Gas</td>
    </tr>
    <tr>
        <td>Ceres</td>
        <td>0.09</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
    <tr>
        <td>Pluto</td>
        <td>1.30</td>
        <td>Dwarf planet</td>
        <td>Ice</td>
    </tr>
</table>> No more erroneous values

<ins>70</ins>

---

# DATA TRANSFORMATION
# CONCLUSION

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
71

---

# Data transformation tasks

> Data Profiling

> Data Structuring

> Data preparation

> Data Enriching

> Data Cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
72

---

# Structuring transformations

> Structuring
> - Intrarecord
>   - Reordering attributes
>   - Creating attributes
>   - Combining attributes
> - Interrecord
>   - Filtering dataset
>   - Aggregation
>   - Pivot

<table>
  <thead>
    <tr>
        <th>Category</th>
        <th>Subcategory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>Intrarecord</td>
        <td>Reordering attributes</td>
    </tr>
    <tr>
        <td>Intrarecord</td>
        <td>Creating attributes</td>
    </tr>
    <tr>
        <td>Intrarecord</td>
        <td>Combining attributes</td>
    </tr>
    <tr>
        <td>Interrecord</td>
        <td>Filtering dataset</td>
    </tr>
    <tr>
        <td>Interrecord</td>
        <td>Aggregation</td>
    </tr>
    <tr>
        <td>Interrecord</td>
        <td>Pivot</td>
    </tr>
  </tbody>
</table>

---

# Enriching transformations

- Enriching
  - Unions
    - Set and bag union
    - Outer union
  - Joins
    - Inner join
    - Outer joins
  - Derivation of values
    - Generic
    - Proprietary
  - Metadata

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
74

---

# Error detection and correction



<table>
  <caption>Error detection and correction transformations</caption>
  <thead>
    <tr>
      <th colspan="3">Error detection</th>
      <th colspan="5">Error correction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Metadata</td>
      <td rowspan="2">Data mining</td>
      <td rowspan="2">Data analysis</td>
      <th colspan="2">Missing values</th>
      <th colspan="3">Erroneous values</th>
    </tr>
    <tr>
      <td>Densification</td>
      <td>Imputation</td>
      <td>Possible worlds</td>
      <td>Standardization</td>
      <td>Value derivation</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
75

---

# Data preparation is a process

Data preparation is the process of converting raw data into a form that allows to extract value from data.



<table>
  <caption>Data preparation is a process</caption>
  <thead>
    <tr>
      <th>Process Stage</th>
      <th>Next Sequential Step</th>
      <th>Feedback Loops (Return to)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Access</td>
      <td>Profile / transform</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Profile / transform</td>
      <td>Publish</td>
      <td>Access</td>
    </tr>
    <tr>
      <td>Publish</td>
      <td>—</td>
      <td>Access, Profile / transform</td>
    </tr>
  </tbody>
</table>





<table>
  <caption>Data Preparation Workflow Process</caption>
  <thead>
    <tr>
      <th>Step</th>
      <th>Tool Type</th>
      <th>Operation / Label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Input Data</td>
      <td>profiling_structuring_tutorial6.csv</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Filter</td>
      <td>[Column4] = "P2016"</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Formula</td>
      <td>Month = substring([Column14],0,2)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Formula</td>
      <td>Day = substring([Column14],2,2)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Formula</td>
      <td>Year = substring([Column14],4,4)</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Select / Data Cleansing</td>
      <td>(No label provided)</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Filter</td>
      <td>[Year] = "2016"</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Formula</td>
      <td>Contributions = ToNumber([Column15])</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Summarize</td>
      <td>(Sigma icon)</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE Nanyang Technological University. All rights reserved. 76

---

# For each of these types of data transformations, you should now be able to...

- ... define and classify various sub-tasks.
- ... determine which data transformations can be used to prepare the data for a specific data science application.
- ... describe and recognize various data quality issues within and across datasets.
- ... implement various data transformation tasks.

> Nanyang Technological University. All rights reserved. 77

---

# References and credits

- Joseph M. Hellerstein, Tye Rattenbury, Jeffrey Heer, Sean Kandel, Connor Carreras. Principles of Data Wrangling. O’Reilly Media. 2017 – Chapter 4 - 7
- Erhard Rahm, Hong Hai Do: Data Cleaning: Problems and Current Approaches. IEEE Data Eng. Bull. 23(4): 3-13 (2000)
- Felix Naumann, Claudia Rolker: Do Metadata Models meet IQ Requirements? IQ 1999: 99-114

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
78