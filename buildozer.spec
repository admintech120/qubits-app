[app]
title = Qubits App
package.name = qubitsapp
package.domain = org.qubits
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
archs = arm64-v8a
api = 31
minapi = 21
sdk_build_tools_version = 30.0.3
accept_sdk_license = True
ndk = 25b
