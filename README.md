# ASCII Magic

Converts images into ASCII art. Requires colorama and PIL.

## Usage

	import ascii_magic
	output = ascii_magic.from_image_file('picture.jpg')
	ascii_magic.to_terminal(output)

## Available functions

	# Converts an image file into ASCII art with terminal color codes
	#	path: a PIL-compatible file, such as picture.jpg
	#	columns: the number of characters per row, more columns = wider art
	#	pixel_width: ASCII characters are not square, so this adjusts the width to height ratio
	#	char: instead of using many different ASCII glyphs, you can use a single one
	ascii_magic.from_image_file(
		path:str,
		columns:int=120,
		width_ratio:float=2.5,
		char:str=None
	) -> str
	
	# As above, but from an image loaded with PIL
	ascii_magic.from_image(
		path:Image, # PIL image
		# ... as above
	) -> str

	# Initializes colorama (required on Windows) and prints ASCII art to the terminal
	# It's the same as doing colorama.init() before printing normally
	ascii_magic.to_terminal(ascii_art: str) -> None