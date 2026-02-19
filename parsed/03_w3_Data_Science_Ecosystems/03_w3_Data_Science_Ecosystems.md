# Data Science Fundamentals
## [SC3021]

### Chapter 3: Data Science Ecosystems

Assoc. Prof. Melanie Herschel | CCDS

---

# Course content

- Data science overview
  - What is Data Science?
  - Data Science Thinking vs. Computational Thinking
  - Data Science Ecosystem
    - •Ecosystem overview
    - •Component details
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
      <td>What is Data Science?</td>
      <td>Data profiling</td>
      <td>Descriptive analytics</td>
      <td>Privacy</td>
    </tr>
    <tr>
      <td>Data Science Thinking vs. Computational Thinking</td>
      <td>Structuring</td>
      <td>Diagnostic Analytics</td>
      <td>Security</td>
    </tr>
    <tr>
      <td>Data Science Ecosystem</td>
      <td>Enriching</td>
      <td>Prescriptive analytics</td>
      <td>Ethics</td>
    </tr>
    <tr>
      <td>• Ecosystem overview</td>
      <td>Data cleaning</td>
      <td>Predictive analytics</td>
      <td>Psychology</td>
    </tr>
    <tr>
      <td>• Component details</td>
      <td>Data management platforms</td>
      <td>Data visualization</td>
      <td>Policies</td>
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
      <td>What is Data Science?</td>
      <td>Data profiling</td>
      <td>Descriptive analytics</td>
      <td>Privacy</td>
    </tr>
    <tr>
      <td>Data Science Thinking vs. Computational Thinking</td>
      <td>Structuring</td>
      <td>Diagnostic Analytics</td>
      <td>Security</td>
    </tr>
    <tr>
      <td>Data Science Ecosystem:
        <ul>
          <li>Ecosystem overview</li>
          <li>Component details</li>
        </ul>
      </td>
      <td>Enriching</td>
      <td>Prescriptive analytics</td>
      <td>Ethics</td>
    </tr>
    <tr>
      <td></td>
      <td>Data cleaning</td>
      <td>Predictive analytics</td>
      <td>Psychology</td>
    </tr>
    <tr>
      <td></td>
      <td>Data management platforms</td>
      <td>Data visualization</td>
      <td>Policies</td>
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

# At the end of this lecture, you should be able to...

- ... describe the main components of the data science ecosystem.
- ... explain how different factors influence the development of a data science system.
- ... define the functionality of data science building blocks at a high level to solve data science applications.
- ... reflect on possible data protection, data ethics, social and policy aspects that may affect the data science application deployment.

> Nanyang Technological University. All rights reserved.

---

# ECOSYSTEM OVERVIEW

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 4

---

# Applications, systems, and deployments

- **Data Science application**
  - Problem instance that applies Data Science Thinking to solve a problem based on data

- **Data Science system**
  - Software system that supports the process underlying Data Science Thinking

- **Data Science application deployment**
  - Use of a data science system for a data science problem in a production environment

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 5

---

# Applications, systems, and deployments

## Data Science application
## Data Science system
## Data Science application deployment

> Data protection and data ethics

> Data visualization and explanation

> Data preparation and data management

> Data modeling and analytics

> Social and policy aspects

<table>
  <thead>
    <tr>
        <th></th>
        <th>Ask</th>
        <th>Prepare</th>
        <th>Process</th>
        <th>Analyze</th>
        <th>Share</th>
        <th>Act</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td></td>
        <td>Ask</td>
        <td>Prepare</td>
        <td>Process</td>
        <td>Analyze</td>
        <td>Share</td>
        <td>Act</td>
    </tr>
  </tbody>
</table>

Nanyang Technological University. All rights reserved. 6

---

# Holistic consideration

- Applications, systems, and deployments are interlinked and influence one another.

- Examples:
  - Data science systems provide tools and technologies that help data scientists address their problems.
  - Data science systems need to be carefully designed to fit the target applications.
  - Data science systems need to support deployments within their social and policy context.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 7

---

# Data Science ecosystem

- A framework designed to guide the development of data science systems.
- The ecosystem is composed of building blocks that are application-informed and context-informed.
- Application-informed: Data Science applications guide the appropriate technologies, tools, algorithms, and methodologies to be incorporated in data science systems and leverage them to address the application needs.
- Context-informed: Social and policy context significantly impact data-science application deployments. Core technologies developed and used in data science systems need to take these into account and reflect them in application deployments.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 8

---

# Illustration of application-informed

- Application problem: Classify if a product sold online will be returned or not.
- Some considerations for system development (there are more):
  - The application defines a classification problem.
  - The product description on the Web is semi-structured, so restructuring and cleaning of the data is necessary to obtain dense feature vectors.
  - The system needs to implement standardization and alignment to ensure that feature representations of online products are compatible with features of the available product transaction data.
  - The choice of model should ensure highly accurate classification results.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 9

---

# Illustration of context-informed

- Application problem: Classify if a person applying for a loan will repay the loan or not.
- Some considerations for system development (there are more):
  - The application defines a classification problem.
  - Customer profiles vary and are semi-structured data, so restructuring and cleaning of the data is necessary to obtain dense feature vectors.
  - The system needs to implement standardization and alignment to ensure that feature representations of applicants are compatible with features of the available bank transaction data.
  - The choice of model should ensure highly accurate classification results.
  - Choose a right model to obtain accurate and fair classification results.
  - Handling of personal data requires the integration of privacy mechanisms into the data science system.
  - Financial data needs to be protected through appropriate security mechanisms.

> Changed social and policy context!

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 10

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th colspan="5">Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data engineering</td>
      <td>Data analytics</td>
      <td>Data understanding</td>
      <td>Data protection</td>
      <td>Data ethics</td>
    </tr>
    <tr>
      <th colspan="5">Data science building blocks</th>
    </tr>
    <tr>
      <th colspan="5">Social and policy context</th>
    </tr>
  </tbody>
</table>



> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 11

---

# Data Science ecosystem

Applications

- **Data engineering**
  - Data preparation
  - Data management
- **Data analytics**
  - Data exploration (data mining)
  - Models and algorithms (machine learning)
- **Data understanding**
  - Explanation
  - Visualization
- **Data protection**
  - Security
  - Privacy
- **Data ethics**
  - Impact on individuals, organizations, and society
  - Bias in data
  - Algorithmic bias
  - Regulatory issues

Data science building blocks

Social and policy context

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
12

---

# Ecosystem structures the remainder of this lecture

- **Data science overview**
  - What is Data Science?
  - Data Science Thinking vs. Computational Thinking
  - Data Science Ecosystems

- **Data preparation and data management**
  - Data profiling
  - Structuring
  - Enriching
  - Data cleaning
  - Data management platforms
  - Schema design
  - Querying data

- **Data analytics and understanding**
  - Descriptive analytics
  - Diagnostic Analytics
  - Prescriptive analytics
  - Predictive analytics
  - Data visualization

- **Design considerations**
  - Privacy
  - Security
  - Ethics
  - Psychology
  - Policies



<table>
  <caption>Data analytics and understanding - Relative Icon Bar Heights</caption>
  <thead>
    <tr>
      <th>Analytics Category</th>
      <th>Relative Bar Height (Estimated %)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Descriptive analytics</td>
      <td>60%</td>
    </tr>
    <tr>
      <td>Diagnostic Analytics</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Prescriptive analytics</td>
      <td>60%</td>
    </tr>
    <tr>
      <td>Predictive analytics</td>
      <td>30%</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 13

---

# COMPONENT DETAILS

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 14

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th colspan="5">Social and policy context</th>
    </tr>
    <tr>
      <th colspan="5">Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data engineering</td>
      <td>Data analytics</td>
      <td>Data understanding</td>
      <td>Data protection</td>
      <td>Data ethics</td>
    </tr>
    <tr>
      <th colspan="5">Data science building blocks</th>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
15

---

# Data Engineering

## Data Engineering

The practice of designing, building, and maintaining systems that collect, manage, and convert raw data into usable information for downstream applications.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- **Data preparation**
  - Operations typically involved in a data engineering process that transform the data.
- **Data management**
  - Solutions devised to organize, protect, store, access, and manipulate data.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 16

---

# Data preparation

Operations transforming data in multiple stages:
- Data profiling
- Data structuring
- Data enriching
- Data cleaning

Data engineering
Data analytics
Data understanding
Data protection
Data ethics

## Running example:
- Goal: analyze the relationship between product ratings and customer demographics (age, gender, place of residence).
- Requires: data on both product reviews by customers and customer demographics.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 17

---

# Data preparation - Example

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Sample data from user_reviews

<table>
    <tr>
        <th>Product</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Text</th>
        <th>Date</th>
        <th>City</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>...</td>
        <td>19/12/2011</td>
        <td>LA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>⊥</td>
        <td>3</td>
        <td>...</td>
        <td>04/24/2012</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>⊥</td>
        <td>21/01/2018</td>
        <td>Austin</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>...</td>
        <td>29/09/2020</td>
        <td>CA</td>
    </tr>
</table>## Sample data for customer_demographics

<table>
    <tr>
        <th>Username</th>
        <th>Name</th>
        <th>Age</th>
        <th>isMale</th>
        <th>isFemale</th>
        <th>City</th>
    </tr>
    <tr>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>⊥</td>
        <td>1</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>John Doe</td>
        <td>24</td>
        <td>1</td>
        <td>0</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>1</td>
        <td>0</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>maxMiller</td>
        <td>Max Miller</td>
        <td>37</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>Miami</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 18

---

# Data preparation - Profiling

- Examine and analyze data to create metadata (data about data).
- Metadata represent a summary of various characteristics of the data.
- These summaries help to assess usefulness and quality of data.

Statistics commonly used in summaries:
- Number of rows
- Min and max values
- Number of missing values
- Outliers
- Data type
- Data format violations
- Histograms
- ...

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
19

---

# Data preparation - Profiling

> Data engineering Data analytics Data understanding Data protection Data ethics

## Metadata for user_reviews

<table>
    <tr>
        <th>Column</th>
        <th>Type</th>
        <th>Missing values</th>
        <th>Unique values</th>
    </tr>
    <tr>
        <td>Product</td>
        <td>String</td>
        <td>55</td>
        <td>10987</td>
    </tr>
    <tr>
        <td>Reviewer</td>
        <td>String</td>
        <td>126</td>
        <td>8426</td>
    </tr>
    <tr>
        <td>Rating</td>
        <td>Int</td>
        <td>0</td>
        <td>5</td>
    </tr>
    <tr>
        <td>Text</td>
        <td>String</td>
        <td>6024</td>
        <td>4963</td>
    </tr>
    <tr>
        <td>Date</td>
        <td>Date</td>
        <td>0</td>
        <td>365</td>
    </tr>
    <tr>
        <td>City</td>
        <td>String</td>
        <td>3024</td>
        <td>430</td>
    </tr>
</table>## Metadata for customer_demographics

<table>
    <tr>
        <th>Column</th>
        <th>Type</th>
        <th>Missing values</th>
        <th>Unique values</th>
    </tr>
    <tr>
        <td>username</td>
        <td>String</td>
        <td>0</td>
        <td>5000</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>String</td>
        <td>0</td>
        <td>4230</td>
    </tr>
    <tr>
        <td>Age</td>
        <td>Int</td>
        <td>10</td>
        <td>89</td>
    </tr>
    <tr>
        <td>isMale</td>
        <td>Bool</td>
        <td>2040</td>
        <td>2</td>
    </tr>
    <tr>
        <td>isFemale</td>
        <td>Bool</td>
        <td>3022</td>
        <td>2</td>
    </tr>
    <tr>
        <td>City</td>
        <td>String</td>
        <td>75</td>
        <td>500</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 20

---

# Data preparation - Structuring

- Organize and transform the data into a well-defined format.
- The format should be suitable for the intended analysis.
- Properly structured data enables efficient and effective data processing.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

Typical structuring tasks:
- Organization of data into tables.
- Table normalization to avoid data redundancy and improve data integrity.
- Splitting values
- Pivoting data
- Group numerical data into ranges
- ...

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 21

---

# Data preparation - Structuring

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Sample data from user_reviews

<table>
    <tr>
        <th>Product</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Text</th>
        <th>Date</th>
        <th>City</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>...</td>
        <td>19/12/2011</td>
        <td>LA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>⊥</td>
        <td>3</td>
        <td>...</td>
        <td>04/24/2012</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>⊥</td>
        <td>21/01/2018</td>
        <td>Austin</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>...</td>
        <td>29/09/2020</td>
        <td>CA</td>
    </tr>
</table>## Restructured data

<table>
    <tr>
        <th>Product</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Day</th>
        <th>Month</th>
        <th>Year</th>
        <th>City</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>LA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>⊥</td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>CA</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 22

---

# Data preparation - Structuring

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Sample data for customer_demographics

<table>
    <tr>
        <th>Username</th>
        <th>Name</th>
        <th>Age</th>
        <th>isMale</th>
        <th>isFemale</th>
        <th>City</th>
    </tr>
    <tr>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>⊥</td>
        <td>1</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>John Doe</td>
        <td>24</td>
        <td>1</td>
        <td>0</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>1</td>
        <td>0</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>maxMiller</td>
        <td>Max Miller</td>
        <td>37</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>Miami</td>
    </tr>
</table>## Restructured data

<table>
    <tr>
        <th>Username</th>
        <th>Name</th>
        <th>Age</th>
        <th>AgeRange</th>
        <th>Gender</th>
        <th>City</th>
    </tr>
    <tr>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>John Doe</td>
        <td>24</td>
        <td>18-30</td>
        <td>M</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>60 - 75</td>
        <td>M</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>maxMiller</td>
        <td>Max Miller</td>
        <td>37</td>
        <td>30-45</td>
        <td>⊥</td>
        <td>Miami</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 23

---

# Data preparation - Enriching

- Enhance existing data by adding new and supplemental information.
- The supplemental information should be relevant to the data science application.
- Enrichment supports improving the accuracy, reliability, and completeness of the data for the task at hand.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Common enrichment steps:
- Add new attributes (columns)
- Join with external data sources
- Create derived attributes
- Data integration
- ...

---

# Data preparation - Enriching

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## user_reviews (restructured)

<table>
    <tr>
        <th>Product</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Day</th>
        <th>Month</th>
        <th>Year</th>
        <th>City</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>LA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>⊥</td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>CA</td>
    </tr>
</table>## user_reviews (enriched)

<table>
    <tr>
        <th>Product</th>
        <th>Category</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Day</th>
        <th>Month</th>
        <th>Year</th>
        <th>City</th>
        <th>State</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>Electronics</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>LA</td>
        <td>CA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td>⊥</td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
        <td>NY</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>Electronics</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
        <td>TX</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>CA</td>
        <td>⊥</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 25

---

# Data preparation - Enriching

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

<table>
    <tr>
        <th>Product</th>
        <th>Category</th>
        <th>Reviewer</th>
        <th>Rating</th>
        <th>Day</th>
        <th>Month</th>
        <th>Year</th>
        <th>City</th>
        <th>State</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>Electronics</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>LA</td>
        <td>CA</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td>⊥</td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
        <td>NY</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>Electronics</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
        <td>TX</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>CA</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr>
        <td>Username</td>
        <td>Name</td>
        <td>Age</td>
        <td>AgeRange</td>
        <td>Gender</td>
        <td>City</td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
        <td>Los Angeles</td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>JD</td>
        <td>John Doe</td>
        <td>24</td>
        <td>18-30</td>
        <td>M</td>
        <td>New York</td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>60 - 75</td>
        <td>M</td>
        <td>⊥</td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>maxMiller</td>
        <td>Max Miller</td>
        <td>37</td>
        <td>30-45</td>
        <td>⊥</td>
        <td>Miami</td>
    <td></td><td></td><td></td></tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 26

---

# Data preparation - Enriching

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## user_reviews(enriched)

<table>
    <tr>
        <th>Product</th>
        <th>Category</th>
        <th>UN1</th>
        <th>R</th>
        <th>D</th>
        <th>M</th>
        <th>Y</th>
        <th>City</th>
        <th>State</th>
        <th>UN2</th>
        <th>Name</th>
        <th>Age</th>
        <th>Range</th>
        <th>Gender</th>
        <th>City2</th>
    </tr>
    <tr>
        <td>iPhone 6</td>
        <td>Electronics</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>LA</td>
        <td>CA</td>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td>⊥</td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
        <td>NY</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>Samsung Galaxy</td>
        <td>Electronics</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
        <td>TX</td>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>60-75</td>
        <td>M</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>⊥</td>
        <td>⊥</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>CA</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
        <td>⊥</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 27

---

# Data preparation - Cleaning

- Identify and correct data errors, inconsistencies, and inaccuracies.
- Final step of data preparation that yields accurate, consistent, and reliable data suitable for analysis and decision-making.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Example data cleaning tasks:
- Identify matches
- Remove duplicates
- Remove irrelevant data
- Handle missing data
- Deal with outliers
- Make values consistent
- ...

---

# Data preparation - Cleaning

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## user_reviews(cleaned)

<table>
    <tr>
        <th>Product</th>
        <th>Category</th>
        <th>UN1</th>
        <th>R</th>
        <th>D</th>
        <th>M</th>
        <th>Y</th>
        <th>City</th>
        <th>State</th>
        <th>UN2</th>
        <th>Name</th>
        <th>Age</th>
        <th>Range</th>
        <th>Gender</th>
        <th>City2</th>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>Los Angeles</td>
        <td>CA</td>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td></td>
        <td>3</td>
        <td>04</td>
        <td>24</td>
        <td>2012</td>
        <td>New York</td>
        <td>NY</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Samsung Galaxy A8</td>
        <td>Electronics</td>
        <td>SecretUser007</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
        <td>TX</td>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>60-75</td>
        <td>M</td>
        <td>Austin</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>helloKitty93</td>
        <td>4</td>
        <td>29</td>
        <td>09</td>
        <td>2020</td>
        <td>Los Angeles</td>
        <td>CA</td>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
        <td>Los Angeles</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 29

---

# Data preparation - Cleaning

> Data engineering Data analytics Data understanding Data protection Data ethics

## user_reviews(cleaned)

<table>
    <tr>
        <th>Product</th>
        <th>Category</th>
        <th>R</th>
        <th>D</th>
        <th>M</th>
        <th>Y</th>
        <th>City</th>
        <th>State</th>
        <th>Name</th>
        <th>Age</th>
        <th>Range</th>
        <th>Gender</th>
    </tr>
    <tr>
        <td>Apple iPhone 6</td>
        <td>Electronics</td>
        <td>4</td>
        <td>19</td>
        <td>12</td>
        <td>2011</td>
        <td>Los Angeles</td>
        <td>CA</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>46-60</td>
        <td>F</td>
    </tr>
    <tr>
        <td>Samsung Galaxy A8</td>
        <td>Electronics</td>
        <td>5</td>
        <td>21</td>
        <td>01</td>
        <td>2018</td>
        <td>Austin</td>
        <td>TX</td>
        <td>James Bond</td>
        <td>65</td>
        <td>60-75</td>
        <td>M</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE Nanyang Technological University. All rights reserved. 30

---

# Data preparation – Wrap-up

- Data preparation, through its different stages, transforms raw data into high-quality, well-structured data that is suitable and ready-to-use for the analysis needed by the target data science application.
- Such data are imperative for meaningful analytical results (prevents “garbage-in-garbage-out” problem).
- Although presented as subsequent stages, the order may vary, and some stages may apply more than once before producing the final dataset.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 31

---

# Data management

- Solutions devised for easy support of operations on data, e.g., organize, protect, store, access, and manipulate data.
- Systems, algorithms, and methods that support efficient and scalable use of data.
- Ease of use via abstraction of data handling issues from physical data storage on disc to processing user queries.
- Many different types of data supported by different data management solutions.

Data engineering
Data analytics
Data understanding
Data protection
Data ethics

Data management

Data task (queries)

Files on disk (data)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 32

---

# Genealogy of Relational Database Management Systems

## Data management
- systems & platforms

- Large variety (for relational data and beyond)
- No one-size-fits-all solution, different solutions fit different needs.
- Data scientists need to know which data management solution best fits their needs.

Key to lines and symbols
- O DBMS name (Company)
- □ Acquisition
- v6.2006 Versions
- Discontinued
- Branch (intellectual and/or code)
- Crossing lines have no special semantics

Felix Naumann, Jana Bauckmann, Claudia Exeler, Jan-Peer Rudolph, Fabian Tschirschnitz  
Contact - Hasso Plattner Institut, University of Potsdam, felix.naumann@hpi.de  
Design - Alexander Sardt Grafik-Design, Hamburg  
Version 6.0 - October 2018  
https://hpi.de/naumann/projects/rdbms-genealogy.html

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE  
Nanyang Technological University. All rights reserved.  
33

---

# Schema design

- A schema defines the structure, organization, and relationships of data stored in a database.
- A clear structure of data supports data scientists in
  - Understanding the data
  - Efficient data exploration
  - Identification of data quality issues
  - Definition of data transformation
  - Model building
  - ...

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 34

---

# Schema design example

- A relational schema structures data into tables with attributes (columns); attributes have data types, data in tuples (rows), schema defines relationships, ...
- A good relational schema is normalized.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

<table>
    <tr><th></th>
        <th>CID</th>
        <th>City</th>
        <th>Order</th>
    </tr>
    <tr>
        <td>1</td>
        <td>KL</td>
        <td>{P3, P506, ...}</td>
    <td></td></tr>
    <tr>
        <td>504</td>
        <td>Kuala Lumpur</td>
        <td>{P1, P205, ...}</td>
    <td></td></tr>
    <tr>
        <td>367</td>
        <td>SG</td>
        <td>{P3, P5, ...}</td>
    <td></td></tr>
    <tr>
        <td>1</td>
        <td>KL</td>
        <td>{P2, P2, P765,...}</td>
    <td></td></tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>Code</td>
        <td>City</td>
    <td></td><td></td></tr>
    <tr>
        <td>KL</td>
        <td>Kuala Lumpur</td>
    <td></td><td></td></tr>
    <tr>
        <td>SG</td>
        <td>Singapore</td>
    <td></td><td></td></tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>CID</td>
        <td>CityCode</td>
    <td></td><td></td></tr>
    <tr>
        <td>1</td>
        <td>KL</td>
    <td></td><td></td></tr>
    <tr>
        <td>504</td>
        <td>KL</td>
    <td></td><td></td></tr>
    <tr>
        <td>367</td>
        <td>SG</td>
    <td></td><td></td></tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td>CID</td>
        <td>OID</td>
        <td>PID</td>
        <td>Amount</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>P3</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>P506</td>
        <td>1</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>P2</td>
        <td>2</td>
    </tr>
</table>PoorSchemaDB

GoodSchemaDB

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved. 35

---

# Querying data

- Different types of queries (analytical queries, search, top-k queries, ...)
- Different languages with different expressive power
- Efficient and scalable query execution strategies exist for each type of query / language.
- Data scientists need to know to
  - Efficiently retrieve the data they need
  - Effectively and efficiently perform data cleaning on large volumes of data
  - Implement easy selection of data subsets for model evaluation
  - ...

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

---

# Querying data example

```python
import pandas as pd

# Read employee data from CSV
df = pd.read_csv('employee_data.csv')

# Filter for employees in the 'Sales' department
sales_employees = df[df['department'] == 'Sales']

# Sort employees by salary in descending order
sorted_sales_employees = sales_employees.
    sort_values(by='salary', ascending=False)

# Get the top 5 highest-paid employees
top_5_sales_employees = sorted_sales_employees.head(5)

print(top_5_sales_employees)
```

```sql
SELECT *
FROM employees
WHERE department = 'Sales'
ORDER BY salary DESC
LIMIT 5;
```

> Get top-5 of best paid sales employees (Python vs SQL)

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 37

---

# Data management - Wrap-up

- Knowledge about data management is crucial for data scientist to devise efficient, effective, and scalable data processing.
- The choice of a data management system, schema design, and query language can significantly impact the performance of data science pipeline development and maintenance.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 38

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th colspan="5">Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data engineering</td>
      <td>Data analytics</td>
      <td>Data understanding</td>
      <td>Data protection</td>
      <td>Data ethics</td>
    </tr>
    <tr>
      <td colspan="5">Data science building blocks</td>
    </tr>
    <tr>
      <td colspan="5">Social and policy context</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
39

---

# TYPES OF DATA ANALYTICS

<ins>VALUE</ins>

<ins>COMPLEXITY</ins>

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

> Nanyang Technological University. All rights reserved.

> 41

---

# Descriptive Analytics

- Summarizes and describes historical data.
- Allows to analyze patterns, trends, and relationships.
- Provides insights on "What happened?" or "What does the data tell us?".

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- PATIENT DEMOGRAPHICS (HEALTHCARE)
- RECRUITMENT CHANNEL EFFECTIVENESS (HUMAN RESOURCES)
- SALES PERFORMANCE ANALYSIS (SALES AND MARKETING)
- SHIPPING AND DELIVERY TIMELINE MONITORING (SUPPLY MANAGEMENT)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 42

---

# Descriptive Analytics

- Summarizes and describes historical data.
- Allows to analyze patterns, trends, and relationships.
- Provides insights on "What happened?" or "What does the data tell us?".

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics



<table>
  <caption>Annual temperature change: Mean annual surface temperature change in OECD countries (°C), relative to 1981-2010</caption>
  <thead>
    <tr>
      <th>Year</th>
      <th>Mean annual surface temperature change (°C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1979</td>
      <td>-0.70</td>
    </tr>
    <tr>
      <td>1980</td>
      <td>-0.30</td>
    </tr>
    <tr>
      <td>1981</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>1982</td>
      <td>-0.90</td>
    </tr>
    <tr>
      <td>1983</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <td>1984</td>
      <td>-0.60</td>
    </tr>
    <tr>
      <td>1985</td>
      <td>-0.70</td>
    </tr>
    <tr>
      <td>1986</td>
      <td>-0.60</td>
    </tr>
    <tr>
      <td>1987</td>
      <td>-0.05</td>
    </tr>
    <tr>
      <td>1988</td>
      <td>-0.05</td>
    </tr>
    <tr>
      <td>1989</td>
      <td>-0.45</td>
    </tr>
    <tr>
      <td>1990</td>
      <td>-0.30</td>
    </tr>
    <tr>
      <td>1991</td>
      <td>-0.20</td>
    </tr>
    <tr>
      <td>1992</td>
      <td>-0.60</td>
    </tr>
    <tr>
      <td>1993</td>
      <td>-0.35</td>
    </tr>
    <tr>
      <td>1994</td>
      <td>-0.10</td>
    </tr>
    <tr>
      <td>1995</td>
      <td>-0.10</td>
    </tr>
    <tr>
      <td>1996</td>
      <td>-0.50</td>
    </tr>
    <tr>
      <td>1997</td>
      <td>-0.15</td>
    </tr>
    <tr>
      <td>1998</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>1999</td>
      <td>0.05</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>2001</td>
      <td>0.30</td>
    </tr>
    <tr>
      <td>2002</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>2003</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>2004</td>
      <td>-0.20</td>
    </tr>
    <tr>
      <td>2005</td>
      <td>0.60</td>
    </tr>
    <tr>
      <td>2006</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>0.30</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>0.35</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>0.60</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>0.20</td>
    </tr>
    <tr>
      <td>2014</td>
      <td>0.40</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>0.75</td>
    </tr>
    <tr>
      <td>2016</td>
      <td>1.20</td>
    </tr>
    <tr>
      <td>2017</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>2018</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>2019</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>2021</td>
      <td>0.80</td>
    </tr>
    <tr>
      <td>2022</td>
      <td>0.55</td>
    </tr>
    <tr>
      <td>2023</td>
      <td>1.40</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 43

---

# Diagnostic Analytics

- Studies reasons for
  observed trends, patterns or
  relationships in historical
  data.
- Allows to identify root
  causes and factors
  underlying observed
  phenomena.
- Provides insights on “Why
  did something happen?”.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- FRAUD DETECTION
  (FINANCE)
- DELAY ANALYSIS
  (LOGISTICS)
- CUSTOMER CHURN
  ANALYSIS (SALES AND
  MARKETING)
- WORKPLACE SAFETY
  INCIDENT ANALYSIS
  (HUMAN RESOURCES)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 44

---

# Diagnostic Analytics

- Studies reasons for
  observed trends, patterns or
  relationships in historical
  data.
- Allows to identify root
  causes and factors
  underlying observed
  phenomena.
- Provides insights on “Why
  did something happen?”.

Table 1 Correlation and information flow between observed global surface
temperature and different external forcing's and internal climate variations.
>
> From: On the causal structure between CO₂ and global temperature

<table>
    <tr>
        <th>Radiative Forcing</th>
        <th>Correlation</th>
        <th>Forcing→GMTA[nat/year]</th>
        <th>GMTA→Forcing[nat/year]</th>
    </tr>
    <tr>
        <td>Total forcing</td>
        <td>0.804 ± 0</td>
        <td>0.244 ± 0.091</td>
        <td>0.036 ± 0.080</td>
    </tr>
    <tr>
        <td>Anthropogenic</td>
        <td>0.863 ± 0</td>
        <td>0.355 ± 0.112</td>
        <td>−0.008 ± 0.005</td>
    </tr>
    <tr>
        <td>All GHG</td>
        <td>0.852 ± 0</td>
        <td>0.318 ± 0.108</td>
        <td>−0.005 ± 0.003</td>
    </tr>
    <tr>
        <td>CO2</td>
        <td>0.852 ± 0</td>
        <td>0.316 ± 0.108</td>
        <td>−0.003 ± 0.003</td>
    </tr>
    <tr>
        <td>Aerosol</td>
        <td>−0.810 ± 0</td>
        <td>0.232 ± 0.095</td>
        <td>−0.002 ± 0.006</td>
    </tr>
    <tr>
        <td>Cloud</td>
        <td>−0.796 ± 0</td>
        <td>0.208 ± 0.092</td>
        <td>−0.001 ± 0.004</td>
    </tr>
    <tr>
        <td>Solar</td>
        <td>0.616 ± 0</td>
        <td>0.082 ± 0.059</td>
        <td>0.035 ± 0.051</td>
    </tr>
    <tr>
        <td>Volcanic</td>
        <td>0.089 ± 0.267</td>
        <td>0.003 ± 0.006</td>
        <td>−0.004 ± 0.009</td>
    </tr>
</table>Data
engin
eering
Data
analyt
ics
Data
under
standi
ng
Data
protec
tion
Data
ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 45

---

# Predictive Analytics

- Relies on historical data and statistical models to predict future trends our outcome.
- Supports the definition of data-based strategies or decisions affecting future outcomes.
- Provides insights on “What will happen?”.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- PERSONALIZED RECOMMENDATIONS (CUSTOMER EXPERIENCE)
- DEMAND FORECASTING (MANUFACTURING AND MAINTENANCE)
- EARLY DISEASE PREDICTION (HEALTHCARE)
- GRID OPTIMIZATION (ENERGY AND SUSTAINABILITY)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 46

---

# Predictive Analytics

- Relies on historical data and statistical models to predict future trends our outcome.
- Supports the definition of data-based strategies or decisions affecting future outcomes.
- Provides insights on “What will happen?”.

Data engineering
Data analytics
Data understanding
Data protection
Data ethics

## HOW ARE CO₂ CONCENTRATIONS RELATED TO WARMING?

The higher the CO₂ concentration in the atmosphere, the higher the Earth's temperature.  
The levels of atmospheric CO₂ depend on the amount of emissions produced by humankind.



<table>
  <caption>HOW ARE CO2 CONCENTRATIONS RELATED TO WARMING? (Warming relative to the 1850–1900 period)</caption>
  <thead>
    <tr>
      <th>Year (Approximate)</th>
      <th>CO2 concentration (ppm)</th>
      <th>Warming (°C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1884</td>
      <td>290</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1902</td>
      <td>295</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>1923</td>
      <td>305</td>
      <td>-0.1</td>
    </tr>
    <tr>
      <td>1940</td>
      <td>310</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>1960</td>
      <td>318</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>1980</td>
      <td>338</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>2000</td>
      <td>370</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td>2020</td>
      <td>415</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td>Projection</td>
      <td>450</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td>Projection</td>
      <td>500</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>



CO₂ concentration is measured in ppm (parts per million). The CO₂ concentration of 400 ppm means that one million of air molecules contains 400 molecules of CO₂.  
Carbon dioxide (CO₂) contributes to global warming more than any other greenhouse gas: the greenhouse effect is intensifying and 70% of this change is caused by CO₂.

VERSION 2022-05-12 LICENCE CC BY 4.0  
Read more at factsonclimate.org/concentration-warming-relationship  
Data source: NOAA, NASA Goddard Institute for Space Studies

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE  
Nanyang Technological University. All rights reserved. 47

---

# Prescriptive Analytics

- Recommends actions
  towards reaching a desired
  result based on data.
- Supports defining measures
  to reach a desired outcome
  in the future.
- Provides insights on “What
  should we do?” or “How can
  we make it happen?”.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- WORKFLOW OPTIMIZATION (FINANCE AND OPERATIONS)
- SALES TERRITORY OPTIMIZATION (RETAIL AND SALES)
- TREATMENT RECOMMENDATION (HEALTHCARE)
- DYNAMIC PRICING STRATEGIES (TELECOM)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 48

---

# Prescriptive Analytics

- Recommends actions towards reaching a desired result based on data.
- Supports defining measures to reach a desired outcome in the future.
- Provides insights on “What should we do?” or “How can we make it happen?”.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## SINGAPORE AIRLINES DEPLOYS SITA OPTICLIMB® TO REDUCE UP TO 15,000 TONS OF AIRCRAFT CARBON EMISSIONS PER YEAR

Press Release | Location: Singapore | 12 Oct, 2022

[ ] Share [ ] [ ] [ ]

SITA OptiClimb®, a digital inflight prescriptive analytics tool for fuel optimization, has been selected by Singapore Airlines to support the carrier's goal of achieving net-zero carbon emissions by 2050.

By deploying SITA OptiClimb®, the airline is able to optimize fuel utilization during the aircraft's climb-out phase. The unique solution combines aircraft tail-specific machine-learning models with 4D weather forecasts to recommend customized climb speeds at different altitudes. It leverages historical flight data to predict fuel burn in different flight scenarios and recommends optimized climb profiles on a user-friendly interface for pilots.

It is estimated that airlines can derive fuel savings of up to 5% during climb-out on each flight, with around 5.6 million tons of carbon dioxide emissions avoided annually if every airline worldwide uses SITA OptiClimb®.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 49

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th colspan="5">Applications</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Data engineering</td>
      <td rowspan="2">Data analytics</td>
      <td rowspan="2">Data understanding</td>
      <td rowspan="2">Data protection</td>
      <td rowspan="2">Data ethics</td>
    </tr>
    <tr>
    </tr>
    <tr>
      <th colspan="5">Data science building blocks</th>
    </tr>
    <tr>
      <th colspan="5">Social and policy context</th>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
50

---

# Data understanding

- Data science aims at gaining insights from data for a particular application / goal.
- Being able to understand and interpret results is essential to gain confidence in them / trust the result and the process producing them.
- Such data understanding is relevant in various phases of the data science process.
- Techniques to explain or more easily understand data and data-derived results include explanation and visualization.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 51

---

# Example: Explanation during processing

Why is there a City missing?
→ location extracted from source could not be transformed to a valid US city.

<table>
  <thead>
    <tr>
        <th>Username</th>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>helloKitty</td>
        <td>Jane Smith</td>
        <td>46</td>
        <td>Los Angeles</td>
    </tr>
    <tr>
        <td>JD</td>
        <td>John Doe</td>
        <td>24</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>SecretUser007</td>
        <td>James Bond</td>
        <td>65</td>
        <td>⊥</td>
    </tr>
    <tr>
        <td>maxMiller</td>
        <td>Max Miller</td>
        <td>37</td>
        <td>Miami</td>
    </tr>
  </tbody>
</table>

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

> <img src="https://i.imgur.com/1234567.png" alt="Process flow diagram" width="600">

---

# Example: Visualization to share insights

Under warming of about 1.8-2°C, climate change could indirectly cause malnutrition in an additional 10 million children by 2050.

## SOUTH EAST ASIA
### COASTAL ZONE AND CITIES AT RISK

Under climate change, South East Asia faces increased sea-level rise, tropical cyclones, heat extremes and ocean warming and acidification. When these impacts combine, they are likely to affect multiple sectors, undermining coastal livelihoods and urban cities along the coast.

#### PROJECTED WARMING, WITHOUT CONCERTED ACTION
- 2030s: 1.5°C
- 2040s: 2°C
- 2060s: 3°C
- 2080s: 4°C

##### RESULTING IN:

###### UNUSUAL SUMMER HEAT EXTREMES
(percentage of land that will experience)
- 4°C+ (GREATER THAN): 90%
- 3°C: 85%
- 2°C: 60-70%
- 1.5°C: 50-60%

###### SEA-LEVEL RISE
- 1.5°-2°C: 75CM
- 3°C: 90CM
- 4°C: 110CM
- By 2080-2100

> By 2100 (3°C warming), an 88 cm rise in sea level could flood 69% of Bangkok.

###### BLEACHING OF CORAL REEFS

- Under 2°C warming, marine fish capture is projected to decrease by about 50% in the southern Philippines during the 2050s due to warmer sea temperatures and ocean acidification.
- 4°C: MOST CORAL REEFS ARE PROJECTED TO BE EXTINCT, WITH THE LOSS OF ASSOCIATED FISHERIES AND COASTAL PROTECTION.
- 2°C: VIRTUALLY ALL CORAL REEFS TO EXPERIENCE SEVERE BLEACHING

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

> Ask
> Prepare
> Process
> Analyze
> Act
> Share

<table>
  <thead>
    <tr>
        <th></th>
        <th>2030s</th>
        <th>2040s</th>
        <th>2060s</th>
        <th>2080s</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td>Projected Warming (°C)</td>
        <td>1.5</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr>
        <th></th>
        <th>1.5°C</th>
        <th>2°C</th>
        <th>3°C</th>
        <th>4°C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td>Sea-Level Rise (cm)</td>
        <td>75</td>
        <td>90</td>
        <td>110</td>
        <td></td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr>
        <th></th>
        <th>1.5°C</th>
        <th>2°C</th>
        <th>3°C</th>
        <th>4°C+</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td>Unusual Summer Heat Extremes (%)</td>
        <td>50-60</td>
        <td>60-70</td>
        <td>85</td>
        <td>90</td>
    </tr>
  </tbody>
</table>
<table>
  <thead>
    <tr>
        <th></th>
        <th>1.5°C</th>
        <th>2°C</th>
        <th>3°C</th>
        <th>4°C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td>Marine Fish Capture Decrease (%)</td>
        <td></td>
        <td></td>
        <td></td>
        <td>50</td>
    </tr>
  </tbody>
</table>

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th>Context Layer</th>
      <th>Application Layer</th>
      <th>Data Science Building Blocks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">Social and policy context</td>
      <td rowspan="5">Applications</td>
      <td>Data engineering</td>
    </tr>
    <tr>
      <td>Data analytics</td>
    </tr>
    <tr>
      <td>Data understanding</td>
    </tr>
    <tr>
      <td>Data protection</td>
    </tr>
    <tr>
      <td>Data ethics</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
54

---

# Data protection

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Data security

- Protects information from unauthorized access or malicious attacks.
- Deals with data confidentiality, access control, infrastructure security, and system monitoring.
- Uses technologies such as encryption, trusted execution environments, and monitoring tools.

## Data privacy

- Focuses on the rights of users and groups over data about themselves
- Deals with privacy policies and regulations, management of data use by third parties, and user consent.
- Supported by privacy-enhancing technologies such as data masking, differential privacy, federated learning.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 55

---

# Example: Security through encryption

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

- Alice
  - "Top secret message for Bob"
  - 🔒
- ??? 
  - "X@!KLDF*#M"
  - 🔑
- Bob
  - "Top secret message for Bob"

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 56

---

# Example: Privacy through federated learning

- Model back-distribution
- Global model aggregation
- Sharing of updated model parameters
- Local training
- Medical records
- Hospitals

Data engineering
Data analytics
Data understanding
Data protection
Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
57

---

# Data Science ecosystem



<table>
  <caption>Data Science ecosystem</caption>
  <thead>
    <tr>
      <th colspan="5">Social and policy context</th>
    </tr>
    <tr>
      <th colspan="5">Applications</th>
    </tr>
    <tr>
      <th colspan="5">Data science building blocks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data engineering</td>
      <td>Data analytics</td>
      <td>Data understanding</td>
      <td>Data protection</td>
      <td>Data ethics</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
58

---

# Data ethics considerations

- Individuals, organizations, and society impacted by data-based decisions.
- Data ethics (data science ethics) considers moral problems related to data, algorithms, and related practices towards devising morally good solutions.

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
59

---

# Example: Ethics of data

- Data bias may lead to unfair treatment of a person or groups of persons due to over- or under-representation of persons with similar features in the training data.
- Example: face-recognition systems predominantly trained on faces of white males.

Payout for Uber Eats driver over face scan bias case  
26 March 2024  
Shiona McCallum  
Technology reporter  

> A black Uber Eats driver has received a payout after "racially discriminatory" facial-recognition checks prevented him accessing the app to secure work.

---

# Example: Ethics of algorithms

- Algorithmic bias caused through inadequate engineering and testing of the data analysis.
- Example: poor predictions of A-level grades in the UK.

> The UK’s A-level grading fiasco

For those who haven’t followed the story – two weeks ago, thousands of students in England and Wales received their “A-level” exam grades. Instead of scoring actual exams, however, grades were determined by an algorithm. Almost 40% of students received grades lower than they had anticipated, sparking public outcry and legal action. Faced with protests, the UK government retracted the grades. Students will now receive grades based on their teacher’s estimate of what their grade would have been, had the exams gone forward as planned.

> How did the algorithm discriminate?

---

# Example: Ethics of practices

- Responsibility, liability, ethical behavior of organizations in charge of data processes, strategies, and policies.
- Example: see previous slides + regulators enforcing ethical practice

> IntelliVision censured for misleading biometric accuracy and bias claims by FTC

> Claims undermined by NIST test results

> Dec 3, 2024, 12:29 pm EST | Chris Burt

> CATEGORIES Biometrics News | Facial Recognition | Trade Notes

> <img src="image.png" alt="Image of a man with a facial recognition overlay">

> Nanyang Technological University. All rights reserved.

> 62

---

# Data Science Ecosystem

## SUMMARY

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

> Nanyang Technological University. All rights reserved.

63

---

# Applications, systems, and deployments

> **Data Science application**  
> **Data Science system**  
> **Data Science application deployment**

> **Data protection and data ethics**

> **Data visualization and explanation**  
> **Data preparation and data management**  
> **Data modeling and analytics**

> **Social and policy aspects**

<table>
  <thead>
    <tr>
        <th></th>
        <th>Ask</th>
        <th>Prepare</th>
        <th>Process</th>
        <th>Analyze</th>
        <th>Share</th>
        <th>Act</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
        <td>---</td>
    </tr>
    <tr>
        <td></td>
        <td>Ask</td>
        <td>Prepare</td>
        <td>Process</td>
        <td>Analyze</td>
        <td>Share</td>
        <td>Act</td>
    </tr>
  </tbody>
</table>

> **Nanyang Technological University. All rights reserved.** 64

---

# Holistic consideration

- Applications, systems, and deployments are interlinked and influence one another.

- Examples:
  - Data science systems provide tools and technologies that help data scientists address their problems.
  - Data science systems need to be carefully designed to fit the target applications.
  - Data science systems need to support deployments within their social and policy context.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 65

---

# Data Science ecosystem

Applications

- **Data engineering**
  - Data preparation
  - Data management
- **Data analytics**
  - Data exploration (data mining)
  - Models and algorithms (machine learning)
- **Data understanding**
  - Explanation
  - Visualization
- **Data protection**
  - Security
  - Privacy
- **Data ethics**
  - Impact on individuals, organizations, and society
  - Bias in data
  - Algorithmic bias
  - Regulatory issues

Data science building blocks

Social and policy context

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
66

---

# You should now be able to...

- ... describe the main components of the data science ecosystem.
- ... explain how different factors influence the development of a data science system.
- ... define the functionality of data science building blocks at a high level to solve data science applications.
- ... reflect on possible data protection, data ethics, social and policy aspects that may affect the data science application deployment.

> Nanyang Technological University. All rights reserved.

---

# References

- M. Tamer Özsu: Data Science - A Systematic Treatment. Commun. ACM 66 (7), (2023), 106-116. [https://doi.org/10.1145/3582491](https://doi.org/10.1145/3582491)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 68