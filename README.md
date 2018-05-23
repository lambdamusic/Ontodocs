Ontodocs
=======================

Ontodocs is a Python command line application aimed at facilitating the creation of documentation for ontologies encoded in RDF/OWL.

#### Links

* [Pypi home](https://pypi.org/project/ontodocs/)
* [Github home](https://github.com/lambdamusic/ontodocs)

#### Examples

- [Schema.org](http://www.michelepasin.org/support/ontospy-examples/schema_org_topbraidttl/index.html) documentation.
- [FOAF](http://www.michelepasin.org/support/ontospy-examples/foafrdf/index.html) documentation.

That's the kind of documentation OntoDocs can generate out-of-the-box. For even more examples,  [take a look at this page](http://www.michelepasin.org/support/ontospy-examples/index.html).


Installation
------------

```
pip install ontodocs -U
```


Description
------------

Ontodocs allows to generate documentation for an RDF vocabulary, using visualization algorithms that create simple HTML pages, Markdown files, or more complex javascript interactive charts based on D3.js.

```
> Ontodocs -h
Usage: ontodocs [OPTIONS] [SOURCE]...

  Ontodocs allows to create  documentation for ontologies encoded in
  RDF/OWL.

  E.g.:

  > ontodocs http://www.w3.org/2008/05/skos# --theme random -o
  ~/Desktop/skos

  ==> generates html docs for the SKOS ontology and save it to your desktop

Options:
  -o, --outputpath TEXT  Output path (default: home folder).
  -t, --title TEXT       Title for the visualization (default=graph uri).
  --theme TEXT           CSS Theme for the html-complex visualization
                         (random=use a random theme).
  --showthemes           Show the available CSS theme choices.
  -v, --verbose          Verbose mode.
  -h, --help             Show this message and exit.
```

The library is not really meant to be used programmatically, but I'm sure there are a few constructs in there which can be reused.

In a nutshell, all visualizations inherit from a [VizFactory](https://github.com/lambdamusic/Ontodocs/blob/master/ontodocs/core/viz_factory.py) class that abstracts away the most common operations involved in rendering a dataviz.

This is how you would invoke a visualization from a script:

```
import ontospy
from ontodocs.viz.viz_html_single import *

g = ontospy.Ontospy("http://cohere.open.ac.uk/ontology/cohere.owl#")

v = HTMLVisualizer(g) # => instantiate the visualization object
v.build() # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser

```


Dependencies
---------------
Ontodocs relies on the [OntoSpy](https://github.com/lambdamusic/Ontospy/wiki) library, which itself relies on [Rdflib](https://github.com/RDFLib/rdflib).

> note: the functionalities of Ontodocs used to be part of OntoSpy until v1.8.

