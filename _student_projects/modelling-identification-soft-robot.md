---
layout: page
title: "Modelling and identification of soft robot"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
topics:
  - Modelling
  - Identification
  - Learning-based
  - Estimation
  - Medical rehabilitation
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
    src="{{ '/assets/img/student-projects/Gripper for soft robot.jpg' | relative_url }}"
    alt="Soft robot project"
    style="max-width: 77%; height: auto;"
  >
</div>

## Overview
Compliance is a strong requirement for human-robot interactions. Soft-robots provide an opportunity to cover the lack of compliance characterising conventional actuation mechanisms. However, control of such robots is very challenging given their intrinsic complex motion patterns. Therefore, soft-robots require new approaches to e.g., modeling, control, dynamics, and planning. 

This project aims at deriving a control-oriented dynamnical model for a modular soft robot with a soft gripper. Control-theoretic and learning-based principles will be explored for identifying a suitable model structure as well its parameters.


## Project Objectives
The following list presents possible objectives (depending on the scope and type of the project) that are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to modelling and identification of nonlinear dynamics.
- Derive a mathematical model of the system suitable for control design and monitoring by using sparse regression and lerning-based methods.
- Identify the parameters of the system and perform sensitivity analysis. 
- Design a set of experimental campgains for data collection and treatment from the real test apparatus. 
- Define performance metrics and compare the designed virtual sensor against real data. 


## Methods & Tools

The project combines **modelling, identification, estimation, implementation, numerical simulation and experiments**.

The theoretical work will focus on the development of the modelling and estimation based on learning-based sparse regression methodologies for the soft robot system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology. Experimental work on the real apparatus is expected.

## Starting Literature and resources

1. Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). "Discovering governing equations from data by sparse identification of nonlinear dynamical systems". Proceedings of the national academy of sciences, 113(15), 3932-3937.
2. Sigurdardóttir, G. D. (2022). "Modelling and Nonlinear Control of a Soft Robotic Arm". DTU Department of Electrical Engineering. Available on [DTU Findit](https://findit.dtu.dk/catalog/6222019b7ced9854d879242c).
3. Brunton, S. L., Proctor, J. L., & Kutz, J. N. (2016). "Sparse identification of nonlinear dynamics with control (SINDYc)". IFAC-PapersOnLine, 49(18), 710-715.


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Silvia Tolu** , stolu@dtu.dk <br>
DTU  Electrical and Photonics Engineering