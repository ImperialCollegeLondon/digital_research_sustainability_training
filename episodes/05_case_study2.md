---
title: 'Case Study 2 - Lab Scientist doing computational work'
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

## Introduction

Emma is a researcher in a Biology lab and was tasked with analysing genomic sequencing data.
While she is an expert in molecular biology, her computational and statistics background
 is limited. Due to the type and volume of data generated in the lab, she chose to write
 custom Python scripts to analyse the data.

Emma's set up:

- Personal laptop: modern and energy efficient laptop (2 years old), which she uses for
 email and paper writing.
- Lab Desktop: a 10 year old Desktop station, with an outdated version of Linux.
 Her lab's sequencing equipment is hard-coded to interface only with this specific OS version.
- Data storage: She backs up the raw sequencing data (approx. 500GB) to a general
 purpose cloud provider

Emma's Workflow:

- She uses cloud-based LLMs to write her Python scripts for processing and analysing data.
- She keeps every version of her data in the clous, and rarely deletes old files
- She runs her scripts on the Lab Desktop station and scripts often take 12-16 hours
 to run. Sometimes Emma leaves the Desktop running 24/7 even over the weekends,
  so the scripts could finish running.

Emma is interested in reducing her digital carbon footprint and wants to optimise
 her computational workflow to balance scientific rigour with environmental
 responsibility.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Emissions

Sort the items below into Scope 1, Scope 2 or Scope 3 emissions:

- The electricity powering the Lab Desktop during a 16-hour run
- The manufacturing of Emmas's personal laptop
- The energy used by the AI/LLM provider to answer Emma's prompts
- The energy used by cloud-storage provider to store Emma's data
- The external monitors used with the Lab Desktop

:::::::::::::::::::::::: solution

- The electricity powering the Lab Desktop (**Scope 2**)
- The manufacturing of Emmas's personal laptop (**Scope 3**)
- The energy used by the AI/LLM provider to answer Emma's prompts (**Scope 3**)
- The energy used by cloud-storage provider to store Emma's data (**Scope 3**)
- The external monitors used with the Lab Desktop (**Scope 2**)

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Collecting more information

### Data storage

Some of the data that Emma will start collecting is considered sensitive data,
so she wants to move the data to a physical storage for better security.
She has heard from other colleagues that she could choose between an external hard drive
 (HDD), a Solid State Drive (SDD) or an LTO magnetic tape. However, she is unsure
  about the enivronment impacts of these.

Emma did some research on the carboon footprint associated with the three storage types
 and found the following:

- SSDs are most carbon efficient when in operation, but their manufacturing produces
 more emissions (320 kgCO2e/TB). SSDs have an average live span of 5-8 years and to use
  them 4.9 kg CO2e/TB/year are produced.
- HDDs have a lifespan of 5-8 years, similar to that of SDDs and using them emits
 around 2.55 kg CO2e/TB/year (Seagate). Their manufacturing produces less carbon
  emissions than SSDs (40 kg CO2e/TB)
- Tape storage has a longer lifespan (average 10 years), with modern ones reaching
 up to 30 years. To use them LTO tapes produce around .07 kg CO2e/TB/year
  over a ten-year life .

| Feature | SSD (Solid State) | HDD (Hard Drive) | Magnetic Tape (LTO) |
| :--- | :--- | :--- | :--- |
| **Embodied Carbon** | ~320kg CO2e per TB | 30-40kg CO2e per TB | 2-5kg CO2e per TB |
| **Operational Carbon** | Low (1.3W) | Moderate (4.2W) | 0 |
| **Lifespan** | 5–10 years | 5-10 years | **30+ years** |

In contrast, she found the carbon emission associated with cloud data storage is
 estimated between 10-40 kg CO2e/TB/year, but the value depends heavily on the data
  center's efficiency, and the region's power grid.

### LLMs use

Emma is also concerned about the carbon footprint of her increasing use of LLMs to write
 the python code to process and analyse her data. While the exact carbon emission
 associated with using LLMs is hard to quantify, her research found the following:

- the carbon emissions associated with LLM use come from model training emissions,
 inference calls (queries) emissions, and infrastructure and hardware emissions.
- The carbon footprint depends heavily on the type of query and result with generating
images beign more carbon intensive than text
- When it comes to programming-related queries, Emma found the following data:

    - when they give the right answer from the first query, some LLM models emit
   between 20% and 59% less emissions than human programmers (GPT-4o-mini), while
   other models can emit 5 to 19 times more carbon than human programmers (GPT4)
    - the number of inference calls (queries) has a high correlation to the amount
   of carbon emissions

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Use of LLMs

Emma has two options for her data processing and analysis workflow:

- Option 1: She spends several days writing the code herself, testing it on
 the old Lab Desktop. The code takes 16h to run.
- Option 2: She uses cloud-hosted LLMs to write the code in 2 hours but in
 order to do that she sends at least 50 large prompts to the LLM.  The resulting
 code is 40% faster to run than the code she wrote herself

Which option do you think creates the least amount of emissions? Does the answer change
 if the lab Desktop or AI/cloud providers are powered by renewable energy?

:::::::::::::::::::::::: solution

- inference calls: depends on the model she chooses, but if a complicated task, GPT4
might be more appropriate but emits at least 5 times more caborn emissions than humans
- inefficient code: if the code is significanlty slower and runs on the old lab desktop,
 the operation carbon (Scope 2) increases significantly over the 16h time
- reasoning LLMs can produce 3x more emissions than models that provide concise answers

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Analysis

Emma decides to quantify the carbon impact of her current workflow (Scenario 1) and find
 how different changes (Scenario 2) can improve it.

### Scenario 1

- Emma uses a reasoning model to write her scripts. It takes 50 queries to debug
- She backs up her entire 500GB dataset to the Cloud
- She runs her script on the Old Lab Desktop, which takes 8 hours to finish

### Scenario 2

- Emma switches to GPT-40-mini but it still takes 50 queries to debug
- She moves 400GB on LTP tape (data she has not used in over 6 months) and
 keeps only 100 GB on the cloud for active work
- She runs her scripts on her modern laptop, which take 6h to finish

::::::::::::::::::::::::::::::::::::: challenge
Given all we know about Emma's
 workflow, calculate the emissions associated with the following scenarios:

:::::::::::::::::::::::: solution

Scenario A

- reasoning LLM use
- Cloud storage use (500GB)
- Computing energy (on Lab Desktop)

Scenario B

- smaller LLM use
- Hybrid storage (Tape + Cloud)
- Compute (6h on Laptop)

Conclusion: Scenario B should be a lot better
:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Steps to reduce emissions

Emma is now happier with her carbon footprint after making the changes in Scenario 2.
 Building on her initial success, Emma has identified several ways to further
  minimize her digital carbon footprint:

- Schedule to run her scripts for then the grid is cleanest (Carbon-Aware Scheduler)
- Use compression technique to further reduce the size of her stored data
- Change which LLMs models she uses based on the task complexity
- Make use of tools such as EcoLogits (open-source python library to estimate
 the carbon footprint of inference queries made to LLMs) and online LLM carbon
  emissions leaderboards
- Explore parallelising her analysis script and running it on HPC
- Identify and deleted dark data (data dat is stored but never used again)
