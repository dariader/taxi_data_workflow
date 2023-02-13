locals {
  data_lake_bucket = "dtc_data_lake"
  project = "taxiworkflow"
  ml_files_dir = "./working_with_ml/fhv/fhv_parq/"
  gcs_bucket = "${local.data_lake_bucket}_${local.project}"
}

variable "project" {
  description = "taxiworkflow"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "europe-west6"
  type        = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type        = string
  default     = "trips_data_all"
}
