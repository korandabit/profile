---
layout: default
title: Blog
permalink: /blog/
---

<style>
/* Completely override layout for blog page - disable floating sidebar */
.wrapper {
    width: auto !important;
    max-width: 960px;
    margin: 0 auto;
}

header {
    position: static !important;
    float: none !important;
    width: auto !important;
    padding: 20px 0;
    text-align: center;
    border-bottom: 1px solid #e5e5e5;
    margin-bottom: 30px;
}

section {
    width: auto !important;
    float: none !important;
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
}

footer {
    display: none !important;
}

/* Override all media queries for this page */
@media print, screen and (max-width: 960px) {
    .wrapper {
        width: auto;
        margin: 0;
    }
    
    header {
        padding: 20px !important;
        padding-right: 20px !important;
    }
    
    section {
        border: none !important;
        padding: 0 20px !important;
        margin: 0 !important;
    }
}

.theme-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.theme-box {
    width: 48%;
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    box-sizing: border-box;
}
@media (max-width: 768px) {
    .theme-box {
        width: 100%;
    }
}
.post-list {
    list-style-type: none;
    padding: 0;
}
.post-list li {
    margin-bottom: 10px;
}
.post-meta {
    font-size: 0.8em;
    color: #666;
}
</style>

# My Blog

Welcome to my blog, where I explore various ideas and topics. Below you'll find curated reading lists on key themes, followed by a chronological list of all my posts.

## Reading Paths

<div class="paths">
    <div class="path">
        <h3>AI Chatbots</h3>
        <ol>
            <li><a href="{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}">Stop Avoiding Yourself</a> <span class="meta">5min, framework</span></li>
            <li><a href="{% post_url 2025-11-12-bot-therapy %}">Bot Therapy</a> <span class="meta">5min, how-to</span></li>
            <li><a href="{% post_url 2024-08-30-ai-the-next-technological-leap %}">Next Technological Leap</a> <span class="meta">3min</span></li>
            <li><a href="{% post_url 2024-09-16-awakening-ai %}">Awakening AI</a> <span class="meta">6min, technical</span></li>
        </ol>
    </div>

    <div class="path">
        <h3>Communication</h3>
        <ol>
            <li><a href="{% post_url 2022-04-18-the-agreement-between-reader-and-writer %}">Reader and Writer</a> <span class="meta">2min</span></li>
            <li><a href="{% post_url 2022-11-20-2-not-the-point %}">Not the Point</a> <span class="meta">2min</span></li>
            <li><a href="{% post_url 2023-08-08-read-receipts-irl %}">Read Receipts IRL</a> <span class="meta">3min</span></li>
        </ol>
    </div>

    <div class="path">
        <h3>Cognitive Growth</h3>
        <ol>
            <li><a href="{% post_url 2024-07-16-all-the-right-words-youve-said-or-read %}">All the Right Words</a> <span class="meta">3min</span></li>
            <li><a href="{% post_url 2020-10-26-bet-your-life %}">Bet Your Life</a> <span class="meta">5min</span></li>
            <li><a href="{% post_url 2024-06-11-introduction-to-empirical-pragmatism %}">Empirical Pragmatism</a> <span class="meta">4min, technical</span></li>
        </ol>
    </div>

    <div class="path">
        <h3>Deaf Culture</h3>
        <ol>
            <li><a href="{% post_url 2013-10-26-the-definition-of-deaf %}">Definition of Deaf</a> <span class="meta">4min</span></li>
            <li><a href="{% post_url 2014-10-10-language-with-a-bionic-ear %}">Bionic Ear</a> <span class="meta">5min, technical</span></li>
            <li><a href="{% post_url 2014-10-04-deafhood-unheard %}">Deafhood Unheard</a></li>
        </ol>
    </div>
</div>

<style>
.paths {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin: 20px 0 30px 0;
    font-size: 0.9em;
}
.path h3 {
    margin: 0 0 8px 0;
    font-size: 1em;
    font-weight: 600;
}
.path ol {
    margin: 0;
    padding-left: 18px;
    list-style: decimal;
}
.path li {
    margin: 4px 0;
    line-height: 1.4;
}
.path .meta {
    color: #666;
    font-size: 0.85em;
}
</style>

## Featured Themes

<div class="theme-container">
    <div class="theme-box">
        <h3>Discovering AI Chatbots</h3>
        <p>For millions who've never had anyone to talk to, chatbots aren't replacing therapy—they're creating conversation where silence existed.</p>
        <ul>
            <li><a href="{% post_url 2025-11-12-bot-therapy %}">From Silence to Bot Therapy</a></li>
            <li><a href="{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}">Stop avoiding yourself: the AI in you</a></li>
            <li><a href="{% post_url 2024-09-16-awakening-ai %}">Awakening the AI</a></li>
            <li><a href="{% post_url 2024-09-17-ai-zombie %}">AI Zombie</a></li>
            <li><a href="{% post_url 2024-08-30-ai-the-next-technological-leap %}">AI: The Next Technological Leap</a></li>
            <li><a href="{% post_url 2024-07-13-right-click-for-ai %}">Right-click for AI</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Communication</h3>
        <p>Dialog is two people saying words. The Point of dialog is an agreed-upon shared result. That said, many dialogs lose the Point because of Tangents.</p>
        <ul>
            <li><a href="{% post_url 2022-11-20-2-not-the-point %}">Not the Point</a></li>
            <li><a href="{% post_url 2023-08-08-read-receipts-irl %}">Read Receipts IRL</a></li>
            <li><a href="{% post_url 2022-04-18-the-agreement-between-reader-and-writer %}">Reader and Writer</a></li>
            <li><a href="{% post_url 2024-07-13-say-less-and-more %}">Say less and more</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Language Science</h3>
        <p>Bridging academic research and practical insights on how language shapes thought and reality.</p>
        <ul>
            <li><a href="{% post_url 2024-06-11-introduction-to-empirical-pragmatism %}">Introduction to Empirical Pragmatism</a></li>
            <li><a href="{% post_url 2024-06-06-words-youve-never-heard %}">Words you've never heard</a></li>
            <li><a href="{% post_url 2024-07-16-all-the-right-words-youve-said-or-read %}">All the right words you've said or read</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Cognitive Growth</h3>
        <p>Self-help for people who are obsessed with analytical lifehacking.</p>
        <ul>
            <li><a href="{% post_url 2020-10-26-bet-your-life %}">Bet your life</a></li>
            <li><a href="{% post_url 2023-11-14-know-thaiself %}">Know Thaiself</a></li>
            <li><a href="{% post_url 2024-07-20-questions-books %}">Questions Books</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Deaf Culture</h3>
        <p>Exploring the unique perspective of growing up as a child of Deaf adults (CODA) in two worlds.</p>
        <ul>
            <li><a href="{% post_url 2014-10-04-deafhood-unheard %}">Deafhood Unheard</a></li>
            <li><a href="{% post_url 2013-10-26-the-definition-of-deaf %}">The Definition of Deaf</a></li>
            <li><a href="{% post_url 2014-10-10-language-with-a-bionic-ear %}">Language with a Bionic Ear</a></li>
            <li><a href="{% post_url 2015-02-23-irrationally-speaking %}">Irrationally Speaking</a></li>
        </ul>
    </div>
    <div class="theme-box">
        <h3>Military</h3>
        <p>Exploring the psychology and existence of someone who participated in war and tried to come back home.</p>
        <p><strong>Retrospective</strong></p>
        <ul>
            <li><a href="{% post_url 2017-04-08-the-unedited-war-story-of-a-veteran %}">The Unedited War Story of a Veteran</a></li>
            <li><a href="{% post_url 2017-07-28-the-intellectual-boot-camp %}">The Intellectual Boot Camp</a></li>
        </ul>
        <p><strong>Afghanistan 2013: Real-Time Deployment</strong></p>
        <ul>
            <li><a href="{% post_url 2013-04-17-preface-one-of-those-guys %}">Preface: One of Those Guys</a></li>
            <li><a href="{% post_url 2013-04-17-1-it-rained %}">1. It Rained</a></li>
            <li><a href="{% post_url 2013-04-18-5-webcam-starts-to-capture %}">5. Webcam Starts to Capture</a></li>
            <li><a href="{% post_url 2013-04-20-7-a-christmas-special %}">7. A Christmas Special</a></li>
            <li><a href="{% post_url 2013-04-23-9-emotional-warfare %}">9. Emotional Warfare</a></li>
            <li><a href="{% post_url 2013-04-25-10-a-fog-of-war %}">10. A Fog of War</a></li>
            <li><a href="{% post_url 2013-04-27-12-grenades-cigarettes-or-melons %}">12. Grenades, Cigarettes, or Melons</a></li>
            <li><a href="{% post_url 2013-05-12-14-everyday %}">14. Everyday</a></li>
            <li><a href="{% post_url 2013-05-16-15-lead-me-home %}">15. Lead Me Home</a></li>
            <li><a href="{% post_url 2013-05-02-a-need-for-combat %}">A Need for Combat</a></li>
        </ul>
    </div>
</div>

<details>
<summary>A letter series: Dear_</summary>
<p>Three letters, one structure, different senders. Human to love. Human to AI. AI to human. The same words mean something different depending on who speaks them.</p>
<ul>
  <li><a href="{% post_url 2023-08-01-dear-love %}">Dear Love,</a> — signed: You</li>
  <li><a href="{% post_url 2023-10-20-dear-a-i %}">Dear A.I.,</a> — signed: Human</li>
  <li><a href="{% post_url 2023-10-20-dear-human %}">Dear Human,</a> — signed: ChatGPT</li>
</ul>
</details>

<style>
details { margin: 10px 0 30px 0; font-size: 0.95em; }
details summary { cursor: pointer; color: #666; font-size: 0.9em; }
details summary:hover { color: #333; }
details ul { margin-top: 10px; }
</style>

## All Blog Posts

<div class="filters">
    <select id="accessibility-filter" onchange="filterPosts()">
        <option value="all">All</option>
        <option value="accessible">Accessible</option>
        <option value="some-expertise">Some expertise</option>
        <option value="specialized">Specialized</option>
    </select>

    <select id="structure-filter" onchange="filterPosts()">
        <option value="all">All types</option>
        <option value="framework">Framework</option>
        <option value="how-to">How-to</option>
        <option value="narrative">Narrative</option>
        <option value="analysis">Analysis</option>
        <option value="advocacy">Advocacy</option>
    </select>

    <select id="length-filter" onchange="filterPosts()">
        <option value="all">All lengths</option>
        <option value="short">&lt;500w</option>
        <option value="medium">500-1000w</option>
        <option value="long">&gt;1000w</option>
    </select>

    <button onclick="resetFilters()">Reset</button>
    <span id="post-count"></span>
</div>

<ul class="post-list" id="post-list">
{% for post in site.posts %}
    {% assign post_data = site.data.post_analysis[post.slug] %}
    {% assign domain_barrier = post.analysis.barriers.domain | default: post_data.accessibility.domain_barrier %}
    {% assign structure = post.analysis.structure | default: post_data.structure_type %}
    {% assign word_count = post_data.word_count | default: 0 %}

    <li class="post-item"
        data-accessibility="{{ domain_barrier }}"
        data-structure="{{ structure }}"
        data-wordcount="{{ word_count }}">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="meta">
            {{ post.date | date: "%b %Y" }}
            {% if word_count > 0 %} • {{ word_count | divided_by: 200 | plus: 1 }}min{% endif %}
            {% if structure %} • {{ structure }}{% endif %}
            {% if domain_barrier == "high" %} • technical{% endif %}
        </span>
    </li>
{% endfor %}
</ul>

<style>
.filters {
    margin: 15px 0;
    font-size: 0.9em;
}
.filters select, .filters button {
    margin-right: 10px;
    padding: 4px 8px;
    font-size: 0.9em;
}
#post-count {
    color: #666;
    margin-left: 10px;
}
.post-item {
    margin: 8px 0;
}
.post-item .meta {
    color: #666;
    font-size: 0.85em;
    margin-left: 8px;
}
.post-item.hidden {
    display: none;
}
</style>

<script>
function filterPosts() {
    const accessFilter = document.getElementById('accessibility-filter').value;
    const structureFilter = document.getElementById('structure-filter').value;
    const lengthFilter = document.getElementById('length-filter').value;

    const posts = document.querySelectorAll('.post-item');
    let visibleCount = 0;

    posts.forEach(post => {
        const accessibility = post.dataset.accessibility;
        const structure = post.dataset.structure;
        const wordCount = parseInt(post.dataset.wordcount);

        let show = true;

        // Accessibility filter
        if (accessFilter !== 'all') {
            if (accessFilter === 'accessible' && accessibility !== 'none' && accessibility !== 'low') {
                show = false;
            } else if (accessFilter === 'some-expertise' && accessibility !== 'medium') {
                show = false;
            } else if (accessFilter === 'specialized' && accessibility !== 'high') {
                show = false;
            }
        }

        // Structure filter
        if (structureFilter !== 'all' && structure !== structureFilter) {
            show = false;
        }

        // Length filter
        if (lengthFilter !== 'all') {
            if (lengthFilter === 'short' && wordCount >= 500) {
                show = false;
            } else if (lengthFilter === 'medium' && (wordCount < 500 || wordCount > 1000)) {
                show = false;
            } else if (lengthFilter === 'long' && wordCount <= 1000) {
                show = false;
            }
        }

        if (show) {
            post.classList.remove('hidden');
            visibleCount++;
        } else {
            post.classList.add('hidden');
        }
    });

    updatePostCount(visibleCount, posts.length);
}

function resetFilters() {
    document.getElementById('accessibility-filter').value = 'all';
    document.getElementById('structure-filter').value = 'all';
    document.getElementById('length-filter').value = 'all';
    filterPosts();
}

function updatePostCount(visible, total) {
    const countEl = document.getElementById('post-count');
    if (visible === total) {
        countEl.textContent = `Showing all ${total} posts`;
    } else {
        countEl.textContent = `Showing ${visible} of ${total} posts`;
    }
}

// Initialize count on page load
document.addEventListener('DOMContentLoaded', function() {
    const posts = document.querySelectorAll('.post-item');
    updatePostCount(posts.length, posts.length);
});
</script>
