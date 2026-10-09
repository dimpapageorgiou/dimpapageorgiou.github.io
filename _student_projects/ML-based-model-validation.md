---
layout: page
title: "Experimental Validation and Probabilistic ML-based Surrogate Modeling of Two-Stroke Marine Engine Simulation"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
  - everllence
topics:
  - Marine systems
  - Machine learning
  - Diesel engines
  - Model validation
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
    src="{{ '/assets/img/student-projects/marine_products_four-stroke.jpg' | relative_url }}"
    alt="EG virtual sensor project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
The master’s project at the investigation of a high-fidelity two-stroke marine engine simulation environment.  The simulation is currently being used to model engine characteristics and behavior for the entire Everllence marine engine portfolio. With its results, critical engine design decisions are being made, and new developments are being tested. In this project, the simulation shall be validated experimentally against real data from a two-stroke marine test engine in Everllence’s Research Center in Copenhagen. An uncertainty and sensitivity analysis of the simulation model will reveal a distribution of model output predictions. Using these, a quantification of model accuracy in different operating conditions can be performed, e.g., with different fuel types or loading conditions, to compare model predictions to reality and thereby identifying model inaccuracies and weaknesses. This will help improve the model and engine design based on simulations in the future.

The second part of the project aims to build an advanced probabilistic machine learning surrogate model as a prototype for replacing and/or correcting the high-fidelity simulation. The surrogate model can be more efficient but should retain simulation accuracy. Further, it should be able to quantify its uncertainty, e.g., by outputting a distribution of its predicted variables. Potential models can be Gaussian processes, Bayesian neural networks, deep ensembles or Monte Carlo dropout methods.

## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

- Perform a literature review on relevant topics (uncertainty/sensitivity analysis, probabilistic ML).
- Perform an uncertainty and sensitivity analysis of high-fidelity simulation environment, using varying ambient conditions as inputs to find expected distributions of outputs. 
- Use real data from a two-stroke marine test engine in the Research Center Copenhagen to map against simulation outputs and quantify model accuracy. 
- Build a probabilistic machine-learning based surrogate model with the simulated and/or real data as target (to be decided). 
- Define scenarios and performance metrics for evaluation of the designed surrogate model. 

## Methods & Tools

The project combines **machine learning, model validation, implementation, and numerical simulation**.

The theoretical work will focus on the systematic (learning-based) valdation of the model for the marine diesel engine system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature and resources

1. Molla, E. (2026). Development of an Operationally Usable Data-Driven Performance Model Based on Engine Simulation Data. DTU Department of Applied Mathematics and Computer Science. Available on [DTU Findit](https://findit.dtu.dk/catalog/6a94c617b8a3322151a06ecd).
2. Williams, C. K., and Rasmussen, C. E. (2006). Gaussian processes for machine learning (Vol. 2, No. 3, p. 4). Cambridge, MA: MIT press.
3. Murphy, K. P. (2023). Probabilistic machine learning: Advanced topics. MIT press.

-	High fidelity engine simulation
-	Research Center Copenhagen (RCC) test engine
-	Distributed computing environment for simulation execution
-	Git, Python, C++, WSL (Ubuntu)


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Nick Hauptvogel** , nick.hauptvogel@everllence.com <br>
Senior RnD Engineer, Everllence

**Armita Pegah Barkhordari** , armita.barkhordari@everllence.com <br>
Senior RnD Engineer, Everllence