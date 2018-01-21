'''OpenGL extension SGIX.ycrcb

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.ycrcb to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a method for OpenGL to read and store 
	images that are defined in standard YCRCB 422 and 444 video formats.
	As with the CYMK extension, conversion to RGBA takes place immediately 
	following the unpack pixel store, and preceding the pack pixel store 
	operations, and is only available on transfers to and from memory.  
	The algorithms that convert between YCRCB and RGBA are "black-box"
	in nature, and left undefined by the extension.
	
	Two new formats are added, YCRCB_422_SGIX and YCRCB_444_SGIX.
	
	To handle the difference in sampling rate for 422 video, the pixel 
	storage operations treat YCRCB_422_SGIX as a 2 component format,
	where the first component represents chroma, and the second luma.
	The chroma component alternates between Cb and Cr values on
	a per pixel basis.  If the specified image <width> parameter is not
	a multiple of 2, then fragments or texels that result from processing 
	the <width>th column of pixels will have undefined color value.
	
	YCRCB_444_SGIX is defined as a 3 component format representing 
	the Cb, Y, and Cr values per pixel.
	
	As with the CMYK extension, this extension doesn't preclude the 
	possiblity of other higher quality conversion methods.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/ycrcb.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.ycrcb import *
from OpenGL.raw.GL.SGIX.ycrcb import _EXTENSION_NAME

def glInitYcrcbSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
from OpenGL import images as _i
_i.COMPONENT_COUNTS[ GL_YCRCB_422_SGIX ] = 1 # must be GL_UNSIGNED_BYTE
_i.COMPONENT_COUNTS[ GL_YCRCB_444_SGIX ] = 1 # must be GL_UNSIGNED_SHORT
