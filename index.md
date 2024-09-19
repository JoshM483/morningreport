---
layout: page
title: Morning Report
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5/dist/slate/bootstrap.min.css">

<!-- Banner -->
<div class="container">
  <div class="jumbotron text-center bg-primary text-white">
    <h1>Your Morning Report</h1>
  </div>
</div>

<!-- Main Content -->
<div class="container">
  {% for article in articles %}
    <div class="card mb-3">
      <!-- Article Title -->
      <h3 class="card-header">{{ article.title | default: 'No title available' }}</h3>

      <!-- Source -->
      <div class="card-body">
        <h5 class="card-title text-muted">{{ article.source | default: 'Unknown Source' }}</h5>
      </div>

      <!-- Optional Article Image -->
      {% if article.image_url %}
        <img src="{{ article.image_url }}" class="card-img-top" alt="Article Image">
      {% endif %}

      <!-- Summary Text -->
      <div class="card-body">
        <p class="card-text">{{ article.summary | default: 'No summary available.' }}</p>
      </div>

      <!-- Link to the Full Article -->
      <div class="card-body">
        {% if article.url %}
          <a href="{{ article.url }}" class="card-link" target="_blank">Read Full Article</a>
        {% else %}
          <span class="text-muted">No link available.</span>
        {% endif %}
      </div>

      <!-- Publication Date -->
      <div class="card-footer text-muted">
        {{ article.published_date | default: 'Publication date unknown' }}
      </div>
    </div>
  {% endfor %}
</div>



<!-- Footer -->
<footer class="footer mt-5 py-3 bg-dark">
  <div class="container text-center">
    <span class="text-muted">
      <a href="https://github.com/joshm483/morningreport" target="_blank">View on GitHub</a>
    </span>
  </div>
</footer>
