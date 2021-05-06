import s3fs
import os
import pandas as pd

s3 = s3fs.S3FileSystem(
	anon=False, 
	key = os.environ["AWS_PUBLIC_KEY"],
	secret = os.environ["AWS_SECRET_KEY"])

def load_dataframe(filepath):
	"""
	Loads a dataframe from s3 and returns a dataframe
	"""
	with s3.open(filepath, 'rb') as f:
		df = pd.read_csv(f)
	return df

df = load_dataframe('bucket/file.csv')
