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

Hugh starts by doing research some background reasearch about the two clusters he uses.

Cluster 1 is based in London. It doesn't publish any sustainability information. The
documentation pages provide some lists of the available hardware but these are fairly
high level and don't include specific CPU or server models. Electricity for this cluster
is backed by renewable energy certificates.

Cluster 2 is based in Wales. It's documentation has some dedicated information on
sustainability including a GHG analysis of the cluster. This includes an embodied
emissions analysis as well as total power usage. Most usefully Hugh finds that the
cluster provides a tool for users to estimate the carbon emissions of their workloads.
This tool has been tested and calibrated for the cluster so should be fairly accurate.

Hugh then considers each of the emissions sources in turn.

### Electricity usage from HPC workloads

Hugh realises that carbon emissions associated with his HPC usage directly related to
his level of usage. Currently Hugh is fairly sure he uses cluster 2 the most but he
doesn't track exactly how much and what workloads he runs. Collecting this data will be
an important first step

Even without detailed data Hugh is confident that his simulation workloads form more 90%
of his cluster usage. As the data analysis workflows also tend to be more diverse he
decides to focus his initial efforts on his simulation workloads as he will get the most
impact from improving those.

Hugh also notes that the of his simulation workloads run for at least 48 hours and he
has no control over when they start running. He therefore concludes that there is little
scope to exploit demand shifting to reduce carbon intensity.

### Embodied Emissions from HPC facilities

Whilst the embodied emissions for the clusters are relevant to calculating the carbon
impact of his work, Hugh notes that these are a sunk cost that he is unable to impact at
this point. Cluster 2 provides some data but Cluster 1 doesn't provide nearly enough
information to make much headway. Hugh emails the admins of Cluster 1 but they're unable
to provide him with more information. Based on this Hugh decides not to consider
embodied emissions in his analysis.

## Analysis

For the next two weeks Hugh keeps track of the workloads that he runs on the different
clusters. He tracks the total cpu-hours spent on different clusters and the different
simulation codes used on each one.

| Cluster | Workload | Total CPU-hours | Notes |
| --- | --- | ---: | --- |
| Cluster 1 | Simulation Code 1 | 9000 | Self-compiled |
| | Simulation Code 2 | 6,000 | |
| | Simulation Code 3 | 4,000 | |
| Cluster 2 | Simulation Code 1 | 12,000 | Self-compiled |
| | Simulation Code 2 | 8,000 | |
| | Simulation Code 3 | 15,000 | |

Using the calculation tool provided by Cluster 2 Hugh is able to get an estimate of the
carbon emissions associated with all of his work there. The total amount is 1,200
kgCO2e. Hugh also decides to estimate his emissions from Cluster 1 by scaling the
emissions of Cluster 2 by the difference in CPU-hours used on both systems - he's aware
that Cluster 1 and Cluster 2 are quite different and so this value for Cluster 1 is very
approximate but still thinks it's useful to know. This gives a total of 651 kgCO2e for
Cluster 1.

Whilst collecting the above data Hugh also notes that around 3,000 CPU-hours were wasted
on workloads that he hadn't setup properly and which had to be repeated. He estimates
this corresponds to around 100 kgCO2e.

Finally Hugh, takes his total emissions figure and tries to better understand what it
means by comparing with other emissions sources. He finds that arond 1,800 kgCO2e is
approximately equivalent to driving for 6,000 miles or more in a petrol fueled car.

## Taking Action

Based on the data gathered above Hugh observes:

- He spends the most cpu-hours on Cluster 2.
- He spends the most cpu-hours using Simulation Code 1.

This suggests Hugh will get the most impact out focussing his efforts on these areas.
Hugh wants to be able to measure the impact of any changes he makes which can be best
done using the emissions tooling on Cluster 2. He's also confident that most changes he
makes on Cluster 2 will be transferable to Cluster 1 even if he can't measure the impact
so directly there.

In order to minimise his emissions Hugh realises he can both improve the efficiency of
the simulations he performs and try to reduce the overall amount of simulation.

### Reducing Simulation

The 3,000 wasted cpu-hours of simulation are an obvious target initial target. Hugh
reviews the jobs that went wrong and identifies the root causes. He then adjusts his
workflows to prevent them happening again. To help in the future, he agrees with a
member of this research group that they will double check each others simulation inputs
before starting significant new simulation projects. With these measures Hugh estimates
that he may be able to reduce his wasted cpu-hours by half.

Hugh's work requires running simulations for many individual timesteps but it's often
not obvious in advance how many timesteps are required. Reviewing some of his recent
projects Hugh concludes that by monitoring his workloads more closely he can terminate
some of them earlier. Hugh estimates this could reduce the cpu-hours used per project by
10%.

### Optimising Workloads

Hugh notes that Simulation Code 1 is less commonly used in his field and so he has had
to compile it himself on both clusters. Hugh doesn't have a lot of experience doing this
and had to piece together how to do it with some online searching and notes from a old
colleague. Hugh reaches out the authors of the code who are able to give him some
general advice but can't offer tailored help. Hugh also gets in touch with the local
research software engineering team at his institute who are more familiar with the
clusters and are able to provide a small amount of effort to help. Together they
identify some tweaks to the compilation and manage to get a 5% speed boost.

To better understand the differences between the codes and clusters he uses Hugh carries
out some performance benchmarking. He runs simulations with all of his simulation codes
across both clusters. Hugh carefully designs these simulations to be short, so as to not
generate too many emissions, but representative of typical workloads. A key finding he
identifies is that Simulation Code 1 runs 15% faster on Cluster 2 when using the same
number of CPU cores. Meanwhile, Codes 2 and 3 don't seem to show much difference between
the two clusters. Hugh realises he can work more efficiently by shifting as much of
using work using Simulation Code 1 to Cluster 2 as possible.

Most of Hugh's simulations require him to run jobs that in parallel using many cpu cores
and cluster nodes at the same time. Hugh is familiar with the fact that as his jobs use
increasing amount of resources there is a trade-off in computational efficiency. With
some of his current projects Hugh realises he has not put much thought into choosing the
resources used. Taking one of his recent projects Hugh carries out some benchmarking by
running the same simulation using different sets of computational resources. He
identifies that for that particular set of simulations he could have reduced his of
computational resources by 20% whilst only losing 10% speed. Hugh resolves to carry out
this sort of benchmarking for all new projects he starts to identify a good trade-off
between speed and efficiency.

### Outcomes

Putting all of the above steps together Hugh estimates that he can reduce his overall
use of cpu-hours by 25% across both clusters. This would result in a saving of ~450
kgCO2 from his two week data collection period. Hugh also continues to collect data on
his HPC workloads so that he can assess the impact of the changes he's made in the
future.

Hugh shares his findings with his colleagues in their regular group meeting. Several of
his colleagues use the same clusters and simulation codes so are as him so are able to
easily make use of Hugh's work.

Hugh also contacts the team maintaining Cluster 1 highlighting the utility of tools to
measure carbon intensity data. The team promises to explore how they can add some more
functionality to Cluster 1.
