---
title: "Case Study 4 - GPU Computing User"
teaching: 20 # teaching time in minutes
exercises: 10 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the sustainability considerations related to using heterogeneous computing
  architectures, including graphical processing units (GPU), tensor cores and other
  alternative hardware?
- What are the practical implications for their use in machine learning and general
  single instruction multiple data (SIMD) computations?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative research case study relating to heterogeneous Computing,
  where GPUs are used to train and deploy a deep leaning artificial neural network
  (ANN) application.
- Discuss some general guidelines for estimating your carbon impact using GPU hardware.
- Consider strategies for reducing carbon impact without sacrificing the benefits of
  using this class of hardware in machine learning applications.

::::::::::::::::::::::::::::::::::::::::::::::::

## Scenario

Miguel is an [MLOps](https://en.wikipedia.org/wiki/MLOps) engineer embedded in an
applied computational neuroscience department, whose applications make heavy use of
heterogeneous compute hardware such as GPUs and neuromorphic processors. While the use
of this hardware is crucial for demanding [single instruction multiple data (SIMD)](
https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) tasks, he is mindful
that his domain of work is often disproportionately carbon-intensive. The sheer size of
the models, and the vast amounts of data used to train them, mean that any procedure he
performs must be carefully planned in advance, as mistakes are costly.

His primary responsibilities are:

- The deployment of cutting edge deep learning models
- The curation and storing of large datasets
- Periodic maintainance of models to add features and prevent model drift

To do his work, Miguel also purchases and maintains top-of-the-line GPU and fileservers,
whilst safely disposing retired equipment. The largest jobs are offloaded to a dedicated
cloud GPU cluster, and datasets are periodically backed up in the cloud.

Miguel is tasked with adding new functionality to a resource-hungry model deployed in
the cloud. Currently the model performs simple detection of cats in images, but Miguel
needs to augment the model to produce bounding boxes.

::::::::::::::::::::::::::::::::::::: challenge

## Identify Scope 2 Emissions

What Scope 2 emissions under the GHG protocol can you identity from Miguel's work?

:::::::::::::::::::::::: solution

- Training a model on the local workstations
- Training and deploying a model to the cloud
- Running local dataset backup servers
- Dataset cloud backups

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

## Identify Scope 3 Emissions

What Scope 3 emissions under the GHG protocol can you identity from Miguel's work?

:::::::::::::::::::::::: solution

- Updating GPUs and fileserver hardware
- Disposal of retired hardware

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

## Collecting Information

Miguel finds that the model was highly trained with vast quantities of real animal
images, and is already quite competent at feline-based image processing. The training
script is very crude, however, and simply passes through the entire dataset through
for 100 epochs of stochastic gradient descent (SGD).

He takes a look at the model's architecture, and notices that it is very large for its
stated purpose, with many channels per convolutional layer, and very wide fully
connected layers in the head. He realises that his workstation's GPUs may not have
enough memory to train the model effectively in its current form, and begins to
consider his options.

The first option is familiar to Miguel: offload the work to a cloud GPU compute
provider. He browses them, in turn, and is able to find the hardware configuration for
most of them from datasheets and documentation. Knowing that FLOPs/Watt is a poor
surrogate for total power usage in deep learning, he consults public datasets measuring
whole-system power usage during inference, such as the
[MLPerf Power](https://mlcommons.org/benchmarks/inference-datacenter/) dataset. He is
able to find the hardware configuration of an acceptible provider, and notes that
`Samples/Joule := (Samples/s)/(Watts) = 9.89`.

Alongside this, he considers a second option: whilst his personal workstation's GPU is
far from cutting-edge, it is by no means obsolete. He knows from experience that newer
does not automatically mean greener, and keeps in mind during pre-job analysis, looking
for oppurtunities to make the model lean enough to run on his GPU.

## Analysis

- What are the FLOPs and memory requirements of the job?
- How does this scale with layer width and dataset size?
- Can floating point precision be reduced?

- FLOPs can help predict scaling performance (estimate runtime before run, useful on HPC)
- but can't predict carbon usage alone
- whole system measurement needed (MLPerf Power)

## Taking Action

- Is a new model necessary, or can an existing model be adapted?
- Does it need to be trained from scratch, or can transfer learning be used?
- Does the entire model need adjustment, or only part of it?

- What is the granularity of your parameter sweep?
- Can training end early on convergence?

- What contingency plans are in place (training checkpoints, data backups, ...)?

::::::::::::::::::::::::::::::::::::: challenge

## Identify Wasteful Computing

Given these requirements, what changes can Miguel make to help bring down the
model's carbon footprint, with minimal effect on its accuracy?

:::::::::::::::::::::::: solution

- Use transfer learning (we are still working with cats, after all).
- Don't adjust the whole model (we only need a new bounding box head).
- Quit early once converged (faster in transfer learning).
- Use sparsity-inducing regularisation techniques. This allows us to...
- Prune weak/redundant neurons/channels, creating a leaner model.
- Any others you notice?

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::
