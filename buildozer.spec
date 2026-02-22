[app]
# (str) Title of your application
title = Your App Title

# (str) Package name
package.name = org.test.YourApp

# (str) Source files
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Version of your application
version = 0.1

# (str) Supported orientation (one of: landscape, sensorLandscape, portrait, sensorPortrait, all)
orientation = all

# (bool) Android persistent application
android.persistent = True

# (str) Minimum API requirement
android.minapi = 21

# (str) Android SDK version
android.sdk = 30

# (str) Target Android version
android.target = 30

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE