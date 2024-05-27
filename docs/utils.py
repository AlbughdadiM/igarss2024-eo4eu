import os
from urllib.parse import urlparse
from io import BytesIO
import requests
from PIL import Image
import numpy as np
import geopandas as gpd
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape


def geometry_to_coords(geometry):
    if geometry.geom_type == "Polygon":
        coordinates = list(geometry.exterior.coords)
    elif geometry.geom_type == "MultiPolygon":
        coordinates = list(geometry.geoms[0].exterior.coords)
    converted_coordinates = [[coord[0], coord[1]] for coord in coordinates]
    return converted_coordinates


def read_image_from_url_asarray(image_url, save=False, output_path=None):
    try:
        response = requests.get(image_url)  # pylint:disable=W3101
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))

        if save and output_path:
            image.save(output_path)

        return np.array(image)

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the image. Error: {e}")
    except Image.UnidentifiedImageError:
        print(
            "Cannot identify the image file. The URL might not point to a valid image."
        )
    except Exception as e:  # pylint:disable=W0718
        print(f"An unexpected error occurred: {e}")


def save_image_from_url(image_url, output_path):
    try:
        response = requests.get(image_url)  # pylint:disable=W3101
        response.raise_for_status()
        with open(output_path, "wb") as file:
            file.write(response.content)
        print(f"Image successfully saved to {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the image. Error: {e}")


def geographic_to_pixel_bbox(
    bbox_geo: np.array,
    image_width: int,
    image_height: int,
    min_latitude: float,
    max_latitude: float,
    min_longitude: float,
    max_longitude: float,
) -> np.array:
    # Calculate the conversion factors
    lat_range = max_latitude - min_latitude
    lon_range = max_longitude - min_longitude
    # lat_factor = image_height / lat_range
    # lon_factor = image_width / lon_range

    # Convert the bounding box coordinates to pixel coordinates
    x_min = ((bbox_geo[:, 0] - min_longitude) / lon_range * image_width).astype(int)
    y_min = ((max_latitude - bbox_geo[:, 3]) / lat_range * image_height).astype(int)
    x_max = ((bbox_geo[:, 2] - min_longitude) / lon_range * image_width).astype(int)
    y_max = ((max_latitude - bbox_geo[:, 1]) / lat_range * image_height).astype(int)

    # Create the pixel bounding box array
    pixel_bbox = np.column_stack((x_min, y_min, x_max, y_max))
    return pixel_bbox


def geometry_to_xy(gdf):
    list_bboxes = []
    for idx, row in gdf.iterrows():
        x_min, y_min, x_max, y_max = row.geometry.bounds
        list_bboxes.append([x_min, y_min, x_max, y_max])
    return list_bboxes


def geographic_to_pixel_point(
    point_geo: np.array,
    image_width: int,
    image_height: int,
    min_latitude: float,
    max_latitude: float,
    min_longitude: float,
    max_longitude: float,
) -> np.array:
    # Calculate the conversion factors
    lat_range = max_latitude - min_latitude
    lon_range = max_longitude - min_longitude
    # lat_factor = image_height / lat_range
    # lon_factor = image_width / lon_range

    # Convert the bounding box coordinates to pixel coordinates
    x_pixel = ((point_geo[:, 0] - min_longitude) / lon_range * image_width).astype(int)
    y_pixel = ((max_latitude - point_geo[:, 1]) / lat_range * image_height).astype(int)

    # Create the pixel bounding box array
    pixel_coord = np.column_stack((x_pixel, y_pixel))
    return pixel_coord


def download_txtfile_from_url(url, ouput_path):
    # Perform the GET request
    response = requests.get(url, stream=True)  # pylint:disable=W3101

    # Check if the request was successful
    if response.status_code == 200:
        # Open a local file with write-binary mode
        with open(ouput_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                # Write the chunk to the file
                f.write(chunk)
        print(f"File downloaded successfully as {ouput_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


def get_filename_from_url(url):
    # Parse the URL to get the path
    parsed_url = urlparse(url)
    # Extract the filename from the path
    filename = os.path.basename(parsed_url.path)
    return filename


def raster_to_shapefile(raster_path, shapefile_path):
    with rasterio.open(raster_path) as src:
        mask = src.read(1)
        shapes_list = []
        for geom, val in shapes(mask, transform=src.transform):
            if val != 0:
                shapes_list.append(shape(geom))
    crs = src.crs
    gdf = gpd.GeoDataFrame(geometry=shapes_list, crs=crs)
    gdf.to_file(shapefile_path)


def obb_to_aabb(obb):
    x_coords = obb[0::2]
    y_coords = obb[1::2]
    x_min = min(x_coords)
    y_min = min(y_coords)
    x_max = max(x_coords)
    y_max = max(y_coords)
    return x_min, y_min, x_max, y_max


def read_annotation_file(annotation_path):
    with open(annotation_path, "r") as file:
        lines = file.readlines()
    annotations = []
    for line in lines:
        values = line.strip().split()
        category = values[0]
        x1, y1, x2, y2, x3, y3, x4, y4 = map(lambda val: float(val) * 1024, values[1:])
        annotations.append(
            {"class_id": int(category), "coordinates": [x1, y1, x2, y2, x3, y3, x4, y4]}
        )
    return annotations
