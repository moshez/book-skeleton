# Copyright (c) Moshe Zadka
# See LICENSE for details.

extensions = []
master_doc = 'index'
project = 'from python import better'
copyright = 'Copyright (c) 2018, Moshe Zadka'
author = 'Moshe Zadka'
version = '1.0'

latex_elements = dict(preamble='\usepackage{amsfonts}\n')

epub_cover = ('../_static/cover.png', '')

html_static_path = ['../_static']

epub_theme = 'epub'

epub_toc_depth = 1

