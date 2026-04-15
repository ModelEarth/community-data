# Farmfresh Data Pull — prep scripts

`fetch_data.py` pulls all listing types from the USDA Local Food Portal API for each state and writes a single combined CSV per state.

## Output

Each state produces a single combined CSV: `../us/<STATE>/<state>-farmfresh.csv`

Example: `../us/GA/ga-farmfresh.csv`

The CSV contains all available listing types merged into one file. Types found in the GA test run:

| API endpoint    | Type value in CSV  | GA records |
|-----------------|--------------------|-----------|
| farmersmarket   | farmers market     | 224       |
| onfarmmarket    | on-farm market     | 24        |
| csa             | csa enterprise     | 16        |
| foodhub         | food hub           | 4         |
| cooperative     | (empty for GA)     | 0         |

All known API endpoints are listed in `MARKET_TYPES` at the top of `fetch_data.py`. Add new endpoints there to include additional types automatically.

## Running

### Requirements

```bash
pip install -r requirements.txt
```

### Set the API key

```bash
export USDA_FARMFRESH_API="UXLbsdPdCU"
```

The key above is the working key as of April 2026. In GitHub Actions it is read from `secrets.USDA_FARMFRESH_API` (see `../.github/workflows/actions.yml`).

### Run for a single state (recommended for testing)

```bash
USDA_FARMFRESH_API="UXLbsdPdCU" python3 -c "
import os, sys
sys.path.insert(0, '.')
os.environ['USDA_FARMFRESH_API'] = 'UXLbsdPdCU'
from fetch_data import export_all_states
export_all_states(['GA'])
"
```

### Run for all states

```bash
USDA_FARMFRESH_API="UXLbsdPdCU" python fetch_data.py
```

States are read from `state_list.txt`.

## Optional: JSON and YAML output

By default only the `.csv` file is written. To also generate `.json` and `.yaml` files, pass `include_json_yaml=True`:

```python
from fetch_data import export_all_states
export_all_states(['GA'], include_json_yaml=True)
```

Or for all states:

```python
export_all_states(include_json_yaml=True)
```

This produces:
- `<state>-farmfresh.csv`
- `<state>-farmfresh.json`
- `<state>-farmfresh.yaml`

## Logs

Script activity and errors are written to `status.log` in this folder.
