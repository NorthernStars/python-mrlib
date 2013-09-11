# ./DataPackage.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-09-11 20:34:58.593685 by PyXB version 1.2.2
# Namespace AbsentNamespace0

import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dc941b54-1b10-11e3-9f97-0019d275b706')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
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
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
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
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type DataPackage with content type ELEMENT_ONLY
class DataPackage (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DataPackage with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DataPackage')
    _XSDLocation = pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 4, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element timestamp uses Python identifier timestamp
    __timestamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timestamp'), 'timestamp', '__AbsentNamespace0_DataPackage_timestamp', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 6, 3), )

    
    timestamp = property(__timestamp.value, __timestamp.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_DataPackage_type', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 7, 3), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element host uses Python identifier host
    __host = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'host'), 'host', '__AbsentNamespace0_DataPackage_host', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 8, 3), )

    
    host = property(__host.value, __host.set, None, None)

    
    # Element data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'data'), 'data', '__AbsentNamespace0_DataPackage_data', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 9, 3), )

    
    data = property(__data.value, __data.set, None, None)

    _ElementMap.update({
        __timestamp.name() : __timestamp,
        __type.name() : __type,
        __host.name() : __host,
        __data.name() : __data
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DataPackage', DataPackage)


# Complex type Data with content type ELEMENT_ONLY
class Data (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Data with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Data')
    _XSDLocation = pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 14, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'item'), 'item', '__AbsentNamespace0_Data_item', True, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 16, 3), )

    
    item = property(__item.value, __item.set, None, None)

    _ElementMap.update({
        __item.name() : __item
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Data', Data)


# Complex type Item with content type ELEMENT_ONLY
class Item (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Item with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Item')
    _XSDLocation = pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element key uses Python identifier key
    __key = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__AbsentNamespace0_Item_key', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 22, 7), )

    
    key = property(__key.value, __key.set, None, None)

    
    # Element val uses Python identifier val
    __val = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__AbsentNamespace0_Item_val', False, pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 23, 7), )

    
    val = property(__val.value, __val.set, None, None)

    _ElementMap.update({
        __key.name() : __key,
        __val.name() : __val
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Item', Item)




DataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timestamp'), pyxb.binding.datatypes.float, scope=DataPackage, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 6, 3), unicode_default=u'0.0'))

DataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'type'), pyxb.binding.datatypes.string, scope=DataPackage, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 7, 3), unicode_default=u'None'))

DataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'host'), pyxb.binding.datatypes.string, scope=DataPackage, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 8, 3), unicode_default=u'None'))

DataPackage._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'data'), Data, scope=DataPackage, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 9, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'timestamp')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 6, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'type')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 7, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'host')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 8, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DataPackage._UseForTag(pyxb.namespace.ExpandedName(None, u'data')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 9, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DataPackage._Automaton = _BuildAutomaton()




Data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'item'), Item, scope=Data, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 16, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 16, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Data._UseForTag(pyxb.namespace.ExpandedName(None, u'item')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 16, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Data._Automaton = _BuildAutomaton_()




Item._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'key'), pyxb.binding.datatypes.string, scope=Item, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 22, 7)))

Item._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'val'), pyxb.binding.datatypes.string, scope=Item, location=pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 23, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Item._UseForTag(pyxb.namespace.ExpandedName(None, u'key')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 22, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Item._UseForTag(pyxb.namespace.ExpandedName(None, u'val')), pyxb.utils.utility.Location('/home/hannes/git/python-mrlib/python-mrLib/src/mrLib/networking/DataPackage.xsd', 23, 7))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Item._Automaton = _BuildAutomaton_2()

