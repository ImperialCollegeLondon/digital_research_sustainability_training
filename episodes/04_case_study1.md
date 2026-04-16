---
title: 'Case Study 1 - Research Software Engineer'
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

Celia is a Research Software Engineer that works as part of a research group. Two years
ago, she developed and released a Python package (hosted on PyPI) with a novel data
analysis technique relevant to her research area. The package has been a big success and
has been widely adopted. However, she has heard from some users that they are using it
on increasingly large datasets that leads to demanding memory requirements and slow
performance.

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

Celia decides to learn more about each of the emission sources, starting with
inspecting the hardware she uses for the package development. She primarily works on her
laptop, on an average, using it for 20 hours per week for the software development.
From the Product Carbon Footprint (PCF) data sheet for her laptop, she finds the
embedded emissions associated with the hardware components - CPU (50 kg CO2e), GPU
(30 kg CO2e), and RAM (20 kg CO2e).

Next, she reviews the code base and notices that it is not optimised for performance.
She finds that the code runs on a single CPU core and does not make use of any
GPU acceleration. She also finds that there are some redundant computations in the
code that could be optimised.

To ensure that her software package follows best practices, she has been using
GitHub Actions for continuous integration and testing. At present, there are around
5 workflows that run on GitHub Actions, and they run around 10 times a day.

For creating inline documentation for her code, Celia has been using AI coding agents.
While she is not using them frequently, she notices that on an average,
she writes approximately 20 prompts to the agents every week.

Finally, Celia reaches out to her research group members who are users of her package.
They agree to provide the necessary information on their usage of the package.
She finds that they are using it on a local server with 16 CPU cores and 64 GB of RAM.
They run the package for around 4 hours per week.

## Analysis

::::::::::::::::::::::::::::::: challenge

## Tracking activities and estimating emissions

Based on the scenario above, what are the activities that Celia should track,
over a period of one week, to estimate the emissions associated with her software
development and usage? What additional information does she need to collect?

::::::::::::::::::::::: solution

Celia tracks the following activities:

1. From the PCF data sheet for her laptop, she can find the embedded emissions
from the hardware components (CPU + GPU + RAM). In this case, the total embedded emissions
is 100 kg CO2e.

2. She notices that, her code is not optimised for performance, it has been
consuming more computational resources and is taking longer to run than it should,
ultimately leading to higher emissions. She notes that the runtime of the code on a
single CPU core is around 4 hours per week.

3. Her package has five workflows on GitHub Actions that run around 10 times a day.
They have a total runtime of 2940 seconds per week. Additionally, she records that
she has been writing approximately 20 prompts to the AI coding agents every week,
which has a total runtime of around 20 minutes per week. At present,
she is not aware of any tools that can be used to estimate the emissions from the use
of GitHub Actions and AI coding agents. So decides to use them sparingly and only when
necessary.

Finally, to compute the carbon footprint of her software package, she records the
following additional information to be used in the [Green
Algorithms Calculator](https://calculator.green-algorithms.org/):

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

:::::::::::::::::::::::
:::::::::::::::::::::::::::::::

## Taking Action

After Celia has identified the emissions sources associated
with the development and usage of her software package, she takes some measures
to reduce these emissions.

She optimises the code base to reduce the computational resources and runtime of its use.
This includes optimising the error handling and input validation in her
code to reduce the likelihood of running into errors that lead to repeated runs
of the code. Thus, minimising wasted computation. She integrates the
[codecarbon](https://github.com/mlco2/codecarbon) tool into her code base so
that it can report the carbon emissions when the code is run. This allows her to track
the emissions associated with the usage of her package and identify areas for
further optimisation.

The users of her package (members of her research group) have been asking her for help
with optimising the performance of the code. She provides them with some tips on how to
optimise the performance of the code when they run it on their local machines. Additionally,
she creates a detailed user guide that includes instructions on how to make
the most efficient use of her package, including tips on how to optimise the
performance of the code when running it on different hardware configurations.

Her package only intends to support a specific set of OS and Python versions. Therefore,
she reduces the number of tests run on GitHub Actions to only include these
OS and Python versions. Moreover, to minimise the number of jobs run in each workflow,
she makes sure that they are run on pull requests against the primary development branch
only.

## References

1. Product Carbon Footprint (PCF) data for [Dell products](https://www.dell.com/en-uk/lp/dt/product-carbon-footprints)

::::::::::::::::::::::::::::::::::::: keypoints

- Research software development can have significant environmental impacts.
- Measuring and estimating carbon emissions from research software development
  is important for identifying areas for improvement.

::::::::::::::::::::::::::::::::::::::::::::::::
