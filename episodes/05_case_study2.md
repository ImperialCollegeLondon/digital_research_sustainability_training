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
- Data storage: She backs up the raw sequencing data (approx. 700 GB) to a cloud provider.

Emma's Workflow:

- She uses cloud-based LLMs to write her scripts for processing and analysing data.
This often requires many queries and iterations.
- She keeps every version of her raw data in the cloud, and rarely deletes old files.
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

## Collecting more information

### Data storage

Emma wants to move some of her research data to a physical storage for better security.
She has heard from other colleagues that she could choose between an external hard drive
 (HDD), a Solid State Drive (SDD) or an LTO magnetic tape. However, she is unsure
 about the enivronmental impacts of these.

Emma did some research on the carbon footprint associated with the three storage types
 and found the following:

- SDDs are the most carbon efficient when in operation, but their manufacturing produces
 significantly more emissions.
- HDDs have a lifespan of 5-10 years, similar to that of SDDs. Their embodied emissions
 are signifcantly lower than that of SDDs but operational emissions are higher.
- Tape storage has a longer lifespan (10-15 years), with modern ones reaching
 up to 30 years. However, moving and accessing data on a LTO tape is slow.

The carbon emissions associated with the three storage types are summarised below:

| Category | SDD | HDD | LTO tape |
| :--- | :--- | :--- | :--- |
| **Embodied Carbon (kg CO₂e per TB)** | High (16-32 kg)^1^ | Moderate (2-4 kg)^1^ | Low (~0.07 kg)^3^ |
| **Operational Carbon (kg CO₂e per TB)** | Low (2-5 kg)^1^ | Moderate - High (2-16 kg)^1,2^ | Low (~0 kg) |
| **Lifespan** | 5–10 years | 5-10 years | 30+ years |

In contrast, she found the carbon emissions associated with cloud data storage are
 estimated between 2-40 kg CO₂e/TB/year (according to
 a WholeGrain [report](https://www.wholegraindigital.com/digitaldeclutter/#cloud-storage)
 and [Greenly](https://greenly.earth/en-gb/blog/industries/what-is-the-carbon-footprint-of-data-storage)),
 but the value depends heavily on the data center's efficiency and the region's power grid.

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

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Use of LLMs

Emma has two options for her data processing and analysis workflow:

- **Option 1**: She spends several days writing the code herself, testing it on
 the old lab Desktop. The code takes 16h to run.
- **Option 2**: She uses cloud-hosted LLMs to write the code in 2 hours but in
 order to do that she sends at least 50 large prompts to the LLM. The resulting
 code is 40% faster to run than the code she wrote herself.

Which option creates the least amount of emissions? Does the answer change
 if the lab Desktop or AI/cloud providers are powered by renewable energy?
 How about choosing different LLM models?

:::::::::::::::::::::::: solution

- inference calls: depends on the model she chooses - if a complicated task, GPT4
might be more appropriate but emits at least 5 times more carbon than humans
- inefficient code: if the code is significanlty slower and runs on the old lab desktop,
 the operation carbon (Scope 2) increases significantly over the 16h time
- reasoning LLMs can produce 3x more emissions than models that provide concise answers

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Analysis

Based on her research into the sustainability impacts of digital practices,
 Emma decides to revise her current workflow (Scenario 1) and adopt more
 environmentally conscious methods (Scenario 2). She now wants to quantify
 the difference in carbon emissions between her existing workflow and the improved one.

### Scenario 1 (current workflow)

- Emma uses a reasoning model to write her scripts, requiring 30 queries over 3h to debug.
- She backs up her entire 700 GB dataset to the cloud.
- She runs her script on the old lab Desktop, which takes 8 hours to finish.

### Scenario 2 (improved workflow)

- Emma switches to GPT-40-mini, which has lower carbon footprint per query, and
 since her computational requirements are fairly light. However, debugging now
 takes 50 queries.
- She moves 500 GB of her data onto TPO tape (data she has not used in over 6 months) and
 keeps only 200 GB on the cloud for active work.
- She runs her scripts on her modern laptop, which take 6h to finish.

::::::::::::::::::::::::::::::::::::: challenge

Given all we know about Emma's workflow, calculate the emissions associated with the current
 workflow and the improved workflow.

:::::::::::::::::::::::: solution

#### Scenario A

- emissions from using her lab old Desktop (3h to debug LLM + 8h to run script) +
 emissions from reasoning LLMs

$$
E_{total} =  E_{Desktop} + E_{LLM} \\
E_{Desktop} = \text{Computer Power Draw} + \text{Grid Carbon Intensity}
$$

**Computer Power Draw**: we can asume a 0.3 kW power draw for the
old Desktop

**Grid Carbon Intensity**: can be obtained from official grid sources (such as [EnergyDashboard](https://www.energydashboard.co.uk/live)).
For UK, we can use a value of 194 gCO₂/kW (high).

**Emissions from LLMs**: could use a tool like [Ecologits calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 to provide estimates. In Emma's case, she is using a reasoning LLM, meaning we could use
  emissions for OpenAI' GPT-5 model, which are estimated to be around 10.8 gCO₂e.

<!-- markdownlint-disable-next-line line-length -->
$$
E_{Desktop} = 0.3 \text{kW} \times (3 + 8) h \times 194 gCO₂/kW \\
E_{Desktop} = 640 gCO₂e = 0.640 kgCO₂e
$$

$$
E_{LLM} = 10.8 gCO₂e/query \times 30 queries \\
E_{LLM} = 325 gCO₂e = 0.324 kgCO₂e
$$

$$
E_{LLM+Desktop} =  E_{Desktop} + E_{LLM} \\
E_{LLM+Desktop} = 0.640 kgCO₂e + 0.324 kgCO₂e \\
E_{LLM+Desktop} = 0.964 kgCO₂e
$$

- emissions from cloud storage

They are also not straightforward to determine and are usually provided by cloud providers
 or carbon emissions tools. In Emma's case, if she is using Microsoft's Azure storage,
 the emission factor is around 0.0003037 kg/TB-hour (value otained from [Climatiq tool](https://www.climatiq.io/data/emission-factor/a76cb021-c639-4b16-bd66-038b93d85826)).
 Therefore, storing the 700 GB data there for 5 years (8760 hours/year) would generate
 the following emissions:

<!-- markdownlint-disable-next-line line-length -->
$$
E_{storage} = \text{cloud emission factor} \times \text{data size} \times \text{time} \\
E_{storage} = 0.0003037 kgCO₂e /TB-hour \times 0.7TB \times 8760 hours \times 5 \\
E_{storage} = 9.311 kgCO₂e
$$

Assumming she only runs her script once and data is stored for 5 years, the total value
for the carbon emissions from Emma's current workflow is:

$$
E_{total} = E_{LLM+Desktop} + E_{storage} \\
E_{total} = 0.964 kgCO₂e + 9.311 kgCO₂e kgCO₂e \\
E_{total} = 10.275
$$

#### Scenario B

- emissions from modern laptop (5h to debug LLM + 6h to run script) + emissions from
 smaller LLM

$$
E_{total} =  E_{Desktop} + E_{LLM} \\
E_{Desktop} = \text{Computer Power Draw} + \text{Grid Carbon Intensity}
$$

**Computer Power Draw**:  Emma is using her modern laptop, which has a lower
 power draw of ~0.1 kW/hour.

**Grid Carbon Intensity**: same value as in her current workflow

**Emissions from LLM**: in this case Emma is using a smaller LLM model, GPT4-0-mini,
 for which emissions are estimated to be around 562 mgCO₂e.

<!-- markdownlint-disable-next-line line-length -->
$$
E_{laptop} = 0.1kW/h \times (5 + 6)hours \times 194 gCO₂/kW \\
E_{laptop} = 213.4 gCO₂e = 0.213 kgCO₂e \\
$$

$$
E_{LLM} = 0.562 gCO₂e/query \times 50 queries \\
E_{LLM} = 28.1 gCO₂e = 0.028 kgCO₂e \\
$$

$$
E_{LLM+laptop} =  E_{laptop} + E_{LLM} \\
E_{LLM+laptop} = 0.213 kgCO₂e + 0.028 kgCO₂e \\
E_{LLM+laptop} = 0.241 kgCO₂e
$$

- emissions storage = emissions from cloud storage + emissions from tape storage

**Emissions form cloud storage**: using the same emission factor as in Option 1,
 storing only 200 GB data there for 5 years (8760h/year x 5 years) would generate the following
 emissions:

<!-- markdownlint-disable-next-line line-length -->
$$
E_{cloud_storage} = \text{emission factor} \times \text{data size} \times \text{time} \\
E_{cloud_storage} = 0.0003037 kgCO₂e /TB-hour \times 0.2TB \times 8760 hours \times 5 \\
E_{cloud_storage} = 2.660 kgCO₂e
$$

**Emissions form LTO magnetig tape storage**: Given magnetic tape has negligible emissions
 when idle, we can assume that the total emissions for storing data on tapes come from
 embodied emissions of magnetic tape of ~0.07 kgCO₂ per TB of data. Therefore, to store
 500 GB of data for 5 years, Emma would generate the following emissions:

$$
E_{tape_storage} = 0.07 kgCO₂e/TB/year \times 0.5TB \times 5 years \\
E_{tape_storage}  = 0.175 kgCO₂e
$$

The total emissions from storage are:

$$
E_{storage} = E_{cloud_storage} + E_{tape_storage} \\
E_{storage} = 2.660 kgCO₂e + 0.175 kgCO₂e \\
E_{storage} = 2.835 kgCO₂e
$$

Therefore, the total carbon emissions for Emma's improved workflow are:

$$
E_{total} = E_{LLM+Desktop} + E_{storage} \\
E_{total} = 0.241 kgCO₂e + 2.835 kgCO₂e \\
E_{total} = 3.076 kg CO₂e
$$

The results are summarised below:

| Scenario | **Scenario 1 (current workflow)** | **Scenario 2 (Improved workflow)** | Change |
| :--- | :--- | :--- | :--- |
| Emissions Computing (kgCO₂e) | 0.640 | 0.2134 | old lab Desktop -> modern laptop |
| Emissions LLM (kgCO₂e) | 0.324 | 0.0281 | GPT-5 -> GPT-4-o-mini |
| Emissions Storage (kgCO₂e) | 9.311 | 2.835 | 0.7 TB cloud -> 0.5 TB tape + 0.2 TB Cloud |
| **Total Emissions (kgCO₂e)** | **10.275** | **3.076** | |

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Steps to reduce emissions

Emma is happy with her carbon footprint after adopting the new workflow.
 Building on her initial success, Emma has identified several ways to further minimise
 her digital carbon footprint:

- Schedule to run her scripts for then the grid is cleanest
- Use compression technique to further reduce the size of her stored data
- Identify and delete dark data (data that is stored but never used again)
- Process the data before uploading to cloud to reduce storage requirements
- Change which LLMs models she uses based on the task complexity
- Make use of tools such as [EcoLogits](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
 (open-source python library to estimate the carbon footprint of inference queries made
 to LLMs) and online LLM carbon emissions leaderboards
- Explore parallelising her analysis scripts and running them on HPC

## References

1. [Woo, N.H. A comparative study of AI and human programming on environmental
 sustainability. Sci Rep 15, 39182 (2025). https://doi.org/10.1038/s41598-025-24658-5](https://www.nature.com/articles/s41598-025-24658-5)
