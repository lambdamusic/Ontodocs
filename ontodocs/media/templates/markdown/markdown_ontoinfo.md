{% extends "markdown_base.md" %}


{% block main_column %}

# _Vocabulary: [{{docs_title}}](index.md)_

---

{% if ontologies %}
#### Metadata
{% for ontology in ontologies %}
**{{ontology.uri}}**
{% if ontology.annotations %}
{% for each in ontology.annotations %}
{% ifchanged each.1 %}
* {{each.1}}
{% endifchanged %}
    * {{each.2}}
{% endfor %}
{% else %}
_No ontology metadata available_
{% endif %}
{% endfor %}
{% endif %}


#### Metrics
{% for each in stats %}
* {{each.0}}: **{{each.1}}**
{% endfor %}



{% if namespaces %}
#### Namespaces

Prefix   | URI      |
---------|----------|
{% for x,y in namespaces %}**{{x}}**| [{{y}}]({{y}} "Open Url")|
 {% endfor %}
{% endif %}


---


## Entities  

{% if ontospy_graph.all_classes%}
#### Classes ({{ontospy_graph.classes|length}})

{% for each in ontospy_graph.all_classes %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}


{% if ontospy_graph.all_skos %}
#### SKOS Concepts ({{ontospy_graph.skosConcepts|length}})

{% for each in ontograph.all_skos  %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}


{% if ontospy_graph.all_properties_object%}
#### Object Properties ({{ontospy_graph.objectProperties|length}})

{% for each in ontospy_graph.all_properties_object %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}


{% if ontospy_graph.all_properties_datatype%}
#### Datatype Properties ({{ontospy_graph.datatypeProperties|length}})

{% for each in ontospy_graph.all_properties_datatype %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}


{% if ontospy_graph.annotationProperties %}
#### Annotation Properties ({{ontograph.annotationProperties|length}})

{% for each in ontospy_graph.annotationProperties  %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}


{% if not ontospy_graph.all_properties_objectand not ontospy_graph.dataProperties and not ontospy_graph.annotationProperties %}
{% if ontospy_graph.all_properties %}
#### Properties ({{ontospy_graph.properties|length}})

{% for each in ontospy_graph.all_properties  %}
- [{{each.qname}}]({{each.slug}}.md "Open")
{% endfor %}

{% endif %}
{% endif %}



{% endblock main_column %}
