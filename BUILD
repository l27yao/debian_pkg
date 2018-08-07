licenses(["notice"])  # Apache 2.0

package(default_visibility = ["//visibility:public"])

load("@base_images_docker//package_managers:download_pkgs.bzl", "download_pkgs")

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
)

download_pkgs(
    name = "debian_pkgs",
    image_tar = "@ubuntu16_04//image",
    packages = [
        "libstdc++-4.9-dev",
        "ca-certificates-java",
        "openjdk-8-jdk-headless",
        "openjdk-8-jre-headless",
        "python-dev",
        "python-setuptools",
        "python3-dev",
        "binutils",
        "ca-certificates",
        "curl",
        "ed",
        "file",
        "git",
        "less",
        "locales",
        "locales-all",
        "netcat",
        "openssh-client",
        "patch",
        "unzip",
        "wget",
        "zip",
    ],
)

container_image(
    name = "my_ubuntu16_04",
    base = "@ubuntu16_04//image",
    cmd = [
        "/bin/sh",
        "-c",
        "/bin/bash",
    ],
    files = ["@ubuntu16_04_debian_pkgs//file"],
)
