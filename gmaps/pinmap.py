
from ._ipywidgets import widgets
from ._traitlets import List, Unicode

import gmaps.gmaps_traitlets as gmaps_traitlets

class PinmapWidget(widgets.DOMWidget):
    _view_name = Unicode("PinmapView", sync=True)
    _bounds = List(sync=True)
    _data = List(sync=True)
    height = gmaps_traitlets.CSSDimension(sync=True)
    width = gmaps_traitlets.CSSDimension(sync=True)

    def __init__(self, data, height, width):
        self._data = data
        self.height = height
        self.width = width
        self._bounds = self._calc_bounds()
        super(widgets.DOMWidget, self).__init__()

    def _calc_bounds(self):
        min_latitude = min(data[0] for data in self._data)
        min_longitude = min(data[1] for data in self._data)
        max_latitude = max(data[0] for data in self._data)
        max_longitude = max(data[1] for data in self._data)
        return [ (min_latitude, min_longitude), (max_latitude, max_longitude) ]


def pinmap(data, height="400px", width="700px"):
    """
    Draw a map with pins for each map.

    This is currently experimental and should be used with
    caution.
    """
    try:
        data = data.tolist()
    except AttributeError:
        # Not a Numpy Array.
        pass
    w = PinmapWidget(data, height, width)
    return w
