title: R Basics
description: Chapter 1 from "Advanced R"
published: 2021-01-11
authour: James M

## Chapter 1

## Questions

1. What are the properties of a vector other than its contents?
    - Three common properties
      - type `typeof()`   
      - length `length()`
      - attributes `attributes()`

2. What are the four common types of atomic vectors? What are the two rare types?
    - logical `is.logical()` and `as.logical()` [logical R Documentation](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/logical)
    - double `is.double()` and `as.double` [double R documentation](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/double)
    - character `is.character()` and `as.character()` [character R documentation](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/character)
    - integer `is.integer()` and `as.integer()` [integer R documentation](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/integer)
    - complex, raw

3. What are attributes and how to you get and set them?
    - Attributes allow extra metadata to be associated with an object using `attr(x, "y"` and `attr(x, "y") <- value` or get and set all attributes at once with `attributes()`.
    - [attributes R documentation](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/attributes)

4. How is a list different from an atomic vector? How is a matrix different from a Data Frame?
    - Elements of a list can be of any type, even a list whereas an atomic vector all the elements must be of the same type.
    - The elements of a matrix can be different types whereas a data frame must have the same types in each of the columns.

5. Can you have a list that is a matrix? Can a Data Frame have a column that is a matrix?
    - You can make a "list-array" by assuming a dimensionless list. It is possible to make a matrix a column of a data frame `data.frame(x = I(matrix()))`.


------

The basic Data structure in R is a vector - they come in **Atomic Vectors** and **Lists**.

`typeof()` ## what it is

`length()` ## How many elements it contains

`attributes()` ## additional arbitrary metadata


#### Atomic Vectors

[Vector Explaination](https://renenyffenegger.ch/notes/development/languages/R/data-structures/vector/)

##### Four kinds
- logical (true/ false)
- integer (numbers without decimals)
- double (numbers with decimals)
- character (strings/ words)


```{r}
dbl_var <- c(1,1.5,2.5)

int_var <- c(1L, 2.5L, 5L) ## with the L suffix there is an integer rather than a double

log_var <- c(TRUE, FALSE, TRUE, T, F)

chr_var <- c("these are some words", "these are some other words", "strings are 'words'.")

```

- Notes
  - Atomic vectors are always flat, even if you nest `c()`'s e.g `c(1,c(1,3.4))` is the same as `c(1,2,3.4)`
  - Missing values are replaced with `NA` which is a logical vector of '1'.

##### Types and Tests

```{r}
typeof(dbl_var)
```

```{r}
is.atomic(log_var)
```
```{r}
is.double(dbl_var)
```
```{r}
is.numeric(dbl_var)
```
##### Coercion

All elements of a vector must be of the same type.

If they aren't then they will be coerced into the most flexible type.

```{r}
str(c(1,"a")) ## integers and strings combine to form 'character' vectors
```

 When a logical vector is coerced to integer or double, `TRUE = 1` and `FALSE = 0`. Often used in conjunction with `sum()` and `mean()`.

```{r}
x <- c(TRUE, FALSE, TRUE, FALSE, FALSE, TRUE)
typeof(x)
sum(x) ## total number of 'TRUE's
as.numeric(x)
mean(x) ## Proportion that are 'TRUE'
```

 If there is any chance of confusion specifically coerce a vector to another type with:

 - `as.logical`
 - `as.integer`
 - `as.character`
 - `as.double`

 ---
#### Lists
Lists are different to vectors because the elements in them can be of any type. List can contain any variable type, vectors, matrices, functions and even lists themselves.

Some useful information on lists is at this [link](https://www.datamentor.io/r-programming/list/).

lists don't have dimensions - this means that `dim()` will return a NULL (as below).

```{r}
y <- list(1:3, "a", c(TRUE, F, T, F,F,T,T), c(2,3,4,5,6))
str(y)
dim(y)
```

Even though the `dim()` function doesn't work `nrow()` and `ncol` will give some details of a list.

List can be called *recursive* vectors because a list can contain other lists - this is the fundamental difference between lists and vectors.

```{r}
z <- list(list(list(list(1:5))))
str(z)
is.recursive(z)
```

`c()` will combine several lists into one. If given a combination of atomic vectors `c()` will coerce the lists to vector before combining them.

```{r}
a <- list(1:3, list(c(4:7)))
b <- c(list(1:3), c(4:7))
str(a)
str(b)

```

Notes:

- `typeof()` a list is list
- testing for a list is `is.list()`
- coerce to a list with `as.list()`
- turn a list into an atomic vector with `unlist()`. The same coercion rules are used for `as.list()` as for `unlist()`.

Both Data frames `as.data.frame()` and the outputs for a linear model objects `lm()` are built from lists.

### Attributes

All objects have a arbitrary additional attributes, used to store metadata about the object.

Some common attributes are in the table below:

- class     - the class of the object
- comment   - a comment on the object, often a description of what it means
- dim       - dimensions of the object
- dimnames  - names associated with each dimension of the object
- names     - names attribute of the object
- row.names - the name of each row of an object
- col.names - the name of each column of an object
- tsp       - the start time for an object
- levels    - levels of a factor

You can get a list of all the attributes of ran object by `attributes()`.

The `structure()` will return the structure of the object. Remember, attributes

```{r}
attr(a, "my_attribute") <- "This is a list" ## insert a comment on a list - set an attribute

attributes(a) ## inspect the attributes of the list
str(attributes(a)) ## get the attributes for the list, only the single one for the list. Note it returns a list itself of the attributes.

structure(b) ## returns the structure for the object

```

By default, most attributes are lost when modifying a vector. The only attributes lost are the three most important:

1. Names
2. Dimensions
3. Class

#### Names
You can name a vector in three ways:

- When creating it
- By modifying an existing vector in place
- By creating a modified copy of an existing vector

Names should be unique to facilitate character sub-setting.

You can unname a vector by `unname()` or remove all names in place `names() <- NULL`

#### Factors

A factor is a vector that can only have predefined values and is used to store categorical data. Factors a built on top of integer vector using two attributes:

- `class()` "factor" which makes them behave differently
- `levels()` which defines the set of allowed values

```{r}
l <- factor(c("a", "b", "c", "a"))
l
class(l)
levels(l)
```

Using a factor instead of a character vector makes it obvious when some groups contain no observations.

Most data loading automatically turns characters to factors, this is suboptimal. To stop this behavior use `stringsAsFactors = FALSE` then manually convert the characters to factors with your knowledge of the data. Factor look like characters but they are actually integers. It's better to explicitly change characters to factors and factors to characters.

### Matrices and Arrays

Adding a `dim()` attribute to a vector allows it to perform like a multi-dimensional *array*. A special case of an array is a **Matrix**, it has two dimensions. Matrices are used for statistics, arrays are rarer.   


```{r}
e <- matrix(1:6,ncol = 3, nrow = 2) ## two scalar arguments to specify rows and columns
e
f <- array(1:12, c(2,3,2)) ## one argument to describe all dimensions
f
g <- 1:6
dim(g) <- c(3,2) ## modify an object in place
g
```

`length()` generalises to `nrow()` and `ncol()` for matrices, and `dim()` for arrays.

`names()` generalises to `rownames()` and `colnames()` for matrices, and `dimnames()`, a list of character vectors for arrays.

`c()` generalises to `cbind()` and `rbind()` for matrices and `abind()` for arrays.

To test or a matrix using `is.matrix()` and an array using `is.array()` or by looking at the length of the `dim()`. `as.martix()` and `as.array()` make it easy to trun vectors into either a matirx or an array.

Vectors are the only one dimensional data structure. Atomic vectors are most commonly turned into matrices, the dimension attribute can be set on a list to make list-matrices and list-arrays.

### Data Frames

A data frame is the most common way of storing data in R. Tidy data is the basis for making data analysis easier. A data frame is a list of equal length vectors, this makes it a two dimension data strcture. It shares the properties of both a matrix and the list.

A data frame has `names()`, `rownames()` and `colnames()`, names and colnames are the same thing. The length of a dataframe is the length of the underliying list so it is the same as `nccol()`; `nrow()` gives the number of rows.

#### Creation of Data Frames

You can create a data frame with `data.frame()`, which takes named vectors a input.

```{r}
df <- data.frame(x = 1:3,y = c("a", "b", "c"))
df
str(df)
```

Data frame is an S3 class, its type reflects the underlying vector used to build it: the list. To test if something is a data frame use `class()` or test explicitly with `is.data.frame()`.

```{r}
typeof(df)
class(df)
is.data.frame(df)
```

It is possible to coerce an object with `as.data.frame()`. The following rules apply:

  - A vector will create a one column data frame
  - A list will create one column for each element; it's an error if they are not all the same length
  - A matrix will create a data frame with the same number of columns and rows as the matrix.

It is possible to combine data frames with `cbind()` and `rbind()`:

  - When combining column wise (`cbind()`) the number of rows must match but row names are igniored.
  - When combining row wise (`rbind()`) both the number and names of the cloumn must match
  - Use `plyr::rbind.fill()` to combine data frames that done have the same columns
  - If you try to create a data frame by `cbind()`ing vectors together a matrix is created - use `data.frame()` instead. -- the extension is to make sure that when using `cbind()` all the columns types are the same.
