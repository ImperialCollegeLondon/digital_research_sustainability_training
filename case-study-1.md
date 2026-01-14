---
title: 'Case Study: Researcher'
teaching: 10
exercises: 2
---

:::::::::::::::::::::::::::::::::::::: questions

- What tools and resources could help estimate emissions associated
   with software development and usage in the given scenario?
- What emission reduction measures would you suggest based on an
   assessment of the emissions sources in the given scenario?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Understand how to identify Scope 2 and Scope 3 emissions sources
  associated with software development and usage.
- Suggest appropriate emission reduction measures
   based on an assessment of emissions sources.
- Identify tools and resources to help estimate emissions
   associated with software development and usage.

::::::::::::::::::::::::::::::::::::::::::::::::

## Scenario

Celia is a researcher. Two years ago, she developed and released a Python package
with a novel data analysis technique relevant to her research area. The package
has been a big success and has been widely adopted. She has heard from some users
that they are using it on increasingly large datasets that leads to demanding
memory requirements and slow performance.

### Scope 2 Emissions Sources

- Emissions from electricity usage of the hardware used for software development.

### Scope 3 Emissions Sources

- Embedded emissions from hardware used for software development.
- Use of services such as GitHub Actions and AI Coding agents.
- Electricity usage of computational resources running the code.

Celia should assess the balance of emissions involved in development of the code
base versus its usage. She should look at how to estimate these then focus her
emission reduction measures appropriately.

Depending on the outcome she should look at measures such as:

- Reducing the use of services such as GitHub Actions.
- Optimising the code base to reduce the computational resources and runtime of its use.
- Producing documentation for users to help them make the most efficient use possible of
her code.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

Inline instructor notes can help inform instructors of timing challenges
associated with the lessons. They appear in the "Instructor View"

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Can you do it?

What is the output of this command?

```r
paste("This", "new", "lesson", "looks", "good")
```

:::::::::::::::::::::::: solution

## Output

```output
[1] "This new lesson looks good"
```

:::::::::::::::::::::::::::::::::

## Challenge 2: how do you nest solutions within challenge blocks?

:::::::::::::::::::::::: solution

You can add a line with at least three colons and a `solution` tag.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

## Figures

You can use pandoc markdown for static figures with the following syntax:

`![optional caption that appears below the figure](figure url){alt='alt text for
accessibility purposes'}`

## Math

One of our episodes contains $\LaTeX$ equations when describing how to create
dynamic reports with {knitr}, so we now use mathjax to describe this:

`$\alpha = \dfrac{1}{(1 - \beta)^2}$` becomes: $\alpha = \dfrac{1}{(1 - \beta)^2}$

Cool, right?

::::::::::::::::::::::::::::::::::::: keypoints

- Identify tools and resources to help estimate emissions
  associated with software development and usage.
- Identify Scope 2 and Scope 3 emissions sources associated with software
  development and usage.

::::::::::::::::::::::::::::::::::::::::::::::::
