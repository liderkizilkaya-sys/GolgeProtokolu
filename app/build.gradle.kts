plugins {
    id("com.android.application")
}

android {
    namespace = "com.golgeprotokolu.game"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.golgeprotokolu.game"
        minSdk = 23
        targetSdk = 36
        versionCode = 1
        versionName = "1.0.0"
    }

    val ksPath = System.getenv("GP_KEYSTORE_PATH")
    val ksStorePass = System.getenv("GP_KEYSTORE_PASSWORD")
    val ksAlias = System.getenv("GP_KEY_ALIAS")
    val ksKeyPass = System.getenv("GP_KEY_PASSWORD")

    signingConfigs {
        if (!ksPath.isNullOrBlank() && !ksStorePass.isNullOrBlank() && !ksAlias.isNullOrBlank() && !ksKeyPass.isNullOrBlank()) {
            create("release") {
                storeFile = file(ksPath)
                storePassword = ksStorePass
                keyAlias = ksAlias
                keyPassword = ksKeyPass
            }
        }
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            if (signingConfigs.names.contains("release")) {
                signingConfig = signingConfigs.getByName("release")
            }
        }
    }
}
