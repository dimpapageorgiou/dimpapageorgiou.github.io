---
layout: page
title: "Virtual sensor design for estimating exhaust gas temperature (EGT) in marine diesel engines"
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
  - Fault diagnosis
  - Diesel engines
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
    src="{{ '/assets/img/student-projects/marine_products_four-stroke.jpg' | relative_url }}"
    alt="EG virtual sensor project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
The master’s project focuses on the development of a virtual sensor for estimating exhaust gas temperature (EGT) in marine diesel engines.
In marine engines, exhaust gas temperature is an important parameter because it indicates combustion quality, engine efficiency, cylinder condition, and possible faults such as injector problems or turbocharger issues. Normally, EGT is measured using thermocouples installed in the exhaust manifold. However, these physical sensors are exposed to harsh operating conditions including high temperature, vibration, soot accumulation, and corrosion, which often lead to sensor failure and maintenance challenges.

The idea of this project is to estimate exhaust gas temperature without relying entirely on direct physical measurement. Instead, the project will use a virtual sensing approach where EGT is predicted using other engine parameters that are already available from the engine monitoring system.

The proposed method is based on collecting operational engine data such as:
1.	Engine RPM 
2.	Engine load 
3.	Fuel injection quantity 
4.	Scavenge air pressure 
5.	Turbocharger speed 
6.	Cooling water temperature 
7.	Cylinder pressure 

These parameters are strongly related to the combustion process and therefore influence exhaust gas temperature. The project will first involve studying the thermodynamic relationship between these engine variables and EGT. Then, a prediction model would be developed using either:
1.	mathematical regression models, 
2.	thermodynamic equations or 
3.	machine learning techniques such as Artificial Neural Networks (ANN) or Random Forest models. 
The general idea is that the model learns the relationship between engine operating conditions and the corresponding exhaust gas temperature. The predicted exhaust gas temperature from the virtual sensor would then be compared with actual measured EGT values to evaluate the accuracy of the model using error analysis methods such as RMSE or MAE.

The long-term goal of the project is to support:
1.	predictive maintenance, 
2.	remote engine monitoring, 
3.	reduced dependence on physical sensors, 
4.	and improved reliability in marine engine diagnostics. 
This project combines marine engineering with data-driven monitoring and could contribute to smart shipping and digitalization in the maritime industry

## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to marine diesel engine dynamics and virtual sensor methods
- Derive a first-principle mathematical model of a of the engine system suitable for virtual sensor design. 
- Augment the derived mathematical model with a descriptino for the EGT sensor and the possible faults. 
- Design a virtual sensor solution that satisfies the perfomrance requirements against considered faults and oprating scenarios. 
- Implement the solution (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and compare the designed virtual sensor against real data. 


## Methods & Tools

The project combines **control theory, fault diagnosis, implementation, and numerical simulation**.

The theoretical work will focus on the development of the virtual sensor solution for the marine diesel engine system.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature and resources

1. Blanke, M., Kinnaert, M., Lunze, J., and Staroswiecki, M. (2015). "Diagnosis and Fault-tolerant Control", 3rd Edition. Springer. Available on [DTU Findit](https://findit.dtu.dk/catalog/561d2a87e64357331200002b).
2. System specific reports (in coordination with the company supervisor).


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Armita Pegah Barkhordari** , armita.barkhordari@everllence.com <br>
Senior RnD Engineer, Everllence