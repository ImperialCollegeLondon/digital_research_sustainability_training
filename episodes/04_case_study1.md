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
a Python package (hosted on PyPI) with a novel data analysis technique relevant to
her research area.
The package has been a big success and has been widely adopted. However,
she has heard from some users that they are using it on increasingly large datasets that
leads to demanding memory requirements and slow performance.

Celia is concerned about the environmental impact of her software package.
She wants to assess the carbon emissions associated with both the development
and usage of her package and identify ways to reduce these emissions.

To begin with, Celia identifies the sources of carbon emissions associated with her work
and categorises them under the GHG protocol.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Scope of the Emissions

Under which scope would the following activities from Celia's work be categorised?

- Emissions from electricity usage of the hardware used for software development.
- Embedded emissions from hardware used for software development.
- Use of services such as GitHub Actions and AI Coding agents.
- Electricity usage when users of the package run the code.

:::::::::::::::::::::::: solution

- Scope 2
- Scope 3
- Scope 3
- Scope 3

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Celia should assess the balance of emissions involved in development of the code
base versus its usage. She should look at how to estimate these then focus her
emission reduction measures appropriately.

## Collecting Information

Celia decides to learn more about each of the emission sources.

- She primarily works on her laptop to develop the software package. In a week, she
spends around 20 hours on the software development.

- Embedded emissions associated with her laptop:

| Component | Emissions (kg CO2e) |
|-----------|---------------------|
| CPU       | 50                  |
| GPU       | 30                  |
| RAM       | 20                  |

- To ensure that her software package follows best practices, she has been using
GitHub Actions for continuous integration and testing. At present, there are around
5 workflows that run on GitHub Actions, and they run around 10 times a day.
She makes a list of these workflows and their runtimes:

| Workflow Name | Runtime (seconds) |
|---------------|-------------------|
| docs          | 10               |
| check-links   | 8                |
| upgrade-dependencies  | 6                |
| auto-merge    | 20               |
| ci            | 5                |

- Celia uses AI coding agents to create inline documentation for her code. She
estimates that she spends around 2 hours a week using these agents.

- To find an estimate of the users of her package, Celia looks at the
package download statistics on PyPI. There are around 200 downloads per month.
(can also refer to [clickpy](https://github.com/ClickHouse/clickpy)). From this,
she estimates that the electricity usage when users run the package is
around 100 kWh per month.

## Analysis

Celia tracks the activities for a week.

- Electricity used by the laptop when it is used for 20 hrs per week for software
development is 2? kWh per week.

- Total embedded emissions from the laptop (CPU + GPU + RAM) is 100 kg CO2e.

- Five workflows on GitHub Actions run (10 X 7) 70 times a week.
Total runtime of these workflows is (10 + 8 + 6 + 20 + 5) * 70 = 2940 seconds per week.

- AI coding agents are used for 2 hours per week.

- Electricity usage by users of her package is around 100 kWh per month.

## Taking Action

After Celia has identified the emissions sources associated
with the development and usage of her software package, she takes some measures
to reduce these emissions.

### Reducing Scope 2 emissions

- Optimising the code base to reduce the computational resources and runtime of its use.
- She uses [codecarbon](https://github.com/mlco2/codecarbon) to estimate and track
carbon emissions from her laptop during the future development of the package.

### Reducing Scope 3 emissions

- Producing documentation for users to help them make the most efficient use possible of
her code.
- Reducing the use of services such as GitHub Actions. She reduces the matrix of tests,
to only include the OS and Python versions that her package intends to support.

::::::::::::::::::::::::::::::::::::: keypoints

- Research software development can have significant environmental impacts.
- Measuring and estimating carbon emissions from research software development
  is important for identifying areas for improvement.

::::::::::::::::::::::::::::::::::::::::::::::::
