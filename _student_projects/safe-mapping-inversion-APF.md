---
layout: page
title: "Safe Mapping Inversion Using Artificial Potential Fields"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 5
partners:
topics:
  - Artificial potential fields
  - Nonlinear control theory
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
    src="{{ '/assets/img/student-projects/Safe_Mapping_Inversion.png' | relative_url }}"
    alt="Safe Mapping Inversion project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
When controlling complex systems such as (soft robots, Aerospace systems, Underwater Robotics etc.), sophisticated control algorithms and architectures are often unavoidable. A key element in generating the required dynamic commands—and translating them into inputs such as voltages for actuators—is inverse mapping. However, this process is prone to mathematical singularities, which can prevent calculations from being completed and disrupt the execution of desired trajectories. The same challenge arises during fault diagnosis and condition monitoring of complex systems. There, laten information has to be extracted from measuements with complicated mathematical representations. Failed estimation of the underlying information due to singularities may lead to wrong diagnosis and therefore inappropriate decision making.

Overcoming such challenges motivates the development of methods that can detect, estimate, and avoid singularities, ensuring stable and reliable system performance even in challenging control scenarios. The project will study the integration of singularity-avoidance features into dynamic mapping inversion algorithms in connected parameter spaces by employing principles from the theory of **Artificial Potential Fields (APFs)**. 

## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

1. Conduct a literature review on the use of APFs for safe control and estimation or collision avoidance. 
2. Formulate a suitable use case for highlighting the challenge with singularities emerging in estimation problems
3. Develop tools to model estimate and detect singularities in estimation architectures
  - Singularity definition within the framework of online parameter estimation
  - Design online singularity detection algorithm
4. Design and implement methods for singularity avoidance in control architectures using model based APFs and search/planning algorithms.
5. Extend the methods for time-varying singularities (moving and expanding)
6. Extend the methods for multiple singularities.
7. Validate the theoretical findings in simulation.


## Methods & Tools

The project combines **nonlinear control theory, stability analysis, and numerical simulation**.

The theoretical work will focus on the representation of singularties in connected parameter estimation spaces and the development of singularity-avoidance methods with APFs.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived results and the proposed tuning methodology.

## Starting Literature

1. Bo, V. (2026). "Safe nonlinear mapping inversion for control and fault diagnosis", MSc Thesis, DTU Department of Electrical and Photonics Engineering. Available on [DTU Findit](https://findit.dtu.dk/catalog/69b8aa0492f48834faa87f6b)
2. Simonsen, J. C. C. de. (2026). "Safe motion control for autonomous interception of underwater vehicles", MSc Thesis, DTU Department of Electrical and Photonics Engineering. Available on [DTU Findit](https://findit.dtu.dk/catalog/69c3360d2c5c5f32fcc9bbe1)

## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering