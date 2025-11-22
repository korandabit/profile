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

<div class="reading-paths">
    <div class="path-intro">
        <p><strong>New to the blog?</strong> These curated reading paths guide you through related posts in a recommended sequence, building from accessible foundations to more specialized topics.</p>
    </div>

    <div class="path-container">
        <div class="reading-path">
            <h3>🤖 AI Chatbots: From Basics to Applications</h3>
            <div class="path-description">Start with practical applications, then explore underlying concepts.</div>
            <ol class="path-sequence">
                <li class="path-step">
                    <span class="step-marker step-start">Start Here</span>
                    <a href="{% post_url 2025-11-12-bot-therapy %}">From Silence to Bot Therapy</a>
                    <span class="step-meta">5 min • How-to • <span class="badge-inline accessible">Accessible</span></span>
                    <div class="step-why">Practical guide to using chatbots effectively for self-reflection</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">2</span>
                    <a href="{% post_url 2023-10-28-stop-avoiding-yourself-the-ai-in-you %}">Stop Avoiding Yourself: The AI in You</a>
                    <span class="step-meta">5 min • Framework • <span class="badge-inline some-expertise">Some expertise</span></span>
                    <div class="step-why">Understanding AI as a cognitive mirror</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">3</span>
                    <a href="{% post_url 2024-08-30-ai-the-next-technological-leap %}">AI: The Next Technological Leap</a>
                    <span class="step-meta">3 min • Analysis • <span class="badge-inline some-expertise">Some expertise</span></span>
                    <div class="step-why">Broader cognitive implications of AI technology</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">4</span>
                    <a href="{% post_url 2024-09-16-awakening-ai %}">Awakening the AI</a>
                    <span class="step-meta">6 min • Framework • <span class="badge-inline specialized">Specialized</span></span>
                    <div class="step-why">Deep dive into recursive semantic mapping and AI consciousness</div>
                </li>
            </ol>
        </div>

        <div class="reading-path">
            <h3>💬 Communication Frameworks</h3>
            <div class="path-description">Build understanding of how language works in dialog.</div>
            <ol class="path-sequence">
                <li class="path-step">
                    <span class="step-marker step-start">Start Here</span>
                    <a href="{% post_url 2022-04-18-the-agreement-between-reader-and-writer %}">The Agreement Between Reader and Writer</a>
                    <span class="step-meta">2 min • Framework • <span class="badge-inline some-expertise">Some expertise</span></span>
                    <div class="step-why">Foundation: How communication creates implicit contracts</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">2</span>
                    <a href="{% post_url 2022-11-20-2-not-the-point %}">Not the Point</a>
                    <span class="step-meta">2 min • Framework • <span class="badge-inline accessible">Accessible</span></span>
                    <div class="step-why">Core framework for managing tangents in conversation</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">3</span>
                    <a href="{% post_url 2023-08-08-read-receipts-irl %}">Read Receipts IRL</a>
                    <span class="step-meta">3 min • Framework • <span class="badge-inline accessible">Accessible</span></span>
                    <div class="step-why">Practical application to real-world conversations</div>
                </li>
            </ol>
        </div>

        <div class="reading-path">
            <h3>🧠 Cognitive Growth & Self-Improvement</h3>
            <div class="path-description">Evidence-based frameworks for personal development.</div>
            <ol class="path-sequence">
                <li class="path-step">
                    <span class="step-marker step-start">Start Here</span>
                    <a href="{% post_url 2024-07-16-all-the-right-words-youve-said-or-read %}">All the Right Words You've Said or Read</a>
                    <span class="step-meta">3 min • How-to • <span class="badge-inline accessible">Accessible</span></span>
                    <div class="step-why">Simple method for capturing personal insights</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">2</span>
                    <a href="{% post_url 2020-10-26-bet-your-life %}">Bet Your Life</a>
                    <span class="step-meta">5 min • Framework • <span class="badge-inline accessible">Accessible</span></span>
                    <div class="step-why">Framework for testing your beliefs against reality</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">3</span>
                    <a href="{% post_url 2024-06-11-introduction-to-empirical-pragmatism %}">Introduction to Empirical Pragmatism</a>
                    <span class="step-meta">4 min • Framework • <span class="badge-inline specialized">Specialized</span></span>
                    <div class="step-why">Philosophical foundation for evidence-based thinking</div>
                </li>
            </ol>
        </div>

        <div class="reading-path">
            <h3>🤟 Deaf Culture & Language</h3>
            <div class="path-description">Understanding Deaf culture from a CODA perspective.</div>
            <ol class="path-sequence">
                <li class="path-step">
                    <span class="step-marker step-start">Start Here</span>
                    <a href="{% post_url 2013-10-26-the-definition-of-deaf %}">The Definition of Deaf</a>
                    <span class="step-meta">4 min • Advocacy • <span class="badge-inline some-expertise">Cultural context</span></span>
                    <div class="step-why">Foundation: Understanding Deaf vs. deaf terminology</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">2</span>
                    <a href="{% post_url 2014-10-10-language-with-a-bionic-ear %}">Language with a Bionic Ear</a>
                    <span class="step-meta">5 min • Analysis • <span class="badge-inline specialized">Specialized</span></span>
                    <div class="step-why">Intersection of technology, language development, and culture</div>
                </li>
                <li class="path-step">
                    <span class="step-marker">3</span>
                    <a href="{% post_url 2014-10-04-deafhood-unheard %}">Deafhood Unheard</a>
                    <span class="step-meta">Framework • Cultural perspective</span>
                    <div class="step-why">Deep exploration of Deafhood and cultural identity</div>
                </li>
            </ol>
        </div>
    </div>
</div>

<style>
.reading-paths {
    margin: 30px 0 40px 0;
}

.path-intro {
    background: #e3f2fd;
    padding: 20px;
    border-radius: 4px;
    margin-bottom: 30px;
    border-left: 4px solid #2196f3;
}

.path-intro p {
    margin: 0;
    color: #1565c0;
}

.path-container {
    display: grid;
    gap: 25px;
}

.reading-path {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 20px;
}

.reading-path h3 {
    margin-top: 0;
    color: #333;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
}

.path-description {
    color: #666;
    font-style: italic;
    margin-bottom: 15px;
}

.path-sequence {
    list-style: none;
    padding: 0;
    margin: 0;
}

.path-step {
    display: flex;
    flex-direction: column;
    padding: 15px;
    margin: 10px 0;
    background: #fafafa;
    border-radius: 4px;
    border-left: 3px solid #e0e0e0;
    transition: all 0.2s;
}

.path-step:hover {
    background: #f5f5f5;
    border-left-color: #007bff;
}

.step-marker {
    display: inline-block;
    width: 28px;
    height: 28px;
    line-height: 28px;
    text-align: center;
    background: #007bff;
    color: white;
    border-radius: 50%;
    font-weight: bold;
    font-size: 0.85em;
    margin-right: 10px;
    flex-shrink: 0;
}

.step-start {
    background: #28a745;
    width: auto;
    padding: 0 12px;
    border-radius: 14px;
    font-size: 0.75em;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.path-step a {
    font-weight: 600;
    font-size: 1.05em;
    margin: 5px 0;
}

.step-meta {
    font-size: 0.8em;
    color: #666;
    margin: 5px 0;
}

.step-why {
    font-size: 0.85em;
    color: #777;
    margin-top: 8px;
    padding-left: 38px;
}

.badge-inline {
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.85em;
    font-weight: 600;
    text-transform: uppercase;
}

.badge-inline.accessible {
    background: #d4edda;
    color: #155724;
}

.badge-inline.some-expertise {
    background: #fff3cd;
    color: #856404;
}

.badge-inline.specialized {
    background: #f8d7da;
    color: #721c24;
}

@media (max-width: 768px) {
    .step-why {
        padding-left: 0;
    }
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

## All Blog Posts

<div class="filters">
    <div class="filter-group">
        <label for="accessibility-filter">🎯 Accessibility:</label>
        <select id="accessibility-filter" onchange="filterPosts()">
            <option value="all">All Posts</option>
            <option value="accessible">Accessible to All</option>
            <option value="some-expertise">Some Expertise Helpful</option>
            <option value="specialized">Specialized Knowledge</option>
        </select>
    </div>

    <div class="filter-group">
        <label for="structure-filter">📝 Type:</label>
        <select id="structure-filter" onchange="filterPosts()">
            <option value="all">All Types</option>
            <option value="framework">Framework</option>
            <option value="how-to">How-to</option>
            <option value="narrative">Narrative</option>
            <option value="analysis">Analysis</option>
            <option value="advocacy">Advocacy</option>
        </select>
    </div>

    <div class="filter-group">
        <label for="length-filter">📖 Length:</label>
        <select id="length-filter" onchange="filterPosts()">
            <option value="all">All Lengths</option>
            <option value="short">Short (&lt;500 words)</option>
            <option value="medium">Medium (500-1000)</option>
            <option value="long">Long (&gt;1000 words)</option>
        </select>
    </div>

    <button onclick="resetFilters()" class="reset-btn">Reset Filters</button>
</div>

<div id="post-count" style="margin: 15px 0; color: #666; font-size: 0.9em;"></div>

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

        <div class="post-meta-enhanced">
            <span class="post-meta">{{ post.date | date: "%B %d, %Y" }}</span>

            {% if word_count > 0 %}
            <span class="meta-badge">📖 {{ word_count | divided_by: 200 | plus: 1 }} min</span>
            {% endif %}

            {% if structure %}
            <span class="meta-badge type-badge">{{ structure | capitalize }}</span>
            {% endif %}

            {% if domain_barrier == "none" or domain_barrier == "low" %}
            <span class="meta-badge access-badge access-easy">Accessible</span>
            {% elsif domain_barrier == "medium" %}
            <span class="meta-badge access-badge access-medium">Some expertise</span>
            {% elsif domain_barrier == "high" %}
            <span class="meta-badge access-badge access-hard">Specialized</span>
            {% endif %}
        </div>

        {% if post.excerpt %}
        <div class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 25 }}</div>
        {% endif %}
    </li>
{% endfor %}
</ul>

<style>
.filters {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 4px;
    margin: 20px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    align-items: flex-end;
}

.filter-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.filter-group label {
    font-size: 0.85em;
    font-weight: 600;
    color: #555;
}

.filter-group select {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    background: white;
    font-size: 0.9em;
    cursor: pointer;
}

.reset-btn {
    padding: 8px 16px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
    font-weight: 600;
}

.reset-btn:hover {
    background: #0056b3;
}

.post-item {
    margin-bottom: 25px;
    padding-bottom: 20px;
    border-bottom: 1px solid #eee;
}

.post-item:last-child {
    border-bottom: none;
}

.post-meta-enhanced {
    margin: 8px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}

.meta-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 0.75em;
    font-weight: 600;
}

.type-badge {
    background: #d1ecf1;
    color: #0c5460;
}

.access-badge {
    text-transform: uppercase;
    font-size: 0.7em;
}

.access-easy {
    background: #d4edda;
    color: #155724;
}

.access-medium {
    background: #fff3cd;
    color: #856404;
}

.access-hard {
    background: #f8d7da;
    color: #721c24;
}

.post-excerpt {
    margin-top: 8px;
    color: #666;
    font-size: 0.9em;
    line-height: 1.5;
}

.post-item.hidden {
    display: none;
}

@media (max-width: 768px) {
    .filters {
        flex-direction: column;
        align-items: stretch;
    }

    .filter-group {
        width: 100%;
    }

    .reset-btn {
        width: 100%;
    }
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
