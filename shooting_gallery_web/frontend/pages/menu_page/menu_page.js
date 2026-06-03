class MenuPage {
    constructor() {
        this.serverUrl = 'http://127.0.0.1:8000';
        this.settingsBtn = document.getElementById('settingsBtn');

        this.init();
    }

    async init() {
        const response = await fetch(`${this.serverUrl}/api/config/paths`);
        const paths = await response.json();

        this.settingsBtn.addEventListener('click', () => {
            window.location.href = `${paths.VIDEO_STREAM_PAGE_PATH}/`;
        });
    }
}

new MenuPage();