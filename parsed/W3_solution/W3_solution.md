# SC3021 Excercises: Computational vs Data Science Thinking

> Sample Solution for Week 3 Tutorial

## 1 Computational Thinking

Consider the problem of listing the distinct values in the list of numbers $L = [2, 4, 3, 2, 3]$ in the order of their first occurrence. That is, the result should be $[2, 4, 3]$.

Apply Computational Thinking to develop an algorithm that solves that problem. Exemplify each step of the computational thinking process for the above example problem. Your answer should be analogous to the example discussion of the kaya toast problem discussed during the lecture. Note that there may be multiple correct solutions for each stage, you may limit to one for each step. However, the steps should be coherent as a whole.

### 1.1 Decomposition

A step by step procedure that decomposes the specific problem into individual steps may look as follows.

- Start by reading in value 2.
- Add 2 to list of distinct numbers because it is the first time it is read.
- Proceed with reading value 4.
- Add 4 to list of distinct numbers because it is the first time it is read.
- Proceed with reading value 3.
- Add 3 to list of distinct numbers because it is the first time it is read.
- Proceed with reading value 2.
- Do nothing, because value 2 has already been read.
- Proceed with reading value 3.
- Do nothing, because value 3 has already been read.
- Return the final list of distinct number $[2, 4, 3]$.

---

# 1.2 Pattern recognition

In the step by step decomposition, we recognize the following patterns:

- Whenever a number is read that has not been seen before, it is recorded as a distinct value.
- Whenever a number is read that has been seen before, nothing needs to be done.
- Checking case 1 or 2 above needs to be repeated for every number that is read.

# 1.3 Abstraction

The following problems are examples of problems that are similar to the initial example problem and that can be solved analogously, leveraging the same patterns that have been recognized on the decomposed problem.

- Same procedure for different lists of numbers
- Same procedure for different ordered data structures (e.g., arrays instead of lists)
- Same procedure for different types of data (e.g., strings, dates)

# 1.4 Algorithm design

The following pseudo-code defines a general algorithm to solve the example problem (and similar ones).

Data: ordered data structure $S$  
Result: ordered data structure $S'$  
$S' \leftarrow []$;  
/* input and output are generalized based on abstraction */  
foreach value $v_i$ at position $i$ ranging from 0 to $|S|$ do  
    /* The body of the loop exploits the patterns (1) and (2) */  
    if $v_i$ is not contained in $S'$ then  
        append $v_i$ to $S'$;  
    end  
end  
return $S'$;

---

# 2 Data Science Thinking

Consider the following data science problem:

How can I free some space on my phone?

Apply Data Science thinking to develop a solution to that problem. Exemplify each step of the data science thinking process for the above example problem. Your answer should be analogous to the example discussion of the sprint training plan optimization discussed during the lecture. Note that there may be multiple correct solutions for each step, you may limit to one for each step. However, the steps should be coherent as a whole.

## 2.1 Ask

Ask may result in the refined question “Recommend files to be removed in order to free space on a phone.” This clarifies the type of analysis (recommendation) and focuses on a specific method to free space (i.e., deletion as opposed to compression).

## 2.2 Prepare

As a result of preparation, we obtain a table that is filled with data extracted from the file system and that stores information about individual files, including the file size, creation date, last access date, share status, label, type of file, file path.

## 2.3 Process

After the processing stage, we have a table that is enriched with additional information about personal relevance / use / preferences with respect to file paths and labels. For instance, file path to Downloads folder or /tmp may have low personal relevance (used as data dump) while label “#doNotDelete” can be flagged as highly relevant.

## 2.4 Analyze

Based on the features described previously and relying on both statistics and machine learning, the analysis outputs a ranked list of files that are recommended for deletion.

## 2.5 Share

The recommendations are displayed to the user as a list of files, using a similar visualization as the standard file explorer. The user can select a subset of the files to delete to get a real-time visualization of how much space the deletion of the selected files would free.

## 2.6 Act

After review of the files recommended for deletion and the potential effect on memory usage, the user decides which files to delete and proceeds with deletion.