# Arabic, Azerbaijani, Chinese, Dutch, English, Finnish, French, German, 
# Hindi, Hungarian, Indonesian, Irish, Italian, Japanese, Korean, Polish, 
# Portuguese, Russian, Spanish, Swedish, Turkish, Ukranian, Vietnamese

import argostranslate.package, argostranslate.translate
import os
import json
import glob

def translate(text,from_code = 'en', to_code = 'es'):
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
	translatedText = translation.translate(text)
	return translatedText


PROJECT_ROOT = os.path.abspath(os.path.join(os.getcwd(), '..', '..', '..'))
english_lang_dir = os.path.join(PROJECT_ROOT, 'public', 'locales', 'en')

json_files = '{0}/*.json'.format(english_lang_dir)
# print(json_files)

def deep_merge(source, destination):
    """
    run me with nosetests --with-doctest file.py

    >>> a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    >>> b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    >>> deep_merge(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
    True
    """
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value

    return destination

def transform_json(data, from_code, to_code):
	for key,value in data.items():
		if isinstance(value, str):
			data[key] = translate(value, from_code, to_code)
			# print('{0} ---> {1}'.format(str(key), translate(value)))
		if isinstance(value, dict):
			transform_json(value, from_code, to_code)
		elif isinstance(value, list):
			for val in value:
				if isinstance(val, str):
					pass
				elif isinstance(val, list):
					pass
				else:
					transform_json(val, from_code, to_code)

def traverse_file(from_code, to_code):
	for filename in glob.glob(json_files):
		target_filename = filename.replace('/{}/'.format(from_code), '/{}/'.format(to_code))
		is_target_file_not_empty = os.path.exists(target_filename) and os.path.getsize(target_filename) != 0
		data_set1, data_set2, output_data = None, None, None

		with open(filename) as f:
			f = open(filename)
			data_set1 = json.load(f)
			transform_json(data_set1, from_code, to_code)

		target_folder = os.path.dirname(target_filename)
		if not os.path.exists(target_filename):
			if not os.path.exists(target_folder):
				os.makedirs(target_folder)
		
		if is_target_file_not_empty:
			with open(target_filename, 'r') as f:
				data_set2 = json.load(f)
		else:
			data_set2 = {}
		
		output_data = deep_merge(data_set2, data_set1)

		with open(target_filename, 'w+') as f:
			json_object = json.dumps(output_data, indent=2)
			f.write(json_object)
		

def main():
	"""
	List of languages that can be installed:
	------

	languages = ['ar','az','zh','cs','da','nl','eo','fi','fr','de','el','he','hi','hu','id','ga','it','ja','ko','fa','pl','pt','ru','sk','es','sv','tr','uk']
	"""
	from_code= 'en'
	languages = ['ar', 'de','es','fr','it','zh', 'hi']
	for language in languages:
		traverse_file(from_code, language)
	

main()