class SoundFlowCard extends HTMLElement {
  setConfig(config) {
    this.config = config;
  }

  set hass(hass) {
    if (!this.content) {
      this.innerHTML = `
        <ha-card header="🎵 SoundFlow">
          <div class="search-bar">
            <input id="searchInput" type="text" placeholder="Pesquisar...">
            <button id="searchBtn">🔍</button>
          </div>
          <div id="tabs"></div>
          <div id="columns"></div>
          <div class="controls">
            <button>⏯️</button>
            <button>⏭️</button>
            <button>⏮️</button>
            <button>🔀</button>
            <button>🔁</button>
          </div>
        </ha-card>
      `;
      this.content = this.querySelector("ha-card");
    }
  }
}

customElements.define("soundflow-card", SoundFlowCard);
