---
layout: page
title: "TRANSITION"
project_id: transition
description: "Resilient Renewable Power Generation: Hybrid Power Plants with Distributed Control"
img: assets/img/research_projects/TRANSITION.png
importance: 7
category: current

full_title: "Resilient Renewable Power Generation: Hybrid Power Plants with Distributed Control"
start_year: 2026
end_year: 2029
role: "Participant"
responsibilities:
    - "WP1"
    - "WP2"

funders: dff
programme: "Green Research"

budget: 7199252
currency: "DKK"

partners:
  - dtu-wind

external_url:
publication_tag: transition
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

To tackle climate change, clean power generation is essential for a just and efficient transition to sustainable energy where power grids will be dominated by converter-based
Renewable Power Plants (RPPs), replacing fossil fuels and avoiding carbon emissions.

Hybrid Power Plants (HPPs) integrating multiple technologies (Wind Power Plants (WPPs), Solar Power Plants (SPPs), Battery Energy Storage Systems (BESS)) with complementary capabilities and operating as cohesive units with a common point of connection (PoC), will become more common among RPPs due to their enhanced grid stability, resource optimization, environmental benefits, resilience, energy storage, and cost efficiency.

TRANSITION proposes a Distributed Control Approach (DCA) for HPPs, utilizing a network of autonomous software agents. Each agent operates with local measurements and decision-making capabilities, enabling fast, robust, and scalable system responses.

## Objectives

This project aims to design, implement, and verify a robust DCA for HPPs that enables fast (< 900 ms), autonomous, and resilient grid service delivery under high uncertainty and complexity.

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