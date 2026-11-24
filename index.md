---
layout: default
title: Home
---

<div class="home-body">
  <aside class="home-profile" aria-label="Academic profile">
    <img class="home-profile-photo" src="{{ '/assets/images/portrait.jpg' | relative_url }}" alt="Portrait of Zhengyang Wang">
    <div>
      <p class="home-affiliation">University of Michigan</p>
      <p class="home-major">Mathematics &amp; Data Science</p>
      <nav class="home-contact-links" aria-label="Contact links">
        <a href="mailto:{{ site.email }}" aria-label="Email" title="Email">
          <img src="{{ '/assets/icons/envelope.svg' | relative_url }}" width="18" height="18" alt="">
        </a>
        <a href="https://github.com/{{ site.github_username }}" aria-label="GitHub" title="GitHub">
          <img src="{{ '/assets/icons/github.svg' | relative_url }}" width="18" height="18" alt="">
        </a>
        <a href="https://linkedin.com/in/zmaxwang" aria-label="LinkedIn" title="LinkedIn">
          <img src="{{ '/assets/icons/linkedin.svg' | relative_url }}" width="18" height="18" alt="">
        </a>
      </nav>
    </div>
  </aside>

  <div>
    <p class="home-intro">
      I go by <strong>Max</strong>. I study learning-based optimization, supply chain decisions under uncertainty,
      and routing games. Here’s my <a href="{{ '/assets/cv/Zhengyang_Wang_CV.pdf' | relative_url }}">CV</a>.
    </p>

    <div class="home-highlights">
      {% for group in site.data.artifacts %}
        {% assign heading_id = group.title | slugify | prepend: 'home-' %}
        <section aria-labelledby="{{ heading_id }}">
          <h2 id="{{ heading_id }}" class="home-heading">
            <a href="{{ group.url | relative_url | escape }}">{{ group.title | escape }}</a>
          </h2>
          <ul class="home-entries" role="list">
            {% for item in group.entries %}
              <li class="home-entry">
                <h3><a href="{{ item.url | relative_url | escape }}">{{ item.title | escape }}</a></h3>
                <p>{{ item.description | escape }}</p>
              </li>
            {% endfor %}
          </ul>
        </section>
      {% endfor %}
    </div>
  </div>
</div>

{% if site.posts.size > 0 %}
  <section class="home-blog" aria-labelledby="home-blog">
    <h2 id="home-blog" class="home-heading">Blog</h2>
    <ul class="home-blog-links" role="list">
      {% for post in site.posts limit: 3 %}
        <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
      {% endfor %}
    </ul>
  </section>
{% endif %}
