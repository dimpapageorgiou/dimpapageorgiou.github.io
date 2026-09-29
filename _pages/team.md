---
layout: page
title: Team
permalink: /team/
description: 
nav: true
show_title: false
nav_order: 4
---

<h2>Research Team</h2>

<div class="row mt-4">

  <!-- Dimitrios -->
  <div class="col-md-6 mb-3">
    <div class="row team-member">
      <div class="col-4">
        <img src="/assets/img/prof_pic.jpg"
             class="img-fluid rounded"
             alt="Dimitrios Papageorgiou">
      </div>
      <div class="col-8">
        <h5>Dimitrios Papageorgiou</h5>
        <strong>Associate Professor</strong>
        <p class="team-member-position">
          <strong>email</strong>: <a href="mailto:dimpa@dtu.dk">dimpa@dtu.dk</a><br>
          <strong>Office</strong>: Building 326, room 124 <br>
          <strong>Group</strong>: Control, Robotics and Embodied AI (CREA)
        </p>
      </div>
    </div>
  </div>

  <!-- Current PhD students -->
  {% assign current_phds = site.data.phd_students
    | where: "status", "current"
    | where: "role", "Main supervisor"
  %}

  {% for member in current_phds %}
    <div class="col-md-6 mb-3">
      <div class="row team-member">

        <div class="col-4">
          {% if member.img %}
            <img
              src="{{ member.img | relative_url }}"
              class="img-fluid rounded team-member-photo"
              alt="{{ member.name }}"
            >
          {% endif %}
        </div>

        <div class="col-8 team-member-info">
          <h5>{{ member.name }}</h5>

          <div class="team-member-position">
            <strong>PhD student</strong>
            {% if member.start_month and member.start_year %}
              · Started {{ member.start_month | slice: 0, 3 }} {{ member.start_year }}
            {% elsif member.start_year %}
              · Started {{ member.start_year }}
            {% endif %}
          </div>

          {% if member.email %}
            <div class="team-member-email">
              <strong>email</strong>: <a href="mailto:{{ member.email }}">{{ member.email }}</a>
            </div>
          {% endif %}

          {% if member.title %}
            <p class="team-member-topic">
              {{ member.title }}
            </p>
          {% endif %}
        </div>

      </div>
    </div>
  {% endfor %}

    <!-- Current postdocs -->
  {% assign current_postdocs = site.data.postdocs | where: "status", "current" %}

  {% for member in current_postdocs %}
    <div class="col-md-6 mb-3">
      <div class="row team-member">

        <div class="col-4">
          {% if member.img %}
            <img
              src="{{ member.img | relative_url }}"
              class="img-fluid rounded team-member-photo"
              alt="{{ member.name }}"
            >
          {% endif %}
        </div>

        <div class="col-8">
          <h5>{{ member.name }}</h5>

          <div class="team-member-position">
            <strong>Postdoc</strong>
            {% if member.start_month and member.start_year %}
              · Started {{ member.start_month | slice: 0, 3 }} {{ member.start_year }}
            {% elsif member.start_year %}
              · Started {{ member.start_year }}
            {% endif %}
          </div>

          {% if member.email %}
            <div class="team-member-email">
              <strong>email</strong>: {{ member.email }}
            </div>
          {% endif %}

          {% if member.title %}
            <p class="team-member-topic">
              <strong>Project</strong>: {{ member.title }}
            </p>
          {% endif %}
        </div>

      </div>
    </div>
  {% endfor %}
</div>


<h2 class="mt-5">Current Students</h2>
{% comment %}
<p> <strong>Hans Christian Falkow</strong> — MSc Thesis<br> <em>Advanced Motion Control of a Variable-Configuration Underwater Vehicle</em> </p>

<p> <strong>Paul Martin Künnapuu</strong> — MSc Thesis<br> <em>Machine Learning for Time-Varying Channels Estimation and Equalization in Maritime Environment</em> </p>

<p> <strong>Jianing Zheng</strong> — MSc Thesis<br> <em>Modelling and homogeneity-based PID control of underwater vehicle</em> </p>
{% endcomment %}

{% assign current_students = site.data.students | where: "status", "current" %}

{% for student in current_students %}
  <p>
    <strong>{{ student.name }}</strong> — {{ student.type }}
    {% if student.type == "MSc" %} Thesis{% elsif student.type == "BSc" %} Project{% endif %}<br>
    <em>{{ student.title }}</em>
  </p>
{% endfor %}

<h2 class="mt-5">Former Group Members</h2>

<div class="row mt-4">

  <!-- Former PhD students -->
  {% assign former_phds = site.data.phd_students
    | where: "status", "former"
    | where: "role", "Main supervisor"
  %}

  {% for member in former_phds %}
    <div class="col-md-6 mb-3">
      <div class="row team-member">

        <div class="col-4">
          {% if member.img %}
            <img
              src="{{ member.img | relative_url }}"
              class="img-fluid rounded team-member-photo"
              alt="{{ member.name }}"
            >
          {% endif %}
        </div>

        <div class="col-8">
          <h5>{{ member.name }}</h5>

          <div class="team-member-position">
            <strong>PhD student</strong>
            {% if member.start_year and member.end_year %}
              · {{ member.start_year }}–{{ member.end_year }}
            {% endif %}
          </div>

          {% if member.title %}
            <p class="team-member-topic">
              <strong>Thesis</strong>: {{ member.title }}
            </p>
          {% endif %}
        </div>

      </div>
    </div>
  {% endfor %}


  <!-- Former postdocs -->
  {% assign former_postdocs = site.data.postdocs | where: "status", "former" %}

  {% for member in former_postdocs %}
    <div class="col-md-6 mb-3">
      <div class="row team-member">

        <div class="col-4">
          {% if member.img %}
            <img
              src="{{ member.img | relative_url }}"
              class="img-fluid rounded team-member-photo"
              alt="{{ member.name }}"
            >
          {% endif %}
        </div>

        <div class="col-8">
          <h5>{{ member.name }}</h5>

          <div class="team-member-position">
            <strong>Postdoc</strong>
            {% if member.start_year and member.end_year %}
              · {{ member.start_year }}–{{ member.end_year }}
            {% elsif member.start_year %}
              · {{ member.start_year }}
            {% endif %}
          </div>

          {% if member.title %}
            <p class="team-member-topic">
              <strong>Project</strong>: {{ member.title }}
            </p>
          {% endif %}
        </div>

      </div>
    </div>
  {% endfor %}

</div>


<h2 class="mt-5">Former Students</h2>

{% assign former_students = site.data.students | where: "status", "former" %}
{% assign former_msc = former_students | where: "type", "MSc" %}
{% assign former_bsc = former_students | where: "type", "BSc" %}

{% assign total_supervisions = former_students | size %}

{% assign unique_msc_titles = former_msc | map: "title" | uniq %}
{% assign unique_bsc_titles = former_bsc | map: "title" | uniq %}

{% assign msc_count = unique_msc_titles | size %}
{% assign bsc_count = unique_bsc_titles | size %}

<p class="student-counts">
  <strong>{{ total_supervisions }}</strong> completed supervisions
  · <strong>{{ msc_count }}</strong> MSc theses
  · <strong>{{ bsc_count }}</strong> BSc projects
</p>

{% assign years = former_students | map: "year" | uniq | sort | reverse %}

{% for year in years %}

<details>
  <summary><h4 style="display: inline;">{{ year }}</h4></summary>

  <div class="mt-3">

    {% assign students_this_year = former_students | where: "year", year %}

    {% for student in students_this_year %}
      <p>
        <strong>{{ student.name }}</strong> — {{ student.type }}
        {% if student.type == "MSc" %} Thesis{% elsif student.type == "BSc" %} Project{% endif %}<br>
        <em>{{ student.title }}</em>
      </p>
    {% endfor %}

  </div>
</details>

{% endfor %}