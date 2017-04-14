# !/usr/bin/env python
#  -*- coding: UTF-8 -*-


"""
ONTODOCS
Copyright (c) 2013-2017 __Michele Pasin__ <http://www.michelepasin.org>.
All rights reserved.

More info in the README file.

"""

import time
import click
# http://click.pocoo.org/5/arguments/
# http://click.pocoo.org/5/options/

from ontospy.core import manager as ontospy_manager

from . import *
from .core.builder import *




CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('source', nargs=-1)
@click.option('--library', '-l', is_flag=True, help='List ontologies saved in the OntoSpy local library.')
@click.option('--outputpath', '-o',  help='Output path (default: home folder).')
@click.option('--title',  help='Title for the visualization (default=graph uri).')
@click.option('--theme',  help='CSS Theme for the html-complex visualization (random=use a random theme).')
@click.option('--showthemes', is_flag=True, help='Show the available CSS theme choices.')
@click.option('--verbose', '-v', is_flag=True, help='Verbose mode.')
def cli_run_viz(source=None, library=False, outputpath="", title="", theme="", showthemes=False, verbose=False):
    """
Ontodocs is an application of the OntoSpy library which can be used to quickly create  documentation for a ontology encoded in RDF/OWL.

E.g.:

> ontodocs http://www.w3.org/2008/05/skos# --theme random -o ~/Desktop/skos

==> generates html docs for the SKOS ontology and save it to your desktop
"""
    sTime = time.time()
    ontospy_manager.get_or_create_home_repo()
    click.secho("Ontodocs " + VERSION,  bold=True)
    # click.secho("Local library: '%s'" % get_home_location(), fg='white')
    click.secho("------------", fg='white')

    if showthemes:
        # from .core.builder import show_themes
        show_themes()
        sys.exit(0)

    if theme and theme=="random":
        # from .core.builder import random_theme
        theme = random_theme()

    if outputpath:
        if not(os.path.exists(outputpath)) or not (os.path.isdir(outputpath)):
            click.secho("WARNING: the -o option must include a valid directory path.", fg="red")
            sys.exit(0)

    if not library and not source:

        # TODO: ask to show local library
        # click.secho("You haven't specified any argument.", fg='red')
        # if click.confirm('Show the local OntoSpy library?'):
        #     filename = ontospy.action_listlocal(all_details=False)
        #     if filename:
        #         g = get_pickled_ontology(filename)
        #         if not g:
        #             g = do_pickle_ontology(filename)
        #         shellPrintOverview(g, print_opts)
        # else:
        #     printDebug("Goodbye.", "comment")
        #     raise SystemExit(1)
        #
        #
        click.secho("WARNING: not enough options. Use -h for help.", fg="red")
        sys.exit(0)

    if library:
        click.secho("Showing the local library: '%s'" % ontospy_manager.get_home_location(), fg='red')

    if source and len(source) > 1:
        click.secho('Note: currently only one argument can be passed', fg='red')


    url = action_visualize(source, fromshell=False, path=outputpath, title=title, theme=theme, verbose=verbose)


    if url:# open browser
        import webbrowser
        webbrowser.open(url)

        # continue and print(timing at bottom )

    # finally: print(some stats.... )
    eTime = time.time()
    tTime = eTime - sTime
    printDebug("\n----------\n" + "Time:	   %0.2fs" %  tTime, "comment")


    # raise SystemExit(1)



if __name__ == '__main__':
    try:
        # http://stackoverflow.com/questions/32553969/modify-usage-string-on-click-command-line-interface-on-windows
        cli_run_viz(prog_name='ontodocs')
        sys.exit(0)
    except KeyboardInterrupt as e: # Ctrl-C
        raise e
