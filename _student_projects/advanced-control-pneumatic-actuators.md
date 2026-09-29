---
layout: page
title: "Advanced control of pneumatic actuator systems"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 3
partners:
  - dtu-construct
topics:
  - Sliding Mode Control
  - Adaptive Control
  - Nonlinear Control
  - Pneumatic actuator
  - Gas bearing systems
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
    src="{{ '/assets/img/student-projects/gas-bearing.png' | relative_url }}"
    alt="Advanced Control for pneumatic actuator project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Advanced control methods comprising sliding-mode and nonlinear adaptive controllers have been shown to facilitate robust high-accuracy stabilisation. This makes such algorithms excellent candidates for servo and positioning solutions in highly nonlinear systems.

This master project aims to explore the design, implementation and evaluation of advanced control schemes for a real pneumatic actuator system. 

## Project Objectives
The project will involve:

-	Improving/extending an existing model of a pneumatic actuator system to include the most dominant perturbations and disturbances.
-	Define a mapping between desired performance specifications and dynamical properties of the closed-loop system (e.g. desired damping and bandwidth).
-	Designing an advanced nonlinear controller that satisfies the performance specifications.
-	Implement and tune the obtained design on the real pneumatic actuator system.
-	Design and carry out experiments for different operation scenarios.
-	Define performance metrics and evaluate the designed controller also in comparison with the baseline controller (PI).


## Methods & Tools

The project combines **nonlinear control theory, stability analysis, experimental campaigns and numerical simulation**.

The theoretical work will focus on the design, implementation and analysis of advacned control loops for the pneumatic actuator system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived results and the proposed tuning methodology. Additionally, experimental tests will be conducted on the real apparatus.

## Starting Literature

1. Slotine, J. J. E., and Li, W. "Applied nonlinear control", Prentice-Hall, 1991.
2. Khalil, Hassan K. “Nonlinear Systems Third Edition”, 2008.
3. Andersen, A. (2020). "Modelling and control practices for motion tracking of pneumatically actuated systems", MSc Thesis. DTU Department of Civil and Mechanical Engineering. Available on [DTU Findit](https://findit.dtu.dk/catalog/5e6b787dd9001d016b1c5308).

## Supervision

**Dimitrios Papageorgiou** , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Ilmar Santos** , ilsa@dtu.dk <br>
DTU Civil and Mechanical Engineering