---
title: 'Case Study 2: Lab Scientist doing computational work'
teaching: 10
exercises: 4
---

:::::::::::::::::::::::::::::::::::::: questions

- How does the increasing use of AI tools affect carbon foorprint and energy efficiency?
- How does relying on old hardware prevent a modern research lab from being energy efficient?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative case study relating to carbon emissions in typical lab workflows
- Understand how relying on older equipment affects the sustainability of scientific work
- Identify practical ways to reduce the hidden carbon footprint of daily research tasks
- Identify tools and resources to help estimate emissions
   associated with daily computational research tasks

::::::::::::::::::::::::::::::::::::::::::::::::

## Scenario

Emma is a researcher in a Biology lab and was tasked with analysing genomic sequencing data.
While she is an expert in molecular biology, her computational and statistics background
 is limited. Due to the type and volume of data generated in the lab, she chose to write
 custom Python scripts to analyse the data.

Emma's set up:

- Personal laptop: modern and energy efficient laptop (2 years old), which she uses for
 email and paper writing.
- Lab Desktop: a 10 year old Desktop station, with an outdated version of Linux.
 Her lab's sequencing equipment is hard-coded to interface only with this specific OS version.

Emma's Workflow:

- To write her Python scripts, she uses cloud-based LLMs.
- She backs her data on a general-purpose cloud provider.
- She runs her scripts on the Lab Desktop station and scripts often take 12-16 hours
 to run. Sometimes Emma leaves the Desktop running 24/7 even over the weekends,
  so the scripts could finish running.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Emissions

Sort the items below into Scope 1, Scope 2 or Scope 3 emissions:

- The electricity powering the Lab Desktop
- The manufacturing of Emmas's personal laptop
- The energy used by the AI/LLM provider to answer Emma's prompts
- The energy used by cloud-storage provider to store Emma's backup data
- A backup diesel generator used during power-outages to prevent the generator
 from stopping mid-run
- Software licence for a proprietary analysis software

:::::::::::::::::::::::: solution

:::::::::::::::::::::::::::::::::

## Challenge 2: Local vs cloud AI trade-offs

Emma has come up with several options to do her workflow:

- Option 1: She spends several days writing the code herself, testing it on
 the old Lab Desktop
- Option 2: She uses cloud-hosted LLMs to write the code in 2 hours but in
 order to do that she sends at least 50 large prompts to the LLM
- Option 3: To speed up her work and save money, Emma can download a local
 LLM to run directly on the lab Desktop (the Desktop lacks a GPU).

Which option do you think creates more emissions? Does the answer change
 if the lab Desktop or AI/cloud providers are powered by renewable energy?

:::::::::::::::::::::::: solution

:::::::::::::::::::::::::::::::::

## Challenge 3: Hidden sources of carbon emissions

Identify the habits or technical setups that are wasting energy without
 adding scientific value in Emma's current workflow.

:::::::::::::::::::::::: solution

- data storage
- leaving the Desktop on
- inneficient code
- old equipment

:::::::::::::::::::::::::::::::::

## Challenge 4: Steps to reduce emissions

Identify steps that Emma could take to reduce her carbon footprint.

:::::::::::::::::::::::: solution

- use of HPC resources

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::
