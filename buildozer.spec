[app]
# THE APP IDENTITY
title = Learn It
package.name = learnit.app
package.domain = org.learnit
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 13.5.2

# REQUIREMENTS (Must include Kivy and any logic libraries)
requirements = python3,kivy,kivymd,requests,jnius

# PERMISSIONS
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# SETTINGS
orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
