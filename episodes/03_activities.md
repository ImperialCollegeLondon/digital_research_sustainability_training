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

### Product Carbon Footprint of different manufacturers

- [HP](https://h20195.www2.hp.com/v2/library.aspx#doctype-95&country-us&sortorder-popular&teasers-off&isRetired-false&isRHParentNode-false&titleCheck-false)
- [Lenovo](https://compliance.lenovo.com/content/esg-document-library/en/esg.html?1_group.propertyvalues.property=.%2Fjcr%3Acontent%2Fmetadata%2FdocumentType&1_group.propertyvalues.operation=equals&1_group.propertyvalues.7_values=PCF%20Sheets&layout=card&p.offset=0&p.limit=24)

[Device Donation Scheme]: https://www.london.gov.uk/coronavirus/volunteer-and-donate/device-donation-scheme

## In the lab

TBC

## In the cloud or datacenter

TBC
