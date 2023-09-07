# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:19:03 2023

@author: Manuel
"""

import dominate
from dominate.util import text
from dominate.tags import meta, comment, link, script, attr, div, ul, li, a, h1, hr, h3, p, img, table, tr, td, span, br
from dominate.tags import html_tag


class emptyline(html_tag):
    def _render(self, sb, indent_level=1, indent_str='  ', pretty=True, xhtml=False):
        return sb
    
class my_header_navbar(html_tag):
    def _render(self, sb, indent_level=1, indent_str='  ', pretty=True, xhtml=False):
        sb.append("<my-header-navbar></my-header-navbar>")
        return sb 
    
class my_artworks_nav(html_tag):
    def _render(self, sb, indent_level=1, indent_str='  ', pretty=True, xhtml=False):
        sb.append("<my-artworks-nav></my-artworks-nav>")
        return sb 


def create_artwork_page_from_model(model):
    doc = dominate.document(title=f'Artworks-{model.name}')
    with doc:
        attr(lang="en")

    with doc.head:
        emptyline()
        meta(charset="UTF-8")
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        emptyline()
        
        comment("UIkit CSS")
        link(rel="stylesheet", href="/schattenorigami/css/uikit.min.css")
        emptyline()
        
        comment("my CSS")
        link(rel="stylesheet", href="/schattenorigami/css/my_css.css")
        
        emptyline()
        comment("UIkit JS")
        
        emptyline()
        script(src="/schattenorigami/js/uikit.js")
        script(src="/schattenorigami/js/uikit-icons.min.js")
        
        emptyline()
        comment("my JS")
        script(src="/schattenorigami/components/header.js", _type="text/javascript", defer=True)
        script(src="/schattenorigami/components/artworks_nav.js", _type="text/javascript", defer=True)

        
    with doc.body:
        attr(style="overflow-y: scroll")
        
        # Navbar
        comment("Navbar")
        my_header_navbar()
        emptyline()
        
        # Versions Nav (right)
        comment("Versions Nav (right)")
        with div(_class="my-sidebar-right uk-padding-small uk-visible@xl"):
            with ul(_class="uk-nav uk-nav-default"):
                with li(_class="uk-nav-header uk-text-center"):
                    text("Versions")
                li(_class="uk-nav-divider")
                for version_title in model.version_titles:
                    with li(__pretty=False):
                        with a(href=f"#version{version_title}", uk_scroll="offset: 110"):
                            text(f"Version {version_title}")
        emptyline()
        
        # Artworks Nav (left)
        comment("Artworks Nav (left)")
        my_artworks_nav()
        emptyline()

        # Main stuff
        comment("Main stuff")
        with div(_class="uk-container uk-container-small uk-padding"):
            with div(_class="uk-grid-medium uk-child-width-1-2@s uk-text-center",
                     uk_grid=""):
                
                # Title
                with h1(_class="uk-width-1-1 my-model-title"):
                    text(model.name)
                emptyline()
                
                hr(_class="uk-width-1-1 uk-margin-left")
                emptyline()
                
                # Tags
                with div(_class="uk-width-1-1"):
                    for tag in model.tags:
                        with span(_class="my-label"):
                            text(tag)
                emptyline()
                
                hr(_class="uk-width-1-1 uk-margin-left")
                emptyline()
                
                # Versions loop
                for v, version_title in enumerate(model.version_titles):
                    # Version title and caption
                    comment(f"Version {version_title}")
                    with div(_class="uk-width-1-1"):
                        with h3(id=f"version{version_title}"):
                            text(f"Version {version_title}")
                        with p(__pretty=True):
                            for idx, paragraph in enumerate(model.captions[v]):
                                text(paragraph)
                                if idx < len(model.captions[v]) - 1:
                                    br()
                    emptyline()
                    
                    # Slideshow
                    comment("Slideshow")
                    with div(_class="uk-position-relative uk-visible-toggle uk-dark",
                             tabindex="-1",
                             uk_slideshow="ratio: 1:1; animation: pull"):
                        emptyline()
                        
                        with ul(_class="uk-slideshow-items"):
                            for i in range(model.nums_of_imgs[v]):
                                with li():
                                    img(src=model.img_paths[v][i], alt="", uk_cover="")
                        emptyline()
                        
                        a(_class="uk-position-center-left uk-position-small uk-hidden-hover",
                          href="#", uk_slidenav_previous="", uk_slideshow_item="previous")
                        a(_class="uk-position-center-right uk-position-small uk-hidden-hover",
                          href="#", uk_slidenav_next="", uk_slideshow_item="next")
                        emptyline()
                        
                        ul(_class="uk-slideshow-nav uk-dotnav uk-flex-center uk-margin")
                    emptyline()
                    
                    # Model info
                    comment("Model info")
                    with div():
                        with table():
                            
                            # Created, paper, time
                            for key, value in zip(["Created", "Paper", "Time"], [model.dates[v], model.papers[v], model.times[v]]):
                                with tr():
                                    with td(_class="uk-text-bold"):
                                        text(key)
                                    with td():
                                        text(value)
                                        
                            # Grid if applicable
                            if model.grids is not None:
                                with tr():
                                    with td(_class="uk-text-bold"):
                                        text("Grid")
                                    with td():
                                        text(model.grids[v])
                            
                            # Trivia if applicable 
                            if model.trivias[v] is not None:
                                with tr():
                                    with td(_class="uk-text-bold"):
                                        text("Trivia")
                                    with td():
                                        text(model.trivias[v])
                            
                            # Note if applicable 
                            if model.notes[v] is not None:
                                with tr():
                                    with td(_class="uk-text-bold"):
                                        text("Note")
                                    with td():
                                        text(model.notes[v])
                            
                            # CP if applicable
                            with tr():
                                with td(_class="uk-text-bold"):
                                    text("CP")
                                with td():
                                    if model.cps[v]:
                                        with div():
                                            with div(uk_lightbox=""):
                                                with a(_class="uk-inline", href=model.cp_paths[v]):
                                                    img(src=model.cp_paths[v], width="500")
                                            with a(_class="uk-button uk-button-text",
                                                   href=model.cp_paths[v], download=""):
                                                text("Download CP")
                                    else:
                                        text("N/A")
                            
                            # Diagrams if applicable
                            if model.diagrams[v]:
                                with td(_class="uk-text-bold"):
                                    text("Diagrams")
                                with td(_class="my-comment"):
                                    text("to be added")
                    emptyline()
                    
                    # No <hr> and emptyline if at end
                    if v < model.num_of_versions - 1:
                        hr(_class="uk-width-1-1 uk-margin-left")
                        emptyline()
                        
    # create the artwork page html file
    # ----- NOTE -----
    # Can't use model.artwork_page_path because it ist equal to
    # "schattenorigami/artwork_pages/[model_name_snake].hmtl" and this won't work
    # (maybe because the "/schattenorigami" the beginning?)
    artwork_page_path = '../artwork_pages/' + model.name_snake + '.html'
    f = open(artwork_page_path, "w+")
    f.write(str(doc))
    f.close()
