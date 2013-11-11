# ./changevisionmodedata.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-11-11 16:00:03.136675 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f182c3d4-4ae1-11e3-8d66-0016e6870683')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: visionMode
class visionMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionMode')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 12, 2)
    _Documentation = None
visionMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=visionMode, enum_prefix=None)
visionMode.VISION_MODE_NONE = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_NONE', tag=u'VISION_MODE_NONE')
visionMode.VISION_MODE_STREAM_ALL = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_STREAM_ALL', tag=u'VISION_MODE_STREAM_ALL')
visionMode.VISION_MODE_STREAM_BOTS = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_STREAM_BOTS', tag=u'VISION_MODE_STREAM_BOTS')
visionMode.VISION_MODE_STREAM_OBJECTS = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_STREAM_OBJECTS', tag=u'VISION_MODE_STREAM_OBJECTS')
visionMode.VISION_MODE_STOPPED = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_STOPPED', tag=u'VISION_MODE_STOPPED')
visionMode.VISION_MODE_CALIBRATE_DISTANCE = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_CALIBRATE_DISTANCE', tag=u'VISION_MODE_CALIBRATE_DISTANCE')
visionMode.VISION_MODE_CALIBRATE_TRANSFORMATION = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_CALIBRATE_TRANSFORMATION', tag=u'VISION_MODE_CALIBRATE_TRANSFORMATION')
visionMode.VISION_MODE_TERMINATE = visionMode._CF_enumeration.addEnumeration(unicode_value=u'VISION_MODE_TERMINATE', tag=u'VISION_MODE_TERMINATE')
visionMode._InitializeFacetMap(visionMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'visionMode', visionMode)

# Complex type changeVisionMode with content type ELEMENT_ONLY
class changeVisionMode (pyxb.binding.basis.complexTypeDefinition):
    """Complex type changeVisionMode with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'changeVisionMode')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element visionmode uses Python identifier visionmode
    __visionmode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'visionmode'), 'visionmode', '__AbsentNamespace0_changeVisionMode_visionmode', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 8, 6), )

    
    visionmode = property(__visionmode.value, __visionmode.set, None, None)

    _ElementMap.update({
        __visionmode.name() : __visionmode
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'changeVisionMode', changeVisionMode)


changevisionmode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'changevisionmode'), changeVisionMode, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', changevisionmode.name().localName(), changevisionmode)



changeVisionMode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'visionmode'), visionMode, scope=changeVisionMode, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 8, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 8, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(changeVisionMode._UseForTag(pyxb.namespace.ExpandedName(None, u'visionmode')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/changevisionmodeschema.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
changeVisionMode._Automaton = _BuildAutomaton()

