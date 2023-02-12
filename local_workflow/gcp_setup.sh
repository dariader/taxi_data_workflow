# create project on GCP, save key
export GOOGLE_APPLICATION_CREDENTIALS="/home/daria/Downloads/taxiworkflow-4cb511a2ae52.json"
gcloud auth application-default login
# Initialize state file (.tfstate)
terraform init
# Check changes to new infra plan
terraform plan -var="project=taxiworkflow"

# Create new infra
terraform apply -var="project=taxiworkflow"

# Delete infra after your work, to avoid costs on any running services
terraform destroy