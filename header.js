// Header component - injects header navigation into pages
function loadHeader() {
    const header = document.querySelector('header');
    if (!header) return;

    // Build header navigation
    header.innerHTML = `
        <nav>
            <h1>21st Century Digital Boy Scout</h1>
            <div class="nav-links">
                <a href="https://www.linkedin.com/newsletters/21st-century-digital-boy-scout-7403830207054290944/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                <a href="https://youtube.com/@aiboyscout?si=jpU5sadd3CJw35Xz" target="_blank" rel="noopener noreferrer">YouTube</a>
                <a href="https://x.com/aiboyscout" target="_blank" rel="noopener noreferrer">X.com</a>
                <a href="https://www.tiktok.com/@jordanbaucke" target="_blank" rel="noopener noreferrer">TikTok</a>
                <a href="https://www.instagram.com/aiboyscout/" target="_blank" rel="noopener noreferrer">Instagram</a>
            </div>
        </nav>
    `;
}

// Load header when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadHeader);
} else {
    loadHeader();
}
