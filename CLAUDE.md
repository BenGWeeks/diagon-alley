# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository

This is a fork. The upstream (original) repository is: https://github.com/lnbits/Diagon-Alley/

**Issues**: https://github.com/lnbits/Diagon-Alley/issues
**PRs**: https://github.com/lnbits/Diagon-Alley/pulls

## Project Overview

Diagon Alley is an LNbits extension that provides a public Nostr marketplace aggregator. It allows users to browse and discover products from multiple Nostr merchants in one place. It implements the buyer/browser side of NIP-15 (Nostr Marketplace).

## Development

### Extension Development with LNbits

This extension must be run inside LNbits. To set up:

1. Clone LNbits to a sibling directory:
   ```bash
   cd ..
   git clone https://github.com/lnbits/lnbits.git
   ```

2. Create a symbolic link from LNbits extensions to this directory:
   ```bash
   cd lnbits/lnbits/extensions
   ln -s ../../../diagon-alley diagonalley
   ```

3. Configure your development environment:
   ```bash
   # Copy the example file
   cp .env.dev.example .env.dev
   # Edit .env.dev to point to your LNbits installation if needed
   ```

4. Use slash commands to manage the dev server:
   - `/run` - Start LNbits dev server in background
   - `/stop` - Stop the LNbits dev server

### Routes

| Route | Description | Auth Required |
|-------|-------------|---------------|
| `/diagonalley/` | Extension landing page | Yes (LNbits user) |
| `/diagonalley/market` | Public marketplace | No |

### UI Notes

- When LNbits shows an "I understand" popup (e.g., for funding source warnings), click it to dismiss and continue.

## Before Committing

1. Run formatters:
   ```bash
   make format
   ```

2. Run checks:
   ```bash
   make check
   ```

3. Commit and push changes

## Nostr Protocol References

- **NIP-15** (Marketplace): https://github.com/nostr-protocol/nips/blob/master/15.md
- **NIP-99** (Classified Listings): https://github.com/nostr-protocol/nips/blob/master/99.md
- **NIP-07** (Browser Extension): https://github.com/nostr-protocol/nips/blob/master/07.md
- **NIP-65** (Relay List Metadata): https://github.com/nostr-protocol/nips/blob/master/65.md
- **Gamma Markets Spec**: https://github.com/GammaMarkets/market-spec

---

## Claude Code Best Practices

### Before Making Changes

1. **Read before editing** - Always read the file before making changes
2. **Understand the pattern** - Check similar existing code for conventions
3. **Run checks** - Use `make check` before committing

### Frontend Development (Vue.js/Quasar)

The marketplace uses a pre-built Vue app from nostrmarket in `static/market/`. The extension pages use Jinja2 templates.

#### Template Structure

- Templates are in `templates/diagonalley/`
- Static assets in `static/` and `static/market/`

#### Quasar Components

- Use Quasar components: https://quasar.dev/components
- Common patterns:
  - `q-dialog` with `v-model` for dialogs
  - `q-input` with `:model-value` for readonly, `v-model` for editable
  - `q-btn` with `@click` for actions

#### LNbits API Calls

```javascript
// GET request
const {data} = await LNbits.api.request(
  'GET',
  '/diagonalley/api/v1/endpoint',
  this.inkey  // or this.adminkey for write operations
)

// Error handling
try {
  await LNbits.api.request(...)
} catch (error) {
  LNbits.utils.notifyApiError(error)
}
```

### Backend Development (Python/FastAPI)

#### API Endpoints

```python
@diagonalley_ext.get("/api/v1/resource")
async def api_get_resource(
    wallet: WalletTypeInfo = Depends(require_invoice_key),
):
    try:
        # Business logic
        return {"status": "ok"}
    except Exception as ex:
        logger.warning(ex)
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail="Error message",
        ) from ex
```

### Git Workflow

1. **Branch naming**: `feature/<description>` or `fix/<description>`
2. **Commit messages**: Use conventional commits (`feat:`, `fix:`, `chore:`, `docs:`, etc.)
3. **Before pushing**: Always run `make check`
4. **PR comments**: Add context about changes and any WIP items

### Slash Commands

Available Claude Code commands in `.claude/commands/`:

| Command | Description |
|---------|-------------|
| `/commit` | Run checks and commit |
| `/push` | Vet with Archie and push |
| `/pr` | Create a pull request |
| `/format` | Format code |
| `/run` | Start LNbits dev server |
| `/stop` | Stop LNbits dev server |
| `/vet` | Code review with Archie |
| `/test` | Test with Teddie |
| `/create-issue` | Create GitHub issue |
| `/add-troubleshooting` | Add troubleshooting entry |

### Agents

- **Teddie the Tester** (`/test`) - Tests changes using Playwright MCP and Chrome extension
- **Archie the Architect** (`/vet`) - Reviews code for quality, security, and accessibility

### Documentation

- `docs/TROUBLESHOOTING.adoc` - Common issues
- `docs/FAQS.adoc` - Frequently asked questions
- `docs/TESTING.adoc` - Testing guide
- `docs/DEPLOYMENT.adoc` - Deployment guide
- `docs/SOLUTION_DESIGN.adoc` - Architecture overview

### Common Gotchas

1. **Vue delimiters** - Use `${...}` not `{{...}}` (conflicts with Jinja2)
2. **Icon names** - Use Material Icons: https://fonts.google.com/icons
3. **Async/await** - Remember to `await` API calls
4. **Formatting** - Run `make format` before committing
