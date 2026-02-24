---
title: 'Case Study 2 - Lab Scientist doing computational work'
teaching: 10
exercises: 4
---

:::::::::::::::::::::::::::::::::::::: questions

- How does the increasing use of LLMs affect carbon foorprint and energy efficiency?
- How does relying on old hardware prevent a modern research lab from being energy efficient?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative case study relating to carbon emissions in typical computational
lab workflows
- Identify tools and resources to help estimate emissions associated with daily
 computational research tasks
- Quantify carbon emissions associated with using LLMs to generate scripts
- Qiantify carbon emissions associate with storing research data

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Emma is a researcher in a biology lab and was tasked with analysing genomic sequencing data.
 While she is an expert in molecular biology, her computational and statistics background
 is limited. Due to the type and volume of data generated in the lab, she chose to write
 custom Python scripts to analyse her data. The project Emma is working on is scheduled
 to run for 5 years.

Emma's set up:

- Personal laptop: modern and energy efficient laptop (2 years old), which she uses for
 email and paper writing.
- Lab Desktop: a 15 year old Desktop station, with an outdated version of Linux and no GPUs.
- Data storage: Her research generates approx. 700 GB of raw data every year. She is
 planning to back up 2 copies of the raw data on different HDDs. In addition, she plans
 to keep a copy of the processed data on different HDDs (approx 400 GB), which
 will be used for active analyses.

Emma's Workflow:

- She uses cloud-based LLMs to write her scripts for processing and analysing data.
This often requires many queries and iterations.
- She keeps every version of her raw data on the HDDs, and rarely deletes old files.
- After pre-processing the raw data, she stores a copy of the processed data on
 different HDDs
- She runs her scripts on the lab Desktop station and scripts often take 12-16 hours
 to complete. Sometimes Emma leaves the Desktop running 24/7 even over the weekends,
  so the scripts could finish running.

Emma is interested in reducing her digital carbon footprint and wants to optimise
 her computational workflow to balance scientific rigour with environmental
 responsibility.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Emissions

Sort the items below into Scope 1, Scope 2 or Scope 3 emissions:

- The electricity powering the lab Desktop during a 16-hour run
- The manufacturing of Emmas's personal laptop
- The energy used by the LLM provider to write the data processing and analysis code
- The energy used by cloud-storage provider to store Emma's data
- The external monitors used with the lab Desktop

:::::::::::::::::::::::: solution

- The electricity powering the lab Desktop (**Scope 2**)
- The manufacturing of Emmas's personal laptop (**Scope 3**)
- The energy used by the LLM provider to write the data processing and analysis code
(**Scope 3**)
- The energy used by cloud-storage provider to store Emma's data (**Scope 3**)
- The external monitors used with the Lab Desktop (**Scope 2**)

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Collecting information

### Data storage

Emma is considering using differnt storage types after she heard that
 storing large amounts of data on HDDs might not be the most evironmentally friendly
 choice. She has heard from other colleagues that she could choose between hard drives
 (HDD), Solid State Drives (SDD), LTO magnetic tapes or cloud-based storage. However,
  she is unsure about the enivronmental impacts of these.

She found the following information for the carbon footprint associated with the four
 storage types and found the following:

- SDDs are the most carbon efficient when in operation, but their manufacturing produces
 significantly more emissions.
- HDDs have a lifespan of 5-10 years, similar to that of SDDs. Their embodied emissions
 are signifcantly lower than that of SDDs but operational emissions are higher.
- Tape storage has a longer lifespan (10-15 years), with modern ones reaching
 up to 30 years. However, moving and accessing data on a LTO tape is slow.
- Cloud storage's associated emissions are estimated between 2-40 kg CO₂e/TB/year
 (according to a WholeGrain [report](https://www.wholegraindigital.com/digitaldeclutter/#cloud-storage)
 and [Greenly](https://greenly.earth/en-gb/blog/industries/what-is-the-carbon-footprint-of-data-storage)),
 but the value depends heavily on the data center's efficiency and the region's power grid.
 Embodied emissions are hard to estimate and depend on the hardware used by the provider
 (HDDs or SSHs). They are often included in the operational carbon footprint emissions.

The carbon emissions associated with the four storage types are summarised below:

| Category | SDD | HDD | LTO tape | Cloud |
| :--- | :--- | :--- | :--- | :--- |
| **Embodied Carbon (kg CO₂e per TB)** | High (16-32 kg)^1^ | Moderate (2-4 kg)^1^ | Low (~0.07 kg)^3^ | Difficult to estimate |
| **Operational Carbon (kg CO₂e per TB)** | Low (2-5 kg)^1^ | Moderate - High (2-16 kg)^1,2^ | Low (~0 kg) | Moderate - High (2-40 kg) |
| **Lifespan** | 5–10 years | 5-10 years | 30+ years | Depends on provider |

Emma’s research produces 700 GB of raw data each year, and since her project will run
 for five years, she will accumulate 3.5 TB of raw data. Because she keeps two
 copies of all raw data, the total required storage for raw data comes to 7 TB.
 Beyond that, Emma generates an additional 400 GB of processed data per year,
 adding up to 2 TB over the duration of the project. Altogether, Emma will need
 9 TB of storage to keep both raw and processed data.

 Emma works out that storing the 9 TB data on HDDs will have associated carbon emissions
 aproximately equal to **108 kgCO2e** in combined embodied and operational emissions,
 based on the average values within the emissions ranges she identified.

### LLMs use

Emma is also concerned about the carbon footprint of her increasing use of LLMs to write
 the python code to process and analyse her data. While the exact carbon footprint
 of using LLMs is hard to quantify, she found the following:

- The carbon emissions associated with LLM use come from model training emissions,
 inference calls (queries) emissions, and infrastructure and hardware emissions.
- When it comes to programming-related queries, Emma found the following data:

    - some LLM models emit between 20% and 59% less emissions than human programmers
    (GPT-4o-mini), while other models can emit 5 to 19 times more carbon than human programmers
    (GPT4)^1^
    - the number of inference calls (queries) has a high correlation to the amount
   of carbon emissions ^1^

Based on her current workflow, Emma uses a reasoning model to write her scripts,
 often requiring more than 30 queries to the LLM to debug and obtain a script which
 produces correct results. Using HuggingFace's [Ecologits calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 tool, she finds that queries generating code using GPT-5 model estimate approx.
 10.8 gCO2e per query. In her case, running 30 queries generates **0.324 kgCO2e**,
 assuming she only has to do this once.

### Emissions from running her scripts

Emma also begins estimating the carbon emmissions asssociated with running her scripts.
 Since she cannot find the exact specifications of the old desktop, she uses a
 0.3 kW **power draw**, a value she found commonly cited for older computer stations.
 However, she is still unable to find any information on the
 embodied carbon cost of the lab Desktop. To estimate operational emissions, she uses
 data from official UK grid sources (such as [EnergyDashboard](https://www.energydashboard.co.uk/live)),
 and finds a **grid carbon intensity** of 194 gCO₂/kW on a day with overcast skies and
 mild winds, typical of the area she works in.

 She uses the information gathered to calculate the total
 emissions associated with running her scripts for 16 to a total of 0.931 kgCO2e. However,
 this numer is probably going to be higher, as Emma is likely to run the script several
 times throughout the course. Assuming, she runs the scripts once a year, the total carbon
 emissions would be closer to approx. **4.656 kgCO2e.**

### Greatest source of carbon emissions

Based on her calculations, Emma concludes that storing her research data and running her
 python scripts are the activities with the largest associated carbon emissions. Even so,
 the emissions linked to using LLMs to help write her code are not insignificant. With
 this in mind, Emma begins developing an improved research workflow to reduce her digital
 cabron footprint.

## Analysis

She has heard that her institution provides a tape-based cold storage options located
 in two different campuses and which are intended for data that is not accessed very often.
 She decides to keep the two copies of the raw data on the LTO-tape based storage
 provided by her institution, with each copy being stored at a different site. This
 ensures the data is safe in case something happens with one of the storages. She decides
 to keep her processed data on HDDs, as she needs easy and fast data access for analyses.

 Emma also decides to switch to using her modern laptop to run her scripts to further
 reduce her carbon emissions. While the carbon footprint of using the LLM to generate
 her scripts is not as high as that associated with data storage and running her scripts,
 she decides to switch to a more simple LLM model, which is more suitable for the type
 of python code she is generating.

 Emma now wants to quantify the difference in carbon emissions between her existing
  workflow (Scenario 1) and the improved one (Scenario 2).

### Scenario 1 (Current Workflow)

- Emma uses a reasoning model to write her scripts, requiring 30 queries to debug.
- She backs up her raw and processed data (9 TB total) on HDDs.
- She runs her script on the old lab Desktop, which takes 16 hours to finish.

Based on the calculations Emma has already done above, the total carbon emissions
associated with her current workflow are **~113 kgCO2.**

### Scenario 2 (Improved Workflow)

- Emma switches to GPT-40-mini, which has a lower carbon footprint per query, and
 since her computational requirements are fairly light. However, debugging now
 takes 50 queries.
- She keeps the two copies of raw data (7 GB) in the LTO-tape based facilities provided
 by her institution. She keeps the processed data (2 GB) on HDDs for active work
- She runs her scripts on her modern laptop, which take 6h to finish.

Given all we know about Emma's workflow, calculate the emissions associated with the current
 workflow and the improved workflow.

#### Using modern laptop instead of old lab Desktop

Emma is using her modern laptop and looks up the specifications for her model to get more
 more accurate emissions. She finds that her laptop has a Core i6-1145G7 process, with 4
 CPU cores and 64 GB memory. [She uses the Green-algorithms calculator](https://calculator.green-algorithms.org/)
 to find that her computeremits 53.20 gCO2e each time she runs the script for 6 hours.
 If she runs the script once every year, the total emissions would be **0.266 kgCo2e**.

#### New data storage strategy

Given that magnetic tape has negligible emissions when idle, we can assume that the
 total emissions from storing data on tape come from embodied emissions, estimated at
 ~0.07 kgCO₂ per TB. Keeping the two copies of raw data (7 GB) in the institution’s
  LTO‑tape storage facilities would therefore generate:

$$
E_{tape storage} = 0.07 kgCO₂e/TB/year \times 7 TB \\
E_{tapestorage}  = 0.49 kgCO₂e
$$

Keeping the 2 GB of processed data on HDDs would generate:

$$
E_{HDDs} =  3 kgCO₂e/TB/year \times 2 TB + 9 kgCO₂e/TB/year \times 2 TB   \\
E_{HDDs}  = 24 kgCO₂e
$$

Therefore, the total costs associated with storing Emma's research data would be
 **24.49 kgCO₂e**.

#### Switching to a simpler LLM model

 Emma is planning to switch from a reasoning model to a smaller LLM model,
 GPT4-0-mini, for which emissions are estimated to be around 562 mgCO₂e per query.

$$
E_{LLM} = 0.562 gCO₂e/query \times 50 queries \\
E_{LLM} = 0.028 kgCO₂e \\
$$

The total emissions associated with using the simpler LLM would be approx. **0.028 kgCO₂e**.

A comparison of the emissions associated with both scenarios can be found below:

| | **Scenario 1 (Current Workflow)** | **Scenario 2 (Improved Workflow)** | Change |
| :--- | :--- | :--- | :--- |
| Emissions Storage (kgCO₂e) | 108 kg | 24.49 kg | HDDs only -> LTO tape + HDDs |
| Emissions Computing (kgCO₂e) | 4.656 kg | 0.266 kg | old lab Desktop -> modern laptop |
| Emissions LLM (kgCO₂e) | 0.324 kg | 0.028 kg | GPT-5 -> GPT-4-o-mini |
| **Total Emissions (kgCO₂e)** | **132.518 kg** | **24.784 kg** | |

Switching to the new, improved workflow would result in a six-fold reduction in Emma's
 carbon emissions. Particularly, moving from storing data on HDDs to a hybrid storing
 approach that includes both HDDs and LTO-tapes has the greatest impact on lowering emissions.

## Steps to reduce emissions

Emma is happy with her carbon footprint after adopting the new workflow.
 Building on this initial success, she has also identified several additional strategies
  to further minimise her digital carbon footprint:

- Schedule to run her scripts for then the grid is cleanest
- Use compression technique to further reduce the size of her stored data
- Identify and delete dark data (data that is stored but never used again)
- Process the data before uploading to cloud to reduce storage requirements
- Change which LLMs models she uses based on the task complexity
- Make use of tools such as [EcoLogits](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 (open-source python library to estimate the carbon footprint of inference queries made
 to LLMs) and online LLM carbon emissions leaderboards

## References

1. [Woo, N.H. A comparative study of AI and human programming on environmental
 sustainability. Sci Rep 15, 39182 (2025). https://doi.org/10.1038/s41598-025-24658-5](https://www.nature.com/articles/s41598-025-24658-5)
