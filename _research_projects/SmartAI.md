---
layout: page
title: Smart AI
project_id: smart-ai
description: Learning-based parameter estimation in high-dimensional spaces for marine engine commissioning
img: assets/img/research_projects/Smart-ai.png
importance: 3
category: current

full_title: "Learning-based parameter estimation in high-dimensional spaces for marine engine commissioning"
start_year: 2026
end_year: 2029
role: "Principal Investigator"
responsibilities:
  - "WP1"
  - "WP2"
  - "WP3"
funders: innovation-fund-denmark
programme: "Industrial PhD"
budget: 
currency: "DKK"

partners:
  - everllence
external_url:
publication_tag: smart-ai
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

Identification of large sets of parameters is a fundamental problem relating to the commissioning of complex industrial systems, such as assembly lines, wind turbine control systems and marine engines. Conventional approaches to this problem involve statistical, heuristic and optimisation-based methods that can fall short in addressing the system complexity and variability. For instance, despite standardised design documents, deployed engines vary due to different manufacturers, unknown brands, and diverse configurations not captured in datasets. These uncertainties make it impractical to solely rely on predefined
rules or fixed statistical models. In contrast, AI-based strategies can dynamically leverage
structured and unstructured data, identifying hidden patterns and generalising across incomplete or noisy datasets. This enables parameter-assignment models that improve with more data available andadapt to differing design and component variations.

Smart AI investigates methdos for learning-based parameter estimation and calibration in complex, high-dimensional systems, using large two-stroke marine engines as the primary application. By combining historical commissioning data, real-world operational data, and high-fidelity simulations, the project aims to automate and improve engine commissioning while accounting for operational and performance constraints.

The project develops [methods] for addressing [problem/application].

## Objectives

- Develop AI-based parameter calibration methods for high-dimensional systems that learn from historical and operational data while respecting system and operational constraints.
- Develop real-time parameter validation and error prevention methods that detect invalid or out-of-range parameter settings and recommend corrective actions.
- Assess robustness and transferability of the AI-based parameter estimation approach across different engine types, configurations, and operating regimes using simulation and sensitivity analysis.

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