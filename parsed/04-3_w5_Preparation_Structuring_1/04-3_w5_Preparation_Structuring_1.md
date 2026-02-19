# Data Science Fundamentals
[SC3021]

## Chapter 4: Data Preparation

Assoc. Prof. Melanie Herschel | CCDS

---

# Data preparation (reminder)

Data preparation is the process of converting raw data into a form that allows to extract value from data.

<table>
  <tbody>
    <tr>
        <td>Access</td>
        <td>Profile / transform</td>
        <td>Publish</td>
    </tr>
  </tbody>
</table>

> Access → Profile / transform → Publish

---

# Data transformation tasks

- Data Profiling
- Data Structuring
- Data preparation
- Data Enriching
- Data Cleaning

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
3

---

# Chapter 4.3: Data Transformation

> NANYANG TECHNOLOGICAL UNIVERSITY SINGAPORE

---

# At the end of Chapter 4.3, you should be able to...

- ... define and classify various data transformation tasks.
- ... determine which data transformations can be used to prepare the data for a specific data science application.
- ... describe and recognize various data quality issues within and across datasets.
- ... implement various data transformation tasks.

> <img src="image.png" alt="Image of arrows hitting a target" width="500">

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 5

---

# STRUCTURING

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
6

---

# Overview of structuring transformations

- Structuring as a transformation action involves changing the structure and granularity of a dataset.
  - Changes form and schema of the data.
- Structuring transformations create new data based on data already present in the dataset.
- Two main subclasses:
  - Intrarecord structuring transformations involve manipulating individual attributes and tuples.
  - Interrecord structuring transformations involve tuples and attributes at once.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 7

---

# Overview of structuring transformations

> Structuring

- Intrarecord
  - Reordering attributes
  - Creating attributes
  - Combining attributes
- Interrecord
  - Filtering dataset
  - Aggregation
  - Pivot

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 8

---

# Running example

## Example data
- “Contributions by Individuals” file from election year 2015-2016
- Data available at
  [http://www.fec.gov/finance/disclosure/ftpdet.shtml#a2015_2016](http://www.fec.gov/finance/disclosure/ftpdet.shtml#a2015_2016)

## Data dictionary
- Can help understand the permissible values.
- Metadata available at
  http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributions/byIndividuals.shtml

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 9

---

# Running example – Data excerpt

<table>
    <tr>
        <th>A</th>
        <th>B</th>
        <th>C</th>
        <th>D</th>
        <th>E</th>
        <th>F</th>
        <th>G</th>
        <th>H</th>
        <th>I</th>
        <th>J</th>
        <th>K</th>
        <th>L</th>
        <th>M</th>
        <th>N</th>
        <th>O</th>
        <th>P</th>
    </tr>
    <tr>
        <td>Column1</td>
        <td>Column2</td>
        <td>Column3</td>
        <td>Column4</td>
        <td>Column5</td>
        <td>Column6</td>
        <td>Column7</td>
        <td>Column8</td>
        <td>Column9</td>
        <td>Column10</td>
        <td>Column11</td>
        <td>Column12</td>
        <td>Column13</td>
        <td>Column14</td>
        <td>Column15</td>
        <td>Column16</td>
    </tr>
    <tr>
        <td>1</td>
        <td>C00276311</td>
        <td>N</td>
        <td>YE</td>
        <td>P</td>
        <td>2.01601E+17</td>
        <td>15</td>
        <td>IND</td>
        <td>KENNEDY, CHARLIE</td>
        <td>SCOTTSBLUFF</td>
        <td>NE</td>
        <td>69361</td>
        <td>BLUE CROSS BLUE SHIELD OF NE</td>
        <td>PROVIDER RELATIONSHIP MANAGER</td>
        <td>12312016</td>
        <td>264</td>
    </tr>
    <tr>
        <td>2</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>MILLER, LUCILE S</td>
        <td>RICHMOND</td>
        <td>VA</td>
        <td>232263208</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12302016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>3</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>SCHULZ, ANDREA</td>
        <td>NEW YORK</td>
        <td>NY</td>
        <td>100106410</td>
        <td>PENGUIN</td>
        <td>EDITOR</td>
        <td>12282016</td>
        <td>250</td>
    </tr>
    <tr>
        <td>4</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>FINLEY, SHANNON J</td>
        <td>WASHINGTON</td>
        <td>DC</td>
        <td>200071107</td>
        <td>CAPITOL COUNSEL, LLC</td>
        <td>LOBBYIST</td>
        <td>12302016</td>
        <td>1700</td>
    </tr>
    <tr>
        <td>5</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>DAKIN, WILLIAM G</td>
        <td>WASHINGTON</td>
        <td>DC</td>
        <td>200082663</td>
        <td>N/A</td>
        <td>RETIRED</td>
        <td>12272016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>6</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>LESTER, HARRY T</td>
        <td>VIRGINIA BEACH</td>
        <td>VA</td>
        <td>234552848</td>
        <td>EASTERN VIRGINIA MEDICAL SCHOOL</td>
        <td>PRESIDENT</td>
        <td>12292016</td>
        <td>2700</td>
    </tr>
    <tr>
        <td>7</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>EVANS, MEGAN</td>
        <td>ALEXANDRIA</td>
        <td>VA</td>
        <td>223143821</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12302016</td>
        <td>500</td>
    </tr>
    <tr>
        <td>8</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>KNAPP, JOHN W SR</td>
        <td>LEXINGTON</td>
        <td>VA</td>
        <td>244501789</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12272016</td>
        <td>50</td>
    </tr>
    <tr>
        <td>9</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>MANUS, JILLIAN</td>
        <td>ATHERTON</td>
        <td>CA</td>
        <td>940275440</td>
        <td>STRUCTURE CAPITAL</td>
        <td>VENTURE CAPITALIST</td>
        <td>12272016</td>
        <td>500</td>
    </tr>
    <tr>
        <td>10</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>CORBETT, LEO</td>
        <td>NEW YORK</td>
        <td>NY</td>
        <td>100295245</td>
        <td>SELF EMPLOYED</td>
        <td>BUSINESS CONSULTANT</td>
        <td>12282016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>11</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>ALTSHULER, SHARMAN</td>
        <td>CAMBRIDGE</td>
        <td>MA</td>
        <td>21383329</td>
        <td>MOONBOX PRODUCTIONS</td>
        <td>THEATER PRODUCER</td>
        <td>12302016</td>
        <td>500</td>
    </tr>
    <tr>
        <td>12</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>DAVID, JOSEPH J</td>
        <td>CHARLOTTESVILLE</td>
        <td>VA</td>
        <td>22902</td>
        <td>SELF-EMPLOYED</td>
        <td>PHYSICIAN</td>
        <td>12102016</td>
        <td>250</td>
    </tr>
    <tr>
        <td>13</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>MISKA, SIMA</td>
        <td>PINECREST</td>
        <td>FL</td>
        <td>331566105</td>
        <td>N/A</td>
        <td>HOMEMAKER</td>
        <td>12312016</td>
        <td>50</td>
    </tr>
    <tr>
        <td>14</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>WALDRON, KAREN HOLLY</td>
        <td>SHAWSVILLE</td>
        <td>VA</td>
        <td>241621840</td>
        <td>FRALIN &amp; WALDRON INC</td>
        <td>REAL ESTATE DEVELOPER</td>
        <td>12192016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>15</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>WARNER, RAY</td>
        <td>WILLIAMSBURG</td>
        <td>VA</td>
        <td>231853976</td>
        <td>SMITH DAWSON &amp; ANDREWS</td>
        <td>GOVERNMENT RELATIONS</td>
        <td>12212016</td>
        <td>250</td>
    </tr>
    <tr>
        <td>16</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>CROSWELL, CLYDE</td>
        <td>BERRYVILLE</td>
        <td>VA</td>
        <td>226112408</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12102016</td>
        <td>25</td>
    </tr>
    <tr>
        <td>17</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>G2018</td>
        <td>2.01804E+17</td>
        <td>15</td>
        <td>IND</td>
        <td>STONE, CATHLEEN D</td>
        <td>BOSTON</td>
        <td>MA</td>
        <td>21081103</td>
        <td>SELF EMPLOYED</td>
        <td>ATTORNEY</td>
        <td>12232016</td>
        <td>2500</td>
    </tr>
    <tr>
        <td>18</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>G2018</td>
        <td>2.01804E+17</td>
        <td>15</td>
        <td>IND</td>
        <td>MASON, CYNTHIA</td>
        <td>CHESTER</td>
        <td>VA</td>
        <td>238314700</td>
        <td>N/A</td>
        <td>RETIRED</td>
        <td>12302016</td>
        <td>500</td>
    </tr>
    <tr>
        <td>19</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>DAKIN, WILLIAM G</td>
        <td>WASHINGTON</td>
        <td>DC</td>
        <td>200082663</td>
        <td>N/A</td>
        <td>RETIRED</td>
        <td>12302016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>20</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>THIBODEAUX, JOYCE</td>
        <td>HOUMA</td>
        <td>LA</td>
        <td>703605932</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12272016</td>
        <td>25</td>
    </tr>
    <tr>
        <td>21</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>HAUSLER, RICHARD W</td>
        <td>FAIRFAX</td>
        <td>VA</td>
        <td>220312711</td>
        <td>INSIGHT PROPERTY GROUP LLC</td>
        <td>EXECUTIVE/ATTORNEY</td>
        <td>12082016</td>
        <td>500</td>
    </tr>
    <tr>
        <td>22</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>KAUFMAN, SUSAN F</td>
        <td>VIRGINIA BEACH</td>
        <td>VA</td>
        <td>234541624</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12102016</td>
        <td>250</td>
    </tr>
    <tr>
        <td>23</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>KAY, SAUL</td>
        <td>ENCINO</td>
        <td>CA</td>
        <td>913164415</td>
        <td>N/A</td>
        <td>RETIRED</td>
        <td>12142016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>24</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>REEDER, JAMES</td>
        <td>FRANKLIN</td>
        <td>VA</td>
        <td>238512863</td>
        <td>TRAVEL INCORPORATED</td>
        <td>TRAVEL AGENT</td>
        <td>12302016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>25</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>HUFFMAN, ROBERT K</td>
        <td>MCLEAN</td>
        <td>VA</td>
        <td>221012239</td>
        <td>AKIN GUMP STRAUSS HAUER &amp; FELD</td>
        <td>LAWYER</td>
        <td>12302016</td>
        <td>25</td>
    </tr>
    <tr>
        <td>26</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>OMOTAYO, ADEWALE</td>
        <td>NORTH CHESTERFIELD</td>
        <td>VA</td>
        <td>232363511</td>
        <td>BIG O'CAB</td>
        <td>TRANSPORTER</td>
        <td>12302016</td>
        <td>25</td>
    </tr>
    <tr>
        <td>27</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>THIBODEAUX, JOYCE</td>
        <td>HOUMA</td>
        <td>LA</td>
        <td>703605932</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12292016</td>
        <td>50</td>
    </tr>
    <tr>
        <td>28</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>MURPHY, ARLENE</td>
        <td>FAIRFIELD</td>
        <td>CT</td>
        <td>68246503</td>
        <td>N/A</td>
        <td>COMMUNITY VOLUNTEER</td>
        <td>12312016</td>
        <td>200</td>
    </tr>
    <tr>
        <td>29</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>CROSWELL, CLYDE</td>
        <td>BERRYVILLE</td>
        <td>VA</td>
        <td>226112408</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12312016</td>
        <td>100</td>
    </tr>
    <tr>
        <td>30</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>THIBODEAUX, JOYCE</td>
        <td>HOUMA</td>
        <td>LA</td>
        <td>703605932</td>
        <td>N/A</td>
        <td>NOT EMPLOYED</td>
        <td>12202016</td>
        <td>50</td>
    </tr>
    <tr>
        <td>31</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>ALTSHULER, SHARMAN</td>
        <td>CAMBRIDGE</td>
        <td>MA</td>
        <td>21383329</td>
        <td>MOONBOX PRODUCTIONS</td>
        <td>THEATER PRODUCER</td>
        <td>12082016</td>
        <td>25</td>
    </tr>
    <tr>
        <td>32</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>FREY, RUSSELL</td>
        <td>MCLEAN</td>
        <td>VA</td>
        <td>221013206</td>
        <td>EDHELPER</td>
        <td>PRESIDENT</td>
        <td>12252016</td>
        <td>1000</td>
    </tr>
    <tr>
        <td>33</td>
        <td>C00495358</td>
        <td>A</td>
        <td>YE</td>
        <td>P2018</td>
        <td>2.01804E+17</td>
        <td>15E</td>
        <td>IND</td>
        <td>SHEEHAN, ROBERT</td>
        <td>NEW YORK</td>
        <td>NY</td>
        <td>100257659</td>
        <td>SKADDEN ARPS SLATE MEAGHER&amp;FLOM</td>
        <td>ATTORNEY</td>
        <td>12312016</td>
        <td>100</td>
    </tr>
</table><ins>itcont_2016_20161208_92060702</ins> Sheet1 + 

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 10

---

# Intrarecord structuring

- **Reordering attributes**
  - Attributes and values remain unchanged
- **Creating attributes**
  - Attributes are added with values extracted from existing attributes
- **Combining attributes**
  - Attributes are merged into a single attribute

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
11

---

# Reordering attributes

> We switch columns 2 and 3 in the example file.

```python
[67] # switch columns based on their initial positions in the original schema
df = df[ df.columns.tolist()[0:1] + #keep first attribute (Column 1)
         df.columns.tolist()[2:3] + # add third attribute (Column 3)
         df.columns.tolist()[1:2] + #add second attribute (Column 2)
         df.columns.tolist()[3:]] #append any remaining attributes
print(df.columns)
```

```text
Index(['Column1', 'Column3', 'Column2', 'Column4', 'Column5', 'Column6',
       'Column7', 'Column8', 'Column9', 'Column10', 'Column11', 'Column12',
       'Column13', 'Column14', 'Column15', 'Column16', 'Column17', 'Column18',
       'Column19', 'Column20', 'Column21'],
      dtype='object')
```

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 12

---

# Extracting Values

- Extraction involves creating a new column (i.e., attribute and values for this new attribute) from an existing column.
- Three common extraction approaches:
  - Positional extraction
  - Pattern extraction
  - Complex structure extraction

> 

<table>
  <caption>Conceptual diagram of a data table with a newly extracted column (red) and existing columns (blue)</caption>
  <thead>
    <tr>
      <th>New Attribute (Red)</th>
      <th>Existing Attribute 1 (Blue)</th>
      <th>Existing Attribute 2 (Blue)</th>
      <th>Existing Attribute 3 (Blue)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Value (Light Red)</td>
      <td>Value (Light Blue)</td>
      <td>Value (Light Blue)</td>
      <td>Value (Light Blue)</td>
    </tr>
    <tr>
      <td>Value (Light Red)</td>
      <td>Value (Light Blue)</td>
      <td>Value (Light Blue)</td>
      <td>Value (Light Blue)</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 13

---

# Extracting values – Positional extraction

- Involves identifying a substring in an existing column C and placing that substring into a new column C'.
- Requires the specification of positions (start index, end index) to delimit the substring to be extracted from values of C and stored in the corresponding value of C'.
- Common use:
  - Date-time fields
  - Fixed-width fields

> 

<table>
  <caption>Positional Extraction Data Table Diagram</caption>
  <thead>
    <tr>
      <th>Extracted Column (C')</th>
      <th>Original Column 1</th>
      <th>Original Column 2</th>
      <th>Original Column 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Value 1 (Extracted)</td>
      <td>Data 1.1</td>
      <td>Data 1.2</td>
      <td>Data 1.3</td>
    </tr>
    <tr>
      <td>Value 2 (Extracted)</td>
      <td>Data 2.1</td>
      <td>Data 2.2</td>
      <td>Data 2.3</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 14

---

# Extracting values – Positional extraction



<table>
  <caption>Positional extraction of date components from Column14</caption>
  <thead>
    <tr>
      <th>Column14</th>
      <th>month</th>
      <th>day</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>12312016</td>
      <td>12</td>
      <td>31</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>12302016</td>
      <td>12</td>
      <td>30</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>12282016</td>
      <td>12</td>
      <td>28</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>12302016</td>
      <td>12</td>
      <td>30</td>
      <td>2016</td>
    </tr>
    <tr>
      <td>12272016</td>
      <td>12</td>
      <td>27</td>
      <td>2016</td>
    </tr>
  </tbody>
</table>



- **Column14**
  - 12312016
  - 12302016
  - 12282016
  - 12302016
  - 12272016
  - 12292016
  - 12302016
  - 12272016
  - 12272016

- This column stores a data in the format MMDDYYYY.
- We extract three attributes from it: month, day, year.
- Fixed positions of extracted values throughout the column.

> Positional extraction
>
> From Column 14, extract values for new attributes based on fixed positions in the fixed length string describing a date in MMDDYYYY format.
>
```python
df['month'] = df['Column14'].astype(str).str[:2]
df['day'] = df['Column14'].astype(str).str[2:4]
df['year'] = df['Column14'].astype(str).str[4:]
print(df[['Column14', 'month', 'day', 'year']])
```
>
<table>
    <tr>
        <th></th>
        <th>Column14</th>
        <th>month</th>
        <th>day</th>
        <th>year</th>
    </tr>
    <tr>
        <td>0</td>
        <td>12312016</td>
        <td>12</td>
        <td>31</td>
        <td>2016</td>
    </tr>
    <tr>
        <td>1</td>
        <td>12302016</td>
        <td>12</td>
        <td>30</td>
        <td>2016</td>
    </tr>
    <tr>
        <td>2</td>
        <td>12282016</td>
        <td>12</td>
        <td>28</td>
        <td>2016</td>
    </tr>
    <tr>
        <td>3</td>
        <td>12302016</td>
        <td>12</td>
        <td>30</td>
        <td>2016</td>
    </tr>
    <tr>
        <td>4</td>
        <td>12272016</td>
        <td>12</td>
        <td>27</td>
        <td>2016</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 15

---

# Extracting values –
Positional extraction

<ins>Column8</ins>
KENNEDY, CHARLIE
MILLER, LUCILE S
SCHULZ, ANDREA
FINLEY, SHANNON J
DAKIN, WILLIAM G
LESTER, HARRY T
EVANS, MEGAN
KNAPP, JOHN W SR
MANUS, JILLIAN
CORBETT, LEO
ALTSHULER, SHARMAN
DAVID, JOSEPH J
MISKA, SIMA

- This column stores strings representing LASTNAME, FIRSTNAMES.
- We can separate them via the position of the comma (,)
- Position of separator varies and has to be determined for extraction

```python
# Find the position of the comma in 'Column8'
df['comma_pos'] = df['Column8'].str.find(',')

# Extract last name and first name (while coping with Column8 values witout ,)
df['firstname'] = df.apply(lambda row:
    row['Column8'][int(row['comma_pos']) + 1:].lstrip()
    if row['comma_pos'] > -1 else None, axis=1)
df['lastname'] = df.apply(lambda row:
    row['Column8'][:int(row['comma_pos'])].rstrip()
    if row['comma_pos'] >-1 else None, axis=1)

# Display the results
print(df[['Column8', 'lastname', 'firstname']])
```

<table>
    <tr>
        <th></th>
        <th>Column8</th>
        <th>lastname</th>
        <th>firstname</th>
    </tr>
    <tr>
        <td>0</td>
        <td>KENNEDY, CHARLIE</td>
        <td>KENNEDY</td>
        <td>CHARLIE</td>
    </tr>
    <tr>
        <td>1</td>
        <td>MILLER, LUCILE S</td>
        <td>MILLER</td>
        <td>LUCILE S</td>
    </tr>
    <tr>
        <td>2</td>
        <td>SCHULZ, ANDREA</td>
        <td>SCHULZ</td>
        <td>ANDREA</td>
    </tr>
    <tr>
        <td>3</td>
        <td>FINLEY, SHANNON J</td>
        <td>FINLEY</td>
        <td>SHANNON J</td>
    </tr>
    <tr>
        <td>4</td>
        <td>DAKIN, WILLIAM G</td>
        <td>DAKIN</td>
        <td>WILLIAM G</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    <tr>
        <td>662545</td>
        <td>MIGNANO, JOHN E. MD, PHD</td>
        <td>MIGNANO</td>
        <td>JOHN E. MD, PHD</td>
    </tr>
    <tr>
        <td>662546</td>
        <td>PACKIANATHAN, SATYASEELAN MD, PHD</td>
        <td>PACKIANATHAN</td>
        <td>SATYASEELAN MD, PHD</td>
    </tr>
    <tr>
        <td>662547</td>
        <td>PAWLICKI, TODD PHD</td>
        <td>PAWLICKI</td>
        <td>TODD PHD</td>
    </tr>
    <tr>
        <td>662548</td>
        <td>DRESTIDGE BRADLEY D MD MS</td>
        <td>DRESTIDGE</td>
        <td>BRADLEY D MD MS</td>
    </tr>
</table>> 

<table>
  <caption>Symbolic Data Table Representation</caption>
  <thead>
    <tr>
      <th>Column 1 (Red/Pink Tones)</th>
      <th>Column 2 (Blue Tones)</th>
      <th>Column 3 (Blue Tones)</th>
      <th>Column 4 (Blue Tones)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dark Red</td>
      <td>Dark Blue</td>
      <td>Dark Blue</td>
      <td>Dark Blue</td>
    </tr>
    <tr>
      <td>Light Pink</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
    </tr>
    <tr>
      <td>Very Light Pink</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
16

---

# Extracting values – Pattern extraction

- Uses rules to describe the sequence of characters or patterns to be extracted.
- Such patterns can frequently be specified by regular expressions (regex).

- Some regex notation
  - `\d` matches a digit
  - `\s` matches a whitespace
  - `*` for 0 or more occurrences
  - `?` For 0 or one occurrence
  - `|` either or
  - `[0-9]` accepted range of values
- Full reference: [Python RegEx](https://www.w3schools.com/python/python_regex.asp)

> 

<table>
  <caption>Conceptual Data Grid Illustration</caption>
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
      <th>Column 3</th>
      <th>Column 4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Red</td>
      <td>Blue</td>
      <td>Blue</td>
      <td>Blue</td>
    </tr>
    <tr>
      <td>Light Red</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
    </tr>
    <tr>
      <td>Very Light Red</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 17

---

# Extracting values – Pattern extraction



<table>
  <caption>Extracting values – Pattern extraction: Column20 Data</caption>
  <thead>
    <tr>
      <th>Column20</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>P/R DEDUCTION ($97.85 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($25.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($75.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($36.55 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($20.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($45.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($20.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($60.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($20.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($25.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($25.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($25.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($20.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($25.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($15.00 SEMI-MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($30.00 MONTHLY)</td>
    </tr>
    <tr>
      <td>P/R DEDUCTION ($42.11 SEMI-MONTHLY)</td>
    </tr>
  </tbody>
</table>



- We want to create a new column
  MONTHLY_CONTRIBUTION
- Needs extraction of the digits + dot + digits between the $-sign and the keyword MONTHLY.

> Regular expression: `\$\\d+.?\\d*\\sMONTHLY`

---

# Extracting values – Pattern extraction

## Regular expression:
`\$\\d+.?\\d*\\sMONTHLY`

- Regular expressions integrated in `re` Python library
- `search()` returns all substrings of text that match the expression (can be more than one).

```python
import re

def extract_contribution(txt):
    # Search for the pattern
    # $ + digits + . (optional) + digits (optional) + space + MONTHLY
    match = re.search(r"\$\d+.?\d*\sMONTHLY", str(txt))
    if match:
        # Remove MONTHLY suffix and $ prefix
        return float(match.group(0).split(' ')[0][1:])
    else:
        return np.NaN

df['MONTHLY_CONTRIBUTION'] = df['Column20'].apply(extract_contribution)
print(
    df[['Column20', 'MONTHLY_CONTRIBUTION']].sort_values(by='MONTHLY_CONTRIBUTION', ascending=False).head(100)
)
```

<table>
    <tr>
        <th>Column20</th>
        <th>MONTHLY_CONTRIBUTION</th>
    </tr>
    <tr>
        <td>3454 P/R DEDUCTION ($437.50 MONTHLY)</td>
        <td>437.50</td>
    </tr>
    <tr>
        <td>16316 P/R DEDUCTION ($416.66 MONTHLY)</td>
        <td>416.66</td>
    </tr>
    <tr>
        <td>26381 P/R DEDUCTION ($416.66 MONTHLY)</td>
        <td>416.66</td>
    </tr>
    <tr>
        <td>14576 ($416.66 MONTHLY)</td>
        <td>416.66</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 19

---

# Extracting values – Complex structures

- Data is not always structured in tables.
- Semi-structured data allows complex hierarchical structures (e.g., XML, JSON)
- Two types of complex structures in JSON, namely JSON array and JSON map



<table>
  <caption>Conceptual Table Structure Diagram</caption>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 20

---

# Complex structures in JSON

## JSON array [e_1, e_2, ..., e_n]
- Ordered sequence of elements e_i
- Elements in arrays can be of simple or complex type, or null

```json
[
  [1, "Alice", 3],
  ["Bob"],
  [ [true, false], 8, 9]
]
```

## JSON map {k_1:v_1, ..., k_n:v_n}
- Set of key-value pairs k_i: v_i
- Key k_i is a string representing a property name and value v_i represents the value of that property.

```json
{
  "courseID": "SC3021",
  "weeks": [
    {
      "weekID": 1,
      "lecture": "Intro",
      "tutorial": "project"
    },
    ...
  ]
}
```

> 

<table>
  <caption>Data Structure Representation Icon</caption>
  <thead>
    <tr>
      <th>Dark Red</th>
      <th>Dark Blue</th>
      <th>Dark Blue</th>
      <th>Dark Blue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Light Red</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
      <td>Light Blue</td>
    </tr>
    <tr>
      <td>Very Light Red</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
      <td>Very Light Blue</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 21

---

# Extracting values – Complex structures

- Semi-structured data allows variable structure across records.
  - Different array lengths
  - Varying properties across records
  - etc.
- Extraction from these complex structures necessary to obtain tabular data.

{ "courseID": "SC3021",
"weeks": [
{ "weekID":1,
"lecture":"Intro",
"tutorial": "project"
}, ...] }



<table>
  <caption>Extracting values from complex structures to obtain tabular data</caption>
  <thead>
    <tr>
      <th>CourseID</th>
      <th>weekID</th>
      <th>Lecture</th>
      <th>Tutorial</th>
      <th>Lab</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SC3021</td>
      <td>1</td>
      <td>Intro</td>
      <td>Project</td>
      <td>NULL</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>SC3021</td>
      <td>4</td>
      <td>Profiling</td>
      <td>Ecosystem</td>
      <td>Task1</td>
    </tr>
  </tbody>
</table>



> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

```latex
\begin{tabular}{|l|l|l|l|l|}
\hline
CourseID & weekID & Lecture & Tutorial & Lab \\
\hline
SC3021 & 1 & Intro & Project & NULL \\
\hline
... & ... & ... & ... & ... \\
\hline
SC3021 & 4 & Profiling & Ecosystem & Task1 \\
\hline
\end{tabular}
```

> Nanyang Technological University. All rights reserved. 22

---

import json

# Create a list to store the JSON records
json_records = []

# Create example data

data = { "courseID": "SC3021",
  "weeks": [{ "weekID":1,"lecture":"Intro", "tutorial": "project"},
               { "weekID":4,"lecture":"Profiling", "tutorial": "Ecosystem", "Lab":"Task1"} ]
  }

# Append the dictionary to the list
json_records.append(data)

# Convert the list of dictionaries to a JSON string
json_data = json.dumps(json_records, indent=4)

# Convert the JSON string back to a list of dictionaries
json_records = json.loads(json_data)

# Create a table that extracts all values
df = pd.json_normalize(json_records[0], 'weeks', ['courseID'])
print(df)

Extracting values –
Complex structures

<table>
    <tr>
        <th></th>
        <th>weekID</th>
        <th>lecture</th>
        <th>tutorial</th>
        <th>Lab</th>
        <th>courseID</th>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>Intro</td>
        <td>project</td>
        <td>NaN</td>
        <td>SC3021</td>
    </tr>
    <tr>
        <td>1</td>
        <td>4</td>
        <td>Profiling</td>
        <td>Ecosystem</td>
        <td>Task1</td>
        <td>SC3021</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 23

---

# When to use which extraction technique

## Positional extraction

- When each record field conforms to a known structure, and each unique substring in the field always begins and ends at the same position
- When each record field contains multiple substrings that are separated by the same delimiter string. Substrings do not necessarily need to be the same length or conform to the same pattern.

## Pattern-based extraction

- When you want to extract a substring that can be defined by a generic pattern.

## Complex structure extraction

- When your record fields contain JSON maps or arrays, and you want to extract individual elements from those structures. Many datasets that are machine-generated contain complex JSON structures.



<table>
  <caption>When to use which extraction technique</caption>
  <thead>
    <tr>
      <th>Extraction Technique</th>
      <th>When to use</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Positional extraction</td>
      <td>
        <ul>
          <li>When each record field conforms to a known structure, and each unique substring in the field always begins and ends at the same position</li>
          <li>When each record field contains multiple substrings that are separated by the same delimiter string. Substrings do not necessarily need to be the same length or conform to the same pattern.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Pattern-based extraction</td>
      <td>
        <ul>
          <li>When you want to extract a substring that can be defined by a generic pattern.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Complex structure extraction</td>
      <td>
        <ul>
          <li>When your record fields contain JSON maps or arrays, and you want to extract individual elements from those structures. Many datasets that are machine-generated contain complex JSON structures.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 24

---

# Combining multiple attributes

# Combine 'Column9' and 'Column10'
df['Combined_Column'] = df['Column9'] + ', ' + df['Column10']
print(df[['Column9', 'Column10', 'Combined_Column']])

<table>
    <tr>
        <th>Column9</th>
        <th>Column10</th>
    <th></th><th></th></tr>
    <tr>
        <td>SCOTTSBLUFF</td>
        <td>NE</td>
    <td></td><td></td></tr>
    <tr>
        <td>RICHMOND</td>
        <td>VA</td>
    <td></td><td></td></tr>
    <tr>
        <td>NEW YORK</td>
        <td>NY</td>
    <td></td><td></td></tr>
    <tr>
        <td>WASHINGTON</td>
        <td>DC</td>
    <td></td><td></td></tr>
    <tr>
        <td>WASHINGTON</td>
        <td>DC</td>
    <td></td><td></td></tr>
    <tr>
        <td>VIRGINIA BEACH</td>
        <td>VA</td>
    <td></td><td></td></tr>
    <tr>
        <td>ALEXANDRIA</td>
        <td>VA</td>
    <td></td><td></td></tr>
    <tr>
        <td>LEXINGTON</td>
        <td>VA</td>
    <td></td><td></td></tr>
    <tr>
        <td>ATHERTON</td>
        <td>CA</td>
    <td></td><td></td></tr>
    <tr>
        <td>NEW YORK</td>
        <td>NY</td>
    <td></td><td></td></tr>
    <tr>
        <td>CAMBRIDGE</td>
        <td>MA</td>
    <td></td><td></td></tr>
    <tr>
        <td></td>
    <td></td><td></td><td></td></tr>
    <tr>
        <td></td>
        <td>Column9</td>
        <td>Column10</td>
        <td>Combined_Column</td>
    </tr>
    <tr>
        <td>0</td>
        <td>SCOTTSBLUFF</td>
        <td>NE</td>
        <td>SCOTTSBLUFF, NE</td>
    </tr>
    <tr>
        <td>1</td>
        <td>RICHMOND</td>
        <td>VA</td>
        <td>RICHMOND, VA</td>
    </tr>
    <tr>
        <td>2</td>
        <td>NEW YORK</td>
        <td>NY</td>
        <td>NEW YORK, NY</td>
    </tr>
    <tr>
        <td>3</td>
        <td>WASHINGTON</td>
        <td>DC</td>
        <td>WASHINGTON, DC</td>
    </tr>
    <tr>
        <td>4</td>
        <td>WASHINGTON</td>
        <td>DC</td>
        <td>WASHINGTON, DC</td>
    </tr>
    <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
    </tr>
    <tr>
        <td>662545</td>
        <td>BROOKLINE</td>
        <td>MA</td>
        <td>BROOKLINE, MA</td>
    </tr>
    <tr>
        <td>662546</td>
        <td>JACKSON</td>
        <td>MS</td>
        <td>JACKSON, MS</td>
    </tr>
    <tr>
        <td>662547</td>
        <td>LA JOLLA</td>
        <td>CA</td>
        <td>LA JOLLA, CA</td>
    </tr>
    <tr>
        <td>662548</td>
        <td>NORFOLK</td>
        <td>VA</td>
        <td>NORFOLK, VA</td>
    </tr>
    <tr>
        <td>662549</td>
        <td>APPLETON</td>
        <td>WI</td>
        <td>APPLETON, WI</td>
    </tr>
</table>NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 25

---

# Overview of structuring transformations

- Structuring
  - Intrarecord
    - Reordering attributes
    - Creating attributes
    - Combining attributes
  - Interrecord
    - Filtering dataset
    - Aggregation
    - Pivot
    - Coming up next

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
26

---

# References and credits

- Joseph M. Hellerstein, Tye Rattenbury, Jeffrey Heer, Sean Kandel, Connor Carreras. Principles of Data Wrangling. O’Reilly Media. 2017 – Chapter 4

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 27