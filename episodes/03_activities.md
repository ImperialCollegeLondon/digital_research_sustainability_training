---
title: "Digital research activities with sustainability issues"
teaching: 20 # teaching time in minutes
exercises: 0 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What digital research activities can have sustainability issues?
- How do different types of data storage (local vs cloud) contribute to carbon emissions?
- What factors influence the energy and power consumption of digital research workflows?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Identify which aspects of a research workflow are most carbon‑intensive and why.
- Explain how different storage technologies (SSD, HDD, LTO tape) differ in embodied and
 operational carbon emissions.

::::::::::::::::::::::::::::::::::::::::::::::::

The environmental impact of digital research can be broadly split into three categories:

- Carbon emissions from powering the computers
- Impact of long-term data storage
- Carbon footprint of the hardware life cycle

## Powering Computers

TBC

## Data storage

Research datasets are increasingly large and replicated across multiple systems for
 reliability. As modern research practices move toward open data and long-term storage,
 the cumulative energy demand of storage becomes a significant component of digital
 research's environmental impact. Data storage options can be split into two main
 categories:

- local storage
- cloud storage

### Local storage

- **Solid-State Disk Drives (SSD)**: They use flash memory with no moving parts to store
 data. Their embodied carbon emissions are high due to the rare metals needed for semiconductor
 manufacturing, while operational emissions are low.
- **Hard Disk Drives (HDD)**: They store data on spinning magnetic disks. Embodied emissions
 are lower than those of SSDs but operational emissions are higher because their disks
 must spin continuously.
- **Linear Tape-Open (LTO Tape)**: Magnetic tape technology used for long-term storage.
 Their manufacturing emissions are low, while their operational emissions are near zero.

Their associated carbon emissions are summarised below:

| Category | SSD | HDD | LTO tape |
| :--- | :--- | :--- | :--- |
| **Embodied Carbon (kg CO₂e per TB)** | High (16-32 kg)^1^ | Moderate (2-4 kg)^1^ | Low (~0.07 kg)^3^ |
| **Operational Carbon (kg CO₂e per TB)** | Low (2-5 kg)^1^ | Moderate - High (2-16 kg)^1,2^ | Low (~0 kg) |
| **Lifespan** | 5–10 years | 5-10 years | 30+ years |

While the numbers vary depending on manufacturers and reporting available, it is generally
 considered that SSDs have a higher 'carbon debt` per unit of storage than HDDs^4^.
 However, recent data suggests that the difference for enterprise-grade drives is shrinking,
 and new SSDs have only 2x the embodied carbon of comparable HDDs^5^.

SSDs allow data to be accessed almost instantly and are typically 10–100× faster than HDDs.
 LTO tapes offer the slowest access speeds, but they remain the preferred option for
 storing cold data due to their low cost and great energy efficiency.

### Cloud storage

Cloud storage has become an important component of modern digital research. The servers
 and hardware that make this possible are housed in large industrial facilities known as
 data centres. Storing 1 TB of data in the cloud for a year results in an estimated
 carbon footprint of 2–40 kg CO₂e, depending on storage type, redundancy, and
 electricity source6^7^. These emissions arise from two main sources: the embodied carbon
 of the hardware and infrastructure, and the operational energy required to run and cool
 the data centre.

**Embodied emissions of cloud storage**:

- **manufacturing of storage devices**: SSDs have higher embodied emissions than HDDs and
magnetic tape
- **data-centre construction**: includes the concrete, steel, electrical infrastructure,
 etc.
- **networking and supporting hardware**: switches, cables, etc.
- **hardware transportation and deployment**: in cloud environments, hardware is
 often decommissioned every 3 to 5 years to maintain reliability

**Operational carbon emissions of cloud storage**:

The operational carbon emissions of cloud storage arise from:

- **powering the hardware**: larger energy usage by HDDs, followed by SSDs, while tape
 consumes almost zero energy when idle
- **cooling systems**: large amounts of energy are needed to maintain optimal temperatures
 for storage devices
- **redundancy and replication**: standard cloud storage providers typically create three
 distributed copies of every file across different physical buildings
- **networking and data transfer**: energy associated with uploading, downloading and syncing
 data. This depends heavily on the distance and type of network (wired vs 5G) used.

Data centres consume around 2.5% of the UK's electricity and the annual consumption
 is expected to increase by 4 times by 2030^9^. In the U.S., data centres are predicted
 to use up to 12% of the country's electricity by 2028, a 3x increase from 4.4% in 2025^8^.

The energy efficiency of data centres is usually measured as their **Power Usage
 Effectiveness (PUE)**, and determines how much of the energy entering the data centre reaches
 the IT equipment used for servers and storage compared to the energy used for cooling
 and lighting.

$$
\mathbf{PUE} = \frac{\text{IT Equipment Power}}{\text{Total Facility Power}}
$$

<!-- markdownlint-disable-next-line line-length -->
![Google Data Center PUE measurement boundaries](fig/pue-infographic.webp){alt="Google Data Center PUE measurement boundaries."}

 An average data centre has a PUE of around 1.59, meaning that for every 1 watt used to
  power the storage drive, an additional 0.5 watts is spent on cooling and power distribution.
  Newer and larger data centres tend to be more efficient^11^, with a global average PUE
  of 1.41 in 2025^11^.

**Operational emissions** represent the greenhouse gas (GHG) impact associated with the
 electricity required for cloud storage. The value depends heavily on the grid carbon
 intensity, with lower emissions in renewable-powered regions and higher emissions
 in fossil-fuel-dominated regions.

<!-- markdownlint-disable-next-line line-length -->
$$
\text{Operational Emissions} =
U \times C_{\text{kWh}} \times \text{PUE} \times E_{\text{CO₂e}}
$$

Where:

- **U**: Cloud provider service usage - can be obtained from cloud providers
- **C\_kWh**: Cloud energy conversion factors - can be obtained from cloud providers or
  academic studies
- **PUE**: Power usage effectiveness - usually published by cloud providers  
- **E\_CO₂e**: Grid emissions factors - provided by regional electricity grid authorities

### Local (on-premise) vs Cloud storage

Local or on‑premises storage refers to data kept on servers, network‑attached storage
 systems, or institutional data centres that are owned and managed directly by a
 university, department, or research group. While storing data in the cloud is usually
 the greener choice, local storage has a number of advantages, including greater
 control over data, predictable access speeds, and the ability to power equipment down
 when not in use.

| Category | Cloud Storage | Local Storage |
| :--- | :--- | :--- |
| **Embodied Carbon** | Lower (shared + efficient infrastructure) | Higher (duplications + under‑used hardware) |
| **Operational Carbon** | Usually lower (efficient cooling) | Usually higher (older facilities + local grid) |
| **Energy Efficiency** | High (fewer idle disks) | Generally lower |
| **Utilisation** | High (resources shared across many users) | Lower (over‑provisioning) |

### Strategies to reduce carbon emissions associated with data storage

- Delete unused or redundant data and avoid unnecessary replication
- Keep frequently accessed data on faster storage (SSDs) and move "cold"
 or infrequently accessed data to slower but more energy efficient systems (tape storage)^12^
- Use compression and efficient file formats to reduce storage requirements
- Clean and preprocess data locally before uploading to the cloud to avoid storing
 large amounts of raw data
- Choose cloud regions powered by renewable energy
- Choose cloud storage options designed for infrequent access when appropiate

## Hardware life-cycle footprint

TBC

### References

1. [Swamit Tannu and Prashant J. Nair. 2023. The Dirty Secret of SSDs: Embodied Carbon. SIGENERGY Energy Inform. Rev. 3, 3 (October 2023), 4–9](https://dl.acm.org/doi/10.1145/3630614.3630616)
2. [Based on Seagate EXOS X18](https://www.seagate.com/content/dam/seagate/assets/esg/planet/product-sustainability/files/life-cycle-assessment-exos-x18.pdf)
3. [Based on LTO 9 - FUJIFILM. *Sustainability Report 2020*. 2020](https://www.fujifilm.com/files-holdings/en/sustainability/report/2020/sustainability_activity_report_2020_ff_sr_2020_all_a4_E.pdf)
4. [Rteil, N., Kenny, R., Andrews, D., & Kerwin, K. (2025). Understanding the carbon footprint of storage media: A critical review of embodied emissions in hard disk drives. International Journal of Environmental and Ecological Engineering, 19(11), 263–270](https://researchportal.lsbu.ac.uk/ws/portalfiles/portal/15145533/understanding-the-carbon-footprint-of-storage-media-a-critical-review-of-embodied-emissions-in-hard-disk-drives_1_.pdf)
5. [How Do the Embodied Carbon Dioxide Equivalents of Flash Compare to HDDs?](https://blog.purestorage.com/perspectives/how-do-the-embodied-carbon-dioxide-equivalents-of-flash-compare-to-hdds-part-1/#:~:text=Instead%20of%20an%208x%20difference,continue%20well%20into%20the%20future.)
6. [Digital Decarbonisation - CO₂e Data Calculator](https://digitaldecarb.org/co2-data-calculator/)
7. [WholeGrain DIgital Report](https://www.wholegraindigital.com/digitaldeclutter/#cloud-storage)
8. [National Energy System Operator](https://www.neso.energy/neso-implements-electricity-grid-connection-reforms-unlock-investment-great-britain)
9. [U.S. Department of Energy - 2024 Report on U.S. Data Center Energy Use](https://escholarship.org/uc/item/32d6m0d1)
10. [Uptime Institute, Large data centres are mostly more efficient, analysis confirms, 7 February 2024](https://journal.uptimeinstitute.com/large-data-centres-are-mostly-more-efficient-analysis-confirms/)
11. [IEA, Energy and AI, April 2025, p259](https://www.iea.org/reports/energy-and-ai)
12. [Sustainable computing in science - EMBL-EBI](https://www.ebi.ac.uk/training/online/courses/sustainable-computing-in-science/what-can-we-do/good-practices-in-data-management/)
