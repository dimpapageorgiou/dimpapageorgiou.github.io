---
layout: page
title: "U-Shield"
project_id: u-shield
description: Underwater Safeguarding High-value Infrastructure Enforcing Lightweight Drones
img: assets/img/research_projects/UShield.png
importance: 6
category: current

full_title: "Underwater Safeguarding High-value Infrastructure Enforcing Lightweight Drones"
start_year: 2025
end_year: 2028
role: "Task Leader"
responsibilities:
  - "WP4"

funders: innovation-fund-denmark
programme: "Grand Solutions"

budget: 25972396
currency: "DKK"

partners:
  - aau
  - sdu
  - teledyne-marine

external_url:
publication_tag: ushield
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

The overall goal of U-SHIELD is to strengthen the security of maritime critical infrastructure by delivering the first Autonomous Underwater Interceptor Drone (AUID) featuring technology for hunting, catching, and immobilizing intruder Autonomous Underwater Vehicles (AUVs). U-SHIELD aims at developing, implementing, and validating at TRL6 the AUID prototype capable of localizing, tracking, and immobilizing an intruder AUV (iAUV) for subsequent recovery by the appointed authorities using a surface vessel.

## Objectives

- Design & prototype a torpedo-shaped AUID capable of high-speed maneuvering with a top
speed of 6-8 knots, operating at water depths up to 100m for at least 2 hours.
- Develop & verify through laboratory and harbor tests an opto-acoustic tracking system (HW
& SW) capable of detecting and tracking the iAUV through its acoustic signature from a maximum distance of 500m in noisy underwater environments, and through visual cues from a maximum distance of 5m in turbid waters.
- Develop & verify through laboratory and harbor tests a software suite for real-time mission, path and motion planning to enable the AUID to optimally intercept the iAUV while performing highspeed obstacle avoidance.
- Develop & verify through laboratory and harbor tests a mechatronic immobilization system
(HW & SW) capable of blocking the iAUV propeller within 1 minute after reaching a relative
distance of maximum 0.5m.
- Validate the AUID in offshore environments and provide a roadmap for technological
upscaling and commercialization.

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