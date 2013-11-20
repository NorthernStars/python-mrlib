# ./positiondata.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-11-13 09:27:44.718769 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:78544f98-4c3d-11e3-828c-0016e6870683')

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
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 48, 2)
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

# Atomic simple type: positionObjectType
class positionObjectType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 61, 2)
    _Documentation = None
positionObjectType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=positionObjectType, enum_prefix=None)
positionObjectType.BOT = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'BOT', tag=u'BOT')
positionObjectType.RECTANGLE = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'RECTANGLE', tag=u'RECTANGLE')
positionObjectType.LINE = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'LINE', tag=u'LINE')
positionObjectType.CIRCLE = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'CIRCLE', tag=u'CIRCLE')
positionObjectType.DOT = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'DOT', tag=u'DOT')
positionObjectType.TEXT = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'TEXT', tag=u'TEXT')
positionObjectType.IMAGE = positionObjectType._CF_enumeration.addEnumeration(unicode_value=u'IMAGE', tag=u'IMAGE')
positionObjectType._InitializeFacetMap(positionObjectType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'positionObjectType', positionObjectType)

# Complex type positionDataPackage with content type ELEMENT_ONLY
class positionDataPackage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type positionDataPackage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionDataPackage')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element visionmode uses Python identifier visionmode
    __visionmode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'visionmode'), 'visionmode', '__AbsentNamespace0_positionDataPackage_visionmode', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 12, 6), )

    
    visionmode = property(__visionmode.value, __visionmode.set, None, None)

    
    # Element objects uses Python identifier objects
    __objects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'objects'), 'objects', '__AbsentNamespace0_positionDataPackage_objects', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 13, 6), )

    
    objects = property(__objects.value, __objects.set, None, None)

    _ElementMap.update({
        __visionmode.name() : __visionmode,
        __objects.name() : __objects
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'positionDataPackage', positionDataPackage)


# Complex type positionObject with content type ELEMENT_ONLY
class positionObject (pyxb.binding.basis.complexTypeDefinition):
    """Complex type positionObject with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionObject')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element objecttype uses Python identifier objecttype
    __objecttype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'objecttype'), 'objecttype', '__AbsentNamespace0_positionObject_objecttype', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6), )

    
    objecttype = property(__objecttype.value, __objecttype.set, None, None)

    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_positionObject_id', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 20, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_positionObject_name', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__AbsentNamespace0_positionObject_location', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element color uses Python identifier color
    __color = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'color'), 'color', '__AbsentNamespace0_positionObject_color', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6), )

    
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
Namespace.addCategoryObject('typeBinding', u'positionObject', positionObject)


# Complex type positionObjectBot with content type ELEMENT_ONLY
class positionObjectBot (positionObject):
    """Complex type positionObjectBot with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionObjectBot')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 27, 2)
    _ElementMap = positionObject._ElementMap.copy()
    _AttributeMap = positionObject._AttributeMap.copy()
    # Base type is positionObject
    
    # Element objecttype (objecttype) inherited from positionObject
    
    # Element id (id) inherited from positionObject
    
    # Element name (name) inherited from positionObject
    
    # Element location (location) inherited from positionObject
    
    # Element color (color) inherited from positionObject
    
    # Element angle uses Python identifier angle
    __angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'angle'), 'angle', '__AbsentNamespace0_positionObjectBot_angle', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 31, 10), )

    
    angle = property(__angle.value, __angle.set, None, None)

    _ElementMap.update({
        __angle.name() : __angle
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'positionObjectBot', positionObjectBot)


# Complex type positionObjectRectangle with content type ELEMENT_ONLY
class positionObjectRectangle (positionObject):
    """Complex type positionObjectRectangle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionObjectRectangle')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 37, 2)
    _ElementMap = positionObject._ElementMap.copy()
    _AttributeMap = positionObject._AttributeMap.copy()
    # Base type is positionObject
    
    # Element objecttype (objecttype) inherited from positionObject
    
    # Element id (id) inherited from positionObject
    
    # Element name (name) inherited from positionObject
    
    # Element location (location) inherited from positionObject
    
    # Element color (color) inherited from positionObject
    
    # Element angle uses Python identifier angle
    __angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'angle'), 'angle', '__AbsentNamespace0_positionObjectRectangle_angle', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 41, 10), )

    
    angle = property(__angle.value, __angle.set, None, None)

    
    # Element size uses Python identifier size
    __size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'size'), 'size', '__AbsentNamespace0_positionObjectRectangle_size', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 42, 10), )

    
    size = property(__size.value, __size.set, None, None)

    _ElementMap.update({
        __angle.name() : __angle,
        __size.name() : __size
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'positionObjectRectangle', positionObjectRectangle)


positiondatapackage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'positiondatapackage'), positionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', positiondatapackage.name().localName(), positiondatapackage)

positionobjectbot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'positionobjectbot'), positionObjectBot, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', positionobjectbot.name().localName(), positionobjectbot)

positionobjectrectangle = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'positionobjectrectangle'), positionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', positionobjectrectangle.name().localName(), positionobjectrectangle)



positionDataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'visionmode'), visionMode, scope=positionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 12, 6)))

positionDataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'objects'), positionObject, scope=positionDataPackage, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 13, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 13, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(positionDataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'visionmode')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(positionDataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'objects')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 13, 6))
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
positionDataPackage._Automaton = _BuildAutomaton()




positionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'objecttype'), positionObjectType, scope=positionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6)))

positionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'id'), pyxb.binding.datatypes.int, scope=positionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 20, 6)))

positionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=positionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6)))

positionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), pyxb.binding.datatypes.double, scope=positionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6)))

positionObject._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'color'), pyxb.binding.datatypes.double, scope=positionObject, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(positionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(positionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(positionObject._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
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
positionObject._Automaton = _BuildAutomaton_()




positionObjectBot._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'angle'), pyxb.binding.datatypes.double, scope=positionObjectBot, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 31, 10)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionObjectBot._UseForTag(pyxb.namespace.ExpandedName(None, u'angle')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 31, 10))
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
positionObjectBot._Automaton = _BuildAutomaton_2()




positionObjectRectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'angle'), pyxb.binding.datatypes.double, scope=positionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 41, 10)))

positionObjectRectangle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'size'), pyxb.binding.datatypes.double, scope=positionObjectRectangle, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 42, 10)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 42, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'objecttype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 20, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 21, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 22, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'color')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 23, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'angle')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 41, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(positionObjectRectangle._UseForTag(pyxb.namespace.ExpandedName(None, u'size')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/positiondatapacketschema.xsd', 42, 10))
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
positionObjectRectangle._Automaton = _BuildAutomaton_3()

