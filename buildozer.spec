[app]
title = Qubits App
package.name = qubitsapp
package.domain = org.qubits
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Added android and pyjnius here
requirements = python3,kivy,android,pyjnius

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Added internet permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

archs = arm64-v8a
api = 33
minapi = 21
ndk = 25b
accept_sdk_license = True
