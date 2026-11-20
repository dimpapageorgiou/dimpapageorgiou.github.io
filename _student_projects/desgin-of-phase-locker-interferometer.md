---
layout: page
title: "Design of an optical phase locked loop for phase sensitive quantum measurement"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
topics:
  - Modelling
  - Control
  - Estimation
  - Quantum
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
    src="{{ '/assets/img/student-projects/phase_locker.jpg' | relative_url }}"
    alt="Phase locker project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
The project aims at studying, designing, and impalementing a control system to stabilise an interferometer, aimed at phase sensitive quantum measurements.

The study can pertain three different cases:
1. Short length interferometers where the main source of instability is attributed to temperature and vibrations, generally up to 100 Hz.
2. Multicore fibers where the goal is to Stabilise the intercore phase drift.
3. Wide length gap in the interferometer arms (the situation where the phase noise of the laser could lead to degradation in interferometry between the reference and signal).

## Project Objectives
The following list presents possible objectives (depending on the scope and type of the project) that are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to CO2 electrolysis systems.
- Derive a first-principle (or data-driven) mathematical model of the system suitable for control design, including noise characteristics.
- Implement the derived model in Matlab/Python and perform Simulations of the diffent optical elements and their responses. This should be in accordance to the project specifications, whether it's a PhotoDiode (PD), Avalanche/Amplified PhotoDiode (APD), or highspeed photodiodes for high-bandwidth noises, as well as feedback elements (Fiber stretcher, phase modulator + Amplifier).
- Design a closed-loop ontrol strategy that optimises the performance with respect to a said target (e.g. high visibility for continuous operation of up to specified time).
- Implement the solution (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and evaluate the designed solutions. 


## Methods & Tools

The project combines **modelling, control theory, estimation, quantum systems, implementation, and numerical simulation**.

The theoretical work will focus on the development of the modelling, control and estimation methodologies for the system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology. Experimental work on the real apparatus is expected.

## Starting Literature and resources

1. System specific reports in coordination with the supervisors.


## Supervision

**Mujtaba Zahidy** , muzah@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Hans Henrik Niemann**  , hahe@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Francesco Sirovich** , frsir@dtu.dk <br>
DTU Electrical and Photonics Engineering