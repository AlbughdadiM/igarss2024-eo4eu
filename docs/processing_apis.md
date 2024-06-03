# Examples of Processing APIs in EO4EU

In this chapter, we will go through some of the APIs available via the EO4EU platform that will be used in the practical use cases.

## Sentinel-2 API

Sentinel-2 is a part of the European Space Agency's (ESA) Copernicus Program, which aims to provide comprehensive Earth observation data. It specifically refers to two satellites, Sentinel-2A and Sentinel-2B, which work in tandem to provide high-resolution optical imagery for land monitoring.

- High-Resolution Imagery: Sentinel-2 satellites provide images at various resolutions ranging from 10 meters to 60 meters.
- Multispectral Imaging: They carry a multispectral imager with 13 spectral bands, covering visible, near-infrared, and shortwave infrared wavelengths.
Wide Swath Width: Each satellite has a swath width of 290 kilometers, allowing for large areas of the Earth's surface to be imaged in a single pass.
- High Revisit Frequency: The two satellites together provide a revisit time of approximately five days at the equator, ensuring up-to-date imagery.
- Environmental Monitoring: Sentinel-2 data is crucial for monitoring various environmental parameters, including land cover changes, forest health, and agricultural productivity.
- Agriculture: Farmers and agricultural planners use Sentinel-2 imagery to monitor crop health, plan irrigation, and manage agricultural practices more efficiently.
- Disaster Management: In the event of natural disasters such as floods, wildfires, and hurricanes, Sentinel-2 provides timely data that helps in assessing damage and planning response strategies.
- Climate Change Studies: The data from Sentinel-2 contributes to understanding and modeling the effects of climate change on land surfaces, vegetation, and water bodies.
- Urban Planning and Land Use: Urban planners and policymakers use the high-resolution imagery to monitor urban sprawl, plan infrastructure development, and manage natural resources.
- Biodiversity and Conservation: Sentinel-2 helps in tracking habitat changes, protecting biodiversity, and managing conservation efforts effectively.
- Water Quality Monitoring: The multispectral capabilities allow for the assessment of water bodies, detecting changes in water quality and aiding in the management of water resources.

This API allows processing and downloading Sentinel-2 data for an ROI or a full Sentinel-2 tile.

The API is available on [Sentinel-2 API](http://sentinel-api-test.dev.apps.eo4eu.eu/)

### Sentinel-2 API Endpoints

`POST api/v1/s2l2a/roi/process`

RGB, NDVI, LAI, Band combination

`GET api/v1/s2l2a/roi/process`

`POST api/v1/s2l2a/tile/process`

Band combination

`GET api/v1/s2l2a/tile/process`

`GET api/v1/task/status`

## Leaf Area Index (LAI) API

The Leaf Area Index (LAI) Model is a dimensionless biophysical parameter representing the total leaf area per unit ground area, specifically defined as the one-sided green leaf area per unit ground surface area. This parameter is crucial for various environmental applications:
  
- Plant Growth and Health: LAI serves as an indicator of plant growth and health, with higher values indicating healthy, dense vegetation, and lower values suggesting sparse or stressed vegetation. This makes LAI essential for assessing crop health and yield.
- Photosynthetic Capacity: LAI is directly related to the photosynthetic capacity of plant canopies, affecting the amount of sunlight plants capture for photosynthesis and influencing the carbon uptake of ecosystems.
- Water Balance: LAI impacts transpiration rates and the overall water balance of plants, which in turn affects local and regional hydrology.
- Climate Modeling: LAI plays a role in simulating energy exchange between the land surface and the atmosphere in climate models. It influences albedo, evapotranspiration rates, and canopy conductance, critical for accurate weather and climate predictions.
- Large-Scale Monitoring: High-resolution optical satellite images, such as Sentinel-2 and LANDSAT, can estimate LAI, allowing for large-scale monitoring of vegetation across different landscapes and time periods.

This API estimates leaf area index for a whole Sentinel-2 scene using a deep neural network.

The API is available on [LAI API](http://lai-api-test.dev.apps.eo4eu.eu/)

### LAI API Endpoints

`POST api/v1/lai/process`

`GET api/v1/lai/process`

`GET api/v1/task/status`

## Segment Anything API

The Segment Anything Model (SAM) is a cutting-edge deep learning model developed by Meta AI that is designed for image segmentation tasks. Image segmentation is the process of partitioning an image into multiple segments or regions, often to simplify or change the representation of an image into something more meaningful and easier to analyze.

- Generalization: SAM is designed to generalize well across a wide variety of images and objects without the need for task-specific fine-tuning.
- Zero-Shot Learning: SAM can perform segmentation tasks on new, unseen images without requiring additional training, making it highly versatile.
- Interactive Segmentation: Users can provide prompts such as points, boxes, or masks to guide the segmentation process interactively.
- Foundation Model: SAM serves as a foundation model that can be adapted for various downstream segmentation tasks with minimal effort.
- Large-Scale Training: SAM is trained on a vast and diverse dataset of images, which enhances its ability to handle a wide range of segmentation challenges.
- Efficiency and Versatility: SAM’s ability to perform zero-shot segmentation means it can be applied to a variety of tasks without the need for extensive task-specific training, saving time and computational resources.
- Broad Applicability: SAM can be used in numerous fields, including medical imaging, autonomous driving, robotics, augmented reality, and more. This makes it a highly valuable tool across industries.
- Improved Accessibility: By enabling interactive segmentation, SAM allows users, even those without extensive technical expertise, to segment images accurately and efficiently.
- Foundation for Further Research: SAM can serve as a robust baseline for researchers developing new segmentation models or applications, fostering innovation and advancement in the field of computer vision.
- Enhanced Performance: SAM's large-scale training and ability to generalize across diverse datasets contribute to its high performance, making it a reliable tool for complex segmentation tasks.

The API of SAM is available on [SAM API](http://sam-api-test.dev.apps.eo4eu.eu)

### SAM API Endpoints

`POST /api/v1/prompt`

`GET /api/v1/prompt`

`POST /api/v1/automatic`

`GET /api/v1/automatic`

`GET /api/v1/task/status`

## Object Detection API

Object detection in remote sensing involves identifying and locating specific objects within images captured by satellite or aerial platforms. These objects can range from buildings, vehicles, and roads to natural features like trees, water bodies, and agricultural fields. Object detection leverages advanced algorithms, often powered by machine learning and deep learning, to analyze vast amounts of remote sensing data efficiently.

- Air Traffic and Infrastructure: Detects planes, helicopters, airports, and helipads to monitor air traffic, infrastructure development, and their impact on noise pollution and local ecosystems.
- Maritime Traffic and Pollution: Identifies ships and harbors to track maritime traffic, assess port activities, monitor pollution, and manage coastal resources.
- Industrial Monitoring: Identifies storage tanks to monitor industrial areas, potential pollution sources, and manage hazardous materials.
- Transportation and Traffic Patterns: Detects large and small vehicles and roundabouts to monitor traffic patterns and plan transportation infrastructure.
- Infrastructure Maintenance: Identifies bridges to inspect infrastructure, assess connectivity, and evaluate the impact of natural disasters.
- Urban Green Spaces: Detects recreational facilities such as baseball diamonds, tennis courts, basketball courts, ground-track fields, soccer fields, and swimming pools to monitor urban green spaces.
- Economic Activities: Identifies container cranes at ports to monitor economic activities.

The object detection API is available on [Object detection API](http://od-api-test.dev.apps.eo4eu.eu)

### Endpoints

`POST api/v1/yolov8/obb/detect`

`GET api/v1/yolov8/obb/detect`

`GET api/v1/task/status`
