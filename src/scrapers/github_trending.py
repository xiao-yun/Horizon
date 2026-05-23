"""GitHub Trending page scraper.

Scrapes github.com/trending to pick up repositories gaining community attention.
"""

import re
from datetime import datetime, timezone
from typing import List, Optional

import httpx

from ..models import ContentItem, GitHubTrendingConfig, SourceType
from .base import BaseScraper


class GitHubTrendingScraper(BaseScraper):
    """Scraper for GitHub Trending page."""

    BASE_URL = "https://github.com/trending"

    def __init__(self, config: GitHubTrendingConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.cfg: GitHubTrendingConfig = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.enabled:
            return []

        items: List[ContentItem] = []
        seen_ids: set[str] = set()

        languages = self.cfg.languages if self.cfg.languages else [""]

        for lang in languages:
            rows = await self._fetch_language(lang)
            for row in rows:
                item = self._row_to_item(row, lang)
                if item is None:
                    continue
                if item.id in seen_ids:
                    continue
                if self.cfg.min_stars and row.get("stars_today", 0) < self.cfg.min_stars:
                    continue
                seen_ids.add(item.id)
                items.append(item)

        items.sort(key=lambda x: x.metadata.get("stars_today", 0), reverse=True)
        return items[: self.cfg.max_items]

    async def _fetch_language(self, language: str) -> List[dict]:
        """Scrape trending page for a given language and return parsed rows."""
        params = {"since": self.cfg.since}
        if language:
            params["language"] = language
        if self.cfg.spoken_language:
            params["spoken_language_code"] = self.cfg.spoken_language

        try:
            response = await self.client.get(
                self.BASE_URL,
                params=params,
                headers={"Accept": "text/html", "User-Agent": "Horizon/1.0"},
                timeout=20.0,
                follow_redirects=True,
            )
            response.raise_for_status()
        except httpx.HTTPError:
            return []

        return self._parse_html(response.text)

    def _parse_html(self, html: str) -> List[dict]:
        """Extract trending repo info from GitHub trending page HTML."""
        rows = []

        # Each repo is in an <article class="Box-row"> block
        articles = re.split(r'<article\s+class="Box-row"[^>]*>', html)
        for block in articles[1:]:  # skip content before first article
            # Find the closing </article> tag boundary
            end_idx = block.find("</article>")
            if end_idx >= 0:
                block = block[:end_idx]

            # Repo name from h2 > a[href]: owner / repo_name
            h2_match = re.search(r'<h2[^>]*>.*?<a\s+[^>]*href="/([^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL)
            if not h2_match:
                continue

            repo_name = h2_match.group(1).strip()
            # Clean up repo name display text
            title_parts = re.sub(r'<[^>]+>', '', h2_match.group(2)).strip()
            title_parts = title_parts.replace("\n", " ").replace("  ", " ")
            # title_parts looks like "owner / repo_name"
            clean_title = re.sub(r'\s+/\s+', '/', title_parts.strip().strip('/').strip())

            if not repo_name:
                continue

            # Description from <p> tag
            desc_match = re.search(r'<p\s+[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', block, re.DOTALL)
            description = ""
            if desc_match:
                description = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip()

            # Language
            lang_match = re.search(r'itemprop="programmingLanguage"[^>]*>\s*(.*?)\s*</span>', block, re.DOTALL)
            language_name = lang_match.group(1).strip() if lang_match else ""

            # Stars today
            stars_today = 0
            stars_matches = re.findall(r'(\d[\d,]*)\s+stars?\s+today', block, re.IGNORECASE)
            if stars_matches:
                stars_today = int(stars_matches[0].replace(",", ""))

            # Forks today
            forks_today = 0
            forks_matches = re.findall(r'(\d[\d,]*)\s+forks?\s+today', block, re.IGNORECASE)
            if forks_matches:
                forks_today = int(forks_matches[0].replace(",", ""))

            # Total stars (from the "built by" section or star count)
            total_stars = 0
            total_match = re.search(r'(\d[\d,]*)\s+stars?\s+this\s+(week|month|year)', block, re.IGNORECASE)
            if total_match:
                total_stars = int(total_match.group(1).replace(",", ""))

            rows.append({
                "repo_name": repo_name,
                "title": clean_title or repo_name,
                "description": description,
                "language": language_name,
                "stars_today": stars_today,
                "forks_today": forks_today,
                "total_stars": total_stars,
            })

        return rows

    def _row_to_item(self, row: dict, language: str) -> Optional[ContentItem]:
        """Convert a parsed row into a ContentItem."""
        repo_name = row.get("repo_name")
        title = row.get("title") or repo_name
        if not repo_name:
            return None

        stars_today = row.get("stars_today", 0)
        display_title = f"{title} (+{stars_today}⭐ today)"

        content_lines = [
            f"Trending on GitHub: {repo_name}",
            f"Stars gained today: {stars_today}",
            f"Forks today: {row.get('forks_today', 0)}",
            f"Language: {row.get('language') or 'N/A'}",
        ]
        if row.get("description"):
            content_lines.append("")
            content_lines.append(row["description"])

        owner = repo_name.split("/")[0] if "/" in repo_name else None

        return ContentItem(
            id=self._generate_id(SourceType.GITHUB_TRENDING.value, "trending", repo_name),
            source_type=SourceType.GITHUB_TRENDING,
            title=display_title,
            url=f"https://github.com/{repo_name}",
            content="\n".join(content_lines),
            author=owner,
            category=self.cfg.category,
            published_at=datetime.now(timezone.utc),
            metadata={
                "repo": repo_name,
                "stars_today": stars_today,
                "forks_today": row.get("forks_today", 0),
                "total_stars": row.get("total_stars", 0),
                "language": row.get("language", ""),
                "description": row.get("description", ""),
                "since": self.cfg.since,
            },
        )
