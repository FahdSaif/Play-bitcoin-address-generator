# Bitcoin Address Generator

## Overview

This project demonstrates a Bitcoin address generation tool. The program allows users to generate Bitcoin addresses using Python. It can be useful for developers working with Bitcoin transactions or creating wallets.

## Requirements

- Python 3.x
- Docker (optional, for containerization)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FahdSaif/bitcoin-address-generator.git


Navigate to the project directory:
cd bitcoin-address-generator

Install dependencies:
pip install -r requirements.txt

(Optional) Build and run using Docker:
docker build -t bitcoin-address-generator .
docker run -d bitcoin-address-generator

Code Explanation
generate_address.py
The Python script contains the logic for generating Bitcoin addresses. It uses cryptographic techniques to generate valid Bitcoin public and private keys and then derives the corresponding address.

Dockerfile
The Dockerfile sets up the environment to run the Bitcoin address generator using Docker. It pulls the base Python image, installs necessary dependencies, and executes the generate_address.py script.

Usage
To generate a Bitcoin address, simply run the Python script:
python generate_address.py

Alternatively, if you prefer using Docker, you can build and run the container as follows:
docker build -t bitcoin-address-generator .
docker run bitcoin-address-generator
