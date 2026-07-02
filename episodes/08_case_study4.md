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

Miguel is an [MLOps] engineer embedded in an applied computational neuroscience
department, whose applications make heavy use of heterogeneous compute hardware such as
GPUs and neuromorphic processors. While the use of this hardware is crucial for
demanding Single Instruction Multiple Data ([SIMD]) tasks, he is mindful that his domain
of work is disproportionately carbon-intensive. The sheer size of the models, and the
vast amounts of data used to train them, mean that any procedure he performs must be
carefully planned in advance, as mistakes are costly.

His primary responsibilities are:

- The deployment of cutting edge deep learning models
- Periodic maintenance of models to add features and prevent model drift
- The curation and storing of large datasets

To do his work, Miguel often trains and fine-tunes models on his local GPU-equipped
workstation when the job is small enough, and offloads larger jobs to dedicated cloud
GPU compute providers.

Miguel is tasked with deploying a new model to the cloud, based on the architecture of
an existing model he deployed last year. The existing model was trained with vast
quantities of real animal images, and is already quite competent at feline-based image
processing. It performed simple detection of cats in images, but the new model must
produce bounding boxes. The previous training script was very crude, and simply passed
the entire dataset through the model in batches of $256$, for exactly $100$ epochs of
stochastic gradient descent (SGD), with no regularisation.

Based on his experience preparing the previous model, he knows that his workstation's
GPU will not have enough memory to train the similarly-sized derived model with a
reasonable batch size in its current form. Like last time, he will aim to offload the
training of the model to a cloud GPU compute provider, however local development and
fine-tuning will still be possible using a very small batch size.

[MLOps]: https://en.wikipedia.org/wiki/MLOps
[SIMD]: https://en.wikipedia.org/wiki/Single_instruction,_multiple_data

## Collecting Information

::::::::::::::::::::::::::::::::::::: challenge

### Data Exploration (20 minutes)

Miguel's work consists of developing and fine-tuning the model on his local workstation,
followed by training and deploying the model on cloud infrastructure. How might Miguel
estimate the associated carbon emissions? What data will be required, and how might he
find such data?

::::::::::::::::::::::::::::::: solution

There are various methods Miguel can build a picture of carbon emissions with, including
real-time measurement, prediction tools and extrapolaring from known data.

- Realtime measurement can be performed locally using either a physical meter measuring
  power usage directly from the mains socket, or by wrapping code with power monitoring
  software packages such as [Code Carbon]. Realtime measurement of cloud jobs may also
  be possible, since many cloud providers offer infrastructure for querying live energy
  usage of running jobs.
- Carbon data from training the previous model may be used as surrogate data for the
  new model, given their near-identical architecture. If carbon data for the previous
  run was not recorded, then predictive tools can be used to estimate it. For example,
  the [Green Algorithms Calculator] may be used to estimate carbon data of a previous
  job given its runtime, server location and compute requirements.

[Green Algorithms Calculator]: https://calculator.green-algorithms.org/
[Code Carbon]: https://github.com/mlco2/codecarbon

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Analysis

::::::::::::::::::::::::::::::::::::: challenge

### Estimating Emissions (20 minutes)

Miguel computes a few simple estimates up-front to give a rough idea of the carbon
footprint of a full training run. Using the following information, try to replicate the
results of Miguel's estimations.

#### Local Development and Testing

Miguel is unable to train the model at target batch size of $256$ on his workstation,
but information from a smaller run might still be useful for estimating the carbon
emissions of the larger run. On his workstation, he times how long it takes to complete
a single training epoch, using $1\%$ of the training data, with a batch size of $32$.
The elapsed time comes to $5.76$ hours.

**How might this information help in estimating emissions in the full run? Try forming
an estimate for carbon emissions of the full run using this information alone.**

#### Previous Training Runs

Given the similarity of the new model to the old one, data obtained during the training
run of the previous model may be used as surrogate data for estimating the carbon usage
of the newer model. He remembers that the previous job ran for approximately 72 hours,
and used the Azure (Southern UK) datacentre with the following hardware:

- $64$ GB of available host RAM
- Eight virtual cores of an Intel Xeon Platinum 8260 CPU
- One whole NVIDIA Tesla V100 GPU

**Use the [Green Algorithms Calculator] to estimate the carbon footprint of training the
new model using information obtained from training the similar previous model. For this
exercise, select data version `v3.0` in the top right of the calculator page.**

::::::::::::::::::::::::::::::: solution

Miguel's results for the two estimate methods are as follows.

#### Local Development and Testing

Miguel can use this information to get another rough estimate of the time required to
completely train the model. Given that only $1\%$ of training data was used, the time
required for $100\%$ of data would be about $576$ hours. Furthermore, given the batch
size used in the test was $32$, eight times lower than the target batch size of $256$,
the time required to train the full model with the final batch size will be around
$576 / 8 = 72$ hours.

#### Previous Training Runs

Whilst Miguel does not have actual measurements for carbon emissions whilst training the
older model, he has enough information to compute an estimate retroactively using, for
instance, the [Green Energy Calculator]. Plugging in the runtime, hardware and location
of the job into the calculator, it estimates that $30.55$ kWh of energy was required to
train the model, with a carbon footprint of $7.06$ kgCO2e.

::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

## Taking Action

From his observations, Miguel formulates a plan. It is clear to him that it is entirely
unnecessary to train a new model from scratch, given the prior model is already quite
competent at processing cats. The existing model can readily be adapted by appending a
new head for cat bounding-boxes, and transfer learning techniques can be utilised to
further fine-tune the model to a reasonable accuracy.

Miguel begins to quantify the computational resources required to train the revised
model. With bytes per value $b = 4$, number of trainable parameters $P ≈ 26,000,000$,
batch size $M = 256$ and number of activation state variables for all layers
$N ≈ 11,000,000$:

| Memory Type      | Formula             | Size (bytes)   |
| ---------------- | ------------------- | -------------- |
| Parameters       | $P \cdot b$         | 104,000,000    |
| Gradients        | $P \cdot b$         | 104,000,000    |
| Optimiser State  | $P \cdot k \cdot b$ | 0              |
| Activation State | $M \cdot N \cdot b$ | 11,264,000,000 |

An extra $20\% ≈ 2,294,400,000$ bytes overhead for internal ML framework usage is also
included, totalling approximately $12.8$ GB. In general, there is an optimiser memory
factor $k$, but plain SGD has no internal state, hence $k = 0$ for now. With this
estimation framework, he is able to know upfront roughly how much GPU memory the job
will require, as a function of batch and layer size. Whilst the SGD optimiser reduces
the memory required to train the model, via $k = 0$ above, the prospect of earlier
convergence using an alternative optimiser with $k > 0$ may make the memory increase
overall worthwhile.

He begins experimenting, appending the new bounding-box head and starting training,
keeping the trainable parameters in the body fixed, and gradually relaxing them as
training progresses. He modifies the training script to back up training state after
each epoch, to avoid starting again on software crash or hardware failure. He is able
to greatly increase the convergence rate with a moderate increase in required memory
($k = 2$ in the memory equations) using the more sophisticated Adam optimiser, and
further improves it by adding a learning rate decay. With the convergence rate noticeably
increased, he adds logic to terminate early once the model's loss function converges.
The 32-bit floating-point numbers for activation state and gradients are switched to
16-bit, increasing operator speed and halving the memory required for both.

Based on experience on similar jobs, Miguel expects at least a 15x increase in training
speed on similar hardware. Plugging the new runtime estimate of 10 hours into the
[Green Algorithms Calculator], his new estimated energy usage is $4.24$ kWh, with a
carbon footprint of $0.98$ kgCO2e from these changes alone.

Miguel takes another look at the model's architecture, and notes that it is very large
for its stated purpose, with many channels per convolutional layer, and very wide fully
connected layers in the head. He Miguel wonders if the model can be pruned to enable
training on his workstation, instead of relying on the cloud provider. Noting again that
the model is very large for its stated purpose, Miguel adds L1 (Lasso) regularisation to
reduce redundant activation, allowing many (now-unused) activation units to be removed
from the model entirely, resulting in a $20\%$ memory saving.

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
of memory from the previous job comes close to full, potentially tripling job speed on
the same hardware.

These experiments highlight the dramatic computational efficiency increases that can
be achieved with careful optimisation of the job. Naive implementation of training and
inference can have a considerably higher carbon foorprint, requiring larger GPUs and
longer run times, while carefully optimised workflows can be run very quickly and be
small enough to run on local hardware.

It can often be the case that running AI workflows on cloud providers has a smaller
carbon foorprint than running on local hardware. The energy efficiency measures of
datacentres make operational carbon relatively lower than smaller dedicated hardware
setups, and embedded carbon can be lower using existing datacentre hardware, compared
to buying and decommissioning in-house hardware. The flipside is that one looses the
ability to choose when a job is executed, meaning demmand shifting to off-peak times
is no longer an option. In either case, Miguel's optimisations have had a huge effect
on the model's carbon footprint, and have afforded him the *choice* of using either,
depending on the circumstances.
