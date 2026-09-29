---
layout: page
title: "Modelling and control for production of chemicals with CO2 electrolysis"
description: 
status: available
project_types:
  - BSc
  - MSc
ects: 30-35 (15-20 for BSc)
orientation: 2
partners:
- dtu-fysik
topics:
  - Modelling
  - Fault diagnosis
  - Control
  - Estimation
  - Chemical plants
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
    src="{{ '/assets/img/student-projects/control problems - Christian Lundgaard.jpeg' | relative_url }}"
    alt="CO2 Electrolysis project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Isotopically labelled compounds are custom-designed molecules. Large-scale usage of isotopically labelled compounds are limited due to costs, quality and long delivery times. CO2 electrolysis is a cost-efficient enabler for production of high quality labelled compounds. DTU Fysik leads a research initiative which aims to developing methods that provide significant competitive advantages and unique selling points in the production of istopically labelled compounds.

The project focuses on the development of modelling, control, estimation and diagnosis methodologies for production of chemicals with CO2 electrolysis.


## Project Objectives
The following list presents possible objectives (depending on the scope and type of the project) that are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to CO2 electrolysis systems.
- Derive a first-principle mathematical model of the system suitable for control design and monitoring. 
- Identify the parameters of the system and perform sensitivity analysis. 
- Design a state estimator.
- Design a closed-loop ontrol strategy.
- Design a scheme for fault diagnosis and condition monitoring of the system. This will include definition and parametrisation of expected faults.
- Implement the solution (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and compare the designed virtual sensor against real data. 


## Methods & Tools

The project combines **modelling, control theory, fault diagnosis, estimation, implementation, and numerical simulation**.

The theoretical work will focus on the development of the modelling, control, estimation and diagnostics methodologies for the CO2 electrolysis system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology. Experimental work on the real apparatus is expected.

## Starting Literature and resources

1. Blanke, M., Kinnaert, M., Lunze, J., and Staroswiecki, M. (2015). "Diagnosis and Fault-tolerant Control", 3rd Edition. Springer. Available on [DTU Findit](https://findit.dtu.dk/catalog/561d2a87e64357331200002b).
2. System specific reports (in coordination with the DTU Fysik supervisor).


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Christian Bach Lundgaard** , chrlund@dtu.dk <br>
VPX R&D Engineer, DTU Fysik