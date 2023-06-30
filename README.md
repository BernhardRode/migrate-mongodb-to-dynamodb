# Project Name

Short description of your project.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Introduction

Provide a brief introduction to your project. Explain what it does and why it is useful.

## Prerequisites

- Python 3.x
- MongoDB
- AWS Account with DynamoDB

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
```

2. Change to the project directory:

```bash
cd your_project
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate # macOS/Linux
env\Scripts\activate # Windows
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt

```

## Configuration

Configure the project by setting the following environment variables:

- `MONGO_URI`: The MongoDB connection URI. Default: `mongodb://localhost:27017`
- `MONGO_DB_NAME`: The name of your MongoDB database. Default: `your_database_name`
- `MONGO_COLLECTION_NAME`: The name of the MongoDB collection. Default: `your_collection_name`
- `AWS_REGION`: The AWS region where your DynamoDB table is hosted. Default: `us-east-1`
- `DYNAMODB_TABLE_NAME`: The name of your DynamoDB table. Default: `your_table_name`

If you prefer to use a `.env` file to load the environment variables, create a file named `.env` in the project directory and populate it with your desired values.

## Usage

1. Make sure your MongoDB instance is running locally.

2. Run the script:


```bash
pip install -r requirements.txt

```

This script connects to your local MongoDB database, iterates over all documents in the specified collection, and writes them to your DynamoDB table on AWS.

3. Check your DynamoDB table to verify that the documents have been successfully written.

## License

[MIT License](LICENSE)
