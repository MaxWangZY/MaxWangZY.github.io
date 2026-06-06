---
layout: default
title: Home
---

<section class="hero">
  <h1>Zhengyang Wang</h1>
  <p class="lede">"Optimization is everywhere."</p>
  <div class="intro">
    <p>
      I go by Max. I am interested in optimization as both a research language
      and a practical way to understand markets. This site collects my work in
      operations research, technical systems, and market research around AI
      infrastructure.
    </p>
  </div>
</section>

{% if site.data.artifacts.size > 0 %}
  <section class="section">
    <h2>Recent</h2>
    <div class="artifact-list">
      {% for artifact in site.data.artifacts limit: 3 %}
        <article class="artifact">
          <div class="artifact-meta">
            <a class="artifact-type" href="{{ artifact.url | relative_url }}">{{ artifact.label | downcase }}</a>
            {% if artifact.date %}
              <time>{{ artifact.date }}</time>
            {% endif %}
          </div>
          <div class="artifact-body">
            <h3><a href="{{ artifact.url | relative_url }}">{{ artifact.title }}</a></h3>
            <div class="artifact-excerpt">
              {% for paragraph in artifact.preview %}
                <p>{{ paragraph }}</p>
              {% endfor %}
              <a class="artifact-link" href="{{ artifact.url | relative_url }}">{{ artifact.cta }}</a>
            </div>
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
{% endif %}

<section class="section link-grid grid">
  <article>
    <h2>Experience</h2>
    <p>
      Research, market work, portfolio theses, and mini projects organized as a
      broader record of what I am building and studying.
    </p>
    <a href="{{ '/experience/' | relative_url }}">View experience</a>
  </article>
  <article>
    <h2>Blog</h2>
    <p>
      Longer notes behind selected artifacts, including market research,
      technical reflections, and ideas that need more room.
    </p>
    <a href="{{ '/blog/' | relative_url }}">Read posts</a>
  </article>
</section>
