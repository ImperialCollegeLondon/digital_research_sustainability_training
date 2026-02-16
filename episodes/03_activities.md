---
title: "Digital research activities with sustainability issues"
teaching: 20 # teaching time in minutes
exercises: 0 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What digital research activities can have sustainability issues?
- What activities consume more energy?
- What activities consume more power?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Identify digital research activities
- Describe which aspects of them could be problematic from the sustainability perspective
- Identify if those aspects are related to power or energy usage

::::::::::::::::::::::::::::::::::::::::::::::::

The environmental impact of digital research can be broadly split into three categories:

- Carbon emissions from powering the computers
- Impact of long-term data storage
- Carbon footprint of the hardware life cycle

## Powering Computers

## Data storage

Research datasets are increasingly large and replicated across multiple systems for
 reliability. As research practices shift toward open data and long-term storage,
 the cumulative energy demand of storage becomes a significant component of digital
 research's environmental impact. Data storage options can be split into two main
 categories:

- local storage
- cloud storage

### Local storage

- **Solid-State Disk Drives (SDD)**: They use flash memory with no moving parts to store
 data. Their emodied carbon emissions are high due to the rare metals needed for semiconductor
 manufacturing, while operational emissions are low.
- **Hard Disk Drives (HDD)**: They store data on spinning magentic disks. Embodied emissions
are lower than those of SDDs but operational emissions are higher because their disks
 must spin continuously.
- **Linear Tape-Open (LTO Tape)**: Magnetic tape technology used for long-term storage.
 Their manufacturing emissions are low, while their operation emissions are near zero.

Their associated carbon emissions are summarised below:

| Category | SDD | HDD | LTO tape |
| :--- | :--- | :--- | :--- |
| **Embodied Carbon (kg CO2e per TB)** | High (160-320 kg)^1^ | Moderate (20-40 kg)^1^ | Low (~0.07 kg)^3^ |
| **Operational Carbon (kg CO2e per TB)** | Low (25-50 kg )^1^ | High (2-160 kg)^1, 2^ | Zero |
| **Lifespan** | 5–10 years | 5-10 years | 30+ years |

SDDs allow data to be accessed almost instantly and are typically 10–100× faster than HDDs.
 LTO tapes offer the slowest access speeds, but they remain the preferred option for
  offloading cold data due to their low cost and excellent energy efficiency.

### Cloud storage

Cloud storage has become an important component of modern digital research. Storing data
 in the cloud has an associated carbon footprint which arises from its embodied
 emissions and its operational emissions.

**Embodied emissions of cloud storage**:

- manufacturing of storage devices (SDDs, HDDs and tape systems)
- data-center construction (concrete, steel, electrical infrastructure, etc.)
- networking and supporting hardware (switched, cables, etc.)
- hardware transportation and deployment

**Operational carbon emission of cloud storage**:

- powering the hardware: larger energy usage by HDDs, followed by SDDs, while tape
 consumes almost zero energy when idle
- cooling systems: large amounts of energy needed to maintain optimal temperatures for
 storage devices
- redundancy and replication: multiple copied storied across regions
- networking and data transfer: energy associated with uploading, downloading and syncing
 data

Operational emissions depend heavily on the grid carbon intensity, with lower emission
 in renewable-powered regions and higher emissions in fossil-fuel-dominated regions.

Choosing between local vs cloud storage depends on several factors, and the table below
 highlights how each option differs in terms of carbon emissions.

| Category | Cloud Storage | On‑Prem Storage |
| :--- | :--- | :--- |
| **Embodied Carbon** | Lower (shared + efficient infrastructure) | Higher (duplications + under‑used hardware) |
| **Operational Carbon** | Usually lower (efficient cooling) | Usually higher(older facilities + local grid) |
| **Energy Efficiency** | High | Generally lower |
| **Utilisation** | High (resources shared across many users) | Lower (over‑provisioning) |

### Strategies to reduce carbon emissions associated with data storage

- Choose cloud regions powered by renewable energy
- Delete unused or redundant data
- Keep frequently accessed data on faster storage (SDDs) and move "cold"
 or infrequently accesed data to slower but more energy efficent systems (tape storage)^4^
- Use compression to reduce storage requirements

## Hardware life-cycle footprint

### References

1. [Swamit Tannu and Prashant J. Nair. 2023. The Dirty Secret of SDDs: Embodied Carbon. SIGENERGY Energy Inform. Rev. 3, 3 (October 2023), 4–9](https://dl.acm.org/doi/10.1145/3630614.3630616)
2. [Based on Seagate EXOS X18](https://www.seagate.com/content/dam/seagate/assets/esg/planet/product-sustainability/files/life-cycle-assessment-exos-x18.pdf)
3. [Based on LTO 9 - FUJIFILM. *Sustainability Report 2020*. 2020](https://www.fujifilm.com/files-holdings/en/sustainability/report/2020/sustainability_activity_report_2020_ff_sr_2020_all_a4_E.pdf)
4. [Sustainable computing in science - EMBL-EBI](https://www.ebi.ac.uk/training/online/courses/sustainable-computing-in-science/what-can-we-do/good-practices-in-data-management/)
