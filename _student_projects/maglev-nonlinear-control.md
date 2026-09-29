---
layout: page
title: "Nonlinear Control for a Magnetic Levitation System"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
topics:
  - Magnetic levitation
  - Nonlinear Control
  - Model calibration
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
    src="{{ '/assets/img/student-projects/ECP_MAGLEV.png' | relative_url }}"
    alt="MagLEv Nonlinear Control project"
    style="max-width: 45%; height: auto;"
  >
</div>

## Overview
The EPC M730 is a double-mass/double-coil magnetic levitation system that comprises two current actuators and two laser position sensors. Up to two magnetic discs can slide along a plastic vertical rod with reduced friction.

Accurate position and velocity control of the magnetic discs can be quite challenging, especially in the entire range of plastic rod. This is due to the strong input nonlinearities, the coupling effects of the two magnetic discs and the model uncertainties.

This master project aims to develop and compare different nonlinear control strategies for the positioning of the magnetic disks.

## Project Objectives
The project will involve:

-	Developing/improving the first-principle mathematical model of M730 MagLev sys-tem.
-	Designing several nonlinear control algorithms (adaptive, sliding-mode etc.) for positioning of the magnetic discs.
-	Defining different operation scenarios on which the controllers will be tested.
-	Performing simulations of the different operation scenarios (Matlab/Simulink or Python).
-	Implement the designed controllers on the ECP M730 test setup.
-	Define and run experiments for the evaluation of the controllers.
-	Define performance metrics and compare the designed controllers against con-ventional solutions (e.g. PID).

## Methods & Tools

The project combines **nonlinear control theory, stability analysis, numerical simulation and experiments**.

The theoretical work will focus on the synthesis and analysis of Adaptive and/or Sliding Mode Control loops as well as the stability analyssis of the resulting closed-loop solution.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived controllers. The results will be compared to experimental findings obtained from tests on the real experimental apparatus.

## Starting Literature

1. Slotine, J. J. E., and Li, W. "Applied nonlinear control", Prentice-Hall, 1991.
2. Khalil, Hassan K. “Nonlinear Systems Third Edition”, 2008.

## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering