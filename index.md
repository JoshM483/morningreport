---
layout: page
title: 
---
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5/dist/slate/bootstrap.min.css">




<!-- Banner -->
<div class="text-center bg-primary text-white py-4 mb-5">
  <h1 class="display-4">{{ site.time | date: "%A" }}'s Morning Report</h1>
</div>

<!-- Main Content -->
<div class="container">
  {% for article in site.data.articles %}
    <div class="card mb-5">
      <!-- Optional Article Image -->
      {% if article.image %}
        <img src="{{ article.image }}" class="card-img-top" alt="Article Image">
      {% endif %}

      <!-- Article Title -->
      <div class="card-header">
        <h3 class="card-title">{{ article.title | default: 'Unable to get title' }}</h3>
      </div>

      <!-- Card Body -->
      <div class="card-body">
        <!-- Source -->
          <h6 class="card-subtitle mb-2">{{ article.source | default: 'Unable to get Source' }}</h6>

        <!-- Summary Text -->
          <p class="card-text">{{ article.summary | markdownify | default: 'No summary available.' }}</p>

        <!-- Link to the Full Article -->
          {% if article.url %}
            <a href="{{ article.url }}" class="card-link" target="_blank">Read Full Article Here</a>
          {% else %}
            <span class="text-muted">Source URL missing.</span>
          {% endif %}
      </div>

      <!-- Publication Date -->
      <div class="card-footer text-muted">
        {{ article.date | default: 'Unable to get publication date' }}
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
