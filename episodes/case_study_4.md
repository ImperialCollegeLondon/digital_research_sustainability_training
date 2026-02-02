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
of GPUs and other exotic hardware is crucial for demanding [single instruction multiple
data (SIMD)](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) tasks, he
is mindful that his domain of work is often disproportionately carbon-intensive.

His primary responsibilities include the deployment of cutting edge deep learning models
and neuromorphic simulations to dedicated performant hardware, and periodically
maintaining these models to add features and prevent model drift. The sheer size of the
models, and the vast amounts of data used to train them, mean that any procedure he
performs must be carefully planned in advance, as mistakes are both financially and
environmentally expensive.

To do his work, Miguel has access to a bank of top-of-the-line GPUs in his
institution's HPC cluster, but also works on various GPU-equipped workstations
throughout the department. Furthermore, larger jobs are offloaded to a dedicated
external GPU cluster.

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 1: Identify Carbon Emissions

Using the definitions of Scopes 1, 2 and 3 carbon emissions, how would you classify the
carbon emissions resulting from the following activities?

1. Training a new model on the HPC cluster
2. Updating workstation GPUs and disposing retired units
3. Data backup and curation
4. Deploying and using a new model in the cloud

:::::::::::::::::::::::: solution

1. **Scope 2**
2. **Scope 3**
3. **Scope 2** (and **Scope 3** when on-site backups are required)
4. **Scope 2**

:::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::

## Digital Waste Reduction

- Is a new model necessary, or can an existing model be adapted?
- Does it need to be trained from scratch, or can transfer learning be used?
- Does the entire model need adjustment, or only part of it?
- What are the FLOPS and memory requirements of the job?
- How does this scale with layer width and dataset size?
- What is the granularity of your parameter sweep?
- Can training end early on convergence?
- What contingency plans are in place (training checkpoints, data backups, ...)?
- Can artifacts be better curated, to reduce duplicate runs?

::::::::::::::::::::::::::::::::::::: challenge

## Challenge 2: Identify Wasteful Computing

We are tasked with adding new functionality to a very resource-hungry deep learning
model deployed in the cloud. Currently the model performs simple detection of cats in
images, but we want to augment the model to produce bounding boxes. The width of the
layers is very large, with many convolutional channels each. The model is highly trained
with vast quantities of animal images, and is already quite competent at feline-based
image processing. The training script is quite crude, and simply passes through the
entire dataset through for 100 epochs.

Given these requirements, can you spot any changes we can make to help bring down the
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
