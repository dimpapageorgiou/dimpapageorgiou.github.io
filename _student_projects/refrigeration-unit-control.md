---
layout: page
title: "Reliable and robust control strategy for a refrigeration unit in a Plug and play framework"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 2
partners:
- danfoss
topics:
  - Refrigeration systems
  - Nonlinear control
  - Auto-tuning
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
    src="{{ '/assets/img/student-projects/refrigeration_unit.png' | relative_url }}"
    alt="Refrigeration unit Control project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Many industrial systems are controlled by a type of classical PI(D) controllers where the installer typically uses an experienced-based set of controller parameters due to the lack of information about the dynamical behavior of these systems (i.e. no detailed dynamical models exists for these systems.) The idea in this project is to investigate the possibility of utilizing a control strategy that, based on simple identification methods, can automatically device a controller that is robust, reliable, and capable of handling both the internal nonlinear behavior as well as external disturbances. The application in this project is a given classical display case, used in a supermarket refrigeration system (as case study). An expected configuration of the used sensor instrumentation for the unit is illustrated in the above figure.

The used sensors are:
- S1: temperature sensor placed at the inlet of the evaporator and after the expansion valve – Alternatively a pressure measurement device placed at the end of the evaporator (P_e).
- S2: temperature sensor that is placed at the outlet of the evaporator and measures the refrigerant temperature. 
- S3: temperature sensor that is placed at the Air inlet of the evaporator and measures the air temperature (the warm air). 
- S4: temperature sensor that is placed at the Air outlet of the evaporator and measures the air temperature (the cold air). 
- OD: Opening degree of the expansion valve which is the main actuator in this application.

In traditional applications the customary design involves using a pressure sensor (indicated by P_e in the figure).

**Purpose**: To develop a control strategy that can be implemented on any refrigerated unit in various refrigeration systems (industrial, air condition, supermarket, heat pumps), i.e. in a plug-n-play framework.

As a baseline the controller should use a simple but very robust control strategy in order to guarantee the overall requirements that are food and operational safety (not causing the compressor failure by ensuring that the refrigerant at the outlet of the evaporator is superheated).

The controller should, furthermore, optimize its performance under different operational conditions. The considered system (a refrigeration system) is chosen to maintain overview and clarity, while at the same time exhibiting nonlinearities that are common in industrial systems.

**Scope**: The focus will be on the evaporation unit (or the refrigerator) of the complete refrigeration cycle. The developed algorithms will primarily be implemented and tested on a (nonlinear model) in Matlab/Simulink environment. However, the resulting solution shall be tested and verified on a real system in the Danfoss Lab. In Nordborg.

## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to refrigeration system dynamics and adaptive control methods
- Derive a first-principle mathematical model of a refrigeration system suitable for control design. 
- Define a mapping between desired performance specifications and dynamical properties of the closed-loop system. 
- Design a nonlinear control scheme that satisfies the performance specifications. Explore the option of adaptation or robust sliding mode control. 
- Implement the controller (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and compare the designed controller against conventional solutions (e.g. PI). 

Any developed method is expected to meet the following requirements:
-	Robustness: The solution strategy should be robust against external disturbances (and unknown internal nonlinearities)
-	Fast adaption and learning period: information on system dynamics can be obtained through implementation of appropriate system identification techniques. The required time for carrying out the system identification periods should be limited (to avoid problems with maintaining food safety requirements) 
-	Plug-n-Play feature: As the detailed dynamics of the underlying systems (i.e. evaporators) are not known in advance, it is required that the controller provides safety (under all conditions) and optimal performance, while maintaining its core functionality during the operation.


## Methods & Tools

The project combines **control theory, implementation, and numerical simulation**.

The theoretical work will focus on the modelling and control sysnthesis for the refrigertation system based on operational constraints.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature and resources

1. Past thesis and special course report (incoordination with the supervisor).
2. A nonlinear simulation model of the considered system (SIMULINK) will be available for test and verification of different solutions.
3. It is possible to test the developed algorithms on real system (Danfoss Lab). It is also possible to arrange a short period stay for the candidate to check the developed solution on the real system.


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Roozbeh Izadi-Zamanabadi** , Roozbeh@danfoss.com <br>
Lead Expert in Cont. Tech., Danfoss A/S