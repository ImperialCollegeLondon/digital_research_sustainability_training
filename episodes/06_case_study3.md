---
title: "Case Study 3 - HPC User"
teaching: 20 # teaching time in minutes
exercises: 10 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the sustainability considerations related to High Performance Computing?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative research case study relating to High Peformance Computing.
- Explore ways to measure and estimate carbon emissions from High Performance Computing
  clusters.
- Explore ways to reduce the carbon emissions associated with a given workload.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Hugh is a computational chemist in a research group whose work involves high fidelity
simulations of the dynamic behaviour of atomistic systems. His work requires
computational resources far beyond that of a single machine so he makes use of a number
of High Performance Computing facilities.

Hugh is working on several different research questions that requires the use of
different simulation softwares. Choice of which software to use is usually driven by
existing research data and the capabilities of different codes. Whilst he often makes
use of software that has been pre-installed by system administrators, he sometimes has
to compile packages himself.

In addition to simulation work, Hugh carries out data analysis and creates
visualisations.

Hugh has access to 2 different HPC facilities he can make use of:

- a general purpose institutional cluster offering a mix of CPUs.
- a cluster providing targeted support for the atomistic simulation community.

Both facilities are heavily subscribed and Hugh tries to maximise his throughput at all
times. Workloads on these clusters are submitted to a queue and will start running at an
unknown time. Almost all of his workloads run for at least 48 hours.

To better understand the emissions related with his work Hugh categorises his activities
under the GHG protocol.

::::::::::::::::::::::::::::::::::::: challenge

## Identify Scope 2 Emissions

What Scope 2 emissions under the GHG protocol can you identity from Hugh's work?

:::::::::::::::::::::::: solution

- Emissions from electricity usage associated with simulation workloads.
- Emissions from electricity usage associated with data analysis and visualisation
  workflows.

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Identify Scope 3 Emissions

What Scope 3 emissions under the GHG protocol can you identity from Hugh's work?

:::::::::::::::::::::::: solution

- Proportional embedded emissions from HPC facilities.

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Collecting Information

Hugh considers each of the emissions sources in turn.

- Hugh also carries out some background research about clusters he uses:
    - Cluster 1 is based in London. Doesn't publish any sustainability information.
    Lists of hardware are available online. Hugh gets in touch with the local team that
    maintains the cluster and they're able to provide him with some basic power usage
    data. Electricity for this cluster is backed by renewable energy certificates.
    - Cluster 2 is based in Wales. Has published a GHG analysis of the cluster. This
    includes an embodied emissions analysis as well as power usage. Provides a tool for
    system users to estimate the carbon emissions of their workloads.
- Electricity usage from calculations.
    - Hugh is fairly sure he uses cluster 2 more than the others but he doesn't track
    exactly how much and what workloads he runs.
    - Hugh is confident that his simulation workloads form > 90% of his cluster usage and
    he will get the most impact out of focus on those over data analysis workloads.
    - The majority of Hugh's workloads run for at least 48 hours. He therefore concludes
    that there is little scope to exploit demand shifting to reduce carbon intensity.
- Whilst the embodied emissions for the clusters are relevant to calculating the carbon
  impact of his work, Hugh notes that these are a sunk cost that he is unable to impact
  at this point. He also doesn't have much data to go on for this.

## Analysis

- Estimate total CPU usage for simulation / data analysis. For the next two weeks Hugh
  keeps track of the workloads that he runs on the different clusters. He tracks the
  total cpu-hours spent on different clusters and the different codes used on each one.

| Cluster | Workload | Total CPU-hours | Notes |
| --- | --- | ---: | --- |
| Cluster 1 | Simulation Code 1 | 9000 | Self-compiled |
| | Simulation Code 2 | 6,000 | |
| | Simulation Code 3 | 4,000 | |
| Cluster 2 | Simulation Code 1 | 12,000 | Self-compiled |
| | Simulation Code 2 | 8,000 | |
| | Simulation Code 3 | 15,000 | |

- Whilst collecting the above data Hugh also notes that around 3,000 CPU-hours were
  wasted on workloads that he hadn't setup properly and which had to be repeated.
- Thanks to the tooling on Cluster 2, Hugh is able to produce a total figure for the
  carbon emissions of his work there

- Hugh also researches the average carbon intensities of different regions.
    - Cluster 1 - 100 gCO2e/kwh
    - Cluster 2 - 60 gCO2e/kwh

## Taking Action

Based on the data gathered above Hugh observes:

- He spends the most cpu-hours on Cluster 2.
- He spends the most cpu-hours using Simulation Code 1.
- The carbon intensity of the electricity for Cluster 2 is significantly lower.

Hugh wants to be able to measure the impact of any changes he makes so he decides to
focus on Cluster 2 as this has tooling to support accurately measuring carbon emissions.
He's confident that any changes he makes on Cluster 2 will be transferable to Cluster 1
even if he can't measure the impact so directly there.

Actions he can take (to be expanded):

- Sanity check his workloads before - to reduce wasted CPU-hours. Pairs up with
  colleagues so they can all check each others.

- Optimise compilation - Simulation Code 1 is the one he uses the most so it's worth
  looking if there are any easy performance boosts from tweaking the compilation. Asks
  the code authors and his friendly local RSE team for help. Gets a 5% speed boost by
  changing some compiler flags and linking a better optimised library.

- Compare code performance on different systems - Hugh identifies that Simulation Code 1
  is 20% faster on cluster 2 with the same number of CPU cores. Codes 2 and 3 don't show
  much difference. Hugh shifts to prioritising running Simulation Code 1 on Cluster 2.

- Optimise workloads - parallel execution has diminishing returns as more resources are
  applied to the same size problem. Hugh adopts the practice of carrying out performance
  profiling of his different simulation setups before commiting to production
  simulations to identify the best tradeoffs between simulation speed and carbon efficiency.

- Monitor workloads more closely for termination. Hugh simulates his systems for many
  timesteps but it's not clear in advance how many are required for a given study. By
  monitoring the progress of his simulations more closely, Hugh can stop running them
  sooner rather than choosing an arbitrary number of timesteps in advance.

Other actions:

- Hugh shares his findings with his colleagues and is able to easily help them make some
  small improvements.

- Hugh contacts the team maintaining Cluster 1 highlighting the utility of tools to
  measure carbon intensity data. The team promise to explore how they can add some more
  functionality to Cluster 1.
