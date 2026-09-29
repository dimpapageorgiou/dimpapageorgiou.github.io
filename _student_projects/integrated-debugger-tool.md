---
layout: page
title: "Integrated Debugger Tool for Subsystem Failure Analysis"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 3
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
    src="{{ '/assets/img/student-projects/Integrated_debugger_tool.png' | relative_url }}"
    alt="Integrated Debugger project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
In this project, the control architecture is organized around a hierarchical state machine design, where a central Plant State Machine acts as the primary coordinator for multiple subordinate subsystems, each governed by its own Sub State Machine.

The Plant State Machine serves as the top-level controller responsible for driving, sequencing, and synchronizing all subsystem operations. It issues high-level commands that define the operational phases of the plant. Typical commands include states such as SFVT_READY, SFVT_CHECK, SFVT_TEST, SFVT_PRESS, and others depending on the process requirements. These commands represent distinct stages in the plant’s workflow and are broadcast to all relevant subsystems.

Each subsystem is implemented as an independent Sub State Machine that listens for commands from the Plant State Machine. Upon receiving a command, the Sub State Machine executes the corresponding task locally. This design allows each subsystem to encapsulate its own logic, handling internal transitions, safety checks, and execution details without burdening the central controller.

Once a subsystem successfully completes the requested action, it sends a feedback signal back to the Plant State Machine. This feedback uses the same identifier as the issued command (e.g., returning SFVT_READY after completing the readiness procedure). The Plant State Machine continuously monitors these feedback signals from all subsystems and evaluates whether the required conditions for progression are met.

Only when all necessary subsystems have confirmed completion of the commanded state does the Plant State Machine transition to the next phase. In this way, it ensures coordinated operation, maintains synchronization across subsystems, and enforces a structured and deterministic workflow throughout the plant.

This architecture provides several advantages, including modularity, scalability, and clear separation of responsibilities. The Plant State Machine focuses on orchestration and decision-making, while Sub State Machines handle execution, resulting in a robust and maintainable control system design.

**Project Scope**: Modern plant control systems rely on hierarchical state machine architectures, where a central Plant State Machine coordinates multiple Sub State Machines to ensure synchronized and reliable operation. While this structure provides robustness and modularity, diagnosing subsystem failures during operation remains a complex and time-consuming task. Engineers often need to analyze large volumes of recorded operational data alongside independently generated alarm logs, which are typically not directly correlated. This separation can delay fault identification and increase system downtime.

The objective of this master project is to design and develop an integrated debugger and diagnostic tool that enhances failure analysis by merging engine operational data with triggered alarm events into a unified framework. The tool aims to support onboard engineers by providing a clear, synchronized view of system behavior, enabling faster and more accurate debugging of subsystem issues.

The proposed solution will collect and align two primary data sources:
1. Engine operation data recordings, including state transitions, command execution (e.g., SFVT_READY, SFVT_CHECK, SFVT_TEST, SFVT_PRESS), subsystem responses, and relevant process variables.
2. Alarm and event logs, which capture fault conditions, warnings, and abnormal system behavior.

By time-synchronizing these datasets, the tool will allow users to directly associate alarm events with the corresponding operational context. For instance, when a subsystem fails to complete a commanded task, the tool will highlight the exact sequence of events leading up to the failure, including state machine interactions and parameter changes. This contextual insight enables engineers to quickly trace root causes rather than manually correlating separate logs.

The final system will include features such as:
- Time-aligned visualization of Plant and Sub State Machine activities
- Correlation of alarms with specific commands and subsystem responses
- Filtering and prioritization of critical events
- Interactive exploration of subsystem-level data for detailed analysis

The outcome of this project is a practical and user-oriented debugging tool that reduces diagnostic time, improves fault isolation, and supports more efficient maintenance and operation of complex plant systems. By transforming raw data and alarms into actionable insights, the tool contributes to increased system reliability and operational safety.

## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

- Perform a literature study on the topics relevant to the project and in particular to theory of discrete-event systems (DES).
- Model the alarm and diagnostics dyamics as a discrete-event system (automata or Petri nets) including transitions due to fautls. 
- Design a reasoning and debugging system that handles the incloming diagnostics from the low-level systems and combines them into a higher-level detection and isolation conclusion. 
- Implement the solution (e.g. Matlab/Simulink or Python) and perform simulations/experiments of different operation scenarios. 
- Define performance metrics and evaluate the proposed solution against real data. 


## Methods & Tools

The project combines **control theory, fault diagnosi, discrete-event systems, implementation, and numerical simulation**.

The theoretical work will focus on the development of the DES framework for modelling the even-triggered dynamics of the debugger.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived methodology.

## Starting Literature and resources

1. Blanke, M., Kinnaert, M., Lunze, J., and Staroswiecki, M. (2015). "Diagnosis and Fault-tolerant Control", 3rd Edition. Springer. Available on [DTU Findit](https://findit.dtu.dk/catalog/561d2a87e64357331200002b).
2. Cassandras, C. G., and Lafortune, S. (2008). "Introduction to discrete event systems". Springer US. Available on [DTU Findit](https://findit.dtu.dk/catalog/544a0073e44c7a86671fe2c3). 
3. System specific reports (in coordination with the company supervisor).


## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering

**Armita Pegah Barkhordari** , armita.barkhordari@everllence.com <br>
Senior RnD Engineer, Everllence