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
  clustesr.
- Explore ways to reduce the carbon emissions associated with a given workload.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Hugh is a computational chemist in a research group whose work requires high fidelity
simulations of the dynamic behaviour of atomistic systems. His work requires
computational resources far beyond that of a single machine so he makes use of a number
of High Performance Computing facilities.

Hugh is working on several different research questions that requires the use of
different simulation softwares. Choice of which software to use is usually driven by
existing research data and the capabilities of different codes. Whilst he often makes
use of software that has been pre-installed by system administrators, he sometimes has
to compile packages himself. The data produced by his simulation work ranges from the
10s of gigabyte scale to low terabytes.

In addition to simulation work, Hugh carries out data analysis and creates
visualisations.

Hugh has access to a number of different HPC facilities he can make use of:

- a general purpose institutional cluster offering a mix of CPUs and older GPU models.
- a dedicated cluster providing access to modern Nvidia GPUs operating in Wales.
- a cluster based on a novel CPU architecture.

Hugh also access to several high powered desktops in the group lab.

To better understand the emissions related with his work Hugh categorises his activities
under the GHG protocol.

::::::::::::::::::::::::::::::::::::: challenge

What Scope 2 emissions under the GHG protocol can you identity from Hugh's work?

:::::::::::::::::::::::: solution

- Emissions from electricity usage associated with simulation workloads.
- Emissions from electricity usage associated with data analysis and visualisation
  workflows.

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

What Scope 3 emissions under the GHG protocol can you identity from Hugh's work?

:::::::::::::::::::::::: solution

- Proportional embedded emissions from HPC facilities.
- Embedded emissions of lab desktop machines.
- Embedded emissions from data storage devices used to store research data.

:::::::::::::::::::::::::::::::::
