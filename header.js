// Header component - injects header navigation into pages
function loadHeader() {
    const header = document.querySelector('header');
    if (!header) return;

    // Build header navigation - large icons from MageCDN (free social icons CDN)
    header.innerHTML = `
        <nav class="site-nav">
            <div class="nav-header-row">
                <h1>21st Century Digital Boy Scout</h1>
                <img src="media/aiboyscout-seal.png" alt="" class="header-seal" width="250" height="250">
            </div>
            <div class="nav-bar">
                <ul class="nav-menu">
                    <li><a href="/">Home</a></li>
                    <li><a href="/blog/">Blog</a></li>
                </ul>
                <div class="nav-links">
                <a href="https://www.linkedin.com/newsletters/21st-century-digital-boy-scout-7403830207054290944/" target="_blank" rel="noopener noreferrer" title="LinkedIn Newsletter">
                    <img src="https://s.magecdn.com/social/tc-linkedin.svg" alt="LinkedIn" class="social-icon">
                </a>
                <a href="https://youtube.com/@aiboyscout?si=jpU5sadd3CJw35Xz" target="_blank" rel="noopener noreferrer" title="YouTube">
                    <img src="https://s.magecdn.com/social/tc-youtube.svg" alt="YouTube" class="social-icon">
                </a>
                <a href="https://x.com/aiboyscout" target="_blank" rel="noopener noreferrer" title="X">
                    <img src="https://s.magecdn.com/social/tc-x.svg" alt="X" class="social-icon">
                </a>
                <a href="https://www.tiktok.com/@aiboyscout" target="_blank" rel="noopener noreferrer" title="TikTok">
                    <img src="https://s.magecdn.com/social/tc-tiktok.svg" alt="TikTok" class="social-icon">
                </a>
                <a href="https://www.instagram.com/aiboyscout/" target="_blank" rel="noopener noreferrer" title="Instagram">
                    <img src="https://s.magecdn.com/social/tc-instagram.svg" alt="Instagram" class="social-icon">
                </a>
                </div>
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
