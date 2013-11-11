# ./networkhandshake.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-11-11 12:06:59.516575 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:629e6ecc-4ac1-11e3-8d9e-0016e6870683')

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


# Complex type connectionAcknowlege with content type ELEMENT_ONLY
class connectionAcknowlege (pyxb.binding.basis.complexTypeDefinition):
    """Complex type connectionAcknowlege with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'connectionAcknowlege')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element servername uses Python identifier servername
    __servername = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'servername'), 'servername', '__AbsentNamespace0_connectionAcknowlege_servername', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 12, 6), )

    
    servername = property(__servername.value, __servername.set, None, None)

    
    # Element clientname uses Python identifier clientname
    __clientname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'clientname'), 'clientname', '__AbsentNamespace0_connectionAcknowlege_clientname', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 13, 6), )

    
    clientname = property(__clientname.value, __clientname.set, None, None)

    
    # Element connectionallowed uses Python identifier connectionallowed
    __connectionallowed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'connectionallowed'), 'connectionallowed', '__AbsentNamespace0_connectionAcknowlege_connectionallowed', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 14, 6), )

    
    connectionallowed = property(__connectionallowed.value, __connectionallowed.set, None, None)

    _ElementMap.update({
        __servername.name() : __servername,
        __clientname.name() : __clientname,
        __connectionallowed.name() : __connectionallowed
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'connectionAcknowlege', connectionAcknowlege)


# Complex type connectionRequest with content type ELEMENT_ONLY
class connectionRequest (pyxb.binding.basis.complexTypeDefinition):
    """Complex type connectionRequest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'connectionRequest')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element clientname uses Python identifier clientname
    __clientname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'clientname'), 'clientname', '__AbsentNamespace0_connectionRequest_clientname', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 20, 6), )

    
    clientname = property(__clientname.value, __clientname.set, None, None)

    _ElementMap.update({
        __clientname.name() : __clientname
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'connectionRequest', connectionRequest)


# Complex type connectionEstablished with content type EMPTY
class connectionEstablished (pyxb.binding.basis.complexTypeDefinition):
    """Complex type connectionEstablished with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'connectionEstablished')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'connectionEstablished', connectionEstablished)


connectionacknowlege = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionacknowlege'), connectionAcknowlege, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', connectionacknowlege.name().localName(), connectionacknowlege)

connectionestablished = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionestablished'), connectionEstablished, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', connectionestablished.name().localName(), connectionestablished)

connectionrequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'connectionrequest'), connectionRequest, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 8, 2))
Namespace.addCategoryObject('elementBinding', connectionrequest.name().localName(), connectionrequest)



connectionAcknowlege._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'servername'), pyxb.binding.datatypes.string, scope=connectionAcknowlege, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 12, 6)))

connectionAcknowlege._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'clientname'), pyxb.binding.datatypes.string, scope=connectionAcknowlege, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 13, 6)))

connectionAcknowlege._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'connectionallowed'), pyxb.binding.datatypes.boolean, scope=connectionAcknowlege, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 14, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 13, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(connectionAcknowlege._UseForTag(pyxb.namespace.ExpandedName(None, u'servername')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(connectionAcknowlege._UseForTag(pyxb.namespace.ExpandedName(None, u'clientname')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 13, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(connectionAcknowlege._UseForTag(pyxb.namespace.ExpandedName(None, u'connectionallowed')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 14, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
connectionAcknowlege._Automaton = _BuildAutomaton()




connectionRequest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'clientname'), pyxb.binding.datatypes.string, scope=connectionRequest, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 20, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 20, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(connectionRequest._UseForTag(pyxb.namespace.ExpandedName(None, u'clientname')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/networkhandshakeschema.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
connectionRequest._Automaton = _BuildAutomaton_()

