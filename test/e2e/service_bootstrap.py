# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may
# not use this file except in compliance with the License. A copy of the
# License is located at
#
#	 http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""Bootstraps the resources required to run the Lambda integration tests.
"""

import os
import boto3
import logging
from time import sleep

from acktest import resources
from acktest.aws.identity import get_region, get_account_id
from e2e import bootstrap_directory
from e2e.bootstrap_resources import TestBootstrapResources
from botocore.exceptions import ClientError

RAND_TEST_SUFFIX = (''.join(random.choice(string.ascii_lowercase) for _ in range(6)))

LAMBDA_IAM_ROLE_NAME = 'ack-lambda-function-role-' + RAND_TEST_SUFFIX
LAMBDA_IAM_ROLE_POLICY = '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": '\
                                '"lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]} '
LAMBDA_BASIC_ROLE_ARN = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'

FUNCTIONS_BUCKET_NAME = "ack-lambda-function-s3-bucket-" + RAND_TEST_SUFFIX

LAMBDA_FUNCTION_FILE_PATH = "./resources/lambda_function/main.py"

def service_bootstrap() -> dict:
    logging.getLogger().setLevel(logging.INFO)
    create_function_role()
    create_functions_bucket()
    upload_function_to_bucket()

    return TestBootstrapResources(
        LAMBDA_IAM_ROLE_NAME,
        LAMBDA_IAM_ROLE_POLICY,
        LAMBDA_BASIC_ROLE_ARN,
        FUNCTIONS_BUCKET_NAME,
        LAMBDA_FUNCTION_FILE_PATH,
    ).__dict__


def create_function_role() -> str:
    region = get_region()
    iam_client = boto3.client("iam", region_name=region)

    logging.debug(f"Creating function iam role {LAMBDA_IAM_ROLE_NAME}")
    try:
        iam_client.get_role(RoleName=LAMBDA_IAM_ROLE_NAME)
        raise RuntimeError(f"Expected {LAMBDA_IAM_ROLE_NAME} role to not exist."
                           f" Did previous test cleanup successfully?")
    except iam_client.exceptions.NoSuchEntityException:
        pass

    resp = iam_client.create_role(
        RoleName=LAMBDA_IAM_ROLE_NAME,
        AssumeRolePolicyDocument=LAMBDA_IAM_ROLE_POLICY
    )
    iam_client.attach_role_policy(RoleName=LAMBDA_IAM_ROLE_NAME, PolicyArn=LAMBDA_BASIC_ROLE_ARN)
    return resp['Role']['Arn']

def create_functions_bucket():
    region = get_region()
    s3_client = boto3.resource('s3')
    logging.debug(f"Creating s3 data bucket {FUNCTIONS_BUCKET_NAME}")
    try:
        s3_client.create_bucket(
            Bucket=FUNCTIONS_BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
    except s3_client.exceptions.BucketAlreadyExists:
        raise RuntimeError(f"Expected {FUNCTIONS_BUCKET_NAME} bucket to not exist."
                           f" Did previous test cleanup successfully?")

def upload_function_to_bucket():
    object_name = os.path.basename(LAMBDA_FUNCTION_FILE_PATH)

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(
            LAMBDA_FUNCTION_FILE_PATH,
            FUNCTIONS_BUCKET_NAME,
            object_name,
        )
    except ClientError as e:
        logging.error(e)

if __name__ == "__main__":
    config = service_bootstrap()
    # Write config to current directory by default
    resources.write_bootstrap_config(config, bootstrap_directory)