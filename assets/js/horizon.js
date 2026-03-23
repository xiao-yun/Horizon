(function () {
  'use strict';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  /** Set up EN/中文 language toggle on the index page */
  function setupLanguageToggle() {
    var zhSection = document.getElementById('lang-zh');
    var enSection = document.getElementById('lang-en');
    if (!zhSection || !enSection) return;

    // Create toggle buttons
    var toggle = document.createElement('div');
    toggle.className = 'lang-toggle';

    var btnEn = document.createElement('button');
    btnEn.textContent = 'EN';
    btnEn.type = 'button';

    var btnZh = document.createElement('button');
    btnZh.textContent = '中文';
    btnZh.type = 'button';

    toggle.appendChild(btnEn);
    toggle.appendChild(btnZh);

    // Insert before the first lang section
    zhSection.parentNode.insertBefore(toggle, zhSection);

    function show(lang) {
      if (lang === 'en') {
        enSection.classList.remove('hidden');
        zhSection.classList.add('hidden');
        btnEn.classList.add('active');
        btnZh.classList.remove('active');
      } else {
        zhSection.classList.remove('hidden');
        enSection.classList.add('hidden');
        btnZh.classList.add('active');
        btnEn.classList.remove('active');
      }
      try { localStorage.setItem('horizon-lang', lang); } catch (e) { /* noop */ }
    }

    btnEn.addEventListener('click', function () { show('en'); });
    btnZh.addEventListener('click', function () { show('zh'); });

    // Initial state from localStorage or default to zh
    var saved = null;
    try { saved = localStorage.getItem('horizon-lang'); } catch (e) { /* noop */ }
    show(saved === 'en' ? 'en' : 'zh');
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupLanguageToggle();
  });
})();
