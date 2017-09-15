# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.urbaweb.importer import UrbawebDataImporter
from rebecq.urban.dataimport.interfaces import IRebecqDataImporter


class RebecqDataImporter(UrbawebDataImporter):
    """ """

    implements(IRebecqDataImporter)
