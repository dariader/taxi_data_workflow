# Terraform notes

 #### How to load object in Cloud Storage:

```
resource "google_storage_bucket_object" "default" {
  name    = "test_fhv_files"
  # Uncomment and add valid path to an object.
  source = "./working_with_ml/fhv/test.csv.gz"
  # content      = "Data as string to be uploaded"
  content_type = "text/plain"
  bucket       = "${local.data_lake_bucket}_${local.project}"
}
```
To remove object simply remove this piece of configuration from `main.tf`


 #### How to upload a whole directory of files  using `gsutils`

in CLI
```commandline
gsutils config
gcloud auth login
gcloud config set project taxiworkflow
```
set variables in `variables.tf`:
```
locals {
  data_lake_bucket = "dtc_data_lake"
  project = "taxiworkflow"
  ml_files_dir = "./working_with_ml/fhv/"
  gcs_bucket = "${local.data_lake_bucket}_${local.project}"
}
```

in `main.tf`:
```commandline

# Load dir in Cloud Storage, to remove object simply remove configuration
resource "null_resource" "upload_folder_content" {

 triggers = {

   file_hashes = jsonencode({

   for fn in fileset(local.ml_files_dir, "**") :

   fn => filesha256("${local.ml_files_dir}/${fn}")

   })

 }

 provisioner "local-exec" {

   command = "gsutil cp -r ${local.ml_files_dir}/* gs://${local.gcs_bucket}/"

 }

}
```

It works by checking hash sum of the files in directory each time you run terraform apply and performs updates
