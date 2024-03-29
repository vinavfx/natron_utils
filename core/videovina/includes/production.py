# archivo que contiene las funciones para generar los proyectos
# para render en produccion a partir de los datos del nodo videovina

from nx import copy, warning, alert, question
from slides import get_slides, delete_slide, get_slide, get_last_slide
from develop import update_post_fx, xdistance, refresh
from base import clean_project


def divide_project(thisNode, workarea):
    # divide el proyecto en varias partes, asi evitamos que cuando renderizamos
    # cargue todas las slides, ya que natron
    # se demora mucho al abrir los proyectos pesados

    slide_range = [2, 5]

    keep_slides = range(slide_range[0], slide_range[-1] + 1)
    for i, slide in enumerate(get_slides(workarea)):

        if not i in keep_slides:
            delete_slide(i)

    update_post_fx(thisNode, workarea)


def production_slides(thisNode, app, workarea):
    slides_range = thisNode.production_slides.get()

    generated = generate_production_slides(thisNode, app, workarea, slides_range)
    if not generated:
        return

    update_post_fx(thisNode, workarea)
    refresh()

    alert('Ya se duplicaron las slide de Produccion.',
          'Duplicate from base slides.')


def production_slide(app, workarea, index, base_slides, base_slide_index, last_transition, last_dot, last_slide, posx):

    slide = base_slides[base_slide_index]['slide']
    transition = base_slides[base_slide_index]['transition']

    new_slide = copy(slide, workarea)
    new_slide.setPosition(posx, 0)
    new_slide.setLabel('slide_' + str(index) + 'p')

    new_transition = copy(transition, workarea)
    new_transition.setColor(.7, .7, .4)
    new_transition.setPosition(posx, 200)
    new_transition.setLabel('slide_' + str(index) + 'p_transition')
    if last_transition:
        new_transition.connectInput(0, last_transition)
    else:
        new_transition.connectInput(0, last_slide['transition'])

    new_transition.connectInput(1, new_slide)

    dot = app.createNode('fr.inria.built-in.Dot', 2, workarea)
    dot_name = 'slide_' + str(index) + 'p_dot'
    dot.setLabel(dot_name)
    dot.setPosition(posx - 50, 100)
    new_transition.connectInput(2, dot)

    if last_dot:
        dot.connectInput(0, last_dot)
    else:
        dot.connectInput(0, last_slide['dot'])

    return [new_transition, dot]


def generate_production_slides(thisNode, app, workarea, slides_range, force=False):

    base_slides, production_slides = get_slides(workarea, separate=True)
    base_count = len(base_slides)
    slides_count = base_count + len(production_slides)

    if not force:
        if not base_count:
            warning('Produccion Slides', 'Tiene que haber slides base')
            return

        if not question('Al crear las slide de produccion se borraran las slide base, desea continuar?', 'Produccion Slides'):
            return

    amount = slides_range[1] + 1
    _slides_range = range(slides_range[0], amount)

    last_transition = None
    last_dot = None

    last_slide = get_last_slide()

    base_slide_index = 0
    posx = xdistance * slides_count
    for i in range(amount - slides_count):
        index = i + slides_count
        if index in _slides_range:
            slide = get_slide(workarea, index)
            if slide:
                last_transition = slide['transition']
                last_dot = slide['dot']
            else:
                # crea la slide si no esta
                last_transition, last_dot = production_slide(
                    app,
                    workarea,
                    index,
                    base_slides,
                    base_slide_index,
                    last_transition,
                    last_dot,
                    last_slide,
                    posx
                )

        base_slide_index += 1
        if base_slide_index >= base_count:
            base_slide_index = 0

        posx += xdistance

    # borra las slide que estan fuera del rango de la cantidad de slides
    for i in range(last_slide['index'] + 1):
        if not i in _slides_range:
            delete_slide(i)

    clean_project()

    return True
