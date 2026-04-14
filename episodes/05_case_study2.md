---
title: 'Case Study 2 - Lab Scientist doing computational work'
teaching: 10
exercises: 4
---

:::::::::::::::::::::::::::::::::::::: questions

- How does the increasing use of LLMs affect carbon foorprint and energy efficiency?
- What strategies can minimise the carbon footprint of research data storage?
- How does relying on old hardware prevent a modern research lab from being energy efficient?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative case study relating to carbon emissions in typical computational
lab workflows
- Identify tools and resources to help estimate emissions associated with daily
 computational research tasks
- Quantify carbon emissions associated with using LLMs to generate Python scripts
- Quantify carbon emissions associated with storing research data

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Emma is a researcher in a biology lab and was tasked with analysing genomic sequencing data.
 While she is an expert in molecular biology, her computational and statistics background
 is limited. Due to the type and volume of data generated in the lab, she chose to write
 custom Python scripts to analyse her data. The project Emma is working on is scheduled
 to run for 5 years.

Emma's set up:

- Work laptop: modern and energy efficient laptop
- Data storage: Her research will generate approx 3.5 Tb for the duration of the project.
 She is planning to back up 2 copies of the raw data on different HDDs. In addition, she
 will generate approx. 400 GB of processed data every year, which will be used for active
analyses, which she plans to store on different HDDs. While the project only runs for 5
 years,there is a 10 year data retention period to comply with her funding's coniditions

Emma's workflow:

- She uses cloud-based LLMs to write her scripts for processing and analysing data.
This often requires many queries and iterations.
- She keeps every version of her raw data on the HDDs, and rarely deletes old files.
- After pre-processing the raw data, she stores a copy of the processed data on
 different HDDs
- She runs her scripts on her laptop and scripts often take 6h to complete.

Emma is interested in reducing her digital carbon footprint and wants to optimise
 her computational workflow to balance scientific rigour with environmental
 responsibility.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Emissions

Sort the items below into Scope 1, Scope 2 or Scope 3 emissions:

- The electricity powering Emma's laptop
- The manufacturing of Emmas's laptop
- The energy used by the LLM provider to write the data processing and analysis code
- The energy used by cloud-storage provider to store Emma's data
- The external monitors used with the laptop

:::::::::::::::::::::::: solution

- The electricity powering Emma's laptop (**Scope 2**)
- The manufacturing of Emmas's laptop (**Scope 3**)
- The energy used by the LLM provider to write the data processing and analysis code
(**Scope 3**)
- The energy used by cloud-storage provider to store Emma's data (**Scope 3**)
- The external monitors used with the laptop (**Scope 2**)

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Collecting information

### Data storage

Emma is considering using different storage types after she heard that
 storing large amounts of data on HDDs might not be the most evironmentally friendly
 option. She has learnt from colleagues that she could choose between hard drives
 (HDD), Solid State Drives (SDD), LTO magnetic tapes or cloud-based storage. However,
  she is unsure about their different enivronmental impacts.

Emma did some research on the above storage types and used the table below summarising
 their emissions below to calculate the carbon footprint of storing her project's data:

| Category | SDD | HDD | LTO tape | Cloud |
| :--- | :--- | :--- | :--- | :--- |
| **Embodied Carbon** | High (16-32 kg) | Moderate (2-4 kg) | Low (~0.07 kg) | Difficult to estimate |
| **Operational Carbon** | Low (2-5 kg) | Moderate - High (2-16 kg) | Low (~0 kg) | Moderate - High (2-40 kg) |
| **Lifespan** | 5–10 years | 5-10 years | 30+ years | Depends on provider |

\* Emissions are in **kg CO₂e per TB per year**

Emma’s research will produce 3.5 TB of raw data for the duration of the project. Because
she keeps two copies of all raw data, the total required storage for raw data comes to 7
TB. Beyond that, Emma will generate an additional 400 GB of processed data per year,
adding up to 2 TB over the duration of the project. Altogether, Emma will need
9 TB of storage to keep both raw and processed data.

However, the data retention policy of 10 years beyond the end of the project means that
the data must be stored for a total of 15 years. Given that the lifespan of HDDs can reach
10 years in best case scenario, Emma will have to replace the HDDs at least once.

$$
E_{HDDs} = E_{embodied}+ E_{operational}
E_{HDDs} = (3 kgCO₂e/TB \times 9 TB + 9 kgCO₂e/TB \times 9 TB) \times 15   \\
E_{HDDs} = 1,620 kgCO₂e
$$

 Emma works out that storing the 9 TB data on HDDs will have associated carbon emissions
 approximately equal to **1,620 kgCO2e** in combined embodied and operational emissions,
 based on the average values within the emissions ranges she identified.

### LLMs use

Emma is also concerned about the carbon footprint of her increasing use of LLMs to write
 the Python code to process and analyse her data. While the exact carbon footprint
 of using LLMs is hard to quantify, she found the following regarding programming-related
  queries:

    - some LLM models emit between 20% and 59% less emissions than human programmers
    (GPT-4o-mini), while other models can emit 5 to 19 times more carbon than human programmers
    (GPT4)^1^
    - the number of inference calls (queries) has a high correlation to the amount
   of carbon emissions ^1^

 Emma uses a reasoning model to write her scripts,
 often requiring more than 30 queries to the LLM to debug and obtain a script which
 produces correct results. Using HuggingFace's [Ecologits calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 tool, she finds that queries generating code using GPT-5 model estimate approx.
 10.8 gCO2e per query. In her case, running 30 queries generates **0.324 kgCO2e**,
 assuming she only has to do this once over the course of the project.

### Emissions from running her scripts

Emma also begins estimating the carbon emissions associated with running her scripts.
Emma is using her modern laptop and looks up the specifications for her model to get more
 more accurate emissions. She finds that her laptop has a Core i6-1145G7 process, with 4
 CPU cores and 64 GB memory. [She uses the Green-algorithms calculator](https://calculator.green-algorithms.org/)
 to find that her computer emits 53.20 gCO2e each time she runs the script for 6 hours.
 If she runs the script once every year, the total emissions would be **0.266 kgCo2e**.

### Greatest source of carbon emissions

Based on her calculations, Emma concludes that storing her research data and running her
Python scripts are the activities with the largest associated carbon emissions. At around
1,900 kgCO2e these activities account to a quarter of the emissions per-capita in the
UK,according to the [International Energy Association](https://www.iea.org/countries/united-kingdom/emissions)
While lower in comparison, the emissions linked to using LLMs to help write her code
are not insignificant and are equivalent to charging a smartphone [27 times](https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator#results).
With this in mind, Emma begins developing an improved research workflow to reduce her digital
carbon footprint.

## Analysis

She has heard that her institution provides a tape-based cold storage options located
 in two different campuses and which are intended for data that is not accessed very often.
 She decides to keep the two copies of the raw data on the LTO-tape based storage
 provided by her institution, with each copy being stored at a different site. This
 ensures the data is safe in case something happens with one of the storages. She decides
 to keep her processed data on HDDs, as she needs easy and fast access for analyses.

 While the carbon footprint of using the LLM to generate
 her scripts is not as high as that associated with data storage and running her scripts,
 she decides to switch to a more simple LLM model, which is more suitable for the type
 of Python code she is generating.

 Emma now wants to quantify the difference in carbon emissions between her existing
  workflow (Scenario 1) and the improved one (Scenario 2).

### Scenario 1 (Current Workflow)

- Emma uses a reasoning model to write her scripts, requiring 30 queries to debug.
- She backs up her raw and processed data (9 TB total) on HDDs.

Based on the calculations Emma has already done above, the total carbon emissions
associated with her current workflow are **~113 kgCO2.**

### Scenario 2 (Improved Workflow)

- Emma switches to GPT-40-mini, which has a lower carbon footprint per query, and
 since her computational requirements are fairly light. However, debugging now
 takes 50 queries.
- She keeps the two copies of raw data (7 TB) in the LTO-tape based facilities provided
 by her institution. She keeps the processed data (2 TB) on HDDs for active work

Given all we know about Emma's workflow, calculate the emissions associated with the current
 workflow and the improved workflow.

#### New data storage strategy

Given that magnetic tape has negligible emissions when idle, we can assume that the
 total emissions from storing data on tape come from embodied emissions, estimated at
 ~0.07 kgCO₂ per TB. Keeping the two copies of raw data (7 GB) in the institution’s
  LTO‑tape storage facilities would therefore generate:

$$
E_{tape storage} = 0.07 kgCO₂e/TB \times 7 TB \times 15 years \\
E_{tape storage}  = 7.35 kgCO₂e
$$

Keeping the 2 GB of processed data on HDDs would generate:

$$
E_{HDDs} =  (3 kgCO₂e/TB \times 2 TB + 9 kgCO₂e/TB \times 2 TB) \times 15 years   \\
E_{HDDs}  = 360 kgCO₂e
E
$$

Therefore, the total costs associated with storing Emma's research data would be
 **367.35 kgCO₂e**.

#### Switching to a simpler LLM model

 Emma is planning to switch from a reasoning model to a smaller LLM model,
 GPT4-0-mini, for which emissions are estimated to be around 562 mgCO₂e per query.

$$
E_{LLM} = 0.562 gCO₂e/query \times 50 queries \\
E_{LLM} = 0.028 kgCO₂e \\
$$

The total emissions associated with using the simpler LLM would be approx. **0.028 kgCO₂e**.

## Conclusion

Adopting this improved workflow would result in a five-fold reduction in Emma’s digital
carbon emissions.  Particularly, moving from storing data on HDDs to a hybrid storing
approach that includes both HDDs and LTO-tapes has the greatest impact on lowering emissions,
saving around 1,250 kgCO2e, which is equivalent to the total annual electricity-related
emissions of three average UK households.

A comparison of the emissions associated with both scenarios can be found below:

| | **Scenario 1 (Current Workflow)** | **Scenario 2 (Improved Workflow)** | Change |
| :--- | :--- | :--- | :--- |
| Emissions Storage (kgCO₂e) | 1,620 | 367.35 | HDDs only -> LTO tape + HDDs |
| Emissions LLM (kgCO₂e) | 0.324 | 0.028 | GPT-5 -> GPT-4-o-mini |

While these improvements are substantial, they represent only one piece of a larger
puzzle. For a life scientist, the total work-related emissions typically range from
4 to 15 tCO2e annually ^2^. These numbers are driven by carbon intensive activities,
 such as international travel, laboratory heating, ventialtion and AC systems,
 and the heavy use of chemical reagents and single-use equipment.

### Steps to reduce emissions

Emma is happy with her carbon footprint after adopting the new workflow.
 Building on this initial success, she has also identified several additional strategies
  to further minimise her digital carbon footprint:

- Schedule to run her scripts for then the grid is cleanest
- Use compression technique to further reduce the size of her stored data
- Identify and delete dark data (data that is stored but never used again)
- Process the data before uploading to cloud to reduce storage requirements
- Change which LLMs models she uses based on the task complexity
- Make use of tools such as [EcoLogits](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 (open-source Python library to estimate the carbon footprint of inference queries made
 to LLMs) and online LLM carbon emissions leaderboards

By combining these new behaviours with her new storage workflow, Emma's digital footprint
will drop even further, proving that even data-intensive research can be done without a
high environmental cost.

## References

1. [Winter N,The paradox of the life sciences: How to address climate change in the lab: How to address climate change in the la. doi: 10.15252/embr.202256683](https://pmc.ncbi.nlm.nih.gov/articles/PMC9986813/)
2. [Woo, N.H. A comparative study of AI and human programming on environmental
 sustainability. Sci Rep 15, 39182 (2025). https://doi.org/10.1038/s41598-025-24658-5](https://www.nature.com/articles/s41598-025-24658-5)
