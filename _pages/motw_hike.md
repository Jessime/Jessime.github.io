---
title: "Micro RPG"
permalink: /motw_hike/
layout: single
author_profile: false
---

<section class="motw-hike-app" aria-labelledby="motw-hike-title">
  <div class="motw-hike-shell">
    <header class="motw-hike-header">
      <p class="motw-hike-kicker">Offline hiking helper</p>
      <h1 id="motw-hike-title">Micro RPG</h1>
      <p class="motw-hike-intro">
        Quick player rolls for when you want the story to keep moving and your
        phone to stay mostly in your pocket.
      </p>
    </header>

    <main class="motw-hike-tools">
      <button class="motw-add-player" type="button" id="motw-add-player">Add Player</button>
      <div class="motw-player-list" id="motw-player-list" aria-live="polite"></div>
    </main>
  </div>
</section>

<style>
  .motw-hike-app {
    --motw-bg: #f7f1e6;
    --motw-panel: #fffaf0;
    --motw-ink: #1f261f;
    --motw-muted: #65705f;
    --motw-border: #d7cab5;
    --motw-accent: #263d2b;

    min-height: 82vh;
    margin: 0 calc(50% - 50vw);
    padding: max(1.25rem, env(safe-area-inset-top)) max(1rem, env(safe-area-inset-right)) max(2rem, env(safe-area-inset-bottom)) max(1rem, env(safe-area-inset-left));
    color: var(--motw-ink);
    background: var(--motw-bg);
  }

  .motw-hike-shell {
    width: min(100%, 42rem);
    margin: 0 auto;
  }

  .motw-hike-header {
    padding: 1rem 0 1.25rem;
  }

  .motw-hike-kicker {
    margin: 0 0 0.35rem;
    color: var(--motw-muted);
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .motw-hike-header h1 {
    margin: 0;
    color: var(--motw-ink);
    font-size: clamp(2.6rem, 16vw, 5.2rem);
    line-height: 0.95;
    letter-spacing: -0.06em;
  }

  .motw-hike-intro {
    max-width: 34rem;
    margin: 1rem 0 0;
    color: var(--motw-muted);
    font-size: clamp(1rem, 4vw, 1.25rem);
    line-height: 1.45;
  }

  .motw-tool-card {
    overflow: hidden;
    border: 1px solid var(--motw-border);
    border-radius: 1.25rem;
    background: var(--motw-panel);
    box-shadow: 0 0.8rem 2rem rgba(31, 38, 31, 0.08);
  }

  .motw-add-player,
  .motw-roll-button {
    width: 100%;
    border: 0;
    color: #fffaf0;
    background: var(--motw-accent);
    font-weight: 900;
    text-transform: uppercase;
    touch-action: manipulation;
    cursor: pointer;
  }

  .motw-add-player {
    min-height: 4.25rem;
    border-radius: 999rem;
    padding: 1rem 1.25rem;
    font-size: 1.1rem;
    letter-spacing: 0.04em;
  }

  .motw-add-player:active,
  .motw-roll-button:active {
    transform: translateY(2px);
    filter: brightness(1.12);
  }

  .motw-add-player:focus-visible,
  .motw-roll-button:focus-visible,
  .motw-stat-button:focus-visible,
  .motw-name-input:focus-visible {
    outline: 0.25rem solid #b46f3b;
    outline-offset: 0.15rem;
  }

  .motw-player-list {
    display: grid;
    gap: 1rem;
    margin-top: 1rem;
  }

  .motw-empty-state {
    margin: 0;
    border: 1px dashed var(--motw-border);
    border-radius: 1.25rem;
    padding: clamp(1.1rem, 5vw, 1.8rem);
    color: var(--motw-muted);
    background: rgba(255, 250, 240, 0.5);
    font-size: 1.05rem;
    text-align: center;
  }

  .motw-player-card {
    border: 1px solid var(--motw-border);
    border-radius: 1.25rem;
    padding: clamp(1rem, 4vw, 1.35rem);
    background: var(--motw-panel);
    box-shadow: 0 0.8rem 2rem rgba(31, 38, 31, 0.08);
  }

  .motw-player-header {
    display: grid;
    gap: 0.7rem;
  }

  .motw-name-label,
  .motw-total {
    color: var(--motw-muted);
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .motw-name-input {
    width: 100%;
    border: 1px solid var(--motw-border);
    border-radius: 0.8rem;
    padding: 0.8rem 0.9rem;
    color: var(--motw-ink);
    background: #fffef9;
    font: inherit;
    font-size: 1.1rem;
  }

  .motw-total {
    margin: 0;
  }

  .motw-total.is-invalid {
    color: #9a3f2d;
  }

  .motw-stat-list {
    display: grid;
    gap: 0.55rem;
    margin: 1rem 0;
  }

  .motw-stat-row {
    display: grid;
    grid-template-columns: minmax(5rem, 1fr) auto auto auto;
    align-items: center;
    gap: 0.55rem;
    border: 1px solid var(--motw-border);
    border-radius: 0.9rem;
    padding: 0.55rem;
    background: #fffef9;
  }

  .motw-stat-name {
    font-size: 1rem;
    font-weight: 850;
    text-transform: capitalize;
  }

  .motw-stat-button {
    width: 2.65rem;
    height: 2.65rem;
    border: 1px solid var(--motw-border);
    border-radius: 999rem;
    color: var(--motw-ink);
    background: var(--motw-bg);
    font-size: 1.35rem;
    font-weight: 900;
    line-height: 1;
    touch-action: manipulation;
  }

  .motw-stat-button:disabled,
  .motw-roll-button:disabled {
    cursor: not-allowed;
    opacity: 0.45;
  }

  .motw-stat-value {
    min-width: 2.2rem;
    font-size: 1.25rem;
    font-weight: 900;
    text-align: center;
  }

  .motw-roll-button {
    min-height: 5.25rem;
    border-radius: 1rem;
    padding: 1.15rem;
    font-size: clamp(1.35rem, 6vw, 2rem);
    letter-spacing: -0.02em;
  }

  .motw-roll-results {
    display: grid;
    gap: 0.5rem;
    margin-top: 1rem;
  }

  .motw-roll-result {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 0.75rem;
    align-items: center;
    border-bottom: 1px solid var(--motw-border);
    padding-bottom: 0.5rem;
  }

  .motw-roll-result:last-child {
    border-bottom: 0;
    padding-bottom: 0;
  }

  .motw-roll-label {
    color: var(--motw-muted);
    font-size: 0.9rem;
    font-weight: 850;
    text-transform: capitalize;
  }

  .motw-roll-number {
    color: var(--motw-ink);
    font-size: 2rem;
    font-weight: 950;
    line-height: 1;
  }

  .motw-roll-outcome {
    grid-column: 1 / -1;
    color: var(--motw-ink);
    font-size: 0.95rem;
  }

  @media (min-width: 48rem) {
    .motw-hike-app {
      padding-top: 3rem;
      padding-bottom: 4rem;
    }

    .motw-player-card {
      border-radius: 1.5rem;
    }

    .motw-player-header {
      grid-template-columns: 1fr auto;
      align-items: end;
    }
  }
</style>

<script>
  (function () {
    "use strict";

    const attributes = ["charm", "cool", "sharp", "tough", "weird"];
    const defaultStats = {
      charm: 0,
      cool: 1,
      sharp: 1,
      tough: 0,
      weird: 0
    };
    const players = [];
    const outcomes = [
      {
        min: 0,
        max: 6,
        outcome: "Miss",
        prompt: "The Keeper makes a move."
      },
      {
        min: 7,
        max: 9,
        outcome: "Mixed Success",
        prompt: "You do it, but there is a cost, choice, or complication."
      },
      {
        min: 10,
        max: 15,
        outcome: "Success",
        prompt: "You get what you wanted."
      }
    ];

    function rollD6() {
      return Math.floor(Math.random() * 6) + 1;
    }

    function classifyMove(total) {
      return outcomes.find(function (outcome) {
        return total >= outcome.min && total <= outcome.max;
      });
    }

    function statTotal(player) {
      return attributes.reduce(function (total, attribute) {
        return total + player.stats[attribute];
      }, 0);
    }

    function formatStat(value) {
      return value > 0 ? "+" + value : String(value);
    }

    function rollForAttribute(stat) {
      return rollD6() + rollD6() + stat;
    }

    function rollPlayer(player) {
      player.results = attributes.map(function (attribute) {
        const total = rollForAttribute(player.stats[attribute]);
        const outcome = classifyMove(total);

        return {
          attribute: attribute,
          total: total,
          outcome: outcome.outcome,
          prompt: outcome.prompt
        };
      });
    }

    function escapeHtml(value) {
      return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }

    function findPlayer(id) {
      return players.find(function (player) {
        return player.id === id;
      });
    }

    function canIncrease(player, attribute) {
      return player.stats[attribute] < 3 && statTotal(player) < 2;
    }

    function canDecrease(player, attribute) {
      return player.stats[attribute] > -2;
    }

    function renderStats(player) {
      return attributes.map(function (attribute) {
        return [
          '<div class="motw-stat-row">',
          '  <span class="motw-stat-name">' + attribute + '</span>',
          '  <button class="motw-stat-button" type="button" data-action="decrease" data-player-id="' + player.id + '" data-attribute="' + attribute + '"' + (canDecrease(player, attribute) ? "" : " disabled") + ' aria-label="Decrease ' + attribute + '">-</button>',
          '  <span class="motw-stat-value">' + formatStat(player.stats[attribute]) + '</span>',
          '  <button class="motw-stat-button" type="button" data-action="increase" data-player-id="' + player.id + '" data-attribute="' + attribute + '"' + (canIncrease(player, attribute) ? "" : " disabled") + ' aria-label="Increase ' + attribute + '">+</button>',
          "</div>"
        ].join("");
      }).join("");
    }

    function renderResults(player) {
      if (!player.results.length) {
        return "";
      }

      return [
        '<div class="motw-roll-results" aria-label="Roll results for ' + escapeHtml(player.name) + '">',
        player.results.map(function (result) {
          return [
            '<div class="motw-roll-result">',
            '  <span class="motw-roll-label">' + result.attribute + '</span>',
            '  <span class="motw-roll-number">' + result.total + '</span>',
            '  <span class="motw-roll-outcome">' + result.outcome + ": " + result.prompt + '</span>',
            "</div>"
          ].join("");
        }).join(""),
        "</div>"
      ].join("");
    }

    function renderPlayer(player) {
      const total = statTotal(player);
      const isValid = total === 2;

      return [
        '<article class="motw-player-card" data-player-card="' + player.id + '">',
        '  <div class="motw-player-header">',
        '    <label>',
        '      <span class="motw-name-label">Player name</span>',
        '      <input class="motw-name-input" type="text" value="' + escapeHtml(player.name) + '" data-action="rename" data-player-id="' + player.id + '" autocomplete="off">',
        "    </label>",
        '    <p class="motw-total' + (isValid ? "" : " is-invalid") + '">Stats total: ' + formatStat(total) + ' / +2</p>',
        "  </div>",
        '  <div class="motw-stat-list">',
        renderStats(player),
        "  </div>",
        '  <button class="motw-roll-button" type="button" data-action="roll" data-player-id="' + player.id + '"' + (isValid ? "" : " disabled") + ">Roll Dice</button>",
        renderResults(player),
        "</article>"
      ].join("");
    }

    function renderPlayers() {
      const root = document.getElementById("motw-player-list");

      if (!players.length) {
        root.innerHTML = '<p class="motw-empty-state">Add a player to start rolling.</p>';
        return;
      }

      root.innerHTML = players.map(renderPlayer).join("");
    }

    function addPlayer() {
      players.push({
        id: "player-" + Date.now() + "-" + players.length,
        name: "Player " + (players.length + 1),
        stats: Object.assign({}, defaultStats),
        results: []
      });
      renderPlayers();
    }

    function handlePlayerAction(event) {
      const target = event.target;
      const action = target.getAttribute("data-action");
      const playerId = target.getAttribute("data-player-id");

      if (!action || !playerId) {
        return;
      }

      const player = findPlayer(playerId);

      if (!player) {
        return;
      }

      if (action === "rename") {
        player.name = target.value || "Player";
        return;
      }

      if (action === "increase" && canIncrease(player, target.getAttribute("data-attribute"))) {
        player.stats[target.getAttribute("data-attribute")] += 1;
        player.results = [];
      }

      if (action === "decrease" && canDecrease(player, target.getAttribute("data-attribute"))) {
        player.stats[target.getAttribute("data-attribute")] -= 1;
        player.results = [];
      }

      if (action === "roll" && statTotal(player) === 2) {
        rollPlayer(player);
      }

      renderPlayers();
    }

    function initialize() {
      document.getElementById("motw-add-player").addEventListener("click", addPlayer);
      document.getElementById("motw-player-list").addEventListener("click", handlePlayerAction);
      document.getElementById("motw-player-list").addEventListener("input", handlePlayerAction);

      renderPlayers();
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", initialize);
    } else {
      initialize();
    }
  })();
</script>
