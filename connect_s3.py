
import os
import boto.s3.connection
from boto.s3.bucketlistresultset import *

class Env:
    __evn_dist = os.environ

    @staticmethod
    def judge_env(env, message):
        env_value = Env.__evn_dist.get(env)
        if env_value is None:
            raise RuntimeError(message + env)

        return env_value


class ConnectS3(object):
    def __init__(self, bucket, model_key, model_dir):
        self.conn = boto.connect_s3(
            aws_access_key_id = Env.judge_env("S3_ACCESS_KEY", "s3_access_key"),
            aws_secret_access_key = Env.judge_env("S3_SECRET_KEY", "s3_secret_key"),
            host = Env.judge_env("S3_HOST", "s3_host"),
            port = int(Env.judge_env("S3_PORT", "s3_port")),
            is_secure=False,  # uncomment if you are not using ssl
            calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

        self.model_key = model_key
        self.model_dir = model_dir
        self.bucket = self.conn.get_bucket(bucket)

        # get model data
        self.set_model_data()

    def set_model_data(self):
        prefix = self.model_key + "/"
        for key in bucket_lister(self.bucket, prefix=prefix):
            file_key = self.bucket.get_key(key.name)
            file_name = self.get_last(key.name)
            file_key.get_contents_to_filename(self.model_dir + "/" + file_name)


    def get_last(self, data):
        key_path = data.split("/")
        key_len = len(key_path)
        if key_len > 1:
            return key_path[key_len - 1]

        return None

    def get_version(self):
        key_path = self.model_key.split("/")
        key_len = len(key_path)
        if key_len > 1:
            return key_path[1]

        return None

#s3 = ConnectS3('kubeflow-anonymous-test', "test/2019-12-16T15-47-38Z/test", None,'test/2019-12-16T17-43-41Z/network')