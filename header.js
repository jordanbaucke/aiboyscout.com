// Header component - injects header navigation into pages
function loadHeader() {
    const header = document.querySelector('header');
    if (!header) return;

    // Build header navigation
    header.innerHTML = `
        <nav>
            <h1>21st Century Digital Boy Scout</h1>
        </nav>
    `;
}

// Load header when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadHeader);
} else {
    loadHeader();
}
