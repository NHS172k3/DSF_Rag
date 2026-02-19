# Data Science Fundamentals
[SC3021]

## Chapter 4: Data Preparation

Assoc. Prof. Melanie Herschel | CCDS

---

# Chapter 4.2: Data profiling

> NANYANG TECHNOLOGICAL UNIVERSITY SINGAPORE

---

# At the end of this sub-chapter, you should be able to...

- ... explain different profiling tasks and how they may apply at different data science stages.
- ... identify profiling tasks suited to gain relevant information on a given dataset for a specific application.
- ... reflect on the computational complexity of profiling tasks when applying them to large data sets.

> Nanyang Technological University. All rights reserved.

---

# INTRODUCTION TO DATA PROFILING

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
4

---

# Data profiling in the Data Science Ecosystem

> Data engineering | Data analytics | Data understanding | Data protection | Data ethics

## Data Engineering

The practice of designing, building, and maintaining systems that collect, manage, and convert raw data into usable information for downstream applications.

### Data preparation

Operations typically involved in a data engineering process that transform the data.

### Data management

Solutions devised to organize, protect, store, access, and manipulate data.

> Data profiling fits here

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved. 5

---

# Data preparation tasks

- Data Profiling
- Data Structuring
- Data Enriching
- Data Cleaning

> Data preparation

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
6

---

# Importance of data profiling

- Ensure ingested data is “as expected”
- Understand main data characteristics
- Assess data utility using data characteristics
- Inspect data to validate and refine data transformation steps.
- Monitor essential data characteristics.

raw  
refined  
production  

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE  
Nanyang Technological University. All rights reserved.  
7

---

# DATA PROFILING TASKS

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
>
> Nanyang Technological University. All rights reserved.
>
> 8

---

# Intuitive data profiling introduction
(reminder)

- Examine and analyze data
  to create metadata (data
  about data).
- Metadata represent a
  summary of various
  characteristics of the data.
- These summaries help to
  assess usefulness and
  quality of data.

Simple examples:
- Number of rows
- Min and max values
- Number of missing values
- Outliers
- Data type
- Data format violations
- Histograms
- ...

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
9

---

# Downloaded file about registered voters

```

---

# Manual profiling example using Excel

Column headers

[ ] N
[ ] 10/01/1994
[ ] W
[ ] NL
[ ] UNA
[ ] F
[ ] 1995
[ ] 99 NY
[ ] N
[ ] 
[ ] 
[ ] 

<table>
    <tr>
        <th>X</th>
        <th>Y</th>
        <th>Z</th>
        <th>AA</th>
        <th>AB</th>
        <th>AC</th>
        <th>AD</th>
        <th>AE</th>
        <th>AF</th>
        <th>AG</th>
        <th>AH</th>
        <th>AI</th>
        <th>AJ</th>
    <th></th><th></th></tr>
    <tr>
        <td>code</td>
        <td>full_phone_number</td>
        <td>confidential_ind</td>
        <td>registr_dt</td>
        <td>race_code</td>
        <td>ethnic_code</td>
        <td>party_cd</td>
        <td>gender_code</td>
        <td>birth_year</td>
        <td>age_at_year_end</td>
        <td>birth_state</td>
        <td>drivers_lic</td>
        <td>precinct_abbrv</td>
        <td>precinct_desc</td>
        <td>municip</td>
    </tr>
    <tr>
        <td>1</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>2</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>3</td>
        <td></td>
        <td>N</td>
        <td>02/23/2018</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>F</td>
        <td>1978</td>
        <td>46 DC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td>MELVILLE 3</td>
        <td></td>
    </tr>
    <tr>
        <td>4</td>
        <td>27302</td>
        <td>N</td>
        <td>10/31/2020</td>
        <td>W</td>
        <td>UN</td>
        <td>REP</td>
        <td>M</td>
        <td>1966</td>
        <td>58 AL</td>
        <td>N</td>
        <td></td>
        <td>103</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>5</td>
        <td>27215</td>
        <td>3362291110 N</td>
        <td>03/26/1996</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>F</td>
        <td>1976</td>
        <td>48 NC</td>
        <td>Y</td>
        <td></td>
        <td>03SE</td>
        <td>SOUTH BOONE E</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>6</td>
        <td>27215</td>
        <td>2228834 N</td>
        <td>08/15/1989</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1945</td>
        <td>79 VA</td>
        <td>Y</td>
        <td></td>
        <td>124</td>
        <td>BURLINGTON 4</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>7</td>
        <td>27340</td>
        <td>2027443411 N</td>
        <td>03/07/2012</td>
        <td>W</td>
        <td>UN</td>
        <td>DEM</td>
        <td>M</td>
        <td>1948</td>
        <td>76 MA</td>
        <td>N</td>
        <td></td>
        <td>08N</td>
        <td>NORTH NEWLIN</td>
        <td></td>
    </tr>
    <tr>
        <td>8</td>
        <td>27215</td>
        <td>2529408167 N</td>
        <td>06/01/2020</td>
        <td>B</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1966</td>
        <td>58 NC</td>
        <td>Y</td>
        <td></td>
        <td>03SE</td>
        <td>SOUTH BOONE E</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>9</td>
        <td>27215</td>
        <td>3362291110 N</td>
        <td>10/10/1994</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>M</td>
        <td>1976</td>
        <td>48 NC</td>
        <td>Y</td>
        <td></td>
        <td>03SE</td>
        <td>SOUTH BOONE E</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>10</td>
        <td>27215</td>
        <td>3362228834 N</td>
        <td>12/05/2013</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>M</td>
        <td>1972</td>
        <td>52 VA</td>
        <td>Y</td>
        <td></td>
        <td>124</td>
        <td>BURLINGTON 4</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>11</td>
        <td>27215</td>
        <td>3362228834 N</td>
        <td>12/05/2013</td>
        <td>W</td>
        <td>HL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1975</td>
        <td>49</td>
        <td>N</td>
        <td></td>
        <td>124</td>
        <td>BURLINGTON 4</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>12</td>
        <td>27215</td>
        <td>3362228834 N</td>
        <td>06/06/1990</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>1944</td>
        <td>80 VA</td>
        <td>Y</td>
        <td></td>
        <td>124</td>
        <td>BURLINGTON 4</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>13</td>
        <td>27258</td>
        <td>3365789123 N</td>
        <td>08/18/1998</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>F</td>
        <td>1972</td>
        <td>52 NC</td>
        <td>Y</td>
        <td></td>
        <td>13</td>
        <td>HAW RIVER</td>
        <td>HAW</td>
    </tr>
    <tr>
        <td>14</td>
        <td>27258</td>
        <td>3362667615 N</td>
        <td>01/19/2006</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>1962</td>
        <td>62 WI</td>
        <td>Y</td>
        <td></td>
        <td>13</td>
        <td>HAW RIVER</td>
        <td>HAW</td>
    </tr>
    <tr>
        <td>15</td>
        <td>27253</td>
        <td>N</td>
        <td>05/06/2020</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>M</td>
        <td>1987</td>
        <td>37</td>
        <td>Y</td>
        <td></td>
        <td>06N</td>
        <td>NORTH GRAHAM</td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>16</td>
        <td>27253</td>
        <td>3362644972 N</td>
        <td>01/16/2009</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>1986</td>
        <td>38 NC</td>
        <td>Y</td>
        <td></td>
        <td>06N</td>
        <td>NORTH GRAHAM</td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>17</td>
        <td>27253</td>
        <td>3366757112 N</td>
        <td>06/12/2017</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>M</td>
        <td>1960</td>
        <td>64 LA</td>
        <td>Y</td>
        <td></td>
        <td>06N</td>
        <td>NORTH GRAHAM</td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>18</td>
        <td>27253</td>
        <td>3365127765 N</td>
        <td>12/02/2008</td>
        <td>W</td>
        <td>UN</td>
        <td>REP</td>
        <td>F</td>
        <td>1951</td>
        <td>73 NC</td>
        <td>Y</td>
        <td></td>
        <td>06N</td>
        <td>NORTH GRAHAM</td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>19</td>
        <td>27258</td>
        <td>N</td>
        <td>08/10/2018</td>
        <td>U</td>
        <td>UN</td>
        <td>REP</td>
        <td>U</td>
        <td>1959</td>
        <td>65</td>
        <td>Y</td>
        <td></td>
        <td>09N</td>
        <td>NORTH THOMPSON</td>
        <td></td>
    </tr>
    <tr>
        <td>20</td>
        <td>27253</td>
        <td>8133102051 N</td>
        <td>06/07/2024</td>
        <td>W</td>
        <td>UN</td>
        <td>REP</td>
        <td>F</td>
        <td>1950</td>
        <td>74 NY</td>
        <td>Y</td>
        <td></td>
        <td>09N</td>
        <td>NORTH THOMPSON</td>
        <td>SWE</td>
    </tr>
    <tr>
        <td>21</td>
        <td>27302</td>
        <td>9196327914 N</td>
        <td>11/01/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1970</td>
        <td>54</td>
        <td>Y</td>
        <td></td>
        <td>10N</td>
        <td>NORTH MELVILLE</td>
        <td>MEB</td>
    </tr>
    <tr>
        <td>22</td>
        <td>27253</td>
        <td>8133100652 N</td>
        <td>05/09/2023</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>1945</td>
        <td>79 NY</td>
        <td>Y</td>
        <td></td>
        <td>09N</td>
        <td>NORTH THOMPSON</td>
        <td>SWE</td>
    </tr>
    <tr>
        <td>23</td>
        <td>27302</td>
        <td>7049961866 N</td>
        <td>08/26/2016</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1990</td>
        <td>34 NC</td>
        <td>Y</td>
        <td></td>
        <td>10S1</td>
        <td>SOUTH MELVILLE</td>
        <td>MEB</td>
    </tr>
    <tr>
        <td>24</td>
        <td>27302</td>
        <td>N</td>
        <td>09/08/2016</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>M</td>
        <td>1989</td>
        <td>35 NC</td>
        <td>Y</td>
        <td></td>
        <td>10S1</td>
        <td>SOUTH MELVILLE</td>
        <td>MEB</td>
    </tr>
    <tr>
        <td>25</td>
        <td>27244</td>
        <td>9147724005 N</td>
        <td>10/04/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>DEM</td>
        <td>U</td>
        <td>2003</td>
        <td>21</td>
        <td>N</td>
        <td></td>
        <td>03N</td>
        <td>NORTH BOONE</td>
        <td>ELO</td>
    </tr>
    <tr>
        <td>26</td>
        <td>27258</td>
        <td>4302953995 N</td>
        <td>05/17/2023</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>F</td>
        <td>1967</td>
        <td>57 FL</td>
        <td>N</td>
        <td></td>
        <td>13</td>
        <td>HAW RIVER</td>
        <td></td>
    </tr>
    <tr>
        <td>27</td>
        <td>27215</td>
        <td>3365850666 N</td>
        <td>10/26/2012</td>
        <td>W</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1980</td>
        <td>44 FL</td>
        <td>Y</td>
        <td></td>
        <td>03C</td>
        <td>CENTRAL BOONE</td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>28</td>
        <td></td>
        <td>N</td>
        <td>03/30/2000</td>
        <td>A</td>
        <td>UN</td>
        <td>DEM</td>
        <td>F</td>
        <td>1952</td>
        <td>72 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>29</td>
        <td>27244</td>
        <td>4018353485 N</td>
        <td>10/11/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>U</td>
        <td>2004</td>
        <td>20</td>
        <td>N</td>
        <td></td>
        <td>035</td>
        <td>BOONE 5</td>
        <td>ELO</td>
    </tr>
    <tr>
        <td>30</td>
        <td>27249</td>
        <td>3366842638 N</td>
        <td>04/15/2021</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>2003</td>
        <td>21 NC</td>
        <td>Y</td>
        <td></td>
        <td>03W</td>
        <td>WEST BOONE</td>
        <td>GIB</td>
    </tr>
    <tr>
        <td>31</td>
        <td>27249</td>
        <td>3363398364 N</td>
        <td>12/09/2019</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>F</td>
        <td>2002</td>
        <td>22 NC</td>
        <td>Y</td>
        <td></td>
        <td>03W</td>
        <td>WEST BOONE</td>
        <td>GIB</td>
    </tr>
    <tr>
        <td>32</td>
        <td>27249</td>
        <td>3364499029 N</td>
        <td>05/14/1996</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>M</td>
        <td>1976</td>
        <td>48 NY</td>
        <td>Y</td>
        <td></td>
        <td>03W</td>
        <td>WEST BOONE</td>
        <td>GIB</td>
    </tr>
    <tr>
        <td>33</td>
        <td>27249</td>
        <td>N</td>
        <td>10/09/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>U</td>
        <td>1979</td>
        <td>45</td>
        <td>Y</td>
        <td></td>
        <td>03W</td>
        <td>WEST BOONE</td>
        <td>GIB</td>
    </tr>
</table>ncvoter1
Sheet1
+

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
11

---

# Manual profiling example using Excel

> Number of rows

<table>
    <tr>
        <th>county_id</th>
        <th>county_desc</th>
        <th>voter_reg_num</th>
        <th>ncid</th>
        <th>last_name</th>
        <th>first_name</th>
        <th>middle_name</th>
        <th>name_suffix_lbl</th>
        <th>status_cd</th>
        <th>voter_status_desc</th>
        <th>reason_cd</th>
        <th>voter_status_reason</th>
    </tr>
    <tr>
        <td>135487</td>
        <td>1 ALAMANCE</td>
        <td>9194677</td>
        <td>AA211067</td>
        <td>ZUNIGA CAMBERO</td>
        <td>ANAKAREN</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135488</td>
        <td>1 ALAMANCE</td>
        <td>9236267</td>
        <td>AA234180</td>
        <td>ZUNIGA CAMBERO</td>
        <td>NORA</td>
        <td>ELIA</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135489</td>
        <td>1 ALAMANCE</td>
        <td>9201310</td>
        <td>AA214486</td>
        <td>ZUNIGA FIERRO</td>
        <td>CHRISTIAN</td>
        <td>DENNIS</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135490</td>
        <td>1 ALAMANCE</td>
        <td>9206554</td>
        <td>BL513369</td>
        <td>ZUNIGA FIERRO</td>
        <td>JISSEL</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135491</td>
        <td>1 ALAMANCE</td>
        <td>9200517</td>
        <td>AA214045</td>
        <td>ZUNIGA HERRERA</td>
        <td>MIGUEL</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135492</td>
        <td>1 ALAMANCE</td>
        <td>9141392</td>
        <td>AA179328</td>
        <td>ZUPANCICH</td>
        <td>MONICA</td>
        <td>ANITA</td>
        <td></td>
        <td>I</td>
        <td>INACTIVE</td>
        <td>IN</td>
        <td>CONFIRMATION NO</td>
    </tr>
    <tr>
        <td>135493</td>
        <td>1 ALAMANCE</td>
        <td>9141406</td>
        <td>AA145791</td>
        <td>ZUPANCICH</td>
        <td>RONALD</td>
        <td>JAMES</td>
        <td>II</td>
        <td>I</td>
        <td>INACTIVE</td>
        <td>IN</td>
        <td>CONFIRMATION NO</td>
    </tr>
    <tr>
        <td>135494</td>
        <td>1 ALAMANCE</td>
        <td>9152399</td>
        <td>AA186234</td>
        <td>ZURIFF</td>
        <td>SOPHIE</td>
        <td>ANNA</td>
        <td></td>
        <td>I</td>
        <td>INACTIVE</td>
        <td>IU</td>
        <td>CONFIRMATION RET</td>
    </tr>
    <tr>
        <td>135495</td>
        <td>1 ALAMANCE</td>
        <td>9166564</td>
        <td>AA194726</td>
        <td>ZWELLING</td>
        <td>AMY</td>
        <td>MARIE</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135496</td>
        <td>1 ALAMANCE</td>
        <td>9230103</td>
        <td>AA230908</td>
        <td>ZWELLING</td>
        <td>JOEDIN</td>
        <td>SHEA</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135497</td>
        <td>1 ALAMANCE</td>
        <td>9187816</td>
        <td>AA206903</td>
        <td>ZWELLING</td>
        <td>PAUL</td>
        <td>J</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135498</td>
        <td>1 ALAMANCE</td>
        <td>9174660</td>
        <td>BN352594</td>
        <td>ZWICK</td>
        <td>MICHAEL</td>
        <td>TODD</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135499</td>
        <td>1 ALAMANCE</td>
        <td>9099472</td>
        <td>AA148089</td>
        <td>ZWIER</td>
        <td>ANDREW</td>
        <td>MICHAEL</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135500</td>
        <td>1 ALAMANCE</td>
        <td>9099260</td>
        <td>AA147942</td>
        <td>ZWIER</td>
        <td>CHRISTOPHER</td>
        <td>ANTHONY</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135501</td>
        <td>1 ALAMANCE</td>
        <td>9228255</td>
        <td>DK27494</td>
        <td>ZWIER</td>
        <td>JESSICA</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135502</td>
        <td>1 ALAMANCE</td>
        <td>9099261</td>
        <td>AA147943</td>
        <td>ZWIER</td>
        <td>KAREN</td>
        <td>JEAN</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135503</td>
        <td>1 ALAMANCE</td>
        <td>9217806</td>
        <td>DE289078</td>
        <td>ZWILLING</td>
        <td>JASON</td>
        <td>ERIC</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135504</td>
        <td>1 ALAMANCE</td>
        <td>9146897</td>
        <td>AA182983</td>
        <td>ZWINGELBERG</td>
        <td>ANNA</td>
        <td>MARIE</td>
        <td></td>
        <td>D</td>
        <td>DENIED</td>
        <td>DU</td>
        <td>VERIFICATION RETU</td>
    </tr>
    <tr>
        <td>135505</td>
        <td>1 ALAMANCE</td>
        <td>9176512</td>
        <td>BL455029</td>
        <td>ZYCZKIEWICZ</td>
        <td>DIANE</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135506</td>
        <td>1 ALAMANCE</td>
        <td>9196290</td>
        <td>DE247523</td>
        <td>ZYCZKIEWICZ</td>
        <td>KRISTINE</td>
        <td>MARIE</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135507</td>
        <td>1 ALAMANCE</td>
        <td>9196289</td>
        <td>AX71581</td>
        <td>ZYCZKIEWICZ</td>
        <td>RICHARD</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135508</td>
        <td>1 ALAMANCE</td>
        <td>9236502</td>
        <td>AA234296</td>
        <td>ZYLOWSKI</td>
        <td>PATRICIA</td>
        <td>ANN</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>135509</td>
        <td>1 ALAMANCE</td>
        <td>9161152</td>
        <td>AA191482</td>
        <td>ZYMECK</td>
        <td>JULIET</td>
        <td>LORE</td>
        <td></td>
        <td>I</td>
        <td>INACTIVE</td>
        <td>IU</td>
        <td>CONFIRMATION RET</td>
    </tr>
    <tr>
        <td>135510</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135511</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135512</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135513</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135514</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135515</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135516</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135517</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135518</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135519</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>ncvoter1 Sheet1 + 

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

Nanyang Technological University. All rights reserved. 12

---

# Manual profiling example using Excel

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
    </tr>
    <tr>
        <td>county_id</td>
        <td>county_desc</td>
        <td>voter_reg_num</td>
        <td>ncid</td>
        <td>last_name</td>
        <td>first_name</td>
        <td>middle_name</td>
        <td>name_suffix_lbl</td>
        <td>status_cd</td>
        <td>voter_status_desc</td>
        <td>reason_cd</td>
        <td>voter_status_reason_cd</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9005990</td>
        <td>AA56273</td>
        <td>AABEL</td>
        <td>RUTH</td>
        <td>EVELYN</td>
        <td></td>
        <td>REMOVED</td>
        <td>RD</td>
        <td>DECEASED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9178574</td>
        <td>AA201627</td>
        <td>AARDEN</td>
        <td>JONI</td>
        <td>AUTUMN</td>
        <td></td>
        <td>REMOVED</td>
        <td>RL</td>
        <td>MOVED FROM COUNTY</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9205561</td>
        <td>AA216996</td>
        <td>AARMSTRONG</td>
        <td>TIMOTHY</td>
        <td>DUANE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9048723</td>
        <td>AA98377</td>
        <td>AARON</td>
        <td>CHRISTINA</td>
        <td>CASTAGNA</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9019674</td>
        <td>AA69747</td>
        <td>AARON</td>
        <td>CLAUDIA</td>
        <td>HAYDEN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9129589</td>
        <td>AA170513</td>
        <td>AARON</td>
        <td>JAMES</td>
        <td>MICHAEL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9194595</td>
        <td>BM49306</td>
        <td>AARON</td>
        <td>KIMBERLY</td>
        <td>GREEN</td>
        <td></td>
        <td>INACTIVE</td>
        <td>IU</td>
        <td>CONFIRMATION RETURN</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9041748</td>
        <td>AA91549</td>
        <td>AARON</td>
        <td>NATHAN</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9144384</td>
        <td>AA125250</td>
        <td>AARON</td>
        <td>RICHARD</td>
        <td>BRIAN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9144385</td>
        <td>AA181361</td>
        <td>AARON</td>
        <td>SANDRA</td>
        <td>ESCOBAR</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9021947</td>
        <td>AA71983</td>
        <td>AARON</td>
        <td>WILLIE</td>
        <td>DALE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9062002</td>
        <td>AA111384</td>
        <td>AARONSON</td>
        <td>GENA</td>
        <td>HOLT</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9096423</td>
        <td>AA145641</td>
        <td>AARONSON</td>
        <td>MICHAEL</td>
        <td>CHARLES</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9194267</td>
        <td>AA210859</td>
        <td>AASEN</td>
        <td>ALEXANDER</td>
        <td>MACNAB</td>
        <td></td>
        <td>INACTIVE</td>
        <td>IN</td>
        <td>CONFIRMATION NOT RECEIVED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9121656</td>
        <td>AA165057</td>
        <td>ABADIE</td>
        <td>JACK</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9168958</td>
        <td>AA196147</td>
        <td>ABADIE</td>
        <td>JACK</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9118154</td>
        <td>AA162459</td>
        <td>ABADIE</td>
        <td>MYRA</td>
        <td>LYNN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9175986</td>
        <td>AA200312</td>
        <td>ABADIE</td>
        <td>WILLIAM</td>
        <td>EARL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AP</td>
        <td>VERIFICATION PENDING</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9233812</td>
        <td>AA233007</td>
        <td>ABAJIAN</td>
        <td>DEBORAH</td>
        <td>RUTH</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9242743</td>
        <td>BL377881</td>
        <td>ABAJIAN</td>
        <td>MICHELLE</td>
        <td>S</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9225186</td>
        <td>AA228074</td>
        <td>ABAJIAN</td>
        <td>ROBERT</td>
        <td>HAROLD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9160433</td>
        <td>CW803328</td>
        <td>ABASHIAN</td>
        <td>ASHLEY</td>
        <td>DENNY PARR</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9160854</td>
        <td>EH730361</td>
        <td>ABASHIAN</td>
        <td>MICHAEL</td>
        <td>DAVID</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9239089</td>
        <td>AA235710</td>
        <td>ABATEMARCO</td>
        <td>MEGAN</td>
        <td>REID</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9225335</td>
        <td>AA228157</td>
        <td>ABAZIED COOPER</td>
        <td>JOY</td>
        <td>GAYLE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9139919</td>
        <td>AA178336</td>
        <td>ABBAS</td>
        <td>JENNIFER</td>
        <td>ANN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9068460</td>
        <td>AA117728</td>
        <td>ABBAS</td>
        <td>RAFAT</td>
        <td></td>
        <td></td>
        <td>REMOVED</td>
        <td>RS</td>
        <td>MOVED FROM STATE</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9239920</td>
        <td>AA236185</td>
        <td>ABBATE</td>
        <td>MICHAEL</td>
        <td>EDWIN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9209221</td>
        <td>AA219101</td>
        <td>ABBATECOLA</td>
        <td>ANTHONY</td>
        <td>JOSEPH</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9189448</td>
        <td>AA207788</td>
        <td>ABBATECOLA</td>
        <td>JENNA</td>
        <td>CAMILLE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9049573</td>
        <td>AA99206</td>
        <td>ABBATECOLA</td>
        <td>RONALD</td>
        <td>JOSEPH</td>
        <td>JR</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9240574</td>
        <td>BY754441</td>
        <td>ABBATECOLA</td>
        <td>THOMAS</td>
        <td>PAUL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
</table>> **Distinct values**
>
> - (Select All)
> - A
> - D
> - I
> - R
> - S

ncvoter1 | Sheet1 | + | : 4

<table>
  <thead>
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
    </tr>
    <tr>
        <th>county_id</th>
        <th>county_desc</th>
        <th>voter_reg_num</th>
        <th>ncid</th>
        <th>last_name</th>
        <th>first_name</th>
        <th>middle_name</th>
        <th>name_suffix_lbl</th>
        <th>status_cd</th>
        <th>voter_status_desc</th>
        <th>reason_cd</th>
        <th>voter_status_reason_cd</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9005990</td>
        <td>AA56273</td>
        <td>AABEL</td>
        <td>RUTH</td>
        <td>EVELYN</td>
        <td></td>
        <td>REMOVED</td>
        <td>RD</td>
        <td>DECEASED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9178574</td>
        <td>AA201627</td>
        <td>AARDEN</td>
        <td>JONI</td>
        <td>AUTUMN</td>
        <td></td>
        <td>REMOVED</td>
        <td>RL</td>
        <td>MOVED FROM COUNTY</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9205561</td>
        <td>AA216996</td>
        <td>AARMSTRONG</td>
        <td>TIMOTHY</td>
        <td>DUANE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9048723</td>
        <td>AA98377</td>
        <td>AARON</td>
        <td>CHRISTINA</td>
        <td>CASTAGNA</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9019674</td>
        <td>AA69747</td>
        <td>AARON</td>
        <td>CLAUDIA</td>
        <td>HAYDEN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9129589</td>
        <td>AA170513</td>
        <td>AARON</td>
        <td>JAMES</td>
        <td>MICHAEL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9194595</td>
        <td>BM49306</td>
        <td>AARON</td>
        <td>KIMBERLY</td>
        <td>GREEN</td>
        <td></td>
        <td>INACTIVE</td>
        <td>IU</td>
        <td>CONFIRMATION RETURN</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9041748</td>
        <td>AA91549</td>
        <td>AARON</td>
        <td>NATHAN</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9144384</td>
        <td>AA125250</td>
        <td>AARON</td>
        <td>RICHARD</td>
        <td>BRIAN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9144385</td>
        <td>AA181361</td>
        <td>AARON</td>
        <td>SANDRA</td>
        <td>ESCOBAR</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9021947</td>
        <td>AA71983</td>
        <td>AARON</td>
        <td>WILLIE</td>
        <td>DALE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9062002</td>
        <td>AA111384</td>
        <td>AARONSON</td>
        <td>GENA</td>
        <td>HOLT</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9096423</td>
        <td>AA145641</td>
        <td>AARONSON</td>
        <td>MICHAEL</td>
        <td>CHARLES</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9194267</td>
        <td>AA210859</td>
        <td>AASEN</td>
        <td>ALEXANDER</td>
        <td>MACNAB</td>
        <td></td>
        <td>INACTIVE</td>
        <td>IN</td>
        <td>CONFIRMATION NOT RECEIVED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9121656</td>
        <td>AA165057</td>
        <td>ABADIE</td>
        <td>JACK</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9168958</td>
        <td>AA196147</td>
        <td>ABADIE</td>
        <td>JACK</td>
        <td>EDWARD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9118154</td>
        <td>AA162459</td>
        <td>ABADIE</td>
        <td>MYRA</td>
        <td>LYNN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9175986</td>
        <td>AA200312</td>
        <td>ABADIE</td>
        <td>WILLIAM</td>
        <td>EARL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AP</td>
        <td>VERIFICATION PENDING</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9233812</td>
        <td>AA233007</td>
        <td>ABAJIAN</td>
        <td>DEBORAH</td>
        <td>RUTH</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9242743</td>
        <td>BL377881</td>
        <td>ABAJIAN</td>
        <td>MICHELLE</td>
        <td>S</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9225186</td>
        <td>AA228074</td>
        <td>ABAJIAN</td>
        <td>ROBERT</td>
        <td>HAROLD</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9160433</td>
        <td>CW803328</td>
        <td>ABASHIAN</td>
        <td>ASHLEY</td>
        <td>DENNY PARR</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9160854</td>
        <td>EH730361</td>
        <td>ABASHIAN</td>
        <td>MICHAEL</td>
        <td>DAVID</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9239089</td>
        <td>AA235710</td>
        <td>ABATEMARCO</td>
        <td>MEGAN</td>
        <td>REID</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9225335</td>
        <td>AA228157</td>
        <td>ABAZIED COOPER</td>
        <td>JOY</td>
        <td>GAYLE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9139919</td>
        <td>AA178336</td>
        <td>ABBA</td>
        <td>JENNIFER</td>
        <td>ANN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9068460</td>
        <td>AA117728</td>
        <td>ABBA</td>
        <td>RAFAT</td>
        <td></td>
        <td></td>
        <td>REMOVED</td>
        <td>RS</td>
        <td>MOVED FROM STATE</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9239920</td>
        <td>AA236185</td>
        <td>ABBATE</td>
        <td>MICHAEL</td>
        <td>EDWIN</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9209221</td>
        <td>AA219101</td>
        <td>ABBATECOLA</td>
        <td>ANTHONY</td>
        <td>JOSEPH</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9189448</td>
        <td>AA207788</td>
        <td>ABBATECOLA</td>
        <td>JENNA</td>
        <td>CAMILLE</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9049573</td>
        <td>AA99206</td>
        <td>ABBATECOLA</td>
        <td>RONALD</td>
        <td>JOSEPH</td>
        <td>JR</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
    </tr>
    <tr>
        <td>1</td>
        <td>ALAMANCE</td>
        <td>9240574</td>
        <td>BY754441</td>
        <td>ABBATECOLA</td>
        <td>THOMAS</td>
        <td>PAUL</td>
        <td></td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td></td>
    </tr>
  </tbody>
</table>

---

# Manual profiling example using Excel

mail_city | mail_state | mail_zipcode | full_phone_number | confidential_ind | registr_dt | race_code | ethnic_code | party_cd | gender_code | birth_year | age_at_year_end | birth_state
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
1928 | MEBANE | NC | 27302 | | | W | NL | UNA | F | 1974 | 50 | NC
3560 | | | | | | W | NL | REP | F | 1932 | 92 | NC
5192 | BURLINGTON | NC | 27216 | 33 | | W | UN | REP | M | 1949 | 75 | NC
6176 | BURLINGTON | NC | 27215 | | | W | NL | DEM | F | 1929 | 95 | NC
6305 | SNOW CAMP | NC | 27349 | 33 | | W | NL | REP | M | 1971 | 53 | NC
7029 | | | | | | W | NL | DEM | M | 1938 | 86 | NC
7107 | GRAHAM | NC | 27253 | 33 | | W | NL | UNA | M | 1941 | 83 | NC
8376 | BURLINGTON | NC | 27217 | 33 | | W | NL | REP | M | 1984 | 40 | VA
11570 | | | | | | W | NL | DEM | F | 1930 | 94 | NC
12322 | BURLINGTON | NC | 27217 | | | W | NL | DEM | F | 1947 | 77 | NC
12354 | GRAHAM | NC | 27253 | 33 | | W | NL | REP | F | 1933 | 91 | NC
12855 | SNOW CAMP | NC | 27349 | 33 | | W | NL | UNA | F | 1941 | 83 | NC
13039 | GRAHAM | NC | 27253 | 33 | | B | UN | DEM | M | 1977 | 47 | NC
14373 | BURLINGTON | NC | 27215 | 33 | | W | NL | UNA | F | 1932 | 92 | SC
14589 | | | | | | W | NL | DEM | M | 1943 | 81 | NC
19633 | BURLINGTON | NC | 27215 | 33 | | W | NL | REP | F | 1937 | 87 | NC
20024 | BURLINGTON | NC | 27217 | 33 | | W | NL | DEM | M | 1942 | 82 | NC
20072 | HAW RIVER | NC | | | | W | NL | DEM | M | 1944 | 80 | NC
21780 | | | | | | W | NL | DEM | M | 1928 | 96 | PA
22026 | GRAHAM | NC | 253 | 33 | | B | NL | DEM | F | 2002 | 22 | VA
22936 | | | | | | W | NL | DEM | F | 1929 | 95 | NC
23877 | BURLINGTON | NC | 27215 | 33 | | W | NL | REP | F | 1938 | 86 | NC
24141 | ELON | NC | 27244 | | | W | NL | REP | M | 1939 | 85 | NC
24886 | | | | | | W | NL | UNA | F | 1939 | 85 | NC
25994 | MEBANE | | 27349 | | | W | NL | REP | M | 1945 | 79 | DC
27094 | SNOW CAMP | NC | | | | W | NL | REP | M | 1948 | 76 | NC
27755 | | | | | | W | NL | REP | F | 1932 | 92 | NC
27759 | N | | | | | W | UN | REP | M | 1929 | 95 | NC
29087 | N | | | | | W | NL | REP | F | 1928 | 96 | OC
29725 | BURLINGTON | NC | 27215 | 3362145254 | N | W | NL | REP | F | 1931 | 93 | NC
29731 | BURLINGTON | NC | 27215 | 0 | N | W | NL | REP | M | 1930 | 94 | NC
33457 | | | | | | W | NL | REP | F | 1939 | 85 | NC

- [ ] (Select All)
- [x] ###/###/####
- [ ] 01/01/1976
- [ ] 01/01/2019
- [ ] 01/01/2020
- [ ] 01/01/2021
- [ ] 01/01/2022
- [ ] 01/01/2023
- [ ] 01/01/2024
- Not all items showing

> Number of dummy values

- [ ] OK
- [ ] Cancel

oter1 | Sheet1 | + | : | 4
--- | --- | --- | --- | ---
Ready 135 of 135508 records found | Accessibility: Investigate | Count: 136 | Display Setti

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 14

---

# Manual profiling example using Excel

<table>
    <tr>
        <th>:thnic_code</th>
        <th>party_cd</th>
        <th>gender_code</th>
        <th>birth_year</th>
        <th>age_at_year_end</th>
        <th>birth_state</th>
        <th>drivers_lic</th>
        <th>precinct_abbrv</th>
        <th>precinct_desc</th>
        <th>municipality_abbrv</th>
        <th>municipality_desc</th>
        <th>ward_abbrv</th>
        <th>ward_desc</th>
        <th>cong_dist_abbr</th>
    </tr>
    <tr>
        <td>4 IN</td>
        <td>REP</td>
        <td>M</td>
        <td>1966</td>
        <td></td>
        <td>58 AL</td>
        <td>N</td>
        <td>103</td>
        <td>M</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>7 IN</td>
        <td>DEM</td>
        <td>M</td>
        <td>1948</td>
        <td></td>
        <td>76 MA</td>
        <td>N</td>
        <td>08N</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>19 IN</td>
        <td>REP</td>
        <td>U</td>
        <td>1959</td>
        <td></td>
        <td>65</td>
        <td>Y</td>
        <td>09N</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>26</td>
        <td>REP</td>
        <td>F</td>
        <td></td>
        <td>1967</td>
        <td>57 FL</td>
        <td>N</td>
        <td>13</td>
        <td>H</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>28 IN</td>
        <td>DEM</td>
        <td>F</td>
        <td>1952</td>
        <td></td>
        <td>72 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>35 IL</td>
        <td>REP</td>
        <td>M</td>
        <td>1968</td>
        <td></td>
        <td>56 NY</td>
        <td>Y</td>
        <td>07</td>
        <td>A</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>36 IL</td>
        <td>REP</td>
        <td>F</td>
        <td>1968</td>
        <td></td>
        <td>56 SC</td>
        <td>Y</td>
        <td>07</td>
        <td>A</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>37 IL</td>
        <td>REP</td>
        <td>M</td>
        <td>2000</td>
        <td></td>
        <td>24 NC</td>
        <td>N</td>
        <td>07</td>
        <td>A</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>40 IL</td>
        <td>UNA</td>
        <td>F</td>
        <td></td>
        <td>1996</td>
        <td>28 NJ</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>44 IL</td>
        <td>UNA</td>
        <td>M</td>
        <td>1968</td>
        <td></td>
        <td>56 OH</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>45 IL</td>
        <td>DEM</td>
        <td>M</td>
        <td>1955</td>
        <td></td>
        <td>69 NC</td>
        <td>Y</td>
        <td>127</td>
        <td>B</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>46 IN</td>
        <td>REP</td>
        <td>M</td>
        <td>1959</td>
        <td></td>
        <td>65 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td>S</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>48 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1952</td>
        <td></td>
        <td>72 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>51 IL</td>
        <td>UNA</td>
        <td>F</td>
        <td></td>
        <td>1983</td>
        <td>41 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td>S</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>54 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td></td>
        <td>1985</td>
        <td>39 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>56 IL</td>
        <td>REP</td>
        <td>M</td>
        <td>1978</td>
        <td></td>
        <td>46 NC</td>
        <td>Y</td>
        <td>02</td>
        <td>C</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>60 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>2001</td>
        <td></td>
        <td>23 PA</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>61 IL</td>
        <td>REP</td>
        <td>F</td>
        <td>1992</td>
        <td></td>
        <td>32 VA</td>
        <td>Y</td>
        <td>10N</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>62 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1953</td>
        <td></td>
        <td>71</td>
        <td>Y</td>
        <td>103</td>
        <td>M</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>63 IN</td>
        <td>UNA</td>
        <td>U</td>
        <td>1965</td>
        <td></td>
        <td>59</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>65 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1973</td>
        <td></td>
        <td>51 NC</td>
        <td>Y</td>
        <td>127</td>
        <td>B</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>86 IL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1991</td>
        <td></td>
        <td>33 NC</td>
        <td>Y</td>
        <td>10N</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>87 IL</td>
        <td>UNA</td>
        <td>M</td>
        <td>1962</td>
        <td></td>
        <td>62 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>88 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1959</td>
        <td></td>
        <td>65 CA</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>99 IL</td>
        <td>UNA</td>
        <td>M</td>
        <td>1964</td>
        <td></td>
        <td>60 NY</td>
        <td>Y</td>
        <td>08S</td>
        <td>A</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>101 IL</td>
        <td>UNA</td>
        <td>F</td>
        <td>1998</td>
        <td></td>
        <td>26 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td></td>
        <td>SOUTH THOMPSON</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>102 IN</td>
        <td>DEM</td>
        <td>U</td>
        <td></td>
        <td>1990</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>SOUTH THOMPSON</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>103 IL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1992</td>
        <td></td>
        <td>32 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td></td>
        <td>SOUTH THOMPSON</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>105 IL</td>
        <td>REP</td>
        <td>M</td>
        <td></td>
        <td></td>
        <td></td>
        <td>Y</td>
        <td>035</td>
        <td></td>
        <td>BOONE 5</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>106 IL</td>
        <td>DEM</td>
        <td>M</td>
        <td>1965</td>
        <td></td>
        <td>59 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td></td>
        <td>SOUTH THOMPSON</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>107 IL</td>
        <td>REP</td>
        <td>M</td>
        <td>1996</td>
        <td></td>
        <td>28 NC</td>
        <td>Y</td>
        <td>09S</td>
        <td></td>
        <td>SOUTH THOMPSON</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>108 IL</td>
        <td>REP</td>
        <td>M</td>
        <td>1989</td>
        <td></td>
        <td>35 NC</td>
        <td>Y</td>
        <td>035</td>
        <td></td>
        <td>BOONE 5</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>110 IN</td>
        <td></td>
        <td></td>
        <td>1981</td>
        <td></td>
        <td>43</td>
        <td>Y</td>
        <td>06S</td>
        <td></td>
        <td>SOUTH GRAHAM</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>> Number of missing values

- A↓ Sort A to Z
- Z↓ Sort Z to A
- Sort by Color
- Sheet View
- Clear Filter From "municipality_abbrv"
- Filter by Color
- Text Filters
- Search
  - [ ] ELO
  - [ ] GIB
  - [ ] GRA
  - [ ] GRE
  - [ ] HAW
  - [ ] MEB
  - [ ] OSS
  - [ ] SWE
  - [x] (Blanks)
- OK
- Cancel

Ready 59100 of 135508 records found Accessibility: Investigate
NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 15

---

# Manual profiling example using Excel

> NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE

<table>
    <tr>
        <th>X</th>
        <th>Y</th>
        <th>Z</th>
        <th>AA</th>
        <th>AB</th>
        <th>AC</th>
        <th>AD</th>
        <th>AE</th>
        <th>AF</th>
        <th>AG</th>
        <th>AH</th>
        <th>AI</th>
        <th>AJ</th>
        <th>AK</th>
    </tr>
    <tr>
        <td>full_phone_number</td>
        <td>confidential_ind</td>
        <td>registr_dt</td>
        <td>race_code</td>
        <td>ethnic_code</td>
        <td>party_cd</td>
        <td>gender_code</td>
        <td>birth_year</td>
        <td>age_at_year_end</td>
        <td>birth_state</td>
        <td>drivers_lic</td>
        <td>precinct_abbrv</td>
        <td>precinct_desc</td>
        <td>municipality_ab</td>
    </tr>
    <tr>
        <td>3362277017 N</td>
        <td>N</td>
        <td>11/02/2004</td>
        <td>W</td>
        <td>UN</td>
        <td>REP</td>
        <td>F</td>
        <td>1909</td>
        <td>115 NC</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>05/11/1946</td>
        <td>B</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1911</td>
        <td>113 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>10/02/2008</td>
        <td>B</td>
        <td>UN</td>
        <td>DEM</td>
        <td>F</td>
        <td>1911</td>
        <td>113 NC</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>10/28/1950</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>F</td>
        <td>1911</td>
        <td>113 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>10/06/1986</td>
        <td>B</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1913</td>
        <td>111 NC</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>10/26/1956</td>
        <td>U</td>
        <td>NL</td>
        <td>DEM</td>
        <td>M</td>
        <td>1914</td>
        <td>110 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>06/24/1994</td>
        <td>W</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1915</td>
        <td>109 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>04/20/1968</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td></td>
        <td>1915</td>
        <td>109 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>11/08/2016</td>
        <td>U</td>
        <td>UN</td>
        <td>DEM</td>
        <td></td>
        <td>1915</td>
        <td>109 NC</td>
        <td>Y</td>
        <td>10S1</td>
        <td>SOUTH MELVILLE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>10/06/2016</td>
        <td>U</td>
        <td>UN</td>
        <td>REP</td>
        <td></td>
        <td>1916</td>
        <td>108 MA</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>09/21/2016</td>
        <td>W</td>
        <td>UN</td>
        <td>UN</td>
        <td>F</td>
        <td>1916</td>
        <td>108 VA</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>05/14/1960</td>
        <td>B</td>
        <td>NL</td>
        <td></td>
        <td></td>
        <td>1916</td>
        <td>108 NC</td>
        <td>N</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>06/20/2000</td>
        <td>W</td>
        <td>NL</td>
        <td></td>
        <td>M</td>
        <td>1916</td>
        <td>108 IN</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>09/13/2016</td>
        <td>W</td>
        <td>NL</td>
        <td></td>
        <td>F</td>
        <td>1916</td>
        <td>108 PA</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>N</td>
        <td>05/17/1952</td>
        <td>W</td>
        <td>NL</td>
        <td>DEM</td>
        <td>F</td>
        <td>1916</td>
        <td>108 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135494</td>
        <td>3363802385 N</td>
        <td>05/28/2024</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>M</td>
        <td>2006</td>
        <td>18 NY</td>
        <td>Y</td>
        <td>11</td>
        <td>PLEASANT GROVE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135495</td>
        <td>3362636795 N</td>
        <td>06/13/2024</td>
        <td>U</td>
        <td>HL</td>
        <td>UNA</td>
        <td>F</td>
        <td>2006</td>
        <td>18</td>
        <td>Y</td>
        <td>064</td>
        <td>GRAHAM 4</td>
        <td></td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>135496</td>
        <td>5512327930 N</td>
        <td>01/05/2024</td>
        <td>B</td>
        <td>UN</td>
        <td></td>
        <td>M</td>
        <td>2006</td>
        <td>18 PA</td>
        <td>Y</td>
        <td>1210</td>
        <td>BURLINGTON 10</td>
        <td></td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>135497</td>
        <td>N</td>
        <td>09/13/2024</td>
        <td>W</td>
        <td>NL</td>
        <td></td>
        <td>F</td>
        <td>2006</td>
        <td>18</td>
        <td>Y</td>
        <td>03N</td>
        <td>NORTH BOONE</td>
        <td></td>
        <td>ELO</td>
    </tr>
    <tr>
        <td>135498</td>
        <td>3365163246 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td></td>
        <td>M</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>07</td>
        <td>ALBRIGHT</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135499</td>
        <td>3362601958 N</td>
        <td>08/29/2024</td>
        <td>W</td>
        <td>UN</td>
        <td>UN</td>
        <td>M</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>10S1</td>
        <td>SOUTH MELVILLE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135500</td>
        <td>9193049069 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td></td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135501</td>
        <td>N</td>
        <td>08/25/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td></td>
        <td>2006</td>
        <td>18</td>
        <td>Y</td>
        <td></td>
        <td>SOUTH MELVILLE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135502</td>
        <td>3362662530 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>F</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>03W</td>
        <td>WEST BOONE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135503</td>
        <td>3365241260 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>M</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>05</td>
        <td>FAUCETTE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135504</td>
        <td>3362788618 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td></td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>08S</td>
        <td>SOUTH NEWLIN</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135505</td>
        <td>3365346144 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>HL</td>
        <td>UNA</td>
        <td>F</td>
        <td>2006</td>
        <td>18 WI</td>
        <td>Y</td>
        <td>03SM</td>
        <td>SOUTH BOONE M</td>
        <td></td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>135506</td>
        <td>3363435524 N</td>
        <td>01/05/2024</td>
        <td>O</td>
        <td>UN</td>
        <td>DEM</td>
        <td>F</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>06E</td>
        <td>EAST GRAHAM</td>
        <td></td>
        <td>GRA</td>
    </tr>
    <tr>
        <td>135507</td>
        <td>3362703926 N</td>
        <td>09/12/2024</td>
        <td>W</td>
        <td>UN</td>
        <td>UNA</td>
        <td>F</td>
        <td>2006</td>
        <td>18 NC</td>
        <td>Y</td>
        <td>125</td>
        <td>BURLINGTON 5</td>
        <td></td>
        <td>BUR</td>
    </tr>
    <tr>
        <td>135508</td>
        <td>3365679723 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>UNA</td>
        <td>M</td>
        <td>2006</td>
        <td>18 MI</td>
        <td>Y</td>
        <td>13</td>
        <td>HAW RIVER</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135509</td>
        <td>6153103615 N</td>
        <td>01/05/2024</td>
        <td>W</td>
        <td>NL</td>
        <td>REP</td>
        <td>F</td>
        <td>2006</td>
        <td>18 NY</td>
        <td>Y</td>
        <td>11</td>
        <td>PLEASANT GROVE</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135510</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>135511</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>Min/max values

Nanyang Technological University. All rights reserved.
16

---

# Manual profiling example using Excel

<table>
    <tr>
        <th>first_name</th>
        <th>middle_name</th>
        <th>name_suffix_lbl</th>
        <th>status_cd</th>
        <th>voter_status_desc</th>
        <th>reason_cd</th>
        <th>voter_status_reason_desc</th>
        <th>res_street_address</th>
        <th>res_city_desc</th>
        <th>state_cd</th>
    </tr>
    <tr>
        <td>RUTH</td>
        <td>EVELYN</td>
        <td></td>
        <td>R</td>
        <td>REMOVED</td>
        <td>RD</td>
        <td>DECEASED</td>
        <td>REMOVED</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>JONI</td>
        <td>AUTUMN</td>
        <td></td>
        <td>R</td>
        <td>REMOVED</td>
        <td>RL</td>
        <td>MOVED FROM COUNTY</td>
        <td>REMOVED</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>TIMOTHY</td>
        <td>DUANE</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>3670 COVINGTON TRL</td>
        <td>MEBANE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>WILLIE</td>
        <td>DALE</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>1013 EDITH ST</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>CLAUDIA</td>
        <td>HAYDEN</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>1013 EDITH ST</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>JAMES</td>
        <td>MICHAEL</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>5608 OLD CHEROKEE LN</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>KIMBERLY</td>
        <td>GREEN</td>
        <td></td>
        <td></td>
        <td>INACTIVE</td>
        <td>IU</td>
        <td>CONFIRMATION RETURNED UNDELIVERABLE</td>
        <td>187 CAVALIER WAY #104</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>RICHARD</td>
        <td>BRIAN</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>1013 EDITH ST</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>SANDRA</td>
        <td>ESCOBAR</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>1013 EDITH ST</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>CHRISTINA</td>
        <td>CASTAGNA</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>421 WHITT AVE</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>NATHAN</td>
        <td>EDWARD</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>421 WHITT AVE</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MICHAEL</td>
        <td>CHARLES</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>107 TERRYWOOD CT</td>
        <td>HAW RIVER</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>GENA</td>
        <td>HOLT</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>107 TERRYWOOD CT</td>
        <td>HAW RIVER</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>ALEXANDER</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>CONFIRMATION NOT RETURNED</td>
        <td>1286 PYRTLE DR</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MYRA</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFICATION PENDING</td>
        <td>612 SIDEVIEW ST</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>WILLIAM</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>3562 S NC HWY 119</td>
        <td>HAW RIVER</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>JACK</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>612 SIDEVIEW ST</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>JACK</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>612 SIDEVIEW ST</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>ROBERT</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>2220 CRESCENT DR</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>DEBORAH</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>2220 CRESCENT DR</td>
        <td>GRAHAM</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MICHELLE</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>201 E CENTER ST #205</td>
        <td>MEBANE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MICHAEL</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>975 SWEET GUM WAY</td>
        <td>MEBANE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>ASHLEY</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>975 SWEET GUM WAY</td>
        <td>MEBANE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MEGAN</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>204 WOODALE DR</td>
        <td>ELON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>JOY</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>1414 TERRYWOOD RD #307</td>
        <td>HAW RIVER</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>RAFAT</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>MOVED FROM STATE</td>
        <td>REMOVED</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>JENNIFER</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>3027 TRUITT DR</td>
        <td>BURLINGTON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>MICHAEL</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>3223 BILL LOY DR</td>
        <td>ELON</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>TRACY</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>504 BROOKFIELD DR</td>
        <td>GIBSONVILLE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>RONALD</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>VERIFIED</td>
        <td>504 BROOKFIELD DR</td>
        <td>GIBSONVILLE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>THOMAS</td>
        <td></td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>250 OBSIDIUM CT</td>
        <td>GIBSONVILLE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>JENNA</td>
        <td>CAMILLE</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>504 BROOKFIELD DR</td>
        <td>GIBSONVILLE</td>
        <td>NC</td>
    </tr>
    <tr>
        <td>ANTHONY</td>
        <td>JOSEPH</td>
        <td></td>
        <td>A</td>
        <td>ACTIVE</td>
        <td>AV</td>
        <td>VERIFIED</td>
        <td>504 BROOKFIELD DR</td>
        <td>GIBSONVILLE</td>
        <td>NC</td>
    </tr>
</table>> **Value distribution**

<table>
  <thead>
    <tr>
        <th>VOTER_STATUS_REASON_DESC_STATISTICS</th>
        <th></th>
    </tr>
    <tr>
        <th>ADMINISTRATIVE NOT RETURNED</th>
        <th>0</th>
    </tr>
    <tr>
        <th>CONFIRMATION PENDING</th>
        <th>1</th>
    </tr>
    <tr>
        <th>CONFIRMATION RETURNED...</th>
        <th>10</th>
    </tr>
    <tr>
        <th>DECEASED</th>
        <th>6339</th>
    </tr>
    <tr>
        <th>FELONY CONVICTION</th>
        <th>77</th>
    </tr>
    <tr>
        <th>MOVED FROM COUNTY</th>
        <th>4228</th>
    </tr>
    <tr>
        <th>MOVED FROM STATE</th>
        <th>8394</th>
    </tr>
    <tr>
        <th>OVERSEAS CITIZEN</th>
        <th>262</th>
    </tr>
    <tr>
        <th>REMOVED AFTER 2 FED...</th>
        <th>57</th>
    </tr>
    <tr>
        <th>REQUEST FROM VOTER</th>
        <th>1454</th>
    </tr>
    <tr>
        <th>TEMPORARY REGISTRANT</th>
        <th>1222</th>
    </tr>
    <tr>
        <th>UNAVAILABLE ESSENTIAL...</th>
        <th>171</th>
    </tr>
    <tr>
        <th>UNVERIFIED...</th>
        <th>121</th>
    </tr>
    <tr>
        <th>VERIFICATION PENDING</th>
        <th>996</th>
    </tr>
    <tr>
        <th>VERIFICATION RETURNED...</th>
        <th>167</th>
    </tr>
    <tr>
        <th>VERIFIED</th>
        <th>342</th>
    </tr>
    <tr>
        <th>VERIFICATION...</th>
        <th>34</th>
    </tr>
    <tr>
        <th>VERIFIED</th>
        <th>4510</th>
    </tr>
    <tr>
        <th>VERIFIED...</th>
        <th>2298</th>
    </tr>
    <tr>
        <th>104772</th>
        <th></th>
    </tr>
  </thead>
</table>

Nanyang Technological University. All rights reserved.
17

---

# Manual profiling example using Excel

> Dependencies among columns (if reason_cd = "DI", then voter_status_desc = "DENIED")

<table>
    <tr>
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
    </tr>
    <tr>
        <td>1</td>
        <td>last_name</td>
        <td>first_name</td>
        <td>middle_name</td>
        <td>name_suffix_lbl</td>
        <td>status_cd</td>
        <td>voter_status_desc</td>
        <td>reason_cd</td>
        <td>voter_status_reason_desc</td>
        <td>res_street_address</td>
    </tr>
    <tr>
        <td>311</td>
        <td>05378</td>
        <td>ADAMS</td>
        <td>PAUL</td>
        <td>WENDELL</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1426 CLOVERDALE ST</td>
    </tr>
    <tr>
        <td>622</td>
        <td>04302</td>
        <td>AGNEW</td>
        <td>MATTHEW</td>
        <td>PATRICK</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>615 TRACY DR</td>
    </tr>
    <tr>
        <td>664</td>
        <td>14513</td>
        <td>AGUIAR</td>
        <td>ROGELIO</td>
        <td>LOPEZ</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>310 N IRELAND ST</td>
    </tr>
    <tr>
        <td>727</td>
        <td>17943</td>
        <td>AHERN</td>
        <td>KATHLEEN</td>
        <td>MARY</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1720 ST MARK'S CHURCH RD</td>
    </tr>
    <tr>
        <td>1224</td>
        <td>13639</td>
        <td>ALESSANDRO</td>
        <td>GUY</td>
        <td>THOMAS</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>600 N MARSHALL ST</td>
    </tr>
    <tr>
        <td>1912</td>
        <td>07109</td>
        <td>ALLISON</td>
        <td>LARRY</td>
        <td>DONNELL</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>425 KERNODLE DR</td>
    </tr>
    <tr>
        <td>3137</td>
        <td>10544</td>
        <td>ANDRES</td>
        <td>KEITH</td>
        <td>CHARLES</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>108 FLORENCE ST</td>
    </tr>
    <tr>
        <td>3341</td>
        <td>14169</td>
        <td>ANGE</td>
        <td>JOSEPH</td>
        <td>FENNER</td>
        <td>JR</td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>4315 NC HWY 54</td>
    </tr>
    <tr>
        <td>3749</td>
        <td>13749</td>
        <td>ARGENTO</td>
        <td>JANIE</td>
        <td>CAROL</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>5533A KIMESVILLE RD</td>
    </tr>
    <tr>
        <td>5244</td>
        <td>05417</td>
        <td>BAILIFF</td>
        <td>JAMIE</td>
        <td>CATES</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1507 TARLETON AVE</td>
    </tr>
    <tr>
        <td>5466</td>
        <td>12314</td>
        <td>BAKER</td>
        <td>JOSHUA</td>
        <td>KEITH</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1400 ROSLYN DR</td>
    </tr>
    <tr>
        <td>6010</td>
        <td>14173</td>
        <td>BANKS</td>
        <td>DALE</td>
        <td>CHRISTOPHER</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>206 N FISHER ST</td>
    </tr>
    <tr>
        <td>6972</td>
        <td>00661</td>
        <td>BARTLETT</td>
        <td>DAVID</td>
        <td>WAYNE</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>4135 PREACHER HOLMES RD</td>
    </tr>
    <tr>
        <td>7116</td>
        <td>13139</td>
        <td>BASS</td>
        <td>KITTY</td>
        <td>R</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>110 EASTGATE DR</td>
    </tr>
    <tr>
        <td>7273</td>
        <td>6220</td>
        <td>BATRES</td>
        <td>RICHARD</td>
        <td>A</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1903 MALONE RD</td>
    </tr>
    <tr>
        <td>7282</td>
        <td>2616</td>
        <td>BATTEN</td>
        <td>MICHAEL</td>
        <td>LYNN</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>2404 N CHURCH ST</td>
    </tr>
    <tr>
        <td>7623</td>
        <td>3562</td>
        <td>BEANE</td>
        <td>RICKY</td>
        <td>EVERETTE</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1721 MEBANE OAKS RD</td>
    </tr>
    <tr>
        <td>7934</td>
        <td>04614</td>
        <td>BEEKER</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>149 CUTLER TR</td>
    </tr>
    <tr>
        <td>8041</td>
        <td>2628</td>
        <td>BELFIELD</td>
        <td>MARY</td>
        <td>E</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>103 ANTIOCH AVE</td>
    </tr>
    <tr>
        <td>8189</td>
        <td>12351</td>
        <td>BELLAMY</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>453 QUINTAS AVE</td>
    </tr>
    <tr>
        <td>8341</td>
        <td>04115</td>
        <td>BENES</td>
        <td>MICHAEL</td>
        <td>WILLIAM</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>219 MOFFITT HALL</td>
    </tr>
    <tr>
        <td>8561</td>
        <td>5668</td>
        <td>BENO</td>
        <td>JOEL</td>
        <td>MARTIN</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>404 S FLANNER ST</td>
    </tr>
    <tr>
        <td>9055</td>
        <td>3572</td>
        <td>BIALLY</td>
        <td>KATHLEEN</td>
        <td>M</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>3508 GARDEN RD</td>
    </tr>
    <tr>
        <td>9419</td>
        <td>9281</td>
        <td>BISCHOF</td>
        <td>BRIAN</td>
        <td>E</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>417 WESTHAMPTON DR</td>
    </tr>
    <tr>
        <td>9558</td>
        <td>06730</td>
        <td>BLACK</td>
        <td>JERRY</td>
        <td>LEE</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>734 BURLINGTON AVE</td>
    </tr>
    <tr>
        <td>9687</td>
        <td>01489</td>
        <td>BLACKMAN</td>
        <td>TERESA</td>
        <td>ANN</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>645 GUNN ST</td>
    </tr>
    <tr>
        <td>9939</td>
        <td>02088</td>
        <td>BLAIR</td>
        <td>LISA</td>
        <td>REGINA</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>847 TROLLINGWOOD-HAWF</td>
    </tr>
    <tr>
        <td>9979</td>
        <td>14360</td>
        <td>BLAKE</td>
        <td>JON</td>
        <td>STEWART</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1528 S MEBANE ST</td>
    </tr>
    <tr>
        <td>10031</td>
        <td>18109</td>
        <td>BLALOCK</td>
        <td>KATHY</td>
        <td>JEAN</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>206 N FISHER ST</td>
    </tr>
    <tr>
        <td>10463</td>
        <td>12374</td>
        <td>BODENHEIMER</td>
        <td>ROBERT</td>
        <td>WAYNE</td>
        <td>JR</td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>1116 HILLSIDE DR</td>
    </tr>
    <tr>
        <td>10511</td>
        <td>7209</td>
        <td>BOGER</td>
        <td>TRACY</td>
        <td>CAPPS</td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>306 BROAD ST</td>
    </tr>
    <tr>
        <td>11598</td>
        <td>03474</td>
        <td>BOWENS</td>
        <td>DERRICK</td>
        <td></td>
        <td></td>
        <td></td>
        <td>DI</td>
        <td>UNAVAILABLE ESSENTIAL INFORMATION</td>
        <td>606 S MEBANE ST</td>
    </tr>
</table>- Sheet2
- ncvoter1
- Sheet1

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 18

---

# Manual profiling example using Excel

Many more interesting questions about the dataset:
- Possible keys?
- Functional dependencies between columns?
- Correlations between columns?
- Frequent patterns in columns?

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 19

---

# Definition of data profiling

- “Data profiling is the process of examining the data available in an existing data source [...] and collecting statistics and information about that data.”
  > Wikipedia 01/2025
- “Data profiling refers to the activity of creating small but informative summaries of a database.”
  > Ted Johnson, Encyclopedia of Database Systems

> Data profiling is the set of activities and processes to determine the metadata about a given dataset.

We cover a fixed set of data profiling tasks and their results.

---

<table>
  <caption>Classification of standard profiling tasks</caption>
  <thead>
    <tr>
      <th>Root</th>
      <th>Scope</th>
      <th>Task Category</th>
      <th>Specific Task / Variation</th>
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
Nanyang Technological University. All rights reserved. 21

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
Nanyang Technological University. All rights reserved. 22

---

# Single-column vs. multi-column

## Single column profiling

- Most basic form of data profiling
- Assumption: All values are of same type
- Assumption: All values have some common properties that are to be discovered
- Often part of the basic statistics gathered by DBMS
- Complexity: Number of values/rows

> **Single column**
>
> - Cardinalities
> - Patterns and data types
> - Value distributions

Nanyang Technological University. All rights reserved. 23

---

# Running example for single column profiling

- Relies on [ydata Profiling](https://docs.profiling.ydata.ai/latest/)
- Integrates into Python Notebooks
- Example exploration of the [Titanic Dataset](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)
- Full ydata Profiling report for this dataset available on the [ydata examples page](https://docs.profiling.ydata.ai/latest/getting-started/examples/).

> Excerpt of Titanic Dataset

```latex
\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|l|}
\hline
PassengerId & Survived & Pclass & Name & Sex & Age & SibSp & Parch & Ticket & Fare & Cabin \\
\hline
1 & 0 & 3 & Braund, Mr. Owen Harris & male & 22 & 1 & 0 & A/5 21171 & 7.25 & \\
\hline
2 & 1 & 1 & Cumings, Mrs. John Bradley (Florence Briggs Thayer) & female & 38 & 1 & 0 & PC 17599 & 71.2833 & C85 \\
\hline
3 & 1 & 3 & Heikkinen, Miss. Laina & female & 26 & 0 & 0 & STON/O2. 3101282 & 7.925 & \\
\hline
4 & 1 & 1 & Futrelle, Mrs. Jacques Heath (Lily May Peel) & female & 35 & 1 & 0 & 113803 & 53.1 & C123 \\
\hline
5 & 0 & 3 & Allen, Mr. William Henry & male & 35 & 0 & 0 & 373450 & 8.05 & \\
\hline
6 & 0 & 3 & Moran, Mr. James & male & & 0 & 0 & 330877 & 8.4583 & \\
\hline
7 & 0 & 1 & McCarthy, Mr. Timothy J & male & 54 & 0 & 0 & 17463 & 51.8625 & E46 \\
\hline
8 & 0 & 3 & Palsson, Master. Gosta Leonard & male & 2 & 3 & 1 & 349909 & 21.075 & \\
\hline
9 & 1 & 3 & Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg) & female & 27 & 0 & 2 & 347742 & 11.1333 & \\
\hline
10 & 1 & 2 & Nasser, Mrs. Nicholas (Adele Achem) & female & 14 & 1 & 0 & 237736 & 30.0708 & \\
\hline
11 & 1 & 3 & Sandstrom, Miss. Marguerite Rut & female & 4 & 1 & 1 & PP 9549 & 16.7 & G6 \\
\hline
12 & 1 & 1 & Bonnell, Miss. Elizabeth & female & 58 & 0 & 0 & 113783 & 26.55 & C103 \\
\hline
13 & 0 & 3 & Saundercock, Mr. William Henry & male & 20 & 0 & 0 & A/5. 2151 & 8.05 & \\
\hline
\end{tabular}
```

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
24

---

# Cardinalities

- Number of values
- Number of distinct values
- Number of NULLs
- MIN, MAX, MEDIAN, AVG value
- Applications: data understanding, attribute assessment, attribute categorization, query optimization

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 25

---

# Cardinalities

> Cardinalities for the Age Attribute

- **Age**
  - Real number (R)
  - Missing
    - [x] Missing
- **Age**

<table>
    <tr>
        <td>**Distinct**</td>
        <td>88</td>
    </tr>
    <tr>
        <td>**Distinct (%)**</td>
        <td>12.3%</td>
    </tr>
    <tr>
        <td>**Missing**</td>
        <td>177</td>
    </tr>
    <tr>
        <td>**Missing (%)**</td>
        <td>19.9%</td>
    </tr>
    <tr>
        <td>**Infinite**</td>
        <td>0</td>
    </tr>
    <tr>
        <td>**Infinite (%)**</td>
        <td>0.0%</td>
    </tr>
    <tr>
        <td>**Mean**</td>
        <td>29.699118</td>
    </tr>
    <tr>
        <td></td>
    <td></td></tr>
    <tr>
        <td>**Minimum**</td>
        <td>0.42</td>
    </tr>
    <tr>
        <td>**Maximum**</td>
        <td>80</td>
    </tr>
    <tr>
        <td>**Zeros**</td>
        <td>0</td>
    </tr>
    <tr>
        <td>**Zeros (%)**</td>
        <td>0.0%</td>
    </tr>
    <tr>
        <td>**Negative**</td>
        <td>0</td>
    </tr>
    <tr>
        <td>**Negative (%)**</td>
        <td>0.0%</td>
    </tr>
    <tr>
        <td>**Memory size**</td>
        <td>7.1 KiB</td>
    </tr>
</table>Number of distinct values
Number of missing values
MIN, MAX, MEAN Age
...

> High number of missing values may be a problem for age-related analysis.

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 26

---

# Data types and value patterns

- String vs. number
- String vs. number vs. date
- Categorical vs. continuous
- SQL data types
  - CHAR, INT, DECIMAL, TIMESTAMP, BIT, CLOB, ...
- Domains
  - VARCHAR(12) vs. VARCHAR(13)
- XML data types (even more fine grained)
- Regular expressions
  - (\d{3})-(\d{3})-(\d{4})-(\d+)
- Semantic domains
  - Address, phone, email, first name
- Applications: data understanding, data modeling, attribute categorization, query optimization

> Increasing difficulty

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 27

---

# Data types and value patterns

> Variable types impact how the attributes are to be handled prior / during analysis.

- **Age**
  - Real number (R)
  - Missing
  - Distinct
  - Distinct (%)
  - Missing
  - Missing (%)
  - Infinite
  - Infinite (%)
  - Mean

- **Embarked**
  - Categorical
  - Distinct
  - 3

- **Dataset statistics**
  - Number of variables: 12
  - Number of observations: 891
  - Missing cells: 866
  - Missing cells (%): 8.1%

- **Variable types**
  - Numeric: 5
  - Categorical: 4
  - Text: 3

> Summary of detected types

NANYANG TECHNOLOGIC

28

---

# Numeric distributions

- Probability distribution for numeric values
- Detect whether data follows some well-known distribution
  - Determine that distribution function for data values
- If no specific/useful function detectable: histograms



<table>
  <caption>Numeric Distributions: Laplace and Normal Probability Density Functions</caption>
  <thead>
    <tr>
      <th rowspan="2">X-axis Value</th>
      <th colspan="4">Laplace Distributions</th>
      <th colspan="4">Normal Distributions</th>
    </tr>
    <tr>
      <th>&mu;=0, b=1</th>
      <th>&mu;=0, b=2</th>
      <th>&mu;=0, b=4</th>
      <th>&mu;=-5, b=4</th>
      <th>&mu;=0, &sigma;&sup2;=0.2</th>
      <th>&mu;=0, &sigma;&sup2;=1.0</th>
      <th>&mu;=0, &sigma;&sup2;=5.0</th>
      <th>&mu;=-2, &sigma;&sup2;=0.5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>-10</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.04</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>-8</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.06</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>-6</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.10</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>-5</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.125</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>-4</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>0.10</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.04</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>-3</td>
      <td>0.02</td>
      <td>0.06</td>
      <td>0.06</td>
      <td>0.08</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.07</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>0.07</td>
      <td>0.09</td>
      <td>0.08</td>
      <td>0.06</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>0.12</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>-1</td>
      <td>0.18</td>
      <td>0.15</td>
      <td>0.10</td>
      <td>0.05</td>
      <td>0.07</td>
      <td>0.24</td>
      <td>0.16</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0.50</td>
      <td>0.25</td>
      <td>0.125</td>
      <td>0.04</td>
      <td>0.89</td>
      <td>0.40</td>
      <td>0.18</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.18</td>
      <td>0.15</td>
      <td>0.10</td>
      <td>0.03</td>
      <td>0.07</td>
      <td>0.24</td>
      <td>0.16</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.07</td>
      <td>0.09</td>
      <td>0.08</td>
      <td>0.02</td>
      <td>0.01</td>
      <td>0.05</td>
      <td>0.12</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.02</td>
      <td>0.06</td>
      <td>0.06</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.07</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.01</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.04</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.04</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.01</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.00</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>



Laplace distributions



<table>
  <caption>Normal distributions</caption>
  <thead>
    <tr>
      <th>$x$</th>
      <th>$\mu=0, \sigma^2=0.2$</th>
      <th>$\mu=0, \sigma^2=1.0$</th>
      <th>$\mu=0, \sigma^2=5.0$</th>
      <th>$\mu=-2, \sigma^2=0.5$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>-5</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>-4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.05</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>-3</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.10</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>-2</td>
      <td>0.00</td>
      <td>0.05</td>
      <td>0.15</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>-1</td>
      <td>0.07</td>
      <td>0.24</td>
      <td>0.17</td>
      <td>0.21</td>
    </tr>
    <tr>
      <td>0</td>
      <td>0.89</td>
      <td>0.40</td>
      <td>0.18</td>
      <td>0.01</td>
    </tr>
    <tr>
      <td>1</td>
      <td>0.07</td>
      <td>0.24</td>
      <td>0.17</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.00</td>
      <td>0.05</td>
      <td>0.15</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.10</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.05</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.02</td>
      <td>0.00</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 29

---

# Histograms

- Determine (and display) value frequencies for value intervals or for individual values
- Estimation of probability distribution for continuous variables
- Applications: Query optimization, outlier detection, visualization

distribution of height of 2 durum wheat varieties


<table>
  <caption>distribution of height of 2 durum wheat varieties</caption>
  <thead>
    <tr>
      <th>height</th>
      <th>Ixos (nbr of plants)</th>
      <th>Primadur (nbr of plants)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>20-30</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <td>30-40</td>
      <td>15</td>
      <td>0</td>
    </tr>
    <tr>
      <td>40-50</td>
      <td>12</td>
      <td>0</td>
    </tr>
    <tr>
      <td>50-60</td>
      <td>40</td>
      <td>0</td>
    </tr>
    <tr>
      <td>60-70</td>
      <td>65</td>
      <td>0</td>
    </tr>
    <tr>
      <td>70-80</td>
      <td>85</td>
      <td>0</td>
    </tr>
    <tr>
      <td>80-90</td>
      <td>135</td>
      <td>0</td>
    </tr>
    <tr>
      <td>90-100</td>
      <td>225</td>
      <td>2</td>
    </tr>
    <tr>
      <td>100-110</td>
      <td>315</td>
      <td>5</td>
    </tr>
    <tr>
      <td>110-120</td>
      <td>415</td>
      <td>10</td>
    </tr>
    <tr>
      <td>120-130</td>
      <td>510</td>
      <td>25</td>
    </tr>
    <tr>
      <td>130-140</td>
      <td>540</td>
      <td>55</td>
    </tr>
    <tr>
      <td>140-150</td>
      <td>495</td>
      <td>95</td>
    </tr>
    <tr>
      <td>150-160</td>
      <td>430</td>
      <td>175</td>
    </tr>
    <tr>
      <td>160-170</td>
      <td>330</td>
      <td>275</td>
    </tr>
    <tr>
      <td>170-180</td>
      <td>225</td>
      <td>365</td>
    </tr>
    <tr>
      <td>180-190</td>
      <td>125</td>
      <td>480</td>
    </tr>
    <tr>
      <td>190-200</td>
      <td>65</td>
      <td>545</td>
    </tr>
    <tr>
      <td>200-210</td>
      <td>30</td>
      <td>510</td>
    </tr>
    <tr>
      <td>210-220</td>
      <td>12</td>
      <td>430</td>
    </tr>
    <tr>
      <td>220-230</td>
      <td>8</td>
      <td>400</td>
    </tr>
    <tr>
      <td>230-240</td>
      <td>2</td>
      <td>275</td>
    </tr>
    <tr>
      <td>240-250</td>
      <td>0</td>
      <td>135</td>
    </tr>
    <tr>
      <td>250-260</td>
      <td>0</td>
      <td>90</td>
    </tr>
    <tr>
      <td>260-270</td>
      <td>0</td>
      <td>65</td>
    </tr>
    <tr>
      <td>270-280</td>
      <td>0</td>
      <td>35</td>
    </tr>
    <tr>
      <td>280-290</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <td>290-300</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>


Image source: (https://www.census.gov/)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
30

---

# Histograms



<table>
  <caption>Histogram for the numerical attribute Fare: Histogram with fixed size bins (bins=50)</caption>
  <thead>
    <tr>
      <th>Fare Range (approximate)</th>
      <th>Frequency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0 - 10</td>
      <td>340</td>
    </tr>
    <tr>
      <td>10 - 20</td>
      <td>185</td>
    </tr>
    <tr>
      <td>20 - 30</td>
      <td>150</td>
    </tr>
    <tr>
      <td>30 - 40</td>
      <td>50</td>
    </tr>
    <tr>
      <td>40 - 50</td>
      <td>15</td>
    </tr>
    <tr>
      <td>50 - 60</td>
      <td>40</td>
    </tr>
    <tr>
      <td>60 - 70</td>
      <td>18</td>
    </tr>
    <tr>
      <td>70 - 80</td>
      <td>30</td>
    </tr>
    <tr>
      <td>80 - 90</td>
      <td>18</td>
    </tr>
    <tr>
      <td>90 - 100</td>
      <td>2</td>
    </tr>
    <tr>
      <td>100 - 110</td>
      <td>8</td>
    </tr>
    <tr>
      <td>110 - 120</td>
      <td>7</td>
    </tr>
    <tr>
      <td>120 - 130</td>
      <td>0</td>
    </tr>
    <tr>
      <td>130 - 140</td>
      <td>7</td>
    </tr>
    <tr>
      <td>140 - 150</td>
      <td>9</td>
    </tr>
    <tr>
      <td>150 - 160</td>
      <td>0</td>
    </tr>
    <tr>
      <td>160 - 170</td>
      <td>2</td>
    </tr>
    <tr>
      <td>170 - 200</td>
      <td>0</td>
    </tr>
    <tr>
      <td>200 - 210</td>
      <td>4</td>
    </tr>
    <tr>
      <td>210 - 220</td>
      <td>0</td>
    </tr>
    <tr>
      <td>220 - 230</td>
      <td>4</td>
    </tr>
    <tr>
      <td>230 - 240</td>
      <td>0</td>
    </tr>
    <tr>
      <td>240 - 250</td>
      <td>2</td>
    </tr>
    <tr>
      <td>250 - 260</td>
      <td>6</td>
    </tr>
    <tr>
      <td>260 - 510</td>
      <td>0</td>
    </tr>
    <tr>
      <td>510 - 520 (Outlier)</td>
      <td>3</td>
    </tr>
  </tbody>
</table>



NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE Nanyang Technological University. All rights reserved. 31

---

# Computational complexity

- All single-column profiling tasks require to scan the data of a table once.
- While reading in each row, variables or data structures are updated, from which the final result is derived.
- Computational dependency depends on the number of values / rows.
- This is considered easy :)

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 32

---

# Next week preview:

- Multiple columns
  - Uniqueness
  - Inclusion Dependencies
  - Functional dependencies

> Multi-column profiling

- Discover joint properties
- Discover dependencies
- Complexity: Number of columns and number of values

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved. 33

---

# References and credits

- Joseph M. Hellerstein, Tye Rattenbury, Jeffrey Heer, Sean Kandel, Connor Carreras. Principles of Data Wrangling. O’Reilly Media. 2017 – Chapter 4
- Ziawasch Abedjan, Lukasz Golab, Felix Naumann: Profiling relational data: a survey. VLDB J. 24(4): 557-581 (2015)
- Slides partially based on slides shared by Felix Naumann, Hasso-Plattner-Institut Potsdam, Germany

NANYANG TECHNOLOGICAL UNIVERSITY | SINGAPORE
Nanyang Technological University. All rights reserved.
34