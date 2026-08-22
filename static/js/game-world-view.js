/**
 * Отрисовка клетчатого поля и проигрывание лога шагов робота.
 */
const GameWorldView = {
  cell: 30,
  gap: 3,
  timer: null,
  playing: false,
  index: 0,
  steps: [],

  init() {
    this.root = document.getElementById("gameWorld");
    this.wrap = document.getElementById("gameWorldWrap");
    this.stage = document.getElementById("gameStage");
    this.celebrateEl = document.getElementById("gameCelebrate");
    this.celebrateBurst = this.celebrateEl
      ? this.celebrateEl.querySelector(".game-celebrate__burst")
      : null;
    this.celebrateTitle = document.getElementById("gameCelebrateTitle");
    this.celebrateSub = document.getElementById("gameCelebrateSub");
    this.messageEl = document.getElementById("gameMessage");
    this.winTimer = null;
    this.audioCtx = null;
    if (this.celebrateEl) {
      this.celebrateEl.addEventListener("click", () => this.clearCelebrate());
    }
  },

  cloneWorld(world) {
    return JSON.parse(JSON.stringify(world || {}));
  },

  asSet(points) {
    const set = {};
    (points || []).forEach(function (p) {
      set[p[0] + "," + p[1]] = true;
    });
    return set;
  },

  key(x, y) {
    return x + "," + y;
  },

  render(world) {
    this.stop();
    this.clearCelebrate();
    this.initial = this.cloneWorld(world);
    this.world = this.cloneWorld(world);
    this.draw();
  },

  reset() {
    this.stop();
    this.clearCelebrate();
    if (this.initial) this.world = this.cloneWorld(this.initial);
    this.draw();
    this.setMessage("");
  },

  setMessage(text, isError) {
    if (!this.messageEl) return;
    this.messageEl.textContent = text || "";
    this.messageEl.classList.toggle("is-error", !!isError);
  },

  stop() {
    this.playing = false;
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = null;
    }
  },

  play(steps, speedMs) {
    const self = this;
    this.stop();
    if (this.initial) this.world = this.cloneWorld(this.initial);
    this.draw();
    this.steps = steps || [];
    this.index = 0;
    this.playing = true;
    const delay = Math.max(40, Number(speedMs) || 320);

    return new Promise(function (resolve) {
      function tick() {
        if (!self.playing) {
          resolve({ stopped: true });
          return;
        }
        if (self.index >= self.steps.length) {
          self.playing = false;
          resolve({ stopped: false });
          return;
        }
        self.applyStep(self.steps[self.index]);
        self.index += 1;
        self.timer = setTimeout(tick, delay);
      }
      tick();
    });
  },

  applyStep(step) {
    if (!step || !this.world) return;
    const w = this.world;
    if (typeof step.x === "number") w.start = [step.x, step.y];
    if (step.facing) w.facing = step.facing;
    if (typeof step.carrying === "boolean") w.carrying = step.carrying;

    if (step.t === "paint") {
      w.painted = w.painted || [];
      w.painted.push([step.x, step.y]);
    }
    if (step.t === "pick") {
      w.items = (w.items || []).filter(function (p) {
        return !(p[0] === step.x && p[1] === step.y);
      });
      w.carrying = true;
    }
    if (step.t === "put") {
      w.items = w.items || [];
      w.items.push([step.x, step.y]);
      w.carrying = false;
    }
    if (step.t === "push" && step.from && step.to) {
      w.boxes = (w.boxes || []).map(function (p) {
        if (p[0] === step.from[0] && p[1] === step.from[1]) return step.to.slice();
        return p;
      });
    }
    this.draw();
    if (this.root) {
      this.root.classList.toggle("is-bump", step.t === "bump" || step.t === "fail");
    }
  },

  clearCelebrate() {
    if (this.winTimer) {
      clearTimeout(this.winTimer);
      this.winTimer = null;
    }
    if (this.wrap) this.wrap.classList.remove("is-win");
    if (this.stage) this.stage.classList.remove("is-win");
    if (this.root) this.root.classList.remove("is-win");
    if (this.celebrateEl) this.celebrateEl.hidden = true;
    if (this.celebrateBurst) this.celebrateBurst.innerHTML = "";
    if (this.celebrateTitle) this.celebrateTitle.textContent = "";
    if (this.celebrateSub) this.celebrateSub.textContent = "";
  },

  prefersReducedMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  },

  playFanfare() {
    if (this.prefersReducedMotion()) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      if (!this.audioCtx) this.audioCtx = new AudioCtx();
      const ctx = this.audioCtx;
      if (ctx.state === "suspended") ctx.resume();
      const notes = [523.25, 659.25, 783.99, 1046.5];
      notes.forEach(function (freq, index) {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = "triangle";
        osc.frequency.value = freq;
        const t0 = ctx.currentTime + index * 0.09;
        gain.gain.setValueAtTime(0.0001, t0);
        gain.gain.exponentialRampToValueAtTime(0.12, t0 + 0.02);
        gain.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.28);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(t0);
        osc.stop(t0 + 0.3);
      });
    } catch (err) {
      /* ignore audio errors */
    }
  },

  spawnConfetti() {
    if (!this.celebrateBurst || this.prefersReducedMotion()) return;
    this.celebrateBurst.innerHTML = "";
    const colors = ["#fbbf24", "#34d399", "#60a5fa", "#f472b6", "#a78bfa", "#fb923c", "#fef08a", "#22d3ee"];
    const kinds = ["rect", "rect", "dot", "star"];
    const count = 72;
    for (let i = 0; i < count; i += 1) {
      const piece = document.createElement("span");
      const kind = kinds[i % kinds.length];
      piece.className = "game-confetti game-confetti--" + kind;
      piece.style.setProperty("--c", colors[i % colors.length]);
      piece.style.setProperty("--x", Math.random() * 100 + "%");
      piece.style.setProperty("--dx", (Math.random() * 140 - 70) + "px");
      piece.style.setProperty("--rot", Math.random() * 720 - 360 + "deg");
      piece.style.setProperty("--dur", 1.15 + Math.random() * 1.1 + "s");
      piece.style.animationDelay = Math.random() * 0.35 + "s";
      this.celebrateBurst.appendChild(piece);
    }
  },

  celebrate() {
    this.clearCelebrate();
    if (!this.celebrateEl) return;
    this.celebrateEl.hidden = false;
    if (this.wrap) this.wrap.classList.add("is-win");
    if (this.stage) this.stage.classList.add("is-win");
    if (this.root) this.root.classList.add("is-win");
    if (this.celebrateTitle) this.celebrateTitle.textContent = t("game.celebrate_title");
    if (this.celebrateSub) this.celebrateSub.textContent = t("game.celebrate_sub");
    this.spawnConfetti();
    this.playFanfare();
    const self = this;
    this.winTimer = setTimeout(function () {
      self.clearCelebrate();
    }, 4200);
  },

  draw() {
    if (!this.root || !this.world) return;
    const w = this.world;
    const width = w.width || 1;
    const height = w.height || 1;
    const walls = this.asSet(w.walls);
    const painted = this.asSet(w.painted);
    const paintTargets = this.asSet(w.paint_targets);
    const items = this.asSet(w.items);
    const itemTargets = this.asSet(w.item_targets);
    const boxes = this.asSet(w.boxes);
    const boxTargets = this.asSet(w.box_targets);
    const finish = w.finish ? this.key(w.finish[0], w.finish[1]) : "";
    const rx = (w.start && w.start[0]) || 0;
    const ry = (w.start && w.start[1]) || 0;
    const facing = w.facing || "right";

    this.root.style.setProperty("--game-cols", String(width));
    this.root.style.setProperty("--game-rows", String(height));
    this.root.innerHTML = "";
    this.root.classList.remove("is-bump");

    for (let y = 0; y < height; y += 1) {
      for (let x = 0; x < width; x += 1) {
        const cell = document.createElement("div");
        const k = this.key(x, y);
        cell.className = "game-cell";
        cell.style.gridColumn = String(x + 1);
        cell.style.gridRow = String(y + 1);
        if ((x + y) % 2 === 1) cell.classList.add("game-cell--alt");
        if (walls[k]) cell.classList.add("game-cell--wall");
        if (paintTargets[k]) cell.classList.add("game-cell--paint-target");
        if (painted[k]) cell.classList.add("game-cell--painted");
        if (itemTargets[k]) cell.classList.add("game-cell--item-target");
        if (boxTargets[k]) cell.classList.add("game-cell--box-target");
        if (finish === k) cell.classList.add("game-cell--finish");
        if (items[k]) {
          const gem = document.createElement("span");
          gem.className = "game-item";
          gem.setAttribute("aria-hidden", "true");
          cell.appendChild(gem);
        }
        if (boxes[k]) {
          const box = document.createElement("span");
          box.className = "game-box";
          box.innerHTML = '<span class="game-box__lid"></span><span class="game-box__mark"></span>';
          box.setAttribute("aria-hidden", "true");
          cell.appendChild(box);
        }
        if (x === rx && y === ry && !walls[k]) {
          const robot = document.createElement("span");
          robot.className = "game-robot game-robot--" + facing;
          if (w.carrying) robot.classList.add("is-carrying");
          robot.innerHTML =
            '<span class="game-robot__antenna"></span>' +
            '<span class="game-robot__head">' +
            '<span class="game-robot__visor"></span>' +
            '<span class="game-robot__eye game-robot__eye--l"></span>' +
            '<span class="game-robot__eye game-robot__eye--r"></span>' +
            "</span>" +
            '<span class="game-robot__torso"></span>' +
            '<span class="game-robot__arm game-robot__arm--l"></span>' +
            '<span class="game-robot__arm game-robot__arm--r"></span>' +
            '<span class="game-robot__leg game-robot__leg--l"></span>' +
            '<span class="game-robot__leg game-robot__leg--r"></span>' +
            '<span class="game-robot__cargo"></span>';
          robot.setAttribute("aria-label", "robot");
          cell.appendChild(robot);
        }
        this.root.appendChild(cell);
      }
    }
  },
};
