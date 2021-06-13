from datetime import datetime, timedelta
now = datetime.now()
one_day_ago = now - timedelta(days = 1)
one_day_ago = one_day_ago.strftime('%d')
year = now.strftime("%Y")
month = now.strftime("%m")

### Configuration Robo Cadastro Nacional de Empresas Punidas

## GCP pointing ------------

# GCP project name
project = 'dev-data'

# GCP bucket name
bucket_name = 'bvs-bigdata-datalake-stage-external-cadastral-rf-dev'

# Blob path
zip_filename = "data.zip"

# File name to save data in GCP
filename = "cnep.csv"



## Scrap definitions ------------

# Download URL 
url =  'http://transparencia.gov.br/download-de-dados/cnep/'

# Headers necessarry to request the data
blob_path1 = 'datalake/stage/external/cadastral/rf/data/cnep/partitions/daily/' + str(year) + '/' + str(month) + '/'
blob_path2 = 'datalake/stage/external/cadastral/rf/data/cnep_log/partitions/daily/' + str(year) + '/' + str(month) + '/'



## File Names ------------

# file name to save logging information
log_filename = "cnep.log"

# File name to save the downloaded data
zip_filename = "data.zip"

# File name to save data in GCP
filename = "cnep.csv"



## Scrap definitions ------------

# Download URL 
url =  'http://transparencia.gov.br/download-de-dados/cnep/' + str(year) + str(month) + str(one_day_ago)

# Headers necessarry to request the data
# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'} 

# Boolean for request certification on data request
certif = False