---
layout: page
title: Research
permalink: /research/
description:
nav: true
show_title: false
nav_order: 1
---

My research focuses on system resilience and fault-tolerance with performance guarantees. I am particularly interested in the development of nonlinear and sliding-mode control and estimation methods to ensure safe operation. Moreover, I investigate singularity-aware mapping inversion for reliable condition monitoring.

## Research Areas

<div class="row research-areas">
  {% for area in site.data.research_interests %}
    <div class="col-md-4 mb-4">
      <div class="research-area-card">

        <div class="research-area-image">
          <img
            src="{{ area.image | relative_url }}"
            alt="{{ area.title }}"
          >
        </div>

        <div class="research-area-content">
          <h3>{{ area.title }}</h3>
          <p>{{ area.description }}</p>
        </div>

      </div>
    </div>
  {% endfor %}
</div>

[View current and past research projects →](/research-projects/)

