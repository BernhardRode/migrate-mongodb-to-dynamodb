import os
import pymongo
import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MongoDB Configuration
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
mongo_db_name = os.environ.get('MONGO_DB_NAME', 'your_database_name')
mongo_collection_name = os.environ.get('MONGO_COLLECTION_NAME', 'your_collection_name')

# DynamoDB Configuration
aws_region = os.environ.get('AWS_REGION', 'us-east-1')
dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME', 'your_table_name')

# Connect to the local MongoDB instance
mongo_client = pymongo.MongoClient(mongo_uri)
mongo_db = mongo_client[mongo_db_name]
mongo_collection = mongo_db[mongo_collection_name]

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name=aws_region)
dynamodb_table = dynamodb.Table(dynamodb_table_name)

# Count number of documents in MongoDB
mongo_doc_count = mongo_collection.count_documents({})
logger.info(f"Number of documents in MongoDB: {mongo_doc_count}")

# Delete all items in the DynamoDB table
dynamodb_table.scan().delete()

# Iterate over all documents in the collection
for document in mongo_collection.find():
    # Here, you can perform any required transformations or manipulations on the document
    # before writing it to DynamoDB

    # Write the document to DynamoDB
    dynamodb_table.put_item(Item=document)

# Count number of documents in DynamoDB
dynamodb_response = dynamodb_table.scan()
dynamodb_doc_count = dynamodb_response['Count']
logger.info(f"Number of documents in DynamoDB: {dynamodb_doc_count}")

# Close the MongoDB connection
mongo_client.close()
