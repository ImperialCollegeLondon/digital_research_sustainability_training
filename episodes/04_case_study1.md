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

- Embedded emissions associated with her laptop. She looks the Product Carbon
 Footprint (PCF) data sheet for her laptop and finds the following information:

| Component | Emissions (kg CO2e) |
|-----------|---------------------|
| CPU       | 50                  |
| GPU       | 30                  |
| RAM       | 20                  |

(Refer: Example of PCF data for [Dell products](https://www.dell.com/en-uk/lp/dt/product-carbon-footprints))

- To ensure that her software package follows best practices, she has been using
GitHub Actions for continuous integration and testing. At present, there are around
5 workflows that run on GitHub Actions, and they run around 10 times a day.
She makes a list of these workflows and their runtimes:

| Workflow Name       | Runtime (seconds) |
|---------------------|-------------------|
| docs                | 10                |
| check-links         | 8                 |
| upgrade-dependencies| 6                 |
| auto-merge          | 20                |
| ci                  | 5                 |

- Celia uses AI coding agents to create inline documentation for her code.
On an average, she writes approximately 20 prompts to the agents every week.
approximately 20 prompts to the agents every week.

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
She comes across a [research study](https://arxiv.org/abs/2510.26413) that compares
the carbon emissions of GitHub Actions with the emissions of quotidian activities.

![Comparison between the yearly
carbon emissions of the GitHub Actions ecosystem and the emissions of
quotidian activities](fig/github_actions_equivalent.pdf){alt = "Comparison between the yearly
carbon emissions of the GitHub Actions ecosystem and the emissions of
quotidian activities."}

This research study also reports that in 2024, the estimates for the carbon footprint
from GitHub Actions range from 150.5 MTCO2e in the most optimistic scenario to
994.9 MTCO2e in the most pessimistic scenario. The most likely scenario estimates
are 456.9 MTCO2e which is equivalent to the carbon captured by 7,615 urban trees
in a year.

- AI coding agents are used for 2 hours per week.

- Electricity usage by users of her package is around 100 kWh per month.

## Taking Action

After Celia has identified the emissions sources associated
with the development and usage of her software package, she takes some measures
to reduce these emissions.

To compute the carbon footprint of her software package, she uses the [Green Algorithms
Calculator](https://calculator.green-algorithms.org/). For the same, she has to record
the following information:

- Runtime of package in hours and minutes
- Types of cores used (CPU, GPU, or both)
- Number of cores used
- Model used
- Memory available in GB
- Platform used for the software development (e.g. local server, personal computer,
cloud computing)
- Location to retrieve the energy mix of the location
- Real usage factor of the CPU
- Power Usage Efficiency (PUE) of the local data centre (if applicable)
- Any multiplicative factor to use

The users of her package also include some members of her research group.
She reaches out to them to get some information on their usage of the package. She
finds that they are using it on a local server with 16 CPU cores and
64 GB of RAM. They run the package for around 4 hours per week. She encourages
them to use the Green Algorithms Calculator to estimate the carbon footprint of
their usage of the package.

### Reducing Scope 2 emissions

- Optimising the code base to reduce the computational resources and runtime of its use.

- She integrates [codecarbon](https://github.com/mlco2/codecarbon) into her code so
that it reports the carbon emissions when the code is run.

- She also inspects and optimises the error handling and input validation in her
 code to reduce the likelihood of running into errors that lead to repeated runs
of the code. Thus, minimising wasted computation.

- To measure the energy and CO2 consumption of her software package through a
software life cycle analysis (SLCA), she uses the [Green Metric Tool](https://metrics.green-coding.io/).

### Reducing Scope 3 emissions

- Producing documentation for users to help them make the most efficient use possible of
her code.
- Reducing the use of services such as GitHub Actions. She reduces the matrix of tests,
to only include the OS and Python versions that her package intends to support.
To minimise the number of jobs run in each workflow, she ensures that they are
run on pull requests against the primary development branch only. Further
reading:

    - Poster on [Environmentally-aware use of GitHub
    Actions](https://zenodo.org/records/12754189) and the [associated
    GitHub repository](https://github.com/ImperialCollegeLondon/game_of_life)
    - Blog post on [Adopting a more rational use of Continuous Integration with GitHub Actions](https://imperialcollegelondon.github.io/RSEBlog/2024/06/26/adopting-a-more-rational-use-of-continuous-integration-with-github-actions/).

::::::::::::::::::::::::::::::::::::: keypoints

- Research software development can have significant environmental impacts.
- Measuring and estimating carbon emissions from research software development
  is important for identifying areas for improvement.

::::::::::::::::::::::::::::::::::::::::::::::::
