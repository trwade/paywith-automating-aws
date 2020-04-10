import boto3
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    'Webotron deploys websites to AWS'
    pass

@cli.command('list-buckets')
def list_buckets():
    '''List all s3 buckets in an account'''
    for b in s3.buckets.all():
        print(b)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    'List objects in an s3 bucket'
    for obj in s3.Bucket(bucket).objects.all():
        print (obj)

if __name__ == '__main__':
    cli()
