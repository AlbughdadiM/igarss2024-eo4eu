# Examples of Processing APIs in EO4EU

In this chapter, we will go through some of the APIs available via the EO4EU platform that will be used in the practical use cases.

## Sentinel-2 API

Sentinel-2 is a part of the European Space Agency's (ESA) Copernicus Program, which aims to provide comprehensive Earth observation data. It specifically refers to two satellites, Sentinel-2A and Sentinel-2B, which work in tandem to provide high-resolution optical imagery for land monitoring.

### Key Features of Sentinel-2

- High-Resolution Imagery: Sentinel-2 satellites provide images at various resolutions ranging from 10 meters to 60 meters.
- Multispectral Imaging: They carry a multispectral imager with 13 spectral bands, covering visible, near-infrared, and shortwave infrared wavelengths.
Wide Swath Width: Each satellite has a swath width of 290 kilometers, allowing for large areas of the Earth's surface to be imaged in a single pass.
- High Revisit Frequency: The two satellites together provide a revisit time of approximately five days at the equator, ensuring up-to-date imagery.
  
### Importance of Sentinel-2

- Environmental Monitoring: Sentinel-2 data is crucial for monitoring various environmental parameters, including land cover changes, forest health, and agricultural productivity.
- Agriculture: Farmers and agricultural planners use Sentinel-2 imagery to monitor crop health, plan irrigation, and manage agricultural practices more efficiently.
- Disaster Management: In the event of natural disasters such as floods, wildfires, and hurricanes, Sentinel-2 provides timely data that helps in assessing damage and planning response strategies.
- Climate Change Studies: The data from Sentinel-2 contributes to understanding and modeling the effects of climate change on land surfaces, vegetation, and water bodies.
- Urban Planning and Land Use: Urban planners and policymakers use the high-resolution imagery to monitor urban sprawl, plan infrastructure development, and manage natural resources.
- Biodiversity and Conservation: Sentinel-2 helps in tracking habitat changes, protecting biodiversity, and managing conservation efforts effectively.
- Water Quality Monitoring: The multispectral capabilities allow for the assessment of water bodies, detecting changes in water quality and aiding in the management of water resources.

This API allows processing and downloading Sentinel-2 data for an ROI or a full Sentinel-2 tile.

The API is available on [Sentinel-2 API](http://sentinel-api-test.dev.apps.eo4eu.eu/)

### Endpoints

`POST api/v1/s2l2a/roi/process`

RGB, NDVI, LAI, Band combination

`GET api/v1/s2l2a/roi/process`

`POST api/v1/s2l2a/tile/process`

Band combination

`GET api/v1/s2l2a/tile/process`

`GET api/v1/task/status`

## Leaf Area Index API

Leaf Area Index (LAI) is a crucial biophysical parameter that measures the total leaf area per unit ground area. It is typically expressed as a dimensionless ratio, representing the one-sided green leaf area in square meters per square meter of ground area (m²/m²). LAI is used to quantify the amount of leaf material in plant canopies and is essential for understanding various ecological and agricultural processes.

### Key Features of LAI

- Dimensionless Ratio: LAI is a unitless measure, as it is a ratio of areas.
- Canopy Density Indicator: LAI provides an indication of the density and structure of plant canopies, which is vital for understanding plant health and productivity.
  
### Importance of LAI

- Photosynthesis and Growth: LAI is directly related to the photosynthetic capacity of plants. A higher LAI typically indicates a greater leaf area available for photosynthesis, leading to increased plant growth and productivity.
- Evapotranspiration and Water Use: LAI influences the rate of transpiration and evaporation from the plant canopy. It helps in modeling water use and understanding the water balance in ecosystems.
- Carbon Cycle: LAI is a critical parameter in carbon cycle models as it affects the amount of carbon dioxide that plants absorb from the atmosphere during photosynthesis.
- Climate Models: LAI data is used in climate models to predict how vegetation interacts with the atmosphere, including the exchange of gases and energy, which affects climate patterns.
- Agricultural Management: Farmers and agronomists use LAI to monitor crop health, optimize planting densities, and manage inputs like water and nutrients more efficiently.
- Forest and Vegetation Management: LAI is used in forest management to assess forest density, health, and growth rates. It helps in making decisions regarding thinning, harvesting, and conservation practices.
- Remote Sensing Applications: Satellite sensors, such as those on Sentinel-2, can estimate LAI over large areas, providing valuable data for monitoring vegetation changes at regional to global scales.

This API estimates leaf area index for a whole Sentinel-2 scene using a deep neural network.

The API is available on [LAI API](http://lai-api-test.dev.apps.eo4eu.eu/)

### Endpoints

`POST api/v1/lai/process`

`GET api/v1/lai/process`

`GET api/v1/task/status`

## Segment Anything API

The Segment Anything Model (SAM) is a cutting-edge deep learning model developed by Meta AI that is designed for image segmentation tasks. Image segmentation is the process of partitioning an image into multiple segments or regions, often to simplify or change the representation of an image into something more meaningful and easier to analyze.

### Key Features of the Segment Anything Model (SAM)

- Generalization: SAM is designed to generalize well across a wide variety of images and objects without the need for task-specific fine-tuning.
- Zero-Shot Learning: SAM can perform segmentation tasks on new, unseen images without requiring additional training, making it highly versatile.
- Interactive Segmentation: Users can provide prompts such as points, boxes, or masks to guide the segmentation process interactively.
- Foundation Model: SAM serves as a foundation model that can be adapted for various downstream segmentation tasks with minimal effort.
- Large-Scale Training: SAM is trained on a vast and diverse dataset of images, which enhances its ability to handle a wide range of segmentation challenges.
  
### Importance of SAM

- Efficiency and Versatility: SAM’s ability to perform zero-shot segmentation means it can be applied to a variety of tasks without the need for extensive task-specific training, saving time and computational resources.
- Broad Applicability: SAM can be used in numerous fields, including medical imaging, autonomous driving, robotics, augmented reality, and more. This makes it a highly valuable tool across industries.
- Improved Accessibility: By enabling interactive segmentation, SAM allows users, even those without extensive technical expertise, to segment images accurately and efficiently.
- Foundation for Further Research: SAM can serve as a robust baseline for researchers developing new segmentation models or applications, fostering innovation and advancement in the field of computer vision.
- Enhanced Performance: SAM's large-scale training and ability to generalize across diverse datasets contribute to its high performance, making it a reliable tool for complex segmentation tasks.

The API of SAM is available on [SAM API](http://sam-api-test.dev.apps.eo4eu.eu)

### Endpoints

`POST /api/v1/prompt`

`GET /api/v1/prompt`

`POST /api/v1/automatic`

`GET /api/v1/automatic`

`GET /api/v1/task/status`

## Object Detection API

Object detection in remote sensing involves identifying and locating specific objects within images captured by satellite or aerial platforms. These objects can range from buildings, vehicles, and roads to natural features like trees, water bodies, and agricultural fields. Object detection leverages advanced algorithms, often powered by machine learning and deep learning, to analyze vast amounts of remote sensing data efficiently.

### Key Features of Object Detection in Remote Sensing

- High Spatial Resolution: Remote sensing technologies provide high-resolution images that allow for the detection of small and detailed objects.
- Multispectral and Hyperspectral Imaging: These technologies capture data across various wavelengths, enhancing the ability to distinguish between different types of objects.
- Automated Analysis: Advanced algorithms can automatically process large datasets, identifying and categorizing objects with high accuracy and speed.
- Scalability: Object detection systems can handle images covering extensive geographic areas, making it feasible to monitor large regions consistently.
  
### Importance of Object Detection in Remote Sensing

- Environmental Monitoring: Detecting changes in natural environments, such as deforestation, desertification, and wetland degradation, helps in managing and protecting ecosystems.
- Urban Planning: Accurate detection of buildings, roads, and other infrastructure supports effective urban planning and development, ensuring sustainable growth.
- Disaster Management: In the aftermath of natural disasters like earthquakes, floods, and hurricanes, object detection helps in assessing damage, locating survivors, and planning recovery efforts.
- Agriculture: Identifying crop types, assessing crop health, and monitoring land use changes aid in improving agricultural practices and ensuring food security.
- Security and Defense: Detecting and monitoring military assets, illegal activities (such as smuggling or unauthorized deforestation), and strategic installations enhance national security and defense operations.

The object detection API is available on [Object detection API](http://od-api-test.dev.apps.eo4eu.eu)

### Endpoints

`POST api/v1/yolov8/obb/detect`

`GET api/v1/yolov8/obb/detect`

`GET api/v1/task/status`
