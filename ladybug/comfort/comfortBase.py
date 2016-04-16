"""Comfort model object."""
from abc import abstractmethod


class ComfortModel(object):
    """
    Thermal Comfort Models.
    """

    def __init__(self):
        self.__calcLength = None
        self.__isDataAligned = False
        self.__isRelacNeeded = True

        self.__headerIncl = None
        self.__headerStr = []
        self.__singleVals = False
