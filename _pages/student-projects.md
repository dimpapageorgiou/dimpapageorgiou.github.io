---
layout: page
title: Student Projects
permalink: /student-projects/
description: 
nav: true
nav_order: 5
---

<p>
I offer BSc, MSc, and special-course projects related to my research.
The available topics are listed below. Click on a project to see the full
description and supervision details.
</p>

<div class="student-projects">

{% assign available_projects = site.student_projects | where: "status", "available" | sort: "importance" %}

{% for project in available_projects %}

<div class="student-project-item">

  <h3>
    <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
  </h3>

  <p class="project-preview-meta">
  {% if project.project_types %}
    <strong>{{ project.project_types | join: " · " }}</strong>
  {% endif %}

  {% if project.orientation %}
    <span class="project-orientation">
      <span>Practical</span>

      <span class="orientation-scale">
        {% for i in (1..5) %}
          <span class="orientation-box {% if i == project.orientation %}active{% endif %}"></span>
        {% endfor %}
      </span>

      <span>Theoretical</span>
    </span>
    {% endif %}
    {% if project.partners %}
  {% for partner_id in project.partners %}
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
</p>

  {% if project.topics %}
    <p><em>{{ project.topics | join: " · " }}</em></p>
  {% endif %}

  <p>{{ project.description }}</p>

  <p>
    <a href="{{ project.url | relative_url }}">Read more →</a>
  </p>

</div>

<hr>

{% endfor %}

</div>