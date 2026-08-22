/**
 * Третий режим редактора: миссии робота на клетчатом поле.
 */
const GameUI = {
  active: false,
  trackId: "",
  missionId: "",
  tracks: [],
  missions: [],
  world: null,
  seed: 1,
  toolboxKind: "linear",

  init() {
    this.pickersRow = document.getElementById("gamePickersRow");
    this.trackSelect = document.getElementById("gameTrackSelect");
    this.missionSelect = document.getElementById("gameMissionSelect");
    this.panel = document.getElementById("gamePanel");
    this.titleEl = document.getElementById("gameTitle");
    this.conditionEl = document.getElementById("gameCondition");
    this.hintEl = document.getElementById("gameHint");
    this.metaEl = document.getElementById("gameMeta");
    this.stage = document.getElementById("gameStage");
    this.outputPanel = document.getElementById("outputPanel");
    this.btnCheck = document.getElementById("btnGameCheck");
    this.btnPrev = document.getElementById("btnGamePrev");
    this.btnNext = document.getElementById("btnGameNext");
    this.btnReset = document.getElementById("btnGameReset");
    this.btnSolution = document.getElementById("btnGameSolution");
    this.speedSelect = document.getElementById("gameSpeed");
    this.debugBtn = document.getElementById("btnDebugStart");
    this.authenticated = document.body.dataset.authenticated === "1";

    if (typeof GameWorldView !== "undefined") GameWorldView.init();
    if (typeof CustomSelect !== "undefined") {
      CustomSelect.enhance(this.trackSelect);
      CustomSelect.enhance(this.missionSelect);
    }

    if (this.trackSelect) {
      this.trackSelect.addEventListener("change", () => this.onTrackChange());
    }
    if (this.missionSelect) {
      this.missionSelect.addEventListener("change", () => this.onMissionChange());
    }
    if (this.btnCheck) this.btnCheck.addEventListener("click", () => this.check());
    if (this.btnPrev) this.btnPrev.addEventListener("click", () => this.navigate(-1));
    if (this.btnNext) this.btnNext.addEventListener("click", () => this.navigate(1));
    if (this.btnReset) this.btnReset.addEventListener("click", () => this.resetField());
    if (this.btnSolution) this.btnSolution.addEventListener("click", () => this.loadMySolution());
  },

  topicIdForTrack(trackId) {
    if (trackId === "conditions") return "game_if";
    if (trackId === "loops") return "game_loops";
    return "game_linear";
  },

  refreshSelect(select) {
    if (typeof CustomSelect !== "undefined") CustomSelect.refresh(select);
  },

  setSelectDisabled(select, disabled) {
    if (!select) return;
    select.disabled = disabled;
    if (typeof CustomSelect !== "undefined") CustomSelect.setDisabled(select, disabled);
  },

  setActive(on) {
    const wasActive = this.active;
    this.active = !!on;
    document.body.classList.toggle("is-game-mode", this.active);
    this.syncChrome();
    if (this.active) {
      this.applyToolbox(this.toolboxKind);
      if (!this.tracks.length) this.loadTracks();
    } else if (wasActive && typeof ScratchToolbox !== "undefined" && typeof PYBLOCKS_TOOLBOX !== "undefined") {
      ScratchToolbox.rebuild(PYBLOCKS_TOOLBOX);
    }
  },

  applyToolbox(kind) {
    this.toolboxKind = kind || "linear";
    if (typeof ScratchToolbox === "undefined" || typeof getGameToolbox !== "function") return;
    ScratchToolbox.rebuild(getGameToolbox(this.toolboxKind));
  },

  syncChrome() {
    const on = this.active;
    const hasMission = on && !!this.missionId;
    if (this.pickersRow) this.pickersRow.hidden = !on;
    if (this.panel) this.panel.hidden = !hasMission;
    if (this.stage) this.stage.hidden = !on;
    if (this.outputPanel) this.outputPanel.hidden = on;
    if (this.debugBtn) this.debugBtn.hidden = on;
    if (this.btnCheck) this.btnCheck.hidden = !hasMission;
    if (this.btnPrev) this.btnPrev.hidden = !hasMission;
    if (this.btnNext) this.btnNext.hidden = !hasMission;
    this.updateSolutionButton();
    if (typeof TopicsUI !== "undefined" && TopicsUI.updateWorkspaceLayout) {
      requestAnimationFrame(() => TopicsUI.updateWorkspaceLayout());
    }
  },

  async loadTracks() {
    try {
      const response = await fetch("/api/game/tracks", { headers: getJsonHeaders() });
      const data = await response.json();
      this.tracks = data.tracks || [];
      this.fillTrackSelect();
    } catch (err) {
      console.error("GameUI.loadTracks", err);
    }
  },

  fillTrackSelect() {
    if (!this.trackSelect) return;
    this.trackSelect.innerHTML = '<option value="">' + t("game.select_track") + "</option>";
    this.tracks.forEach((track) => {
      const opt = document.createElement("option");
      opt.value = track.id;
      opt.textContent = track.title;
      opt.disabled = track.unlocked === false;
      this.trackSelect.appendChild(opt);
    });
    if (this.trackId) this.trackSelect.value = this.trackId;
    this.refreshSelect(this.trackSelect);
  },

  async onTrackChange() {
    this.trackId = this.trackSelect ? this.trackSelect.value : "";
    this.missionId = "";
    this.world = null;
    if (this.missionSelect) {
      this.missionSelect.innerHTML = '<option value="">' + t("game.select_mission") + "</option>";
      this.setSelectDisabled(this.missionSelect, !this.trackId);
    }
    if (!this.trackId) {
      this.syncChrome();
      return;
    }
    const track = this.tracks.find((item) => item.id === this.trackId);
    if (track && track.unlocked === false) {
      setStatus("error", t("game.locked"));
      setOutput(track.unlock_hint || t("game.locked"), true);
      return;
    }
    this.applyToolbox(this.trackId);
    await this.loadMissions();
  },

  async loadMissions() {
    try {
      const response = await fetch("/api/game/tracks/" + encodeURIComponent(this.trackId) + "/missions", {
        headers: getJsonHeaders(),
      });
      const data = await response.json();
      if (!response.ok) {
        setStatus("error", t("game.locked"));
        setOutput(data.error || t("game.locked"), true);
        return;
      }
      this.missions = data.missions || [];
      this.fillMissionSelect();
    } catch (err) {
      console.error("GameUI.loadMissions", err);
    }
  },

  fillMissionSelect() {
    if (!this.missionSelect) return;
    this.missionSelect.innerHTML = '<option value="">' + t("game.select_mission") + "</option>";
    this.missions.forEach((item, index) => {
      const opt = document.createElement("option");
      opt.value = item.id;
      opt.textContent = index + 1 + ". " + item.title + (item.completed ? " ✓" : "");
      if (item.completed) {
        opt.dataset.completed = "1";
        opt.title = t("topics.task_solved");
      }
      this.missionSelect.appendChild(opt);
    });
    this.setSelectDisabled(this.missionSelect, false);
    this.refreshSelect(this.missionSelect);
    this.syncChrome();
  },

  async onMissionChange() {
    this.missionId = this.missionSelect ? this.missionSelect.value : "";
    if (!this.missionId) {
      this.syncChrome();
      return;
    }
    await this.loadMission();
  },

  async loadMission() {
    try {
      const response = await fetch("/api/game/missions/" + encodeURIComponent(this.missionId), {
        headers: getJsonHeaders(),
      });
      const data = await response.json();
      if (!response.ok) {
        setStatus("error", t("status.error"));
        setOutput(data.error || t("game.mission_missing"), true);
        return;
      }
      const mission = data.mission || {};
      this.world = data.world;
      this.seed = data.seed;
      this.toolboxKind = mission.toolbox || this.trackId || "linear";
      this.applyToolbox(this.toolboxKind);
      if (this.titleEl) this.titleEl.textContent = mission.title || t("game.mission");
      if (this.conditionEl) this.conditionEl.textContent = mission.condition || "";
      if (this.hintEl) {
        if (mission.hint) {
          this.hintEl.hidden = false;
          this.hintEl.textContent = t("topics.hint_label") + " " + mission.hint;
        } else {
          this.hintEl.hidden = true;
          this.hintEl.textContent = "";
        }
      }
      if (this.metaEl) {
        const index = this.missions.findIndex((item) => item.id === this.missionId);
        this.metaEl.textContent =
          index >= 0 ? t("game.mission_of", "", { current: index + 1, total: this.missions.length }) : "";
      }
      if (typeof GameWorldView !== "undefined") {
        GameWorldView.render(this.world);
        GameWorldView.setMessage(t("game.ready_field"));
      }
      this.updateNav();
      this.updateSolutionButton();
      this.syncChrome();
      setStatus("idle", t("status.ready"));
    } catch (err) {
      console.error("GameUI.loadMission", err);
    }
  },

  updateNav() {
    const index = this.missions.findIndex((item) => item.id === this.missionId);
    if (this.btnPrev) this.btnPrev.disabled = index <= 0;
    if (this.btnNext) this.btnNext.disabled = index < 0 || index >= this.missions.length - 1;
  },

  navigate(delta) {
    const index = this.missions.findIndex((item) => item.id === this.missionId);
    const next = this.missions[index + delta];
    if (!next || !this.missionSelect) return;
    this.missionSelect.value = next.id;
    this.refreshSelect(this.missionSelect);
    this.onMissionChange();
  },

  resetField() {
    if (typeof GameWorldView !== "undefined") GameWorldView.reset();
  },

  getCode() {
    if (typeof getActivePythonCode === "function") return getActivePythonCode();
    return "";
  },

  speed() {
    return this.speedSelect ? Number(this.speedSelect.value) || 320 : 320;
  },

  async run() {
    const code = this.getCode();
    if (!code.trim()) {
      setStatus("error", t("status.error"));
      setOutput(t("run.no_blocks"), true);
      return;
    }
    if (!this.missionId) {
      setStatus("error", t("status.error"));
      setOutput(t("game.select_mission_first"), true);
      return;
    }
    setStatus("running", t("status.running"));
    if (typeof GameWorldView !== "undefined") GameWorldView.setMessage(t("game.running"));
    try {
      const response = await fetch("/api/game/run", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({
          code: code,
          mission_id: this.missionId,
          world: this.world,
          seed: this.seed,
        }),
      });
      const data = await response.json();
      const limitMsg = getApiErrorMessage(data, response);
      if (limitMsg) {
        setStatus("error", t("status.wait"));
        setOutput(limitMsg, true);
        return;
      }
      if (typeof GameWorldView !== "undefined") {
        await GameWorldView.play(data.steps || [], this.speed());
      }
      if (data.success && data.goal_met) {
        setStatus("success", t("game.goal_ok"));
        GameWorldView.setMessage(t("game.goal_ok"));
      } else if (data.success) {
        setStatus("error", t("game.goal_miss"));
        GameWorldView.setMessage(t("game.goal_miss"), true);
      } else {
        setStatus("error", t("status.error"));
        GameWorldView.setMessage(data.error || t("status.error"), true);
      }
    } catch (err) {
      setStatus("error", t("status.error"));
      setOutput(t("run.network_error", "Network error: {message}", { message: err.message }), true);
    }
  },

  async check() {
    const code = this.getCode();
    if (!code.trim() || !this.missionId) {
      setStatus("error", t("status.error"));
      setOutput(t("game.select_mission_first"), true);
      return;
    }
    setStatus("running", t("topics.checking"));
    let blocksXml = "";
    if (typeof workspace !== "undefined" && typeof WorkspaceStorage !== "undefined") {
      blocksXml = WorkspaceStorage.serialize(workspace);
    }
    try {
      const response = await fetch("/api/game/check", {
        method: "POST",
        headers: getJsonHeaders(),
        body: JSON.stringify({
          code: code,
          mission_id: this.missionId,
          blocks_xml: blocksXml,
        }),
      });
      const data = await response.json();
      const limitMsg = getApiErrorMessage(data, response);
      if (limitMsg) {
        setStatus("error", t("status.wait"));
        setOutput(limitMsg, true);
        return;
      }
      const result = data.result || {};
      const mapToShow = data.failed_world || data.world;
      if (mapToShow && typeof GameWorldView !== "undefined") {
        GameWorldView.render(mapToShow);
      }
      if (result.steps && typeof GameWorldView !== "undefined") {
        await GameWorldView.play(result.steps, this.speed());
      }
      if (data.success) {
        setStatus("success", t("game.check_ok"));
        if (typeof GameWorldView !== "undefined") {
          GameWorldView.setMessage(t("game.check_ok"));
          GameWorldView.celebrate();
        }
        const current = this.missions.find((item) => item.id === this.missionId);
        if (current) {
          current.completed = true;
          current.has_solution = true;
        }
        this.fillMissionSelect();
        if (this.missionSelect) {
          this.missionSelect.value = this.missionId;
          this.refreshSelect(this.missionSelect);
        }
      } else {
        setStatus("error", t("game.check_fail"));
        const extra =
          data.total > 1
            ? " (" + (data.passed || 0) + "/" + data.total + ")"
            : "";
        if (typeof GameWorldView !== "undefined") {
          GameWorldView.setMessage((data.message || t("game.check_fail")) + extra, true);
        }
      }
    } catch (err) {
      setStatus("error", t("topics.check_error"));
      setOutput(t("run.network_error", "", { message: err.message }), true);
    }
  },

  updateSolutionButton() {
    if (!this.btnSolution) return;
    const mission = this.missions.find((item) => item.id === this.missionId);
    const show = this.authenticated && mission && mission.has_solution;
    this.btnSolution.hidden = !show;
  },

  async loadMySolution() {
    if (!this.authenticated || !this.missionId) return;
    const topicId = this.topicIdForTrack(this.trackId);
    try {
      const response = await fetch(
        "/api/progress/" + encodeURIComponent(topicId) + "/" + encodeURIComponent(this.missionId),
        { headers: getJsonHeaders() }
      );
      const data = await response.json();
      if (!data.solution_xml || typeof WorkspaceStorage === "undefined") return;
      WorkspaceStorage.load(workspace, data.solution_xml);
    } catch (err) {
      console.error("GameUI.loadMySolution", err);
    }
  },

  async applyUrlParams(params) {
    const mode = params.get("mode");
    const track = params.get("track");
    const mission = params.get("mission");
    if (mode !== "game" && !track && !mission) return false;
    await this.loadTracks();
    if (track && this.trackSelect) {
      this.trackSelect.value = track;
      this.refreshSelect(this.trackSelect);
      await this.onTrackChange();
    }
    if (mission && this.missionSelect) {
      this.missionSelect.value = mission;
      this.refreshSelect(this.missionSelect);
      await this.onMissionChange();
    }
    return true;
  },
};
