#!/bin/bash
# Check all links on the site (from index.html and header.js).
# Uses extract_links.py to find links, then lychee to validate them.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

echo "🔗 Link Validation Tool"
echo "======================"
echo ""

if ! command -v lychee &> /dev/null; then
    echo "❌ Error: lychee is not installed."
    echo ""
    echo "Installation options:"
    echo "  1. Using cargo (Rust):"
    echo "     cargo install lychee"
    echo ""
    echo "  2. Using Homebrew (macOS):"
    echo "     brew install lychee"
    echo ""
    echo "  3. Download binary from:"
    echo "     https://github.com/lycheeverse/lychee/releases"
    echo ""
    exit 1
fi

echo "📄 Step 1: Extracting links from index.html and header.js..."
if command -v python3 &> /dev/null; then
    python3 "$SCRIPT_DIR/extract_links.py"
else
    echo "❌ Error: python3 is required to extract links"
    exit 1
fi

echo ""
echo "🔍 Step 2: Validating all links with lychee..."
echo ""

# Run lychee on both HTML and JS so it finds every link on the page
lychee \
    --config "$SCRIPT_DIR/lychee.toml" \
    --output "$SCRIPT_DIR/link_check_results.txt" \
    --format detailed \
    "$PROJECT_ROOT/index.html" \
    "$PROJECT_ROOT/header.js" || true

LYCHEE_EXIT_CODE=$?

echo ""
echo "📊 Results saved to: $SCRIPT_DIR/link_check_results.txt"
echo ""

if [ $LYCHEE_EXIT_CODE -eq 0 ]; then
    echo "✅ All links are valid!"
else
    echo "⚠️  Some links failed validation. Check the results file for details."
fi

echo ""
echo "📋 Summary files:"
echo "   - Outbound links list: $SCRIPT_DIR/outbound_links.txt"
echo "   - Link check results:  $SCRIPT_DIR/link_check_results.txt"
echo ""

exit $LYCHEE_EXIT_CODE
