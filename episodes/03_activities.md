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

## Laptops and workstations

Everyone in research uses a laptop, desktop PC or workstation to do their work, even if
they are not involved in coding or running simulations. Browsing the web or checking the
email are everyday activities that consume energy. These are all called
_operational carbon emissions_.

But just the fact that you have one of these machines, also has a carbon impact. This is
related to the process of sourcing the materials the computer is made off, manufacturing
and transporting it. These are called _embodied carbon emissions_.

Both play a significant role in the carbon footprint of using a laptop or workstation,
but how to estimate them and reduce them is very different.

The following aspects should be considered:

### Embodied emissions

Embodied carbon emissions **do not change** once the machine is in your hands: they only
depend on the manufacturing and transport process. However,
**embodied carbon emissions per year** are reduced the more years the machine
is in use. Hence, the longer the lifetime of the machine, the lower their embodied
carbon footprint per year.

::::::::::::::::::::::::::::::::::::: callout

Before replacing a laptop, desktop PC or workstation, make sure that it is really
needed and that it is no longer fit for purpose.

- Can you replace just some parts to extend its lifetime, eg. memory, GPUs?
- Can you give it another useful purpose, if not as your main machine anymore?
- Can you donate it to charity (eg. see options in the [Device Donation Scheme]) to
extend its useful life instead of trashing it (or recycling it)?

:::::::::::::::::::::::::::::::::::::::::::::

Finding the embodied carbon emissions of computers often relies on the information
provided by the manufacturers themselves, which might be vague or based on different
assumptions. However, it is a good starting point for estimating the carbon impact of
your research activities.

Below there is a list of common laptop manufacturers' webpages providing information on
their product's embodied carbon emissions. If your machine is custom made or very old,
you might need to dig into the individual parts's manufacturers, as well.

As a specific example, [in this link](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=c08207991)
you have the report corresponding to the laptop model used to write this bit of the
course, an HP EliteBook 840 G9, also shown in the following image.

<!-- markdownlint-disable-next-line line-length -->
![Embodied carbon emissions for HP EliteBook 840 G9](episodes/fig/embodied_emissions_laptop.png){alt='Embodied carbon emissions for HP EliteBook 840 G9.'}

If we exclude the `Use` section of the chart, which obviously depends on the usage and
the location, as discussed in the [previous episode](02_carbon.md), the remaining,
related to production and transportation, accounts for about ~80% of the estimated
total, i.e. 160 kg CO$_2$e.

It should be noted that different manufacturers use different criteria to calculate their
embodied emissions, so choosing the computer with the lowest reported embodied emissions
is not necessarily the best approach. Other aspects like the expected lifetime, the
possibility oif replacing individual components, etc. might be more useful and impactful
aspects to look at.

::::::::::::::::::::::::::::::::::::: challenge

#### What are the embodied carbon emissions of your computer?

Find the model of the computer you are using right now to do this course and try to find
out its embodied carbon emissions. The links below from some manufacturers might be
useful.

- What part is the one that produces a larger carbon footprint?
- If it is a laptop and the battery is failing, how much carbon could you save if you
just replace the battery for a new one instead of replacing the whole laptop?

:::::::::::::::::::::::::::::::::::::::::::::::

### Operational emissions

Operational emissions are those that are produced when _using_ the equipment. They depend
on its design and performance, but also on _how_ it is used and _where_ it is used. For
the later reason, it is often better to consider the energy usage, rather than the carbon
emitted as this depends on the energy mix where the machine is being used.

#### Idle energy usage

These represent a baseline of energy usage just because of the computer (and the monitor
in the case of desktop computers) being on. There are a number of factors that influence
this:

- The age of the computer: Modern computers have generally more advanced technology that
makes them more energy-efficient than older ones.
- Nature of the computer: Laptops, designed to work with batteries, are often also more
energy efficient than desktops.
- The power management settings: That control when to go to sleep after a time of inactivity,
switch the screen off, etc. have a very strong influence on the idle energy consumption.
- Peripherals: Especially, monitors (sometimes having two or more), but also printers
can also consume large amounts of energy.

To figure out the idle energy consumption of a specific machine, one option is to check
the [ECO Declaration] for the equipment. All manufacturers need to provide this document
where, in principle, you can find such information. For example, the
[ECO declaration of the HP EliteBook 840 G9] indicates an energy consumption of 22.67 kWh/year.
This declaration also includes useful information about the product, like which components
can be replaced or upgrade, useful knowledge to reduce the embodied emissions, as pointed
out above. Having said that, this document is sometimes not as complete as it should, or
might not represent the exact configuration of your machine. Or might not even exist if
the machine has been made bespoke with specific components.

In this case, the best option to get the idle energy usage of a machine is to use a plug
in power meter. These plug in the mains socket and then the computer and any other
peripherals, like monitors, can be plugged to it (possibly via a power strip). There are
many models, but most will provide both the instantaneous power and the energy used over
a period of time.

Once the baseline energy usage is found, strategies can be defined to reduce it, like
adjusting the power management settings, changing usage habits, etc.

#### Application energy usage

Typically, you will be interested in the energy usage of specific applications, so you
can minimize its energy usage. For example, a particular simulation software you have
been working on or a 3D visualization tool.

This is not an easy task, and the solution depends greatly on your accessibility to the
source code of the application, as well as the hardware you are using.

If you do have access to the source code, then you could use tools like the
[Intel's Performance Counter Monitor (PCM)] (which [can be used in C++ programs]) or [Codecarbon]
(for Python programs). These tools require some setting up - and obviously modify your
code - but will give you the most accurate readings of the energy usage specific for
your application.

If you do not have access to the source code, then your only option is to rely on external
tools to monitor the energy usage of the application (e.g. using PCM) or to calculate it
based on the hardware being used and the time it is being used for using the
[Green Algorithms Calculator], for example.

It is beyond the scope of this course to teach you how to use any of these tools, given
the range of use cases and configurations, but in the case studies described in the next
episodes, there will be examples of how some of these can be employed in practice to
understand your energy usage and consider ways of reducing them.

### Product Carbon Footprint of different manufacturers

- [HP](https://h20195.www2.hp.com/v2/library.aspx#doctype-95&country-us&sortorder-popular&teasers-off&isRetired-false&isRHParentNode-false&titleCheck-false)
- [Lenovo](https://compliance.lenovo.com/content/esg-document-library/en/esg.html?1_group.propertyvalues.property=.%2Fjcr%3Acontent%2Fmetadata%2FdocumentType&1_group.propertyvalues.operation=equals&1_group.propertyvalues.7_values=PCF%20Sheets&layout=card&p.offset=0&p.limit=24)
- [Dell](https://www.dell.com/en-uk/lp/dt/product-carbon-footprints)

[Device Donation Scheme]: https://www.london.gov.uk/coronavirus/volunteer-and-donate/device-donation-scheme
[ECO Declaration]: https://ecma-international.org/publications-and-standards/standards/ecma-370/
[ECO declaration of the HP EliteBook 840 G9]: https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=c08155359&search=HP%20EliteBook%20840%20G9
[can be used in C++ programs]: https://greencompute.uk/Measurement/RAPL
[Codecarbon]: https://github.com/mlco2/codecarbon
[Green Algorithms Calculator]: https://calculator.green-algorithms.org/

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
 electricity source ^6,7^. These emissions arise from two main sources: the embodied carbon
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

## When using GitHub Actions

In a research study on [Environmental Impact of CI/CD
Pipelines](https://arxiv.org/abs/2510.26413) the authors compare the carbon emissions
of GitHub Actions with the emissions of quotidian activities.

![Comparison between the yearly
carbon emissions of the GitHub Actions ecosystem and the emissions of
quotidian activities](fig/github_actions_equivalent.pdf){alt = "Comparison between the yearly
carbon emissions of the GitHub Actions ecosystem and the emissions of
quotidian activities." width = "140%"}

This study also reports that in 2024, the estimates for the carbon footprint
from GitHub Actions range from 150.5 MTCO2e in the most optimistic scenario to
994.9 MTCO2e in the most pessimistic scenario. The most likely scenario estimates
are 456.9 MTCO2e which is equivalent to the carbon captured by 7,615 urban trees
in a year.

### References

1. [Swamit Tannu and Prashant J. Nair. 2023. The Dirty Secret of SSDs: Embodied Carbon. SIGENERGY Energy Inform. Rev. 3, 3 (October 2023), 4–9](https://dl.acm.org/doi/10.1145/3630614.3630616)
2. [Based on Seagate EXOS X18](https://www.seagate.com/content/dam/seagate/assets/esg/planet/product-sustainability/files/life-cycle-assessment-exos-x18.pdf)
3. [Based on LTO 9 - FUJIFILM. _Sustainability Report 2020_. 2020](https://www.fujifilm.com/files-holdings/en/sustainability/report/2020/sustainability_activity_report_2020_ff_sr_2020_all_a4_E.pdf)
4. [Rteil, N., Kenny, R., Andrews, D., & Kerwin, K. (2025). Understanding the carbon footprint of storage media: A critical review of embodied emissions in hard disk drives. International Journal of Environmental and Ecological Engineering, 19(11), 263–270](https://researchportal.lsbu.ac.uk/ws/portalfiles/portal/15145533/understanding-the-carbon-footprint-of-storage-media-a-critical-review-of-embodied-emissions-in-hard-disk-drives_1_.pdf)
5. [How Do the Embodied Carbon Dioxide Equivalents of Flash Compare to HDDs?](https://blog.purestorage.com/perspectives/how-do-the-embodied-carbon-dioxide-equivalents-of-flash-compare-to-hdds-part-1/#:~:text=Instead%20of%20an%208x%20difference,continue%20well%20into%20the%20future.)
6. [Digital Decarbonisation - CO₂e Data Calculator](https://digitaldecarb.org/co2-data-calculator/)
7. [WholeGrain DIgital Report](https://www.wholegraindigital.com/digitaldeclutter/#cloud-storage)
8. [National Energy System Operator](https://www.neso.energy/neso-implements-electricity-grid-connection-reforms-unlock-investment-great-britain)
9. [U.S. Department of Energy - 2024 Report on U.S. Data Center Energy Use](https://escholarship.org/uc/item/32d6m0d1)
10. [Uptime Institute, Large data centres are mostly more efficient, analysis confirms, 7 February 2024](https://journal.uptimeinstitute.com/large-data-centres-are-mostly-more-efficient-analysis-confirms/)
11. [IEA, Energy and AI, April 2025, p259](https://www.iea.org/reports/energy-and-ai)
12. [Sustainable computing in science - EMBL-EBI](https://www.ebi.ac.uk/training/online/courses/sustainable-computing-in-science/what-can-we-do/good-practices-in-data-management/)
13. Poster on [Environmentally-aware use of GitHub
Actions](https://zenodo.org/records/12754189) and the [associated GitHub repository](https://github.com/ImperialCollegeLondon/game_of_life)
14. Blog post on [Adopting a more rational use of Continuous Integration with GitHub Actions](https://imperialcollegelondon.github.io/RSEBlog/2024/06/26/adopting-a-more-rational-use-of-continuous-integration-with-github-actions/).
