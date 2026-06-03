class VideoPage {
    constructor() {
        this.serverUrl = 'http://127.0.0.1:8000';
        this.backBtn = document.getElementById('backBtn');
        this.videoImage = document.getElementById('videoImg');

        this.init();
    }

    async init() {
        const response = await fetch(`${this.serverUrl}/api/config/paths`);
        const paths = await response.json();

        if (this.backBtn) {
            this.backBtn.addEventListener('click', () => {
                window.location.href = `${paths.MENU_PAGE_PATH}/`;
            });
        }
    }
}

new VideoPage();