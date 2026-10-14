---
layout: page
title: "Development of framework for early detection of groudning risk due to bank effects"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
- abb
topics:
  - Fault diagnosis
  - Early detection
  - Marine systems
importance: 14
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
    src="{{ '/assets/img/student-projects/MSc_Maritime_Collision_Risk_Project.png' | relative_url }}"
    alt="CO2 Electrolysis project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Vessels operating in confined waterways are subject to hydrodynamic forces and moments collectively known as banking effects, which can significantly impact manoeuvrability. These effects can challenge navigational control, particularly in narrow channels, and in extreme cases, may lead to vessel grounding. A prominent example is the 2021 Ever Given incident, where a large container ship became lodged in the Suez Canal, halting traffic for six days and blocking a vital route for international shipping. Avoiding such severe incidents necessitates operating under protocols of safe navigation while in confined waters.

The project focuses on the development of a warning system that can advice on incipient grounding risk due to banking phenomena during navigation in confined waters.


## Project Objectives
The following list of objectives are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to warning for incipient risks, baking effects during navigation in confined waters, discrete-event systems and change detection.
- Design an overacrhing architecture for detection of bank-related grounding risk and monitoring of incipient bank effects. 
- Identify the necessary modules for the arning system.
- Formulate the interconnection and dynamics of the system modules as discrete event systems.
- Integrate excisting subsystems, such as banking hydrodynamic models and risk functions into the designed framework.
- Implement the solution (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and evaluate the desinged framework. 


## Methods & Tools

The project combines **fault diagnosis, change detection, supervisory control, implementation, and numerical simulation**.

The theoretical work will focus on the development of the banking warning framework as an integrated system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature and resources

1. Mikkelsen, J. H., Enevoldsen, T. T., Jensen, B. T., Jeppesen, M., Galeazzi, R., & Papageorgiou, D. (2026, July). "Closed Form Modelling and Identification of Banking Effects in Confined Waters". In 2026 European Control Conference (ECC) (pp. 3277-3282). IEEE..
2. Mikkelsen, J. H., Enevoldsen, T. T., Jensen, B. T., Jeppesen, M., Galeazzi, R., & Papageorgiou, D. "Learning-Based Detection of Incipient
Banking Effects for Navigation in Confined Waters".
3. Blanke, M., Kinnaert, M., Lunze, J., and Staroswiecki, M. (2015). "Diagnosis and Fault-tolerant Control", 3rd Edition. Springer. Available on [DTU Findit](https://findit.dtu.dk/catalog/561d2a87e64357331200002b).
4. Cassandras, C. G., and Lafortune, S. (2008). "Introduction to discrete event systems". Springer US. Available on [DTU Findit](https://findit.dtu.dk/catalog/544a0073e44c7a86671fe2c3).


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Thomas Theusen Enevoldsen** , thomas.t.enevoldsen@dk.abb.com <br>
R&D Principal Engineer, ABB Marine & Ports