def displayVR(toRender):
	videoTemplate = """
	<video class="viewframe" autoplay>
	<source src=""" + toRender + """ type="video/mp4">
	Your browser does not support the video tag.
	</video>
	"""

	defaultContainers = "<div class='split left split-obj'>" + videoTemplate + "</div><div class='split right split-obj'>" + videoTemplate + "</div>"

	return defaultContainers
