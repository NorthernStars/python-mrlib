# ./worlddataaa.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-11-15 17:44:18.061515 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2b5f1af4-4e15-11e3-82df-0016e6870683')

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


# Atomic simple type: playMode
class playMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'playMode')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 69, 2)
    _Documentation = None
playMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=playMode, enum_prefix=None)
playMode.kick_off = playMode._CF_enumeration.addEnumeration(unicode_value=u'kick off', tag=u'kick_off')
playMode.play_on = playMode._CF_enumeration.addEnumeration(unicode_value=u'play on', tag=u'play_on')
playMode.corner_kick_blue = playMode._CF_enumeration.addEnumeration(unicode_value=u'corner kick blue', tag=u'corner_kick_blue')
playMode.corner_kick_yellow = playMode._CF_enumeration.addEnumeration(unicode_value=u'corner kick yellow', tag=u'corner_kick_yellow')
playMode.goal_kick_blue = playMode._CF_enumeration.addEnumeration(unicode_value=u'goal kick blue', tag=u'goal_kick_blue')
playMode.goal_kick_yellow = playMode._CF_enumeration.addEnumeration(unicode_value=u'goal kick yellow', tag=u'goal_kick_yellow')
playMode.time_out_blue = playMode._CF_enumeration.addEnumeration(unicode_value=u'time out blue', tag=u'time_out_blue')
playMode.time_out_yellow = playMode._CF_enumeration.addEnumeration(unicode_value=u'time out yellow', tag=u'time_out_yellow')
playMode.frozen_operator = playMode._CF_enumeration.addEnumeration(unicode_value=u'frozen operator', tag=u'frozen_operator')
playMode.frozen_match = playMode._CF_enumeration.addEnumeration(unicode_value=u'frozen match', tag=u'frozen_match')
playMode.penalty = playMode._CF_enumeration.addEnumeration(unicode_value=u'penalty', tag=u'penalty')
playMode.warn_ending = playMode._CF_enumeration.addEnumeration(unicode_value=u'warn ending', tag=u'warn_ending')
playMode.warming_up = playMode._CF_enumeration.addEnumeration(unicode_value=u'warming up', tag=u'warming_up')
playMode.time_over = playMode._CF_enumeration.addEnumeration(unicode_value=u'time over', tag=u'time_over')
playMode.team_adjustmest = playMode._CF_enumeration.addEnumeration(unicode_value=u'team adjustmest', tag=u'team_adjustmest')
playMode._InitializeFacetMap(playMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'playMode', playMode)

# Atomic simple type: id
class id (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'id')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 89, 2)
    _Documentation = None
id._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=id, enum_prefix=None)
id.nofixedname = id._CF_enumeration.addEnumeration(unicode_value=u'nofixedname', tag=u'nofixedname')
id.player = id._CF_enumeration.addEnumeration(unicode_value=u'player', tag=u'player')
id.ball = id._CF_enumeration.addEnumeration(unicode_value=u'ball', tag=u'ball')
id.bottom_center = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_center', tag=u'bottom_center')
id.bottom_left_corner = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_left_corner', tag=u'bottom_left_corner')
id.bottom_left_goal = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_left_goal', tag=u'bottom_left_goal')
id.bottom_left_pole = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_left_pole', tag=u'bottom_left_pole')
id.bottom_left_small_area = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_left_small_area', tag=u'bottom_left_small_area')
id.bottom_right_corner = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_right_corner', tag=u'bottom_right_corner')
id.bottom_right_goal = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_right_goal', tag=u'bottom_right_goal')
id.bottom_right_pole = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_right_pole', tag=u'bottom_right_pole')
id.bottom_right_small_area = id._CF_enumeration.addEnumeration(unicode_value=u'bottom_right_small_area', tag=u'bottom_right_small_area')
id.middle_center = id._CF_enumeration.addEnumeration(unicode_value=u'middle_center', tag=u'middle_center')
id.top_center = id._CF_enumeration.addEnumeration(unicode_value=u'top_center', tag=u'top_center')
id.top_left_corner = id._CF_enumeration.addEnumeration(unicode_value=u'top_left_corner', tag=u'top_left_corner')
id.top_left_goal = id._CF_enumeration.addEnumeration(unicode_value=u'top_left_goal', tag=u'top_left_goal')
id.top_left_pole = id._CF_enumeration.addEnumeration(unicode_value=u'top_left_pole', tag=u'top_left_pole')
id.top_left_small_area = id._CF_enumeration.addEnumeration(unicode_value=u'top_left_small_area', tag=u'top_left_small_area')
id.top_right_corner = id._CF_enumeration.addEnumeration(unicode_value=u'top_right_corner', tag=u'top_right_corner')
id.top_right_goal = id._CF_enumeration.addEnumeration(unicode_value=u'top_right_goal', tag=u'top_right_goal')
id.top_right_pole = id._CF_enumeration.addEnumeration(unicode_value=u'top_right_pole', tag=u'top_right_pole')
id.top_right_small_area = id._CF_enumeration.addEnumeration(unicode_value=u'top_right_small_area', tag=u'top_right_small_area')
id._InitializeFacetMap(id._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'id', id)

# Atomic simple type: team
class team (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'team')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 116, 2)
    _Documentation = None
team._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=team, enum_prefix=None)
team.yellow = team._CF_enumeration.addEnumeration(unicode_value=u'yellow', tag=u'yellow')
team.blue = team._CF_enumeration.addEnumeration(unicode_value=u'blue', tag=u'blue')
team.none = team._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
team._InitializeFacetMap(team._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'team', team)

# Complex type worldData with content type ELEMENT_ONLY
class worldData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type worldData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'worldData')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'time'), 'time', '__AbsentNamespace0_worldData_time', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 8, 6), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element playMode uses Python identifier playMode
    __playMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'playMode'), 'playMode', '__AbsentNamespace0_worldData_playMode', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 9, 6), )

    
    playMode = property(__playMode.value, __playMode.set, None, None)

    
    # Element score uses Python identifier score
    __score = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'score'), 'score', '__AbsentNamespace0_worldData_score', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 10, 6), )

    
    score = property(__score.value, __score.set, None, None)

    
    # Element max_agent uses Python identifier max_agent
    __max_agent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'max_agent'), 'max_agent', '__AbsentNamespace0_worldData_max_agent', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 11, 6), )

    
    max_agent = property(__max_agent.value, __max_agent.set, None, None)

    
    # Element ball uses Python identifier ball
    __ball = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ball'), 'ball', '__AbsentNamespace0_worldData_ball', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 12, 6), )

    
    ball = property(__ball.value, __ball.set, None, None)

    
    # Element players uses Python identifier players
    __players = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'players'), 'players', '__AbsentNamespace0_worldData_players', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 13, 6), )

    
    players = property(__players.value, __players.set, None, None)

    
    # Element flag uses Python identifier flag
    __flag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'flag'), 'flag', '__AbsentNamespace0_worldData_flag', True, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 14, 6), )

    
    flag = property(__flag.value, __flag.set, None, None)

    _ElementMap.update({
        __time.name() : __time,
        __playMode.name() : __playMode,
        __score.name() : __score,
        __max_agent.name() : __max_agent,
        __ball.name() : __ball,
        __players.name() : __players,
        __flag.name() : __flag
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'worldData', worldData)


# Complex type score with content type ELEMENT_ONLY
class score (pyxb.binding.basis.complexTypeDefinition):
    """Complex type score with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'score')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element yellow uses Python identifier yellow
    __yellow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'yellow'), 'yellow', '__AbsentNamespace0_score_yellow', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 20, 6), )

    
    yellow = property(__yellow.value, __yellow.set, None, None)

    
    # Element blue uses Python identifier blue
    __blue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'blue'), 'blue', '__AbsentNamespace0_score_blue', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 21, 6), )

    
    blue = property(__blue.value, __blue.set, None, None)

    _ElementMap.update({
        __yellow.name() : __yellow,
        __blue.name() : __blue
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'score', score)


# Complex type referencePoint with content type ELEMENT_ONLY
class referencePoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type referencePoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'referencePoint')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 33, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pointtype uses Python identifier pointtype
    __pointtype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pointtype'), 'pointtype', '__AbsentNamespace0_referencePoint_pointtype', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6), )

    
    pointtype = property(__pointtype.value, __pointtype.set, None, None)

    
    # Element position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'position'), 'position', '__AbsentNamespace0_referencePoint_position', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6), )

    
    position = property(__position.value, __position.set, None, None)

    _ElementMap.update({
        __pointtype.name() : __pointtype,
        __position.name() : __position
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'referencePoint', referencePoint)


# Complex type point2D with content type EMPTY
class point2D (pyxb.binding.basis.complexTypeDefinition):
    """Complex type point2D with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'point2D')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'point2D', point2D)


# Complex type ballPosition with content type ELEMENT_ONLY
class ballPosition (referencePoint):
    """Complex type ballPosition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ballPosition')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 25, 2)
    _ElementMap = referencePoint._ElementMap.copy()
    _AttributeMap = referencePoint._AttributeMap.copy()
    # Base type is referencePoint
    
    # Element pointtype (pointtype) inherited from referencePoint
    
    # Element position (position) inherited from referencePoint
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ballPosition', ballPosition)


# Complex type serverPoint with content type ELEMENT_ONLY
class serverPoint (point2D):
    """Complex type serverPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'serverPoint')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 40, 2)
    _ElementMap = point2D._ElementMap.copy()
    _AttributeMap = point2D._AttributeMap.copy()
    # Base type is point2D
    
    # Element x uses Python identifier x
    __x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__AbsentNamespace0_serverPoint_x', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 44, 10), )

    
    x = property(__x.value, __x.set, None, None)

    
    # Element y uses Python identifier y
    __y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'y'), 'y', '__AbsentNamespace0_serverPoint_y', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 45, 10), )

    
    y = property(__y.value, __y.set, None, None)

    _ElementMap.update({
        __x.name() : __x,
        __y.name() : __y
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'serverPoint', serverPoint)


# Complex type player with content type ELEMENT_ONLY
class player (referencePoint):
    """Complex type player with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'player')
    _XSDLocation = pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 55, 2)
    _ElementMap = referencePoint._ElementMap.copy()
    _AttributeMap = referencePoint._AttributeMap.copy()
    # Base type is referencePoint
    
    # Element pointtype (pointtype) inherited from referencePoint
    
    # Element position (position) inherited from referencePoint
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_player_id', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 59, 10), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element nickname uses Python identifier nickname
    __nickname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'nickname'), 'nickname', '__AbsentNamespace0_player_nickname', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 60, 10), )

    
    nickname = property(__nickname.value, __nickname.set, None, None)

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__AbsentNamespace0_player_status', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 61, 10), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element orientationangle uses Python identifier orientationangle
    __orientationangle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'orientationangle'), 'orientationangle', '__AbsentNamespace0_player_orientationangle', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 62, 10), )

    
    orientationangle = property(__orientationangle.value, __orientationangle.set, None, None)

    
    # Element team uses Python identifier team
    __team = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'team'), 'team', '__AbsentNamespace0_player_team', False, pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 63, 10), )

    
    team = property(__team.value, __team.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __nickname.name() : __nickname,
        __status.name() : __status,
        __orientationangle.name() : __orientationangle,
        __team.name() : __team
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'player', player)


WorldData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WorldData'), worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', WorldData.name().localName(), WorldData)



worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'time'), pyxb.binding.datatypes.double, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 8, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'playMode'), playMode, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 9, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'score'), score, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 10, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'max_agent'), pyxb.binding.datatypes.int, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 11, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ball'), ballPosition, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 12, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'players'), player, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 13, 6)))

worldData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'flag'), referencePoint, scope=worldData, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 14, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 9, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 10, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 12, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 13, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 14, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'time')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'playMode')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'score')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 10, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'max_agent')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 11, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'ball')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 12, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'players')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 13, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(worldData._UseForTag(pyxb.namespace.ExpandedName(None, u'flag')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 14, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
worldData._Automaton = _BuildAutomaton()




score._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'yellow'), pyxb.binding.datatypes.int, scope=score, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 20, 6)))

score._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'blue'), pyxb.binding.datatypes.int, scope=score, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 21, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(score._UseForTag(pyxb.namespace.ExpandedName(None, u'yellow')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(score._UseForTag(pyxb.namespace.ExpandedName(None, u'blue')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
score._Automaton = _BuildAutomaton_()




referencePoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pointtype'), id, scope=referencePoint, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6)))

referencePoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'position'), serverPoint, scope=referencePoint, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(referencePoint._UseForTag(pyxb.namespace.ExpandedName(None, u'pointtype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(referencePoint._UseForTag(pyxb.namespace.ExpandedName(None, u'position')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
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
referencePoint._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ballPosition._UseForTag(pyxb.namespace.ExpandedName(None, u'pointtype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ballPosition._UseForTag(pyxb.namespace.ExpandedName(None, u'position')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
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
ballPosition._Automaton = _BuildAutomaton_3()




serverPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'x'), pyxb.binding.datatypes.double, scope=serverPoint, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 44, 10)))

serverPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'y'), pyxb.binding.datatypes.double, scope=serverPoint, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 45, 10)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(serverPoint._UseForTag(pyxb.namespace.ExpandedName(None, u'x')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 44, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(serverPoint._UseForTag(pyxb.namespace.ExpandedName(None, u'y')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 45, 10))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
serverPoint._Automaton = _BuildAutomaton_4()




player._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'id'), pyxb.binding.datatypes.int, scope=player, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 59, 10)))

player._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'nickname'), pyxb.binding.datatypes.string, scope=player, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 60, 10)))

player._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'), pyxb.binding.datatypes.boolean, scope=player, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 61, 10)))

player._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'orientationangle'), pyxb.binding.datatypes.double, scope=player, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 62, 10)))

player._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'team'), team, scope=player, location=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 63, 10)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 60, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 61, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 63, 10))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'pointtype')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 35, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'position')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 36, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'id')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 59, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'nickname')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 60, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'status')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 61, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'orientationangle')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 62, 10))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(player._UseForTag(pyxb.namespace.ExpandedName(None, u'team')), pyxb.utils.utility.Location('/home/northernstars/git/python-mrlib/python-mrLib/mrLib/networking/data/worlddataschema.xsd', 63, 10))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
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
player._Automaton = _BuildAutomaton_5()

