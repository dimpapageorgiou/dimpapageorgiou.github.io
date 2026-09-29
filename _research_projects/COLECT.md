---
layout: page
title: "COLECT"
project_id: colect
description: Control and Learning of Contact Transitions
img: assets/img/research_projects/COLECT.png
importance: 12
category: past

full_title: "Control and Learning of Contact Transitions"
start_year: 2023
end_year: 2024
role: "WP Leader"
responsibilities:
  - "WP1"

funders: OR
programme:

budget: 500000
currency: "DKK"

partners:
  - sdu

external_url:
publication_tag: colect
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

COLECT aims to develop safe and robust control and learning methods for robotic manipulators performing force-sensitive contact tasks. The project combines advanced contact detection, adaptive compliant control, constant-force mechanisms, and learning from demonstration to enable smooth transitions between free motion and contact while maintaining accurate and safe interaction forces. The developed methods target applications ranging from industrial processes such as grinding and polishing to medical robotics, where reliable and adaptable physical interaction with the environment is essential.

## Objectives

- Develop robust contact detection methods for smooth and safe transitions between free motion and contact.
- Develop adaptive compliant control methods for accurate and safe force regulation during contact.
- Develop adjustable constant-force mechanisms for passive force regulation with adaptable force references.
- Develop learning-from-demonstration methods to encode and reproduce motion, force, and impedance profiles for force-sensitive robotic tasks.

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

  <div class="publications">
    {% bibliography -f papers -q @*[projects={{ page.publication_tag }}] %}
  </div>
{% endif %}