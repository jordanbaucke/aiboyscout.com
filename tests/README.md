# Link Validation Tests

Tools to validate all links on the site (from `index.html` and `header.js`).

## Contents

- **`extract_links.py`** – Extracts outbound links from `index.html` and `header.js` and writes `outbound_links.txt` and `lychee_input.txt`.
- **`check_links.sh`** – Runs the extractor, then [lychee](https://github.com/lycheeverse/lychee) on `index.html` and `header.js` to check every link.
- **`lychee.toml`** – Lychee config (timeouts, retries, accepted status codes).
- **`outbound_links.txt`** – Generated list of outbound links and which file they appear in.
- **`link_check_results.txt`** – Generated lychee report (OK/failed, status codes, errors).

## Prerequisites

1. **Python 3** – Used to extract links from HTML and JS.
2. **lychee** – Link checker (Rust).

### Install lychee

**Cargo (Rust):**
```bash
cargo install lychee
```

**Homebrew (macOS):**
```bash
brew install lychee
```

**Binary:** [Releases](https://github.com/lycheeverse/lychee/releases)

## Usage

### Run full link check

From the project root:

```bash
./tests/check_links.sh
```

This will:

1. Extract links from `index.html` and `header.js`.
2. Write `tests/outbound_links.txt`.
3. Run lychee on `index.html` and `header.js`.
4. Write `tests/link_check_results.txt`.

### Extract links only

```bash
python3 tests/extract_links.py
```

### Check links only (lychee already installed)

```bash
lychee --config tests/lychee.toml --output tests/link_check_results.txt \
  index.html header.js
```

## Configuration

Edit `lychee.toml` to change timeouts, retries, accepted status codes, user agent, etc. See [lychee docs](https://github.com/lycheeverse/lychee).
