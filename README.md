# api.vitalim.dev
Different Types Of APIs

# Locations
Cadastre data of Georgian locations. Data according to maps.gov.ge. Data includes the following fields
```json
{
  "id": 1498,
  "created": "2024-05-30T22:46:48.521686+04:00",
  "modified": "2024-05-30T22:46:48.521686+04:00",
  "name_en": "q. xaSuri",
  "name_geo": "ქ. ხაშური",
  "country_en": "geo",
  "country_geo": "საქართველო",
  "location_type": "VILLAGE",
  "zone_id": "69",
  "sector_id": "8",
  "latitude": 41.99639642340134,
  "longitude": 43.59902916367556
}
```
On top of location data distances between points are calculated through Google distance matrix api. Distance data includes the following fields
```json
{
  "id": 1172,
  "created": "2024-06-09T21:26:13.190227+04:00",
  "modified": "2024-06-09T21:26:13.190227+04:00",
  "origin_zone_id": "69",
  "origin_name_geo": "ხაშური",
  "dest_zone_id": "84",
  "dest_name_geo": "თეთრიწყარო",
  "distance": 195.594, 
  "duration": 10058.0
}
```

### Usage can be found [here](apps/location/README.md)
```shell

certbot certonly --force-renew -d api.vitalim.dev -d www.api.vitalim.dev

```