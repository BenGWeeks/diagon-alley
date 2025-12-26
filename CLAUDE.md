# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository

This is a fork. The upstream (original) repository is: https://github.com/lnbits/Diagon-Alley/

## Project Overview

Diagon Alley is an LNbits extension that provides a public Nostr marketplace aggregator. It allows users to browse and discover products from multiple Nostr merchants in one place.

## Development

### Local Testing

1. Create symbolic link in lnbits extensions folder:
   ```bash
   ln -s /home/benweeks/GitHub/diagon-alley /home/benweeks/GitHub/lnbits/lnbits/extensions/diagonalley
   ```

2. Restart LNbits to detect the extension

3. Go to http://127.0.0.1:5000/extensions and enable the extension in the "Installed" tab

### UI Notes

- When LNbits shows an "I understand" popup (e.g., for funding source warnings), click it to dismiss and continue.

## Before Committing

1. Run formatters:
   ```bash
   uvx black .
   uvx ruff check --fix .
   ```

2. Commit and push changes
