# ./visiondatapackage.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-11-08 16:28:32.534080 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6d24a84a-488a-11e3-8169-0016e6870683')

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
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 48, 2)
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

# Atomic simple type: visionObjectType
class visionObjectType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 61, 2)
    _Documentation = None
visionObjectType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=visionObjectType, enum_prefix=None)
visionObjectType.BOT = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'BOT', tag=u'BOT')
visionObjectType.RECTANGLE = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'RECTANGLE', tag=u'RECTANGLE')
visionObjectType.LINE = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'LINE', tag=u'LINE')
visionObjectType.CIRCLE = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'CIRCLE', tag=u'CIRCLE')
visionObjectType.DOT = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'DOT', tag=u'DOT')
visionObjectType.TEXT = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'TEXT', tag=u'TEXT')
visionObjectType.IMAGE = visionObjectType._CF_enumeration.addEnumeration(unicode_value=u'IMAGE', tag=u'IMAGE')
visionObjectType._InitializeFacetMap(visionObjectType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'visionObjectType', visionObjectType)

# Complex type visionDataPackage with content type ELEMENT_ONLY
class visionDataPackage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type visionDataPackage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionDataPackage')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element visionmode uses Python identifier visionmode
    __visionmode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'visionmode'), 'visionmode', '__AbsentNamespace0_visionDataPackage_visionmode', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 12, 6), )

    
    visionmode = property(__visionmode.value, __visionmode.set, None, None)

    
    # Element visionobjects uses Python identifier visionobjects
    __visionobjects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'visionobjects'), 'visionobjects', '__AbsentNamespace0_visionDataPackage_visionobjects', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 13, 6), )

    
    visionobjects = property(__visionobjects.value, __visionobjects.set, None, None)

    _ElementMap.update({
        __visionmode.name() : __visionmode,
        __visionobjects.name() : __visionobjects
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visionDataPackage', visionDataPackage)


# Complex type visionObject with content type ELEMENT_ONLY
class visionObject (pyxb.binding.basis.complexTypeDefinition):
    """Complex type visionObject with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionObject')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objecttype uses Python identifier objecttype
    __objecttype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'objecttype'), 'objecttype', '__AbsentNamespace0_visionObject_objecttype', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6), )

    
    objecttype = property(__objecttype.value, __objecttype.set, None, None)

    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_visionObject_id', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 20, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_visionObject_name', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__AbsentNamespace0_visionObject_location', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'color'), 'color', '__AbsentNamespace0_visionObject_color', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6), )

    
    color = property(__color.value, __color.set, None, None)

    _ElementMap.update({
        __objecttype.name() : __objecttype,
        __id.name() : __id,
        __name.name() : __name,
        __location.name() : __location,
        __color.name() : __color
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visionObject', visionObject)


# Complex type visionObjectBot with content type ELEMENT_ONLY
class visionObjectBot (visionObject):
    """Complex type visionObjectBot with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionObjectBot')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 27, 2)
    _ElementMap = visionObject._ElementMap.copy()
    _AttributeMap = visionObject._AttributeMap.copy()
    # Base type is visionObject
    
    # Element objecttype (objecttype) inherited from visionObject
    
    # Element id (id) inherited from visionObject
    
    # Element name (name) inherited from visionObject
    
    # Element location (location) inherited from visionObject
    
    # Element color (color) inherited from visionObject
    
    # Element angle uses Python identifier angle
    __angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'angle'), 'angle', '__AbsentNamespace0_visionObjectBot_angle', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 31, 10), )

    
    angle = property(__angle.value, __angle.set, None, None)

    _ElementMap.update({
        __angle.name() : __angle
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visionObjectBot', visionObjectBot)


# Complex type visionObjectRectangle with content type ELEMENT_ONLY
class visionObjectRectangle (visionObject):
    """Complex type visionObjectRectangle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'visionObjectRectangle')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 37, 2)
    _ElementMap = visionObject._ElementMap.copy()
    _AttributeMap = visionObject._AttributeMap.copy()
    # Base type is visionObject
    
    # Element objecttype (objecttype) inherited from visionObject
    
    # Element id (id) inherited from visionObject
    
    # Element name (name) inherited from visionObject
    
    # Element location (location) inherited from visionObject
    
    # Element color (color) inherited from visionObject
    
    # Element angle uses Python identifier angle
    __angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'angle'), 'angle', '__AbsentNamespace0_visionObjectRectangle_angle', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 41, 10), )

    
    angle = property(__angle.value, __angle.set, None, None)

    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__AbsentNamespace0_visionObjectRectangle_size', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 42, 10), )

    
    size = property(__size.value, __size.set, None, None)

    _ElementMap.update({
        __angle.name() : __angle,
        __size.name() : __size
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'visionObjectRectangle', visionObjectRectangle)


visiondatapackage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'visiondatapackage'), visionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', visiondatapackage.name().localName(), visiondatapackage)

visionobjectbot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'visionobjectbot'), visionObjectBot, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', visionobjectbot.name().localName(), visionobjectbot)

visionobjectrectangle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'visionobjectrectangle'), visionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', visionobjectrectangle.name().localName(), visionobjectrectangle)



visionDataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'visionmode'), visionMode, scope=visionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 12, 6)))

visionDataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'visionobjects'), visionObject, scope=visionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 13, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 13, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(visionDataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'visionmode')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(visionDataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'visionobjects')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 13, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
visionDataPackage._Automaton = _BuildAutomaton()




visionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'objecttype'), visionObjectType, scope=visionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6)))

visionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'id'), pyxb.binding.datatypes.int, scope=visionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 20, 6)))

visionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=visionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6)))

visionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), pyxb.binding.datatypes.double, scope=visionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6)))

visionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'color'), pyxb.binding.datatypes.double, scope=visionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(visionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(visionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(visionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(visionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
visionObject._Automaton = _BuildAutomaton_()




visionObjectBot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'angle'), pyxb.binding.datatypes.double, scope=visionObjectBot, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 31, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(visionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'angle')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 31, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
visionObjectBot._Automaton = _BuildAutomaton_2()




visionObjectRectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'angle'), pyxb.binding.datatypes.double, scope=visionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 41, 10)))

visionObjectRectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'size'), pyxb.binding.datatypes.double, scope=visionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 42, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 42, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 23, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'angle')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 41, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(visionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'size')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/visiondatapackage.xsd', 42, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
visionObjectRectangle._Automaton = _BuildAutomaton_3()

