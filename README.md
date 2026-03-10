# ParkIt – Parking Detection Module

## Overview

This repository contains the **parking detection component** of the **ParkIt Smart Parking** project.

The system detects vehicles in parking lots and determines which parking spaces are **occupied or free**. The results are used by the ParkIt website to display the **number of available parking spots for each parking area registered in the system**.

This implementation is currently a **functional prototype**.

---

## Detection Method

Vehicle detection is performed using **YOLOv8**.

The model was trained using:

* a **public parking/vehicle dataset**
* a **custom dataset** created from images of the parking areas used in the project

The custom dataset helps improve detection accuracy for the **specific parking layouts and camera angles**.

---

## Features

* Vehicle detection in parking areas
* Identification of **free and occupied parking spaces**
* Detection of **incorrect parking**, such as:

  * cars occupying multiple spaces
  * cars partially blocking adjacent spots

---

## Technologies Used

* **Python**
* **YOLOv8 (Ultralytics)**
* Several **Python scripts** used for:

  * training the model
  * testing detection results
  * integrating the detection logic

---

## Project Status

The detection system is implemented as a **working prototype**, designed to demonstrate the concept of automated parking space monitoring.

---

## Contribution

My work in this project focused on:

* training the **YOLOv8 detection model**
* creating and integrating a **custom dataset**
* implementing the **vehicle detection logic**
* developing Python scripts for **testing and experimentation**
