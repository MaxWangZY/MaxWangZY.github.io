---
layout: default
title: Home
---

<section class="hero hero-with-portrait">
  <figure class="portrait">
    <img src="{{ '/assets/images/portrait.jpg' | relative_url }}" alt="Portrait of Zhengyang Wang">
  </figure>
  <div class="hero-copy">
    <h1>Zhengyang Wang</h1>
    <div class="intro">
      <p>
        I go by Max. I'm a rising senior at the University of Michigan studying
        Mathematics and Data Science. My research interests
        include constrained optimization, vehicle routing problems, and game
        theory. This site collects my research, projects, and notes on markets
        and systems. Here is my
        <a href="{{ '/assets/cv/Zhengyang_Wang_CV.pdf' | relative_url }}">CV</a>.
      </p>
    </div>
  </div>
</section>

{% if site.data.artifacts.size > 0 %}
  <section class="section">
    <h2>Recent</h2>
    <div class="artifact-list">
      {% for artifact in site.data.artifacts limit: 6 %}
        {% if artifact.more %}
          <article class="artifact artifact-more">
            <div class="artifact-meta"></div>
            <div class="artifact-body">
              <a class="artifact-dots" href="{{ artifact.url | relative_url }}" aria-label="View more experience">...</a>
            </div>
          </article>
        {% else %}
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
              </div>
            </div>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>
{% endif %}

<section class="section link-grid grid">
  <article>
    <h2>Experience</h2>
    <p>
      A curated companion to my CV, focused on research, optimization projects,
      and selected technical work.
    </p>
    <a href="{{ '/experience/' | relative_url }}">View full experience</a>
  </article>
  <article>
    <h2>Blog</h2>
    <p>
      Analytical notes on markets, systems, and ideas I am trying to understand
      more clearly.
    </p>
    <a href="{{ '/blog/' | relative_url }}">Read posts</a>
  </article>
</section>
