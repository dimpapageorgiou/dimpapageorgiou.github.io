---
layout: page
title: SAFE-LIFT
project_id: safe-lift
description: Learning-based dimension lifting for singularity avoidance in dynamical systems
img: assets/img/research_projects/SAFE-LIFT.png
importance: 2
category: current

full_title: "Learning-based dimension lifting for singularity avoidance in dynamical systems"
start_year: 2026
end_year: 2029
role: "Principal Investigator"
responsibilities:
  - "WP1"
  - "WP2"
  - "WP3"
funders: ddsa
programme: "DDSA PhD Scholarship"
budget: 2000000
currency: "DKK"

partners:

external_url:
publication_tag: safe-lift
---

<div class="project-hero">
  <img
    src="{{ page.img | relative_url }}"
    alt="{{ page.title }}"
  >
</div>

<div class="project-summary">
  {% if page.start_year %}
    <span>
      {{ page.start_year }}{% if page.end_year %}–{{ page.end_year }}{% endif %}
    </span>
  {% endif %}

  {% if page.role %}
    <span>{{ page.role }}</span>
  {% endif %}

  {% if page.programme %}
    <span>{{ page.programme }}</span>
  {% endif %}

  <a class="project-back-link" href="{{ '/research-projects/' | relative_url }}">
    All research projects →
  </a>
</div>

## About the project

Accurate and robust estimation of system parameters from complex nonlinear mappings is central to data-driven inference, from dynamic monitoring to adaptive control. However, conventional parameter estimation laws can become ill-conditioned or singular in certain regions of the parameter space, resulting in unreliable or undefined estimates. This challenge is particularly relevant in renewable-dominated power systems, where the Short Circuit Ratio (SCR)—a key indicator of grid strength and stability—must be continuously monitored. As inverter-based resources proliferate, grid dynamics become increasingly nonlinear, and singularities in the mappings between operational data and strength indicators pose barriers to classical inversion methods.

SAFE-LIFT develops a novel safe dynamic mapping inversion framework for reliable estimation in the presence of such singularities. By combining geometric data science with adaptive estimation and selective learning, the approach characterizes and manages unsafe regions where standard inversion laws become ill-posed. When these regions form algorithmic barriers, structured coordinate transformations and higher-dimensional immersions are constructed to enable the estimation process to traverse them while maintaining numerical stability and interpretability.


## Objectives

- Develop a theoretical framework for singularity-safe and reliable parameter estimation in complex nonlinear systems.
- Characterize singularities and unsafe regions that compromise the stability and reliability of parameter estimation.
- Develop geometric and learning-based dimension-lifting methods to enable stable estimation across singular and disconnected parameter regions.
- Validate the developed estimation framework through SCR monitoring in renewable-dominated power systems using synthetic and experimental data.

## Project information

<div class="project-info">

  {% if page.funders %}
  <div class="project-info-item">
    <span class="project-info-label">
      {% if page.funders.size > 1 %}Funders{% else %}Funder{% endif %}
    </span>

    <span class="project-info-value project-funders">
      {% for funder_id in page.funders %}
        {% assign funder = site.data.funders[funder_id] %}

        {% if funder %}
          {% if funder.url and funder.url != "" %}
            <a class="project-funder"
               href="{{ funder.url }}"
               target="_blank"
               rel="noopener">

              {% if funder.logo %}
                <img
                  class="project-funder-logo"
                  src="{{ funder.logo | relative_url }}"
                  alt="{{ funder.name }}"
                >
              {% endif %}

              <span>{{ funder.name }}</span>
            </a>
          {% else %}
            <span class="project-funder">
              {% if funder.logo %}
                <img
                  class="project-funder-logo"
                  src="{{ funder.logo | relative_url }}"
                  alt="{{ funder.name }}"
                >
              {% endif %}
              <span>{{ funder.name }}</span>
            </span>
          {% endif %}
        {% else %}
          <span>{{ funder_id }}</span>
        {% endif %}
      {% endfor %}
    </span>
  </div>
{% endif %}

  {% if page.programme %}
  <div class="project-info-item">
    <span class="project-info-label">Programme</span>
    <span class="project-info-value">{{ page.programme }}</span>
  </div>
  {% endif %}

  {% if page.start_year %}
  <div class="project-info-item">
    <span class="project-info-label">Period</span>
    <span class="project-info-value">
      {{ page.start_year }}{% if page.end_year %}–{{ page.end_year }}{% endif %}
    </span>
  </div>
  {% endif %}

  {% if page.role %}
  <div class="project-info-item">
    <span class="project-info-label">Role</span>
    <span class="project-info-value">{{ page.role }}</span>
  </div>
  {% endif %}

  {% if page.budget %}
  <div class="project-info-item">
    <span class="project-info-label">Budget</span>
    <span class="project-info-value">
      {{ page.currency }}
      <span class="formatted-number" data-number="{{ page.budget }}">
        {{ page.budget }}
      </span>
    </span>
  </div>
  {% endif %}

  {% if page.partners %}
  <div class="project-info-item">
    <span class="project-info-label">Partners</span>

    <span class="project-info-value project-partners">
      {% for partner_id in page.partners %}
        {% assign partner = site.data.partners[partner_id] %}

        {% if partner %}
          <a class="project-partner"
             href="{{ partner.url }}"
             target="_blank"
             rel="noopener"
             title="{{ partner.name }}">

            {% if partner.logo %}
              <img
                src="{{ partner.logo | relative_url }}"
                alt="{{ partner.name }}"
                class="project-partner-logo">
            {% endif %}

            <span>{{ partner.name }}</span>
          </a>
        {% else %}
          <span>{{ partner_id }}</span>
        {% endif %}
      {% endfor %}
    </span>
  </div>
{% endif %}

</div>

{% if page.external_url and page.external_url != "" %}
<a class="project-external-link"
   href="{{ page.external_url }}"
   target="_blank"
   rel="noopener">
  Official project page →
</a>
{% endif %}

## People

<div class="project-people">

{% for person in site.data.phd_students %}
  {% if person.projects contains page.project_id %}
    <div class="project-person">

      {% if person.img %}
        <img
          src="{{ person.img | relative_url }}"
          alt="{{ person.name }}"
          class="project-person-photo">
      {% endif %}

      <div class="project-person-info">
        <strong>{{ person.name }}</strong>
        <span>PhD Student</span>
        <span>DTU Department of Electrical and Photonics Engineering</span>
      </div>

    </div>
  {% endif %}
{% endfor %}


{% for person in site.data.postdocs %}
  {% if person.projects contains page.project_id %}
    <div class="project-person">

      {% if person.img %}
        <img
          src="{{ person.img | relative_url }}"
          alt="{{ person.name }}"
          class="project-person-photo">
      {% endif %}

      <div class="project-person-info">
        <strong>{{ person.name }}</strong>
        <span>Postdoc</span>
        <span>DTU Department of Electrical and Photonics Engineering</span>
      </div>

    </div>
  {% endif %}
{% endfor %}


{% for person in site.data.collaborators %}
  {% if person.projects contains page.project_id %}

    {% assign institution = site.data.partners[person.company] %}

    <div class="project-person">

      {% if person.img %}
        <img
          src="{{ person.img | relative_url }}"
          alt="{{ person.name }}"
          class="project-person-photo">
      {% endif %}

      <div class="project-person-info">
        <strong>{{ person.name }}</strong>
        <span>Collaborator</span>

        {% if institution %}
          <span>{{ institution.name }}</span>
        {% elsif person.company %}
          <span>{{ person.company }}</span>
        {% endif %}
      </div>

    </div>
  {% endif %}
{% endfor %}

</div>

{% if page.publication_tag %}
  <h2>Publications</h2>

  <div class="publications">
    {% bibliography -f papers -q @*[projects={{ page.publication_tag }}] %}
  </div>
{% endif %}