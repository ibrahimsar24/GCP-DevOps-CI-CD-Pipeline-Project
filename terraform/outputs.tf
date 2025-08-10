output "gke_cluster_name" {
  description = "Name of the GKE cluster"
  value       = google_container_cluster.primary.name
}

output "gke_endpoint" {
  description = "GKE cluster endpoint"
  value       = google_container_cluster.primary.endpoint
}

output "gke_master_version" {
  description = "Kubernetes master version"
  value       = google_container_cluster.primary.initial_cluster_version
}
