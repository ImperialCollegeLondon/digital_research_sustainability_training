---
title: "Case Study 4 - Heterogeneous Computing User"
teaching: 20 # teaching time in minutes
exercises: 10 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What are the sustainability considerations related to using heterogeneous computing architectures,including graphical processing units (GPU), tensor cores and other alternative hardware?
- What are the practical implications for their use in machine learning and general single instruction multiple data (SIMD) computations?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Introduce a representative research case study relating to heterogeneous Computing, where GPUs are used to train and deplioy a deep leaning artificial neural network (ANN) application.
- Discuss some general guidelines for estimating your carbon impact using GPU hardware.
- Consider strategies for reducing carbon impact without sacrificing the benefits of using this class of hardware in machine learning applications.

::::::::::::::::::::::::::::::::::::::::::::::::

## Introduction

Miguel is an MLOps engineer embedded in an applied computationsl neuroscience department, whose applications make heavy use of heterogeneous compute hardware such as GPUs and neuromorphic processors. While the use of GPUs and other exotic hardware is crucial for demanding SIMD tasks, he is mindful that his particular domain of work is disproportionately carbon-intensive.

His primary responsibilities include the deployment of cutting edge deep learning models and neuromphic simulations to dedicated performant hardware, and periodically maintaining these models to add features and prevent model drift. The sheer size of the models, and the vast amounts of data used to train them, mean that any procedure he performs must be carefully planned in advance, as mistakes are both financially and environmentally expensive.

To do his work, Miguel has access to a bank of top-of-the-line NVIDIA GPUs in his institution's HPC cluster, but also works on various GPU-equipped workstations throughout the department. Furthermore, larger jobs are offloaded to a dedicated external GPU cluster. 

## Pre-Job Analysis

- Determine FLOPS and memory requirements of the job
- How does this scale with layer width and dataset size?
- What is the granularity of your parameter sweep?

## Digital Waste Reduction

- Is a new model necessary, or can an existing model be adapted?
- Does it need to be trained from scratch, or can transfer learning be used?
- Does the entire model need adjustment, or only part of it?
- Can training end early on convergence?
- Contingency planning, such as training checkpoints and backups
- Curation of artifacts, to reduce duplicate runs
