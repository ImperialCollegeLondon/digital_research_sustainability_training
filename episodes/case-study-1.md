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

Celia is concerned about the environmental impact of her software package.
She wants to assess the carbon emissions associated with both the development
and usage of her package and identify ways to reduce these emissions.

The GHG protocol divides emissions into three scopes (Reference: [GHG protocol](https://learn.greensoftware.foundation/measurement#the-ghg-protocol)):

- **Scope 1**: Direct emissions from operations owned or controlled by the
   reporting organisation, such as on-site fuel combustion or fleet vehicles.

- **Scope 2**: Indirect emissions related to emission generation of
   purchased energy, such as heat and electricity.

- **Scope 3**: Other indirect emissions from all the other activities you are
   engaged in. Including all emissions from an organisation's supply chain,
   business travel for employees, and the electricity customers may
   consume when using your product.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: instructor

Inline instructor notes can help inform instructors of timing challenges
associated with the lessons. They appear in the "Instructor View"

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Scope 2 Emissions

Refer to the definition of Scope 2 emmissions above and identify which
of the following activities during the research process would be
classified as Scope 2 emission source?

- Emissions from electricity usage of the hardware used for software development.
- Emissions from travel to attend a conference for presenting research findings.
- Emissions from the use of cloud computing services for data analysis.
- Emissions from heating the office where the researcher works.

:::::::::::::::::::::::: solution

Option 1: Is correct. Scope 2 emissions are indirect emissions related to
purchased energy, such as electricity usage of hardware.
Option 2: Is incorrect. Emissions from travel are classified as Scope 3 emissions.
Option 3: Is incorrect. Emissions from cloud computing services are classified
as Scope 3 emissions.
Option 4: Is correct. Emissions from heating the office are classified as
Scope 2 emissions.

:::::::::::::::::::::::::::::::::

## Challenge 2: Identify Scope 3 Emissions

Refer to the definition of Scope 3 emmissions above and identify which
of the following activities during the research process would be
classified as Scope 3 emission source?

- Embedded emissions from hardware used for software development.
- Use of services such as GitHub Actions and AI Coding agents.
- Electricity usage when users of the package run the code.
- Electricity usage of the researcher's office for lighting and heating.

:::::::::::::::::::::::: solution

Option 1: Is correct. Embedded emissions from hardware are classified as
Scope 3 emissions.
Option 2: Is correct. Use of services such as GitHub Actions and AI Coding
agents are classified as Scope 3 emissions.
Option 3: Is correct. Electricity usage when users run the code are classified
as Scope 3 emissions.
Option 4: Is incorrect. Emissions from office lighting and heating are classified
as Scope 2 emissions.

:::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

Celia should assess the balance of emissions involved in development of the code
base versus its usage. She should look at how to estimate these then focus her
emission reduction measures appropriately.

Depending on the outcome she should look at measures such as:

- Reducing the use of services such as GitHub Actions.
- Optimising the code base to reduce the computational resources and runtime of its use.
- Producing documentation for users to help them make the most efficient use possible of
her code.

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
