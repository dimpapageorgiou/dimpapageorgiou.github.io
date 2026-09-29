---
layout: page
title: "Stability and Systematic Tuning of Super-Twisting Sliding Mode Control Loops"
description: 
status: available
project_types:
  - MSc
ects: 30-35
orientation: 5
partners:
topics:
  - Sliding Mode Control
  - Nonlinear Control
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
    src="{{ '/assets/img/student-projects/stsmc-stability-tuning.png' | relative_url }}"
    alt="Super-Twisting Sliding Mode Control project"
    style="max-width: 100%; height: auto;"
  >
</div>

## Overview
Sliding-mode controllers have been shown to facilitate robust high-accuracy stabilisation. This makes sliding-mode algorithms excellent candidates for servo and positioning solutions in motion control systems. Second-order sliding mode controllers and in particular, the STSMC, have simple design, while at the same time are very robust and with reduced chatter. However, systematic tuning of STSMCs that corresponds to the real system limitations can be a challenging task. Relating the controller gains to the system performance specifications is desirable if prescribed accuracy is to be guaranteed.

This master project concerns the performance analysis of STSMC loops where the finite-time stability conditions of the controller gains do not hold. More specifically, the aim of the project is to compare the performance of under-tuned STSMC before and after discretisation for the case of **periodic** and **bounded perturbations**. Furthermore, the goal is to extract – if possible – extensions of the conditions for boundedness of under-tuned STSMC loops in the discrete time. Such conditions can eventually be leveraged for the systematic tuning of the controller. 


## Project Objectives
The following objectives are expected to be met and documented in the thesis by the end of the project:

1. Perform a literature study on the topics relevant to the project and in particular to
    - Tuning methods for the STSMC algorithm and stability of under-tuned STSMC loops.
    - Discrete-time STSMC and its variations.
    - Existence of periodic solutions in discrete time.
2. Set up a simple simulator of a first-order perturbed system with a STSMC in Matlab/Python.
3. Investigate the effects of equivalent descriptions of a given perturbation on the closed-loop system (e.g. energy-based, amplitude-based etc.).
4. Implement continuous under-tuned STSMC and its discretised counterparts.
5. Test and compare the properties of the closed loops (boundedness, periodicity) for both types of STSMC (continues and discretised) and for different perturbations (periodic and just bounded).
6. Extend the conditions for boundedness to the case of under-tuned discrete STSMC.
7. Validate the theoretical findings in simulation.


## Methods & Tools

The project combines **nonlinear control theory, stability analysis, and numerical simulation**.

The theoretical work will focus on the analysis of Super-Twisting Sliding Mode Control loops under bounded perturbations, including conditions for boundedness and periodic behaviour and their relation to closed-loop accuracy.

Numerical investigations will be carried out in **MATLAB/Simulink or Python** to evaluate the derived results and the proposed tuning methodology.

## Starting Literature

1. D. Papageorgiou and C. Edwards, “On the behaviour of under-tuned super-twisting sliding mode control loops,” *Automatica*, 135, 109983, 2022.
2. D. Papageorgiou, “Towards Prescribed Accuracy in Under-tuned Super-Twisting Sliding Mode Control Loops — Experimental Verification,” *American Control Conference (ACC)*, 2022.
3. P. A. Refosco, C. Edwards, and D. Papageorgiou. "Conditions for boundedness of under-tuned super-twisting sliding mode control loops". *IEEE Transactions on Automatic Control*, 2026.
4. J. A. Moreno and M. Osorio, “Strict Lyapunov functions for the super-twisting algorithm,” *IEEE Transactions on Automatic Control*, 57(4), 1035–1040, 2012.
5. R. Seeber and M. Horn, “Necessary and sufficient stability criterion for the super-twisting algorithm,” *International Workshop on Variable Structure Systems (VSS)*, 120–125, 2018.
6. M. A. Gomez, C. D. Cruz-Ancona, and L. Fridman, “On the Notion of Safe Sliding Mode Control,” 2022.
7. H. Obeid, S. Laghrouche, L. Fridman, Y. Chitour, and M. Harmouche, “Barrier function-based adaptive super-twisting controller,” *IEEE Transactions on Automatic Control*, 65(11), 4928–4933, 2020.
8. C. Edwards and Y. Shtessel, “Adaptive dual-layer super-twisting control and observation,” *International Journal of Control*, 89(9), 1759–1766, 2016.

## Supervision

**Dimitrios Papageorgiou**  , dimpa@dtu.dk <br>
DTU Electrical and Photonics Engineering