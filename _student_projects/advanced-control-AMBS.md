---
layout: page
title: "Advanced control of active magnetic bearings systems"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 3
partners:
  dtu-construct
topics:
  - Sliding Mode Control
  - Adaptive Control
  - Nonlinear Control
  - Active magnetic bearings
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
    src="{{ '/assets/img/student-projects/AMB_setup.jpg' | relative_url }}"
    alt="Advanced Control for AMBS project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Active Magnetic Bearings (AMB) in rotating machines are very advantageous since they allow motion with low friction. This facilitates
-	Removal of lubricant
-	Reduction of wear and tear
-	Increase rotational speed limit 

Due to high nonlinear couplings of the magnetic interactions, conventional linear control methods often fall short in terms of accuracy and range of operation. Additional challenge emerges when trying to invert the input nonlinearity to apply a desired control signal.

This master project aims to the design, implementation and evaluation of nonlinear control strategies for an AMB system that employ tools from adaptive, sliding-mode and cascaded control theory.


## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

-	Develop a first-principle mathematical model of an AMB System or improve/extend an existing one to include the most dominant perturbations and disturbances.
-	Define parametrisation for the identified perturbations.
-	Define a suitable reference model that describe the desired dynamical properties of the closed-loop system (e.g. desired damping and bandwidth).
-	Design an advanced nonlinear controller that satisfies the performance specifications.
-	Implement and tune the obtained design on the real AMB system.
-	Design and carry out experiments for different operation scenarios.
-	Define performance metrics and evaluate the designed controller.


## Methods & Tools

The project combines **nonlinear control theory, stability analysis, experimental campaigns and numerical simulation**.

The theoretical work will focus on the design, implementation and analysis of advacned control loops for the AMB system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived results and the proposed tuning methodology. Additionally, experimental tests will be conducted on the real apparatus.

## Starting Literature

1. Slotine, J. J. E., and Li, W. "Applied nonlinear control", Prentice-Hall, 1991.
2. Khalil, Hassan K. “Nonlinear Systems Third Edition”, 2008.
3. Hassager, G. S., and Christoffersen, N. (2023). "Modelling and Nonlinear Control of Active Magnetic Bearings", MSc Thesis. DTU Department of Civil and Mechanical Engineering. Available on [DTU Findit](https://findit.dtu.dk/catalog/64c6fbedd58f051f4f1dd389).

## Supervision

**Dimitrios Papageorgiou** , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Ilmar Santos** , ilsa@dtu.dk <br>
DTU Civil and Mechanical Engineering