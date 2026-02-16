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

Energy famously cannot be created or destroyed but the energy used for research
activities has to come from somewhere. In practice the majority of energy used for
digital research comes from a national electricity grid so this will be our focus.

The elecrical grid serves to transport energy from electricity generators to end users.
Economies of scale tend to mean that electricity generation is a large scale activity.
The electrical energy supplied to the grid comes from a variety of different sources.
This can be fossil fuels like coal and gas or green energy sources like solar and wind.

A key feature of electrical grids is that supply must be balanced with demand. Demand
for electricity can vary greatly throughout a year or even an individual day. The grid
responds to increases in demand by purchasing additional electricity from suppliers.

### Energy Mix and Carbon Intensity

Different methods of electricity generation have different properties. Some important
ones:

- Cost - The cost of generating each kWh of energy.
- Carbon Intensity - A measure of the kgCO2e emitted per kWh of energy.
- Dispatchability - How easily or quickly generation can be scaled up in response to
  demand.

::::::::::::::::::::::::::::::::::::: callout

The below provides a quick summary of how different energy sources compare on their key
properties:

| Energy source | Cost | Carbon intensity | Dispatchability |
| --- | --- | --- | --- |
| Gas | Medium | Medium | High |
| Solar | Low | Low | Low |
| Wind | Low | Low | Low |
| Nuclear | High | Low | Medium |

::::::::::::::::::::::::::::::::::::::::::::

The energy sources used by the grid will change on an hourly timescale and some sources
such as wind and solar can be subject to seasonal and climate effects. The relative cost
of different sources can also be impacted by global events and markets. The sources of
electricity used by the grid are referred to as the energy mix. The energy mix of the
grid leads to an overall carbon intensity value given as gCO2/kWh of electricity
generated. This can also be broken down by geographical region or given as an average
for a time period.

### Carbon Intensity in the UK

The following graphs show a typical UK day in 2026.

<!-- markdownlint-disable-next-line line-length -->
![Electricity demand, energy mix and carbon intensity of the UK power grid on 12/01/2026](fig/demand-mix-intensity.png){alt="Three graphs showing the relationship between the electricity demand, energy mix and carbon intensity of the UK power grid over the course of a day."}

The following dynamics are at play:

- At midnight initial energy demand and carbon intensity is low.
- Around 5am, energy usage begins to increase as people wake up and businesses open. As
  demand increases, the proportion of gas in the energy mix increases as more gas
  generation is brought online to keep the grid balanced. This also drives an increase
  in carbon intensity.
- Carbon intensity peaks in the morning around 7am. Although energy demand continues to
  rise, gas usage and carbon intensity drop slightly as cheaper imported energy becomes
  available. Slightly later a small amount of solar power also becomes available as the
  sun rises.
- Demand remains steady throughout the day before increasing in the evening. This is
  driven by domestic usage as people come home, cook and use domestic appliances. Again
  additional gas generation is brought online to meet the demand and carbon intensity
  rises to its peak value.
- As the evening progresses and people go to bed, demand drops again and carbon
  intensity also falls as gas generation goes offline. Overall carbon intensity ends up
  lower at the end of the day than the beginning as more imported energy is available.

:::::::::::::::::::::::::: callout

## Takeaways

- The pattern shown is typical for a day in the UK. There are however many other factors
  that can determine the relationship between demand and carbon intensity which can play
  out at a variety of timescales.

- There is considerable variability in the carbon intensity of electricity throughout
  the day - a factor of two in the above example. A simple strategy to reduce the
  emissions from digital research is therefore to shift electricity usage to times when
  carbon intensity is low. This is known as demand shifting. A simple rule of thumb is
  to favor running computationally intensive work at night.

- Gas is a key part of the UK's energy mix because of it's dispatchability i.e., it's
  ability to rapidly respond to changes in demand. Some green technologies like solar
  and wind have low dispatchability as they depend on factors like the weather.

::::::::::::::::::::::::::::::::::

<!-- markdownlint-disable-next-line line-length -->
![Carbon intensity of the UK power grid during 2025](fig/daily_carbon_intensity_2025.png){alt="A graph showing the daily carbon intensity of the UK power grid during 2025. The mean, maximum and minimum values for each day are shown."}

The above graph demonstrates how carbon intensity can vary throughout the year. Whilst
there is little pattern month to month, it is interestirng to observe that the mimimum
and maximum carbon intensity of the grid can vary between ~50 gCO2/kWh and ~250
gCO2/kWh, a factor of five.

:::::::::::::::::::::::::: callout

## Carbon Intensity Forecasts

For the UK there are publically available forecasts for the carbon intensity available
at <https://carbonintensity.org.uk>.

::::::::::::::::::::::::::::::::::

## Embodied carbon and carbon awareness

- Embodied carbon covers emissions from the extraction of raw materials, creation,
  transportion and disposal of a product.
- Breakdown of the embodied emissions of a laptop.

## The greenhouse gass (GHG) protocol and how to use it

- A framework for greenhouse gas accounting.
- Built to help organisations understand and start to measure the sources of their
  emissions.
- Holistic - considers both the direct and indirect sources of emissions.
- Explanation of scopes.
- Example application.

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
