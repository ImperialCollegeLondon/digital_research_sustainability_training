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
provided by the manufacturers themselves, which might be sketchy or based on different
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

- The age of the computer: Modern computers have generally more advance technology that
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
out above. Having sid that, this document is sometimes not as complete as it should, or
might not represent the exact configuration of your machine. Or might not even exist if
the machine has been made bespoke with specific components.

In this case, the best option to get the idle energy usage of a machine is to use a plug
in power meter. These plug in the mains socket and then the computer and any other
peripherals, like monitors, can be plugged to it (possibly via a power strip). There are
many models, but most will provide both the instantaneous power and the energy used over
a period of time.

Once the baseline energy usage is found, strategies can be defined to reduce it, like
adjusting the power management settings, changing usage habits, etc.

### Product Carbon Footprint of different manufacturers

- [HP](https://h20195.www2.hp.com/v2/library.aspx#doctype-95&country-us&sortorder-popular&teasers-off&isRetired-false&isRHParentNode-false&titleCheck-false)
- [Lenovo](https://compliance.lenovo.com/content/esg-document-library/en/esg.html?1_group.propertyvalues.property=.%2Fjcr%3Acontent%2Fmetadata%2FdocumentType&1_group.propertyvalues.operation=equals&1_group.propertyvalues.7_values=PCF%20Sheets&layout=card&p.offset=0&p.limit=24)

[Device Donation Scheme]: https://www.london.gov.uk/coronavirus/volunteer-and-donate/device-donation-scheme
[ECO Declaration]: https://ecma-international.org/publications-and-standards/standards/ecma-370/
[ECO declaration of the HP EliteBook 840 G9]: https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=c08155359&search=HP%20EliteBook%20840%20G9

## In the lab

TBC

## In the cloud or datacenter

TBC
