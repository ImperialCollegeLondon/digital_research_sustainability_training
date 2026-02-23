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

Miguel is tasked with deploying a new model to the cloud, based on the architecture of
an existing model he deployed last year. The existing model performs simple detection of
cats in images, but the new model must produce bounding boxes.

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

Miguel finds that the previous model was highly trained with vast quantities of real
animal images, and is already quite competent at feline-based image processing. It may
not be necessary to train the model from scratch if transfer learning is utilised.

He takes a look at the model's architecture, and notices that it is very large for
its stated purpose, with many channels per convolutional layer, and very wide fully
connected layers in the head. He realises that his workstation's GPUs may not have
enough memory to train the model effectively in its current form, and begins to
consider his options.

The first option is familiar to Miguel: offload the work to a cloud GPU compute
provider. He browses them, in turn, and is able to find the hardware configuration for
most of them from datasheets and documentation. Knowing that FLOPs/Watt is a poor
surrogate for total power usage in deep learning, he consults public datasets measuring
whole-system power usage during inference, such as the
[MLPerf Power](https://mlcommons.org/working-groups/benchmarks/power/) dataset. He is
able to find the hardware configuration of an acceptible provider, and notes that
$Samples/Joule = (Samples/s)/(Watts) ≈ 9.89$.

Alongside this, he considers a second option: whilst his personal workstation's GPU is
far from cutting-edge, it is by no means obsolete. He knows from experience that newer
does not automatically mean greener, and keeps in mind during pre-job analysis, looking
for oppurtunities to make the model lean enough to run on his GPU.

## Analysis

For the next step, Miguel begins to quantify the computational resources required to
modify the model. He makes a rough total memory estimate; with the number of trainable
parameters $P$, the sum of all layer sizes $N$, the batch size $M$, a constant $j$
depending on the chosen optimiser, a constant $k$ depending on the unit model, and
bytes per number as $b$, he reserves memory (in bytes) for:

- Parameters: $P \cdot b$
- Parameter gradients: $P \cdot b$
- Optimiser state: $P \cdot j \cdot b$
- Activations: $M \cdot N \cdot k \cdot b$
- An extra $20%$ for ML frameworks usage

With this estimation framework, he is able to know (before submitting) roughly
how much GPU memory the job will require, as a function of batch and layer size. Next,
Miguel roughly estimates the computational complexity of the model. Whilst FLOPs is a
poor surrogate metric for carbon footprint, it can help for estimating run duration
scaling, which is useful to prevent wasting computation by reserving enough time for
the cloud job whilst experimenting.

Finally, Miguel notices that the training script of the base model was very crude, and
simply passed through the entire dataset through the model for exactly 100 epochs of
stochastic gradient descent (SGD). No regularisation schemes were used. Whilst the
choice of optimiser affects the memory required to train the model, via $j$ above, the
possible energy savings of early convergence may be overall worth it.

## Taking Action

From his observatons, Miguel formulates a plan. It is clear to him that is entirely
unnecessary to train a new model from scratch, given the prior model is already quite
competent at processing cats. The existing model can readily be adapted by appending a
new head for cat bounding-boxes, and transfer learning techniques can be utilised to
further fine-tune the model to a reasonable accuracy.

He begins experimenting, appending the new bounding-box head and starting training,
keeping the trainable parameters in the body fixed, and gradually relaxing them as
training progresses. In doing so, he notices that the model comes close to converging
well before the programmed 100 epochs. He modifies the training script to terminate
early, once the model's loss function converges, and back up training state after each
epoch, to avoid starting again on software crash or hardware failure. He is able to
further reduce training time with a moderate increase in required memory ($j$ in the
memory equations) using a more sophisticated optimiser, and finds this extra memory
requirement is easily offset by reducing floating-point number precision at practically
no detriment to model accuracy.

Finally, revisiting the earlier issue of model size, Miguel wonders if the model can be
pruned to enable training on his workstation, instead of relying on the cloud provider.
Noting again that the model is very large for its stated purpose, Miguel adds L1 (Lasso)
regularisation to reduce redundant activation, allowing many (now-unused) activation
units to be removed from the model entirely, promoting a leaner and more power-efficient
model in the process.
