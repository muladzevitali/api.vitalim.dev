# Usage

1. <b>List locations.</b> Queryset params: zone_id, sector_id, name_en, name_geo
    ```shell
    curl --location 'http://127.0.0.1:8000/api/location/locations/' \
    --header 'Authorization: Token <token>'
    ```

2. <b>Get distance between two places.</b> Queryset params: origin_zone_id, origin_name_geo, dest_zone_id, dest_name_geo
    ```shell
    curl --location 'http://127.0.0.1:8000/api/location/distances/' \
    --header 'Authorization: Token <token>'
    ```