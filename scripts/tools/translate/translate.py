# Arabic, Azerbaijani, Chinese, Dutch, English, Finnish, French, German, 
# Hindi, Hungarian, Indonesian, Irish, Italian, Japanese, Korean, Polish, 
# Portuguese, Russian, Spanish, Swedish, Turkish, Ukranian, Vietnamese

import argostranslate.package, argostranslate.translate

from_code = "en"
to_code = "es"

# Download and install Argos Translate package
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
download_path = available_package.download()
argostranslate.package.install_from_path(download_path)

# Translate
installed_languages = argostranslate.translate.get_installed_languages()
from_lang = list(filter(
	lambda x: x.code == from_code,
	installed_languages))[0]
to_lang = list(filter(
	lambda x: x.code == to_code,
	installed_languages))[0]
translation = from_lang.get_translation(to_lang)
translatedText = translation.translate("Hi my name is Arindam!")
print(translatedText)
# '¡Hola Mundo!'
