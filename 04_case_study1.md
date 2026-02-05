---
title: 'Case Study 1 - Researcher'
teaching: 20
exercises: 10
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the sustainability considerations related to research software development?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative research case study relating to research software development.
- Explore ways to measure and estimate carbon emissions from research software development.
- Explore ways to reduce the carbon emissions associated with a given workload.

::::::::::::::::::::::::::::::::::::::::::::::::

## Scenario

Celia is a researcher in a university. Two years ago, she developed and released
a Python package with a novel data analysis technique relevant to her research area. She
had the chance to travel internationally for conducting a workshop based on her package
at a conference. The package has been a big success and has been widely adopted. However,
she has heard from some users that they are using it on increasingly large datasets that
leads to demanding memory requirements and slow performance.

Celia is concerned about the environmental impact of her software package.
She wants to assess the carbon emissions associated with both the development
and usage of her package and identify ways to reduce these emissions.

To begin with, Celia identifies the sources of carbon emissions associated with her work
and categorises them under the GHG protocol.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Scope 2 Emissions

What Scope 2 emissions under the GHG protocol can you identity from Celia's work?

:::::::::::::::::::::::: solution

- Emissions from electricity usage of the hardware used for software development.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Identify Scope 3 Emissions

What Scope 3 emissions under the GHG protocol can you identity from Celia's work?

:::::::::::::::::::::::: solution

- Embedded emissions from hardware used for software development.
- Use of services such as GitHub Actions and AI Coding agents.
- Electricity usage when users of the package run the code.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Celia should assess the balance of emissions involved in development of the code
base versus its usage. She should look at how to estimate these then focus her
emission reduction measures appropriately.

## Suggested Approach

After Celia has identified the Scope 2 and Scope 3 emissions sources associated
with the development and usage of her software package, she could take some measures
to reduce these emissions.

### Reducing Scope 2 emissions

- Optimising the code base to reduce the computational resources and runtime of its use.

### Reducing Scope 3 emissions

- Producing documentation for users to help them make the most efficient use possible of
her code.
- Reducing the use of services such as GitHub Actions.

::::::::::::::::::::::::::::::::::::: keypoints

- Research software development can have significant environmental impacts.
- Measuring and estimating carbon emissions from research software development
  is important for identifying areas for improvement.

::::::::::::::::::::::::::::::::::::::::::::::::
