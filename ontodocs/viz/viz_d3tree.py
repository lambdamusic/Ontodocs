# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
#
#
# ==================
# VIZ D3 Tree - a d3 dendogram
# ==================


import os, sys
import json

from ..core import *
from ..core.utils import *
from ..core.builder import *  # loads and sets up Django
from ..core.viz_factory import VizFactory





class D3TreeViz(VizFactory):
    """
    D3 viz tree

    """


    def __init__(self, ontospy_graph, title=""):
        """
        Init
        """
        super(D3TreeViz, self).__init__(ontospy_graph, title)
        self.static_files = ["libs/d3-v2", "libs/jquery"]


    def _buildTemplates(self):
        """
        OVERRIDING THIS METHOD from Factory
        """


        c_mylist = build_D3treeStandard(0, 99, 1, self.ontospy_graph.toplayer)
        p_mylist = build_D3treeStandard(0, 99, 1, self.ontospy_graph.toplayerProperties)
        s_mylist = build_D3treeStandard(0, 99, 1, self.ontospy_graph.toplayerSkosConcepts)

        c_total = len(self.ontospy_graph.classes)
        p_total = len(self.ontospy_graph.properties)
        s_total = len(self.ontospy_graph.skosConcepts)


        if False:
            # testing how a single tree would look like
            JSON_DATA_CLASSES = json.dumps(
            {'children' :
                [ {'children' : c_mylist, 'name' : 'Classes', 'id' : "classes" },
                {'children' : p_mylist, 'name' : 'Properties', 'id' : "properties" },
                {'children' : s_mylist, 'name' : 'Concepts', 'id' : "concepts" }],
                'name' : 'Entities', 'id' : "root"
                }
                )

        # hack to make sure that we have a default top level object
        JSON_DATA_CLASSES = json.dumps({'children' : c_mylist, 'name' : 'owl:Thing', 'id' : "None" })
        JSON_DATA_PROPERTIES = json.dumps({'children' : p_mylist, 'name' : 'Properties', 'id' : "None" })
        JSON_DATA_CONCEPTS = json.dumps({'children' : s_mylist, 'name' : 'Concepts', 'id' : "None" })

    #
	# c = Context({
	# 				"ontology": ontology,
	# 				"main_uri" : uri,
	# 				"STATIC_PATH": ONTODOCS_VIZ_STATIC,
	# 				"save_on_github" : save_on_github,
	# 				"classes": graph.classes,
	# 				"classes_TOPLAYER": len(graph.toplayer),
	# 				"properties": graph.properties,
	# 				"properties_TOPLAYER": len(graph.toplayerProperties),
	# 				"skosConcepts": graph.skosConcepts,
	# 				"skosConcepts_TOPLAYER": len(graph.toplayerSkosConcepts),
	# 				"TOTAL_CLASSES": c_total,
	# 				"TOTAL_PROPERTIES": p_total,
	# 				"TOTAL_CONCEPTS": s_total,
	# 				'JSON_DATA_CLASSES' : JSON_DATA_CLASSES,
	# 				'JSON_DATA_PROPERTIES' : JSON_DATA_PROPERTIES,
	# 				'JSON_DATA_CONCEPTS' : JSON_DATA_CONCEPTS,
	# 			})
    #
    #

        extra_context = {
                        "ontograph": self.ontospy_graph,
    					"TOTAL_CLASSES": c_total,
    					"TOTAL_PROPERTIES": p_total,
    					"TOTAL_CONCEPTS": s_total,
    					'JSON_DATA_CLASSES' : JSON_DATA_CLASSES,
    					'JSON_DATA_PROPERTIES' : JSON_DATA_PROPERTIES,
    					'JSON_DATA_CONCEPTS' : JSON_DATA_CONCEPTS,
                        }

        # Ontology - MAIN PAGE
        contents = self._renderTemplate("d3/d3tree.html", extraContext=extra_context)
        FILE_NAME = "index.html"
        main_url = self._save2File(contents, FILE_NAME, self.output_path)

        return main_url




# if called directly, for testing purposes pick a random ontology

if __name__ == '__main__':

    TEST_ONLINE = False
    try:

        g = get_onto_for_testing(TEST_ONLINE)

        v = D3TreeViz(g, title="")
        v.build()
        v.preview()

        sys.exit(0)

    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
