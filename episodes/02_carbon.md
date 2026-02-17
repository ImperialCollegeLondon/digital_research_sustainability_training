---
title: "Energy, power and carbon"
teaching: 30 # teaching time in minutes
exercises: 10 # exercise time in minutes
---

:::::::::::::::::::::::::::::::::::::: questions

- What is energy?
- What is power?
- How power and energy relate to carbon emissions?
- What other sources of carbon involve digital research?
- How do we calculate carbon emissions?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Explain what energy and power are
- Explain how energy is produced
- Explain what low-carbon energy sources are and how they opperate
- Explain what embeded carbon is
- Use the greenhouse gas (GHG) protocol to estimate carbon emissions

::::::::::::::::::::::::::::::::::::::::::::::::

(This episode will be heavy on pointing to the [Green software practitioner course] sections)

## Energy and power

- Energy = useful work - J or kwh.
- Power is a rate at which energy is consumed - watt -> joules/second.
- Kettle at 1kw for 1 hour -> 1kwh. 200watt for 5 hours = 1kwh.

## Energy sources and carbon emissions

- Energy has to come from somewhere - primarily either burning a fuel directly or an
  electrical grid.
- By the nature of digital research we're primarily concerned with electricity.
- Electricity generation is typically a national infrastructure though there may be corner
  cases such as small scale backup generators.
- An electricity grid is constantly trying to match demand with production.
- Different methods of electricity generation release different amounts of carbon per
  kwh - carbon intensity.
- Different methods of electricity generation have different properties - e.g. solar
  relies on the sun shining, gas can quickly respond to demand.
- Using a plot of grid demand and carbon intensity of a typical UK day explain
  the core dynamics at play, i.e. what drives demand and supply and how that interacts
  with the carbon intensity of different sources.
- Forecasts of carbon intensity are available.
- Links to some UK based resources.

## Embodied carbon and carbon awareness

So far we've focussed on the relationship between carbon emissions and electricity
usage. This is relevant to the operation of equipment used in digital research and is
usually the dominant component of the **operational carbon**. Another key source to
consider however are **embodied emissions**.

Embodied carbon is the greenhouse gas emissions produced during the full lifecycle of a
product or system before it starts being used: raw material extraction, manufacturing,
transport, construction and eventual disposal or recycling. It represents the "upfront"
carbon locked into goods and infrastructure. Accounting for embodied carbon helps teams
choose lower‑carbon options by considering repair, reuse, material choices and service
life in addition to operational energy use.

We'll discuss in detail the embodied carbon contributions associated with digital
research activities in the next episode.

## The Greenhouse Gas (GHG) Protocol and how to use it

So far we've discussed several sources of emissions. A key requirement to managing and
reducing emissions is to measure and account for them. The [Greenhouse Gas Protocol]
provides a framework for identifying and categorising different emission sources. It's
holistic and covers both direct and indirect emission sources.

The GHG protocol breaks down emissions into three categories called scopes:

- Scope 1 are direct emissions. These come from activities that directly emit carbon
  such as burning fuel. This would cover fuel used in a vehicle or an on-site heating
  system or electricity generation.

- Scope 2 are indirect emissions. These come activities that consume energy produced
  elsewhere. This is primarily the emissions associated with electricity generation
  covered in detail above..

- Scope 3 are "Value chain emissions". These come from everything upstream i.e.,
  requirements you need to carry out research activities and everything downstream i.e.,
  emissions associated with the use of your research outputs even by others. Upstream
  emissions includes things like the embodied emissions of hardware whilst
  downstream emissions might include use of software or data you've created.

The GHG protocol is most often applied to businesses, countries or cities but it can be
applied at any scale including an individual or research group. It's easy to get hung up
on which scope to place emissions in but perhaps the key takeaway is to take a broad
view of different emissions sources.

[Greenhouse Gas Protocol]: https://ghgprotocol.org/

::::::::::::::::::::::::::::::::::::: challenge

## According to the GHG protocol, what are the carbon emissions of...?

- Using a laptop in the office for coding 4h a day, 5 days a week. No calculations run.
- Brewing 5 cups of coffee per day, at home, 5 days a week.

:::::::::::::::::::::::: solution

## Output

No idea. We need to do it.

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::

[Green software practitioner course]: https://learn.greensoftware.foundation/
