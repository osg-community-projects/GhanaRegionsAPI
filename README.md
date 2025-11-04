# Ghana Regions API

A comprehensive FastAPI-based REST API for Ghana's administrative divisions including regions, districts, and towns.

## Features

- **16 Regions**: All current regions of Ghana with their capitals
- **Districts**: Administrative districts within each region
- **Towns**: Major towns and cities with population data
- **Search Functionality**: Search across regions, districts, and towns
- **Population Queries**: Filter towns by population ranges
- **Modular Architecture**: Clean, maintainable code structure

## API Endpoints

### Regions
- `GET /api/v1/regions` - Get all regions
- `GET /api/v1/regions/{id}` - Get region by ID
- `GET /api/v1/regions/{id}/details` - Get region with districts
- `GET /api/v1/regions/name/{name}` - Get region by name
- `GET /api/v1/regions/search?q={query}` - Search regions

### Districts
- `GET /api/v1/districts` - Get all districts
- `GET /api/v1/districts/{id}` - Get district by ID
- `GET /api/v1/districts/{id}/details` - Get district with towns
- `GET /api/v1/regions/{region_id}/districts` - Get districts by region
- `GET /api/v1/districts/search?q={query}` - Search districts

### Towns
- `GET /api/v1/towns` - Get all towns
- `GET /api/v1/towns/{id}` - Get town by ID
- `GET /api/v1/districts/{district_id}/towns` - Get towns by district
- `GET /api/v1/towns/search?q={query}` - Search towns
- `GET /api/v1/towns/largest?limit={n}` - Get largest towns
- `GET /api/v1/towns/population?min_pop={min}&max_pop={max}` - Filter by population

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd GhanaRegionsAPI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Usage

Once running, visit:
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## Project Structure

```
app/
├── main.py              # FastAPI application entry point
├── models/              # Pydantic data models
│   ├── region.py
│   ├── district.py
│   └── town.py
├── routers/             # API route handlers
│   ├── regions.py
│   ├── districts.py
│   └── towns.py
├── services/            # Business logic layer
│   ├── region_service.py
│   ├── district_service.py
│   └── town_service.py
└── database/            # Data storage
    └── data.py          # Sample data
```

## Example Responses

### Get Region with Districts
```json
{
  "id": 7,
  "name": "GREATER ACCRA",
  "capital": "ACCRA",
  "districts": [
    {
      "id": 1,
      "name": "Accra Metropolitan",
      "region_id": 7
    }
  ]
}
```

### Get District with Towns
```json
{
  "id": 1,
  "name": "Accra Metropolitan",
  "region_id": 7,
  "towns": [
    {
      "id": 1,
      "name": "Accra",
      "district_id": 1,
      "population": 2291352
    }
  ]
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
