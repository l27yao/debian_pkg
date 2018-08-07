workspace(name = "experiment")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1fb58b32f4bf26fc64313c6d1d5dc415579be0eb3411e8845df72c699958fc1",
    strip_prefix = "rules_docker-090f1e6214dcfa34a48b1440c97df4e9721fb921",
    urls = ["https://github.com/bazelbuild/rules_docker/archive/090f1e6214dcfa34a48b1440c97df4e9721fb921.tar.gz"],
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
    container_repositories = "repositories",
)

container_repositories()

container_pull(
    name = "ubuntu16_04",
    digest = "sha256:9f9775c124417057fd58d28835b42b30f5d0410530256d857b12eae640d0a359",
    registry = "l.gcr.io",
    repository = "google/ubuntu16_04",
)

http_archive(
    name = "base_images_docker",
    sha256 = "182572f7a2c3a34879e8e3f66e5f9ad829cc620bf2c8e6e18c384aae3cd11863",
    strip_prefix = "base-images-docker-5530512a9e27f4dd76848a6b40ce2b2b23a87ece",
    urls = ["https://github.com/GoogleCloudPlatform/base-images-docker/archive/5530512a9e27f4dd76848a6b40ce2b2b23a87ece.tar.gz"],
)

load("//:gcs.bzl", "gcs_file")

gcs_file(
    name = "ubuntu16_04_debian_pkgs",
    file = "ubuntu16-04-debian_pkgs.tar",
    bucket = "gs://rbe-toolchain-debs",
    sha256 = "ef442b29630142062177527786c60d9bed9485d6dcc549ba71c095a956566620",
)