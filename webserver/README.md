# Parts Explorer

Search the local OOMP catalogue, inspect component drawings and datasheets,
look up short names, and record new manual entries. Parts Explorer is a Flask
application that reads generated component records from disk.

**[Back to OOMP Electronics](../README.md)** · **[Component catalogue](../navigation/README.md)** · **[Adding components](../ADDING_COMPONENTS.md)**

## Start the explorer

From the repository root, using the project's Python environment:

```powershell
python -X utf8 -m webserver.app
```

Open `http://127.0.0.1:<port>/explore`, using the port in `config_port.yaml`.
A config file at the repository root takes precedence over the corresponding
file in `webserver/`. Without a port config, the fallback is `127.0.0.1:5000`.
The `-X utf8` option also keeps the startup progress display readable on Windows.

## Browse and inspect components

- **Search and filter:** search names, supplier codes, ratings, and collected
  details; combine text search with taxonomy, sorting, and recorded JLCPCB tiers.
- **Read the evidence:** component pages include manufacturer details, ordering
  codes, LCSC/JLCPCB links, datasheets, specifications, dimensions, pins, and notes.
- **Inspect drawings:** pinout thumbnails lead to uncropped previews and a diagram
  gallery with thumbnail selection, previous/next buttons, and arrow-key navigation.
- **Find labels:** part-ID and short-code SVG labels are promoted in the file list,
  including labels stored in nested folders.

Basic, Extended (including Preferred Extended), and Unclassified tiers start
enabled. Clearing every tier shows no parts. Selections survive search, sorting,
and taxonomy navigation. Stock and MOQ values remain dated observations.

### Pages and actions

| Page or control | What it does |
| --- | --- |
| `/explore` | Browse compact component rows with search, sorting, and taxonomy filters. `/` redirects here. |
| `/short_names` | Narrow cached parts by `md5_6` and BIP39 short names. |
| `/id/<extra>` | Resolve a unique part ID, `md5_6`, or two-/three-word BIP39 variant. |
| `/add` | Save a manual entry to `working_manual.yaml` at the repository root. |
| **Reload Fast** | Reload new or changed part folders; rebuild fully if the UI config changed. |
| **Reload All** | Rebuild the catalogue cache from disk. |
| **Run Generation** | Launch `action_make_all.py` in a separate visible Windows command window. |

## Configure the explorer

| File | Controls |
| --- | --- |
| `config_port.yaml` | Server host and port. |
| `config_part_source.yaml` | Ordered list of component source directories. |
| `config_ui.yaml` | Preview priority and image serving/cache options. |
| `config_form_base.yaml` | Default fields for the manual-entry form. |
| `config_form.yaml` | Form overrides, when present. |

### Component sources

Each entry in `config_part_source.yaml`'s `directories` list can point to a
`parts` directory or its parent. When IDs appear in multiple sources, the first
directory wins. Both reload controls pick up source-config changes.

### Previews and image caching

`preview_priority` is evaluated from top to bottom, with exact filenames before
wildcard fallbacks. Both reload controls apply UI changes.

Raster previews are resized and cached for result rows, file popovers, detail
pages, and the popup viewer. The default machine-local cache is
`%LOCALAPPDATA%\project_base\webserver_image_cache`; set an absolute
`image_serving.cache_dir` to use another location. SVGs are served as their
original assets. **Open Original** always gives access to the full-size file.

The catalogue cache is built at startup, with a per-part progress display.
Full file inventories, image metadata, and viewer data load on demand.

### Manual entries

The default generic form exposes `taxonomy_1` through `taxonomy_15`. It records
validated form values without remapping the taxonomy. IC entries must follow
the current [component naming rules](../README.md#ic-naming).

## Developer map

| Area | Files |
| --- | --- |
| Application setup and cache/config lifecycle | `app.py`, `runtime.py` |
| Explore and short-name routes | `routes/explore.py`, `routes/short_names.py` |
| Component details, files, and image serving | `routes/parts.py` |
| Manual entries, reload, and generation | `routes/manual.py`, `routes/actions.py` |
| Shared presentation helpers | `presentation.py` |
| Design tokens, layout, and shared controls | `static/style.css`, `templates/base.html` |
| Page interactions | `static/explore.js`, `static/short_names.js`, `static/add_item.js` |
| Popup image viewer | `static/image_viewer.js` |
