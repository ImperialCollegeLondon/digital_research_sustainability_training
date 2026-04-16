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
not be necessary to train the model from scratch if transfer learning can be utilised.
He takes a look at the model's architecture, and notes that it is very large for its
stated purpose, with many channels per convolutional layer, and very wide fully
connected layers in the head. He realises that his workstation's GPUs will not have
enough memory to train the model efficiently in its current form.

For rough comparison, he approximates the environmental impact of retraining the model
based on the impact of training the original model. He remembers that the previous job
ran for approximately 72 hours, and used the Azure (Southern UK) datacentre with the
following hardware:

- $64$ GB of available host RAM
- Eight virtual cores of an Intel Xeon Platinum 8260 CPU
- One whole NVIDIA Tesla V100 GPU ($16$ GB memory variant)

Using the [Green Algorithms Calculator](https://calculator.green-algorithms.org/), he
estimates that $30.57$ kWh of energy was required to train the model, with a carbon
footprint of $7.06$ kgCO2e.

Miguel's first option is familiar to him: offload the work to a cloud GPU compute
provider. In his searches, he is able to find the hardware configuration for several
candidates by looking in documentation and datasheets. He consults the
[MLPerf Power](https://mlcommons.org/working-groups/benchmarks/power/) datasets of
whole-system inference power usage, and finds the energy efficiency for representaive ML
models $Samples/Joule = (Samples/second)/Watts$ for some of the candidate datacentres,
helping him to choose a favourite.

Alongside this, he considers a second option: whilst his personal workstation's GPU is
far from cutting-edge, it is by no means obsolete. He knows from experience that newer
does not automatically mean greener, and keeps this in mind during pre-job analysis,
looking for oppurtunities to make the model lean enough to run on his GPU.

## Analysis

For the next step, Miguel begins to quantify the computational resources required to
train the modified model. With bytes per value $b = 4$, the number of trainable
parameters $P ≈ 26,000,000$, the batch size $M = 256$ and the number of activation state
variables for all layers $N ≈ 11,000,000$:

| Memory Type      | Formula             | Size (bytes)   |
| ---------------- | ------------------- | -------------- |
| Parameters       | $P \cdot b$         | 104,000,000    |
| Gradients        | $P \cdot b$         | 104,000,000    |
| Optimiser State  | $P \cdot k \cdot b$ | 0              |
| Activation State | $M \cdot N \cdot b$ | 11,264,000,000 |

An extra $20\% ≈ 2,294,400,000$ bytes overhead for internal ML framework usage is also
included, totalling approximately $12.8$ GB. In general, there is an optimiser memory
factor $k$, but plain stochastic gradient descent (SGD) has no internal state, hence
$k = 0$ for now. With this estimation framework, he is able to know upfront roughly how
much GPU memory the job will require, as a function of batch and layer size.

Finally, Miguel notices that the training script of the base model was very crude, and
simply passed through the entire dataset through the model, with a fixed batch size,
for exactly 100 epochs of SGD. No regularisation schemes were used. Whilst the initial
decision to use the SGD optimiser reduces the memory required to train the model, via
$k = 0$ above, the prospect of earlier convergence using an alternative optimiser with
$k > 0$ may make the memory increase overall worthwhile.

## Taking Action

From his observations, Miguel formulates a plan. It is clear to him that it is entirely
unnecessary to train a new model from scratch, given the prior model is already quite
competent at processing cats. The existing model can readily be adapted by appending a
new head for cat bounding-boxes, and transfer learning techniques can be utilised to
further fine-tune the model to a reasonable accuracy.

He begins experimenting, appending the new bounding-box head and starting training,
keeping the trainable parameters in the body fixed, and gradually relaxing them as
training progresses. He modifies the training script to back up training state after
each epoch, to avoid starting again on software crash or hardware failure. He is able
to greatly increase convergence rate with a moderate increase in required memory
($k = 2$ in the memory equations) using the more sophisticated Adam optimiser, and
further improves it by adding learning rate decay. With convergence rate noticeably
increased, he adds logic to terminate early once the model's loss function converges.
The 32-bit floating-point numbers for activation state and gradients are switched to
16-bit, increasing operator speed and halving the memory required for both.

Based on experience on similar jobs, Miguel expects at least a 15x increase in training
speed on similar hardware. Plugging the new runtime estimate of 10 hours into the
[Green Algorithms Calculator](https://calculator.green-algorithms.org/), his new
estimated energy usage is $4.25$ kWh, with a carbon footprint of $0.98$ kgCO2e from
these changes alone.

Revisiting the earlier issue of model size, Miguel wonders if the model can be pruned
to enable training on his workstation, instead of relying on the cloud provider. Noting
again that the model is very large for its stated purpose, Miguel adds L1 (Lasso)
regularisation to reduce redundant activation, allowing many (now-unused) activation
units to be removed from the model entirely, resulting in a $20\%$ memory saving.

With the model now small enough to run efficiently on his workstation, Miguel runs
a short test-run to check that all is well before the main training run. He notes that
even on his relatively small GPU, the model is not utilising his GPU entirely. Since a
partially-occupied GPU is disproportionally less efficient than an occupied one, he
estimates the memory requirements of this revised model, with the aim of maximising
batch size to better-utilise the GPU. With new values $b_{16} = 2$, $b_{32} = 4$,
$P ≈ 20,800,000$, $k = 2$, $M = 256$ and $N ≈ 8,800,000$:

| Memory Type      | Formula                  | Size (bytes)   |
| ---------------- | ------------------------ | -------------- |
| Parameters       | $P \cdot b_{32}$         | 83,200,000     |
| Gradients        | $P \cdot b_{16}$         | 41,600,000     |
| Optimiser State  | $P \cdot k \cdot b_{32}$ | 166,400,000    |
| Activation State | $M \cdot N \cdot b_{16}$ | 4,505,600,000  |

and extra $20\% ≈ 959,360,000$ bytes overhead, totalling approximately $5.4$ GB only.
Indeed, Miguel finds he can increase batch size even up to $M = 728$ before the $16$ GB
of memory from the previous job comes close to full, further increasing job speed.

TODO: Add discussion around execution considerations.
Naive implementation would require large GPU resources,
clever approach is small enough to maybe run locally.

Discuss considerations around:

- cloud vs local execution,
- operational vs embedded
- potential demand shifting
