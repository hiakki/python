import boto3
import json

from botocore.exceptions import ClientError


def get_secret():
    secret_name = "pow-secrets"
    region_name = "ap-southeast-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            print("The requested secret " + secret_name + " was not found")
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            print("The request was invalid due to:", e)
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            print("The request had invalid params:", e)
        elif e.response['Error']['Code'] == 'DecryptionFailure':
            print("The requested secret can't be decrypted using the provided KMS key:", e)
        elif e.response['Error']['Code'] == 'InternalServiceError':
            print("An error occurred on service side:", e)
    else:
        # print(get_secret_value_response)

        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of these fields will be populated
        # if 'SecretString' in get_secret_value_response:
        #     text_secret_data = get_secret_value_response['SecretString']
        #     print(text_secret_data)
        #     c = text_secret_data.replace(':"',': "')
        #     d = c.replace('"{','{')
        #     e = d.replace('}"','}')
        #     with open('testing.json','w') as file:
        #         file.write(e)
        #     with open('testing.json','r') as file:
        #         secrets = json.load(file)
        #     port = secrets['PORT']
        #     print(port)
        # else:
        #     binary_secret_data = get_secret_value_response['SecretBinary']
        #     # print(binary_secret_data)
        print(type(get_secret_value_response))
        secretstring = get_secret_value_response['SecretString'].replace()
        print(secretstring)
        port = secretstring['PORT']
        print(port)


get_secret()





IPtoBlock = event['detail']['service']['action']['networkConnectionAction']['remoteIpDetails']['ipAddressV4'] ### INDEX INTO THE 'ipAddressV4'

{
    "version": "0",
    "id": "f8439d17-dddf-7d2a-491c-26e76860c6df",
    "detail-type": "GuardDuty Finding",
    "source": "aws.guardduty",
    "account": "123456789012",
    "time": "fakeConstruct",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "schemaVersion": "2.0",
        "accountId": "123456789012",
        "region": "us-east-1",
        "partition": "aws",
        "id": "redacted",
        "arn": "redacted",
        "type": "UnauthorizedAccess:EC2/MaliciousIPCaller.Custom",
        "service": {
            "serviceName": "guardduty",
            "detectorId": "redacted",
            "action": {
                "actionType": "NETWORK_CONNECTION",
                "networkConnectionAction": {
                    "connectionDirection": "UNKNOWN",
                    "remoteIpDetails": {
                        "ipAddressV4": "1.1.1.1"
                    }
                }
            }
        }
    }
}