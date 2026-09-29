---
layout: page
title: "Modelling and control of Grid Forming IBRs networks"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 3
partners:
- oersted
topics:
  - Power grids
  - Stability analysis
  - Control
  - Estimation
importance: 1
---

<div class="project-meta">
  <em>
    {{ page.project_types | join: " / " }} Project
    {% if page.ects %} · {{ page.ects }} ECTS{% endif %}
    {% if page.status %} · {{ page.status | capitalize }}{% endif %}
  </em>

  {% if page.orientation %}
    <span class="project-orientation">
      <span>Practical</span>

      <span class="orientation-scale">
        {% for i in (1..5) %}
          <span class="orientation-box {% if i == page.orientation %}active{% endif %}"></span>
        {% endfor %}
      </span>

      <span>Theoretical</span>
    </span>
  {% endif %}
  {% if page.partners %}
  {% for partner_id in page.partners %}
    {% assign partner = site.data.partners[partner_id] %}

    {% if partner %}
      <a href="{{ partner.url }}"
         target="_blank"
         class="project-partner"
         title="In collaboration with {{ partner.name }}">
        <img src="{{ partner.logo | relative_url }}"
             alt="{{ partner.name }}">
      </a>
    {% endif %}
  {% endfor %}
  {% endif %}
</div>

<div style="text-align: center; margin: 1.5rem 0;">
  <img
    src="{{ '/assets/img/student-projects/GridLoads_Windenergie.jpg' | relative_url }}"
    alt="Grid-forming Control project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Current Type-4 wind turbines and other inverter based resources (IBR) operate based on a control method which seeks to control the output current quickly and precisely to ensure the desired active- and reactive power under all electrical grid conditions. Such so called “Grid Following” inverter control aims to have perfect disturbance rejection and only change output given a new reference signal. This Grid Following ensures a predictable output, however it relies on other systems to provide fast-acting countermeasures to disturbances on the grid such as voltage sags or the loss of an interconnector/power plant that causes the frequency of the system to drop rapidly.

As IBRs are replacing the synchronous generators providing this fast-acting countermeasure, they need to take on the challenge.  A control concept called  ‘Grid Forming’ has increased in popularity with the aim to in some manner emulate synchronous generators or provide system services that may replace them. However, while synchronous machines react intrinsically and instantaneously to power imbalances by being stiffly coupled to the frequency of the grid via their rotating masses, IBRs does not. By allowing disturbances on the electrical grid to directly affect the output of the turbine, one can achieve a similar response for IBRs at the cost of tracking performance.

If one allow each turbine in a cluster to independently act on the electrical disturbances and modify their output (within 5 ms), how does an operator of such cluster ensure that the cumulative output limit is not violated, e.g. given that upstream equipment out of service, while having a central controller which has sample time between 60-150ms and a time delay of tens of milliseconds between the central controller and the individual IBRs.

Additionally one should ensure that the services provided are optimized in the sense of utilizing the availability capacity of each system in a way that minimizes post-event generation impact, and plays to the strengths of each type, e.g. battery systems vs. P2X systems, vs. wind turbines. Some Grid Forming inverters can be parameterized by an equivalent inertia representation, H-value, and a dampening value (D-value), of the expected response, which may be used to shape the desired combined output of the cluster.

## Project Objectives
The project will involve:

-	Model a simplified network of grid forming IBRs
-	Determine a parameterization methods for grid forming response
-	Investigate control methods to limit or optimize the common response in the presence of limits and time delays

## Methods & Tools

The project combines **control theory, stability analysis, and numerical simulation**.

The theoretical work will focus on the modelling of grid-forming networks as dyamical systems and the analysis of their stability. Control and estimation sysnthesis will be based on power output specifications and operational constraints.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature

1. Kristoffer Erbo Kjær, "Modelling and Stability Assessment of Grid Forming Wind Power Plants Subject to Hardware Constraints", MSc Thesis, Available on [DTU Findit](https://findit.dtu.dk/catalog/6a72822c8d61ed18a94b298f) 

## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering